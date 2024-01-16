import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia 


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")


    elif hour >= 12 and hour < 18:
        speak("good afternoon!")


    else:
        speak("Good evening!")

    speak("Hey Anurag Yadav.")
     #sir, I just want to remind that your some work is left today and you also haven't complete this program and days are passing. so, please focus on this first rest Enjoy your day sir.

def takeCommand():
    #It take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        print(e)
        print("Say that again please...!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
         
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=10)
            speak("Accordind to wikipedia, i found this for you!")
            print(results)
            speak(results)
'''
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR, the Time is {strTime}")
'''
