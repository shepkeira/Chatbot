import socket
import select
import errno
import os
import sys

import dialogflow
import json
import requests
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account


'''
DIALOGFLOW
'''

DIALOGFLOW_PROJECT_ID = 'cosc-310-ewoqcu'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
credential_path =  os.path.join(sys.path[0], "cosc-310-ewoqcu-db61ea9e0e22.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
SESSION_ID = 'current-user-id'

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def getresponse(text, lang_code, sech):
    text_input = dialogflow.types.TextInput(language_code=lang_code, text=text)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(sech, query_input)
    except InvalidArgument:
        raise
    # print("Query text:", response.query_result.query_text)
    # print("Detected intent:", response.query_result.intent.display_name)
    # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    if not response.query_result.fulfillment_text:
        print("Dr. Azile: Tell me more")
    else:
        # print("Fulfillment text:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text # I think this is an object, not just a string

'''
CLIENT CODE
'''
HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

def handle_input(msg_recieved):
    # Wait for user to input a message
    print(msg_recieved)
    message = getresponse(msg_recieved, DIALOGFLOW_LANGUAGE_CODE, session)
    print(message)

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    else:
        print("no message recieved")

handle_input("Hello!")

while True:

    
    try:
        #RECIEVES MESSAGES FROM SERVER
        msg_recieved = ""
        # Receive our "header" containing username length, it's size is defined and constant
        username_header = client_socket.recv(HEADER_LENGTH)

        # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(username_header):
            print('Connection closed by the server')
            sys.exit()

        # Convert header to int value
        username_length = int(username_header.decode('utf-8').strip())

        # Receive and decode username
        username = client_socket.recv(username_length).decode('utf-8')

        # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
        message_header = client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8').strip())
        message = client_socket.recv(message_length).decode('utf-8')

        # Print message
        print(f'{username} > {message}')
        msg_recieved = message

        #SENDS MESSAGE TO SERVER
        handle_input(msg_recieved)


    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
    
    