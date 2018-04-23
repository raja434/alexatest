import logging
import os
import webbrowser
from flask import Flask
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Welcome i will show nice Display'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('HomeIntent')
def hello_world():
    speech_text = 'Hi hows going on ..?'
    return statement(speech_text).simple_card('Homepage ', speech_text)

@ask.intent('locationIntent')
def location():
    speech_text = 'I think you are in this place'
    return statement(speech_text).simple_card('your location is.. ', speech_text)

@ask.intent('PlayIntent')
def youtube():
    speech_text = 'ok.. right now  i am playing avengers in local youtube '
    return statement(speech_text).simple_card('playing local youtube  ', speech_text)

@ask.intent('WIntent')
def hello_world():
    speech_text = 'I am thinking Right now the weather'
    return statement(speech_text).simple_card('weather ', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
