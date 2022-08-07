from datetime import datetime
from unittest import result
import webbrowser
from cv2 import threshold
from matplotlib.pyplot import connect
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
from pynput.keyboard import Key, Controller
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source,duration=1)
        r.non_speaking_duration = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print ("Say that again please...")
        return "None"
    return query

def webopen(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

def playmusic():
    keyboard = Controller()
    key = "a"
    keyboard.press(key)
    keyboard.release(key)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your_pass')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    # takeCommand()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webopen("youtube.com")
        
        elif 'open college mail' in query:
            speak("Opening Zimbra Mail...")
            webopen("stud.iitp.ac.in")

        elif 'open google' in query:
            speak("Opening Google...")
            webopen("google.com")

        elif 'play music' in query:
            speak("Playing Music...")
            music_dir = 'C:\\Users\\Harsh\\Desktop\\FavMusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open spotify' in query:
            speak("Opening Spotify...")
            webopen("open.spotify.com")

        elif 'play locha' in query:
            speak("Playing...")
            webopen("https://open.spotify.com/track/3V3QbgrOZKtFv5MXzAAdZr?si=fa79f44bc22240ae")
            playmusic()
        
        elif 'play mala' in query:
            speak("Playing...")
            webopen("https://open.spotify.com/track/5kOuoPsmNJ58PQdeMIKnRJ?si=98410c2ccd4e4811")
            playmusic()
            
        elif 'time' in query:
            strTime = datetime.datetime.now().satrftime("%H:%M")
            speak(f"Time now is {strTime}")

        elif 'open code' in query:
            speak("Opening VS Code...")
            codepath = 'C:\\Users\\Harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        
        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harsh.cheer@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            
            except Exception as e:
                print(e)
                speak("Sorry... Unable to send email!")

        elif 'close' in query:
            speak("Take Care...")
            exit()
