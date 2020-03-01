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

def getresponse(text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE, session):
    text_input = dialogflow.types.TextInput(language_code=DIALOGFLOW_LANGUAGE_CODE, text=text_to_be_analyzed)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session, query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    print("Dr. Azile: ", response.query_result.fulfillment_text)

done = False
while(not done):
    text_to_be_analyzed = input("You: ")
    if text_to_be_analyzed == "bye":
        done = True
    getresponse(text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE, session)