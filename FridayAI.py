import os
import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date
import subprocess
import time
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        p = r.recognize_google(audio, language='en-in')
        print(f"User said: {p}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return p


def usrname():
    speak("What should i call you sir")
    uname = input().lower()
    speak("Welcome")
    speak(uname)
    speak("How can i Help you, Sir")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!I am your virtual assistant Friday")
        speak("how may i help you?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!I am your virtual assistant Friday")
        speak("how may i help you?")

    else:
        speak("Good Evening sir!I am your virtual assistant Friday")
        speak("how may i help you?")


if __name__ == "__main__":
    wishMe()
while True:
    p = takeCommand().lower()
    #p = input().lower()

    if (("run" in p) or ("open" in p) or ("execute" in p)) and (("google" in p) or ("chrome" in p) or ("browser" in p)):
        speak("opening google chrome")
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("player" in p) or ("media" in p)):
        speak("opening window media player")
        os.startfile("C:\Program Files (x86)\Windows Media Player\wmplayer.exe")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("firefox" in p) or ("browser" in p)):
        speak("opening firefox")
        os.startfile("C:\Program Files\Mozilla Firefox\\firefox.exe")

    elif 'send a mail' in p:
        try:
            speak("What should I say?")
            content = input()
            speak("whome should i send")
            to = input()
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("excell" in p) or ("ms excell" in p)):
        speak("opening microsoft excell")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\microsoft office Excel 2007.lnk")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and ("notepad" in p):
        speak("opening notepad")
        os.system("notepad")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("word" in p) or ("ms word" in p)):
        speak("opening microsoft word")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\microsoft office word 2007.lnk")


    elif (("run" in p) or ("open" in p) or ("execute" in p)) and ("control panel" in p):
        speak("opening control panel")
        os.system("control panel")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("whatsapp" in p) or ("messanger" in p)):
        speak("opening whatsapp")
        os.system("google whatsapp.com")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (("cmd" in p) or ("command prompt" in p)):
        speak("opening command prompt")
        os.system("command prompt")

    elif (("run" in p) or ("open" in p) or ("execute" in p)) and (
            ("documents" in p) or ("document folder" in p) or ("my documents" in p)):
        speak("opening documents folder")
        os.system("documents")

    elif ('time' in p):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("the time is")
        print(strTime)
        speak(strTime)


    elif ('date' in p):
        today = date.today()
        speak("Today's date is ")
        print(today)
        speak(today)

    elif (("run" in p) or ("open" in p)) and ("youtube" in p):
        speak("opening youtube")
        webbrowser.open("youtube.com")

    elif 'how are you' in p:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in p or "good" in p:
        speak("It's good to know that your fine")

    elif "who are you" in p:
        speak("I am virtual assistant Friday created by Anshul")

    elif "hey" in p or "hi" in p or "hello" in p and "friday" in p:
        speak("hello sir")

    elif 'shutdown system' in p:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif "restart" in p:
        subprocess.call(["shutdown", "/r"])

    elif ("don't listen" in p) or ("stop listening" in p):
        speak("for how much time you want to stop me from listening commands")
        a = int(input())
        time.sleep(a)

    elif ("open" in p and "facebook" in p):
        speak("opening facebook")
        webbrowser.open("www.facebook.com")


    elif ("help" in p):
        print("""1.Please check you have entered the right command or request
                \n2.Check whether you have added the file of application to the path of your PC.\n(Check environmental variables of your PC for this
                 \n3.Check your PC for system or code runner for problems
                 \n4.Enter menu to know the applications""")

    elif ("exit" in p) or ("quit" in p) or ("stop" in p):
        speak("good bye sir!hope to meet soon")
        print("good bye sir!hope to meet soon")
        break

    else:
        speak("I don't support it Please check in HELP.")
