#Presented by Kartik Gathibandhe
#Submitted to D.Y. Patil School of engineering and Technology, Pune

import pyttsx3
import datetime
import speech_recognition as spr
import wikipedia
import os
import datetime
import webbrowser
import smtplib
import socket

socket.getaddrinfo('127.0.0.1', 8080)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Sir")
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        print("Good Afternoon! Sir")
        speak("Good Afternoon! Sir")

    else:
        print("Good Evening! Sir")
        speak("Good Evening! Sir")

    print("Jarvis :How may I help you")
    speak("How may I help you ? ")

def Command():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        question = r.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")


    except Exception as e:
        print("Jarvis couldn't understand what you said, TRY AGAIN!")
        speak("Sir, I didn't understand what you said, Try saying it again!")
        return "None"
    return question

def sendEmail(to, content):
    server = smtplib.SMTP('64.233.184.108', 587)
    server.ehlo()
    server.starttls()
    server.login('kartik.j.g2003@gmail.com', '@118111Kg')
    server.sendmail('kartik.j.g2003@gmail.com' ,to, content)
    server.close()
    
if __name__ == "__main__":
    WishMe()
    Command()
    while True:
        question = Command().lower()

        if 'wikipedia' in question:
            print("Searching Wikipedia, pls wait!")
            speak("I am searching Wikipedia, Sir please wait!")
            question = question.replace("wikipedia", "")
            answers = wikipedia.summary(question, sentences=2)
            print("According to Wikipedia...")
            speak("According to Wikipedia...")
            print(answers)
            speak(answers)

        elif 'time' in question:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open youtube' in question:
            print("User said: Open YouTube")
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in question:
            print("User said: Opening google")
            speak("Opening google")
            webbrowser.open("google.com")      

        elif 'open stackoverflow' in question:
            print("User said: Opening stackoverflow")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in question:
            print("user said:Opening Facebook")
            speak("Opening Facebook")
            webbrowser.open("facebook.com")


        elif 'play music' in question:
            music_dir = 'C:\\Users\\karti\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open code' in question:
            codePath = "C:\\Users\\karti\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'what are you' in question:
           print("I am your personal assistant Jarvis")
           speak("I am your personal assistant Jarvis")

        elif 'how are you' in question:
            print("user said: I am fine sir")
            speak("I am fine sir")


        elif 'email to kartik' in question:
            try:
                speak("What should I say ?")
                content = Command()
                to = "kartik.j.g2003@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send email")




        elif 'quit' in question:
            print("Bye Sir!")
            speak("Bye Sir!")
            break
