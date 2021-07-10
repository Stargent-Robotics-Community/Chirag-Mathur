import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

a = pyttsx3.init()
voices = a.getProperty('voices')
a.setProperty('voice',voices[1].id)
a.say("Hello there! I am Edith! What can I do for you today?")
a.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    r.pause_threshold=1

    print("Listening....")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    query = text.lower()
    print(query)
    if 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'how are you' in query:
        pyttsx3.speak("I am fine")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        pyttsx3.speak(f"The current time is {strTime}")
    
    elif 'your name' in query:
        pyttsx3.speak("I am popularly known as Edith.")

except:
    print("Sorry I am unable to understand. Can you please repeat.")
