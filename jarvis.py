import pyttsx3
import datetime
import speech_recognition as sr

#intialize module, get voice module, change voice (voice[0].id for male, voice[1].id for female)
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

#voice speed
voice_rate = 150
engine.setProperty('rate', voice_rate)

#method-1: tts conversion, runAndWait to pause program untill say function is done
# engine.say("Hello, how may I help you?")
# engine.runAndWait()

#method-2: define function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak(audio="Hello, how are you?")

def time():
    time = datetime.datetime.now().strftime('%I:%M:%S')    #.strftime is for time format
    speak('The current time is')
    speak(time)

#time()

def date():
    year = int (datetime.datetime.now().year)
    month = int (datetime.datetime.now().month)
    date = int (datetime.datetime.now().day)
    speak('The current date is')
    speak(date)
    speak(month)
    speak(year)

#date()

def greet():
    speak("Welcome!")
    time()
    date()
    hour = datetime.datetime.now().hour

    if (6<= hour <12):
        speak("Good Morning!")
    elif(12<= hour <18):
        speak("Good Afternoon!")
    elif(18<= hour <=24):
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("How may I help you?")

greet()

# user speech recognition
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold = 1
     audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, 'en=us')
        print(query)
    except Exception as e:
        print(e)
        speak("Could you please say that again...")
    
        return "None"

    return query

#takecommand()