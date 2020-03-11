"""Install the following requirements:
    dialogflow        0.5.1
    google-api-core   1.4.1
"""
import os
import sys

import dialogflow
import json
import requests
from google.api_core.exceptions import InvalidArgument
from google.oauth2 import service_account


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
    print("Detected intent:", response.query_result.intent.display_name)
    # print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    if not response.query_result.fulfillment_text:
        print("Dr. Azile: Tell me more")
    else:
        # print("Fulfillment text:", response.query_result.fulfillment_text)
        print("Dr. Azile: ", response.query_result.fulfillment_text)


print("Say hi to get started. Say bye at anytime to end the conversation.")
text_to_be_analyzed = input("You: ")
print("Formal Disclaimer that this is a chatbot and not a professional help bot for people.")
print("Hello my name is Dr. Azile, I am here to help with your psychological needs. Please know that I am not a real "
      "person; I am a chat bot, created by some amazing people to help you. If you need a real person or I feel you "
      "need someone real I can give you resources like a helpline number.")
print("Dr. Azile: To get started I have a few question about you. Just let me know when you are ready")
text_to_be_analyzed = input("You: ")
print("Dr. Azile: How old are you?")
age = input("You: ")
print("Dr. Azile: What is your name?")
name = input("You: ")
print("Dr. Azile: Are you currently a elementary school student, middle school student, high school student, "
      "univeristy school student, or not a student?")
isStudent = input("You: ")
print("Dr. Azile: Do you currently work full time, part time, or not at all?")
work = input("You: ")
print("Dr. Azile: On a scale of 1 to 5 with one being terrible and five being great, how are you feeling currently?")
feel = input("You: ")
print("Dr. Azile: My focus is anxiety. On a scale of 1 to 5 with one being no anxiety and 5 being a anxiety attack,"
      " how anxious are you feeling today?")
anxiety = input("You: ")
print("Dr. Azile: Ok lets get started. Tell me about how you are feeling today.")

done = False
while not done:
    text_to_be_analyzed = input("You: ")
    if text_to_be_analyzed == "bye":
        done = True
    getresponse(text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE, session)
