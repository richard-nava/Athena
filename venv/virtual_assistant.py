import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import random
import wolframalpha
import wikipedia
import calendar
import time
from djitellopy import tello
import cv2
import factialrecognition

# ignore any warning messages
warnings.filterwarnings('ignore')


# drone connection
me = tello.Tello()
me.connect()
print(me.get_battery())
print(me.get_temperature())

# convert audio to string
def recordAudio():
    # Record Audio
    r = sr.Recognizer()  # Creating a recognizer object

    # Start mic and record
    with sr.Microphone() as source:
        print('Say something...')
        audio = r.listen(source)

    # Use google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:  # Check for unknown errors
        print('Google Speech Recog did not understand the audio - unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recog service error...' + e)

    return data


# Function to get the Athena to respond
def athenaResp(text):
    print(text)

    # convert text into speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # save the converted audio to a file
    myobj.save('athena_response.mp3')

    # Play the converted file
    os.system('open athena_response.mp3')


# Function for wake word(s) or phrase
def wakeWords(text):
    WAKE_WORDS = ['hello athena', 'hey athena', 'say hi athena', 'okay athena']  # list of wake words

    text = text.lower()

    # check if wake word is anywhere in the text
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # If the wake word isn't found in the text form the loop, return false
    return False


# Function to return date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # e.g. Friday
    monthNum = now.month
    dayNum = now.day

    # List of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + " " + str(dayNum)


# A function to return a random greeting response

def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hello', 'hi', 'whats up', 'wassup', 'hey', 'whats up athena']

    # Greeting responses
    GREETING_RESPONSES = ['hello. ', 'pleased to meet you. ', 'hey there. ', 'hello there. ']

    # If the users input is a greeting, return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

    return ''


def getToKnow():
    WHO = ['introduce yourself', 'who are you']
    print(text)
    # for phrase in WHO:
    #
    #     if phrase == 'how are you':
    #         return 'I am a machine, therefore I do not feel. But I hope you are feeling well today.'
    #     elif phrase == 'who are you':
    #         print('here')
    #         return 'My name is athena. I am a virtual assistant program created by richard nava. i can tell you the time, date, or any other information you may seek. how may I help?'

    return 'My name is athena. I am an autonomous drone personality and virtual assistant program created by richard nava. i can tell you the time and date, random info about whatever, or just fly around and chill. how may I help?'


# Get a persons first and last name from a text
def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


while True:
    # Record audio
    text = recordAudio()
    response = ''

    # Check for wake keys
    if (wakeWords(text) == True):
        # Check for greetings
        response = response + greeting(text)

        # Check if user said anything to do with date?
        if 'date' in text:
            get_date = getDate()
            response = response + ' ' + get_date

        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m.'
                hour = now.hour - 12
            else:
                meridiem = 'a.m.'
                hour = now.hour

            # Convert minute into a proper string
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridiem + ' .'

        # Check to see if the user said 'who is'
        if 'who is' in text:
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if 'who are you' in text:
            response = response + getToKnow()

        if 'introduce yourself' in text:
            response = response + getToKnow()

        if 'fly' in text:
            me.takeoff()
            me.send_rc_control(0, 50, 0, 0)
            time.sleep(2)
            me.send_rc_control(0, 0, 0, 0)
            time.sleep(2)
            me.send_rc_control(0, 0, 0, 50)
            time.sleep(3)
            me.send_rc_control(0, 0, 0, 0)
            me.land()
            me.end()

        if 'follow' in text:
            exec(open('facialrecognition.py').read())

        if cv2.waitKey(1) & 0xFF == ord('q'):  # when q is pressed, land
            me.land()
            break

        athenaResp(response)
        text = ''
        time.sleep(2)
