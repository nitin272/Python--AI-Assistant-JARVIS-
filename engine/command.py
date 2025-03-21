import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    
@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,10,6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return ""
    return query.lower()


@eel.expose
def allCommands(message=1):

    try:
        query = takecommand()
        print(query)
       

        if "open" in query:
            from engine.feature import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.feature import PlayYoutube
            PlayYoutube(query)
        
        eel.ShowHood()
    except Exception as e:
        print(f"An error occurred: {e}")
 


# speak("I Love India")