#This is using if else conditions 
# I am trying with nltk python but not able to get accurate results
#I will share that code too once I got accurate results
# yet to add flask code in this to connect with the html
from flask import Flask
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def greetings():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def getinput():
    statement=input()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me,please say that again")
            return "None"
    return statement
print("Loading your AI personal assistant A1bot")
speak("Loading your AI personal assistant A1bot")
greetings()
from cv2 import *
if __name__=='__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement=getinput().lower()
        if statement==0:
            continue
        if statement in ["good bye","ok bye","stop"]:
            speak('your personal assistant A1bot is shutting down,Good bye')
            print('your personal assistant A1bot is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia..')
            statement=statement.replace("wikipedia","")
            results=wikipedia.summary(statement,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab('gmail.com')
            speak("Google Mail open now")
            time.sleep(5)  
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'news' in statement:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif "camera" in statement or "take a photo" in statement:
             ec.capture(0,False,"img.jpg")
        elif 'search' in statement:
            statement=statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=getinput()
            app_id="329UA6-RU843YYAW7"
            client=wolframalpha.Client('329UA6-RU843YYAW7')
            res=client.query(question)
            answer=next(res.results).text
            speak(answer)
            print(answer)
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am A1bot  your personal assistant. I am programmed to minor tasks like'
                 'opening youtube,google chrome,gmail and stackoverflow, predict time, take a photo,search wikipedia,predict weather'
                 'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif 'who made you' in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sai shankar")
            print("I was built by Sai shankar")
        elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")
        elif "weather" in statement:
            api_key="680b68d05d10e3cf91d9e0a976a494fc"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=getinput()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response=requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature=y["temp"]
                current_humidity=y["humidity"]
                z=x["weather"]
                weather_description=z[0]["description"]
                speak(" Temperature in kelvin unit is "+str(current_temperature)+"\n humidity in percentage is "+str(weather_description))
                print(" Temperature in kelvin unit = "+str(current_temperature)+"\n humidity (in percentage) ="+str(current_humidity)+"\n description = "+str(weather_description)) 
        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown","/1"])
            time.sleep(3)         
