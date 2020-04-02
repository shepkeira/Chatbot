"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
    pip install dialogflow==0.5.1
    pip install google-api-core==1.4.1
"""
import os
import sys

import dialogflow
import json
import requests
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account


def do_thing(said, num):
    if num > 7:
        response = getresponse(said, DIALOGFLOW_LANGUAGE_CODE, session)
        return response
    else:
        response = intro(num)
        return response


DIALOGFLOW_PROJECT_ID = 'cosc-310-ewoqcu'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
credential_path =  os.path.join(sys.path[0], "cosc-310-ewoqcu-db61ea9e0e22.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
SESSION_ID = 'current-user-id'

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


# connects with DialogFlow Agent to get responses
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
        response = "Tell me more"
    else:
        # print("Fulfillment text:", response.query_result.fulfillment_text)
        print("Dr. Azile: ", response.query_result.fulfillment_text)
        response = response.query_result.fulfillment_text
    return response

# filler intro conversation
def introconversation(printString):
    print(printString)
    input("You: ")


return2 = "Formal Disclaimer that this is a chatbot and not a professional help bot for people.\nHello my name is Dr. Azile, I am here to help with your psychological needs. Please know that I am not a real person; I am a chat bot, created by some amazing people to help you. If you need a real person or I feel you need someone real I can give you resources like a helpline number.\nDr. Azile: To get started I have a few question about you. Just let me know when you are ready"

def intro(num):
    if num == 0:
        return "Say hi to get started"
    elif num == 1:
        return return2
    elif num == 2:
        return "How old are you?"
    elif num == 3:
        return "What is your name?"
    elif num == 4:
        return "Are you currently a elementary school student, middle school student, high school student, univeristy school student, or not a student?"
    elif num == 5:
        return "On a scale of 1 to 5 with one being terrible and five being great, how are you feeling currently?"
    elif num == 6:
        return "My focus is anxiety. On a scale of 1 to 5 with one being no anxiety and 5 being a anxiety attack, how anxious are you feeling today?"
    elif num == 7:
        return "Ok lets get started. Tell me about how you are feeling today."

# introconversation("Say hi to get started")
# introconversation("Formal Disclaimer that this is a chatbot and not a professional help bot for people." +
#       "\nHello my name is Dr. Azile, I am here to help with your psychological needs. Please know that I am not a real " +
#       "person; I am a chat bot, created by some amazing people to help you. If you need a real person or I feel you " +
#       "need someone real I can give you resources like a helpline number." +
#       "\nDr. Azile: To get started I have a few question about you. Just let me know when you are ready")
# introconversation("Dr. Azile: How old are you?")
# introconversation("Dr. Azile: What is your name?")
# introconversation("Dr. Azile: Are you currently a elementary school student, middle school student, high school student, "
#       "univeristy school student, or not a student?")
# introconversation("Dr. Azile: On a scale of 1 to 5 with one being terrible and five being great, how are you feeling currently?")
# introconversation("Dr. Azile: My focus is anxiety. On a scale of 1 to 5 with one being no anxiety and 5 being a anxiety attack,"
#       " how anxious are you feeling today?")
# print("Dr. Azile: Ok lets get started. Tell me about how you are feeling today.")
#
#
# done = False
# while not done:
#     text_to_be_analyzed = input("You: ")
#     if text_to_be_analyzed == "bye":
#         done = True
#     getresponse(text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE, session)