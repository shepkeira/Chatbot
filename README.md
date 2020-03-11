# COSC310 ChatBot Group 19 [Azile - the Psychiatrist Chatbot]
Members: Katrina Martel, Jeff Hatton, Keira Shepherd, Matthew Currie, Brian Su

## What is Azile?
Azile is a psychiatrist bot that is based on the psychiatrist bot "Eliza" created by Joseph Weizenbaum from 1964 to 1966. Azile aims to converse with the user about their day to day and has a focus on helping users with anxiety. Despite Azile's focus on anxiety, it is still suited to help people experiencing different types of emotions. “Eliza”.  It was created as a general chatbot and not a professional help bot for individuals.  It is meant to give assistance dependant on key words entered.

## Motivation:
The application was created as part of COSC 310 Assignment Two.  It will only be maintained during the duration of this course assignment completion.  It is not intended for real world existence.


## How to interact with Azile:
1. Download the repository files to the local machine.
2. Import the repository into desired python IDE or continue using command-line interfaces of preference (e.g., command prompt).  
3. Install the following dependencies Dialogflow (version 0.5.1) and Google-api-core (version 1.4.1). Via pip run:
```
pip install dialogflow==0.5.1
pip install google-api-core==1.4.1
```
5. To run the bot from the command prompt. After the installation, cd into the directory of the repository, run main.py to start interacting.
```
python main.py
```
6. To run via IDE, `run main.py`.  Users on Pycharm by Jetbrains,  may have to create a new VENV for the specific project after installing the dependencies. Run `main.py` when you want to interact with the bot.


Once the bot is started, Azile will start with some basic input questions to get started with the session.
Follow along with the prompts until the disclaimer is displayed. Then go ahead to chat about anything that the user wishes to talk about with Azile.
Specific phrases, words will prompt individual responses.

## About our code:
In our project, we utilized Dialogflow, a Google-owned developer of human-computer interaction technologies based on Natural Language conversations (WIKI). Within the Dialogflow client, where all API calls are handled, are different intents coded to respond to different inputs. The intents identify emotions and phrases, then in the coded responses, will either prompt the user to elaborate more or provide specific actions for the user to follow. Such as, our bot must advise users to seek professional health support if they express self-harming/ suicidal tendencies. All uncategorizable, and unrecognized inputs will trigger a fall back intent that feeds generic conversation prompts. Our code is within `main.py` that handles the chat interface, an API interaction.
