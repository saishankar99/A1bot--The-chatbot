from flask import Flask,render_template,request
import datetime
import wikipedia
import webbrowser
import time
import wolframalpha
import requests
import cv2
from cv2 import *
path="C:/Users/saika/Gbot/templates"
app=Flask(__name__)
import nltk
from nltk.chat.util import Chat,reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"(what is your name ?|what's your name)",
        ["I am  A1bot created by sai shankar, you can call me A1b!",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Shankar created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['kakinada, Andhra pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"(quit|bye)",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(fine|ok)",
        ["What else do you want from me??"]
    ],
 
]
chat = Chat(pairs, reflections)
@app.route("/")
def home():
    return render_template("top.html")
@app.route("/success",methods = ['GET', 'POST'])
def main():
    return render_template("index.html")
@app.route('/get')
def get_bot_response():
        statement=request.args.get('msg')
        
        
        if statement==0:
            return 
        if statement in ["good bye","ok bye","stop"]:
            return ('your personal assistant G-one is shutting down,Good bye')
            
        if 'wikipedia' in statement:
         
            statement=statement.replace("wikipedia","")
            results=wikipedia.summary(statement,sentences=3)
            return results
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            time.sleep(5)
            return "youtube opened in the new tab"
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(5)
            return "google opened in the new tab"
        elif 'open gmail' in statement:
            webbrowser.open_new_tab('gmail.com')
            time.sleep(5)
            return "G mail opened in the new tab"
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            return "The time is "+str(strTime)
        elif 'news' in statement:
            news=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            time.sleep(6)
            return "News opened in the new tab"
        elif "camera" in statement or "take a photo" in statement:
             key = cv2.waitKey(1)
             webcam = cv2.VideoCapture(0)
             check, frame = webcam.read()
             key = cv2.waitKey(1)
             cv2.imwrite(filename='sav1.jpg', img=frame)
             webcam.release()
             img_new = cv2.imread('sav1.jpg', cv2.IMREAD_GRAYSCALE)
             img_new = cv2.imshow("Captured Image", img_new)
             cv2.waitKey(0)
             cv2.destroyAllWindows()
             return 'Image saved in your pc'
             
        elif 'search' in statement:
            statement=statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'ask' in statement:
            question=statement.replace("ask","")
            app_id="329UA6-RU843YYAW7"
            client=wolframalpha.Client('329UA6-RU843YYAW7')
            res=client.query(question)
            answer=next(res.results).text
            return (answer)
        elif 'who are you' in statement or 'what can you do' in statement or 'what are you made for' in statement:
             return "I am A1Bot-The chatbot  your personal assistant. I am programmed to minor tasks like opening youtube,google chrome,gmail, predict time, take a photo,search wikipedia,predict weather In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!'"
        elif 'who made you' in statement or "who created you" in statement or "who discovered you" in statement:
            return ("I was built by Sai shankar")
        elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                return "stack overflow opened in the new tab"
        elif "weather" in statement:
            api_key="680b68d05d10e3cf91d9e0a976a494fc"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            city_name=statement.replace("weather","")
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response=requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature=y["temp"]
                current_humidity=y["humidity"]
                z=x["weather"]
                weather_description=z[0]["description"]
                return (" Temperature in kelvin unit = "+str(current_temperature)+"\n humidity (in percentage) ="+str(current_humidity)+"\n description = "+str(weather_description)) 
            else:
                return ("Make sure you entered 'weather cityname' without quotations.\nMake sure you entered city name correctly")
        else:
            return chat.respond(statement)   
    
app.run(debug=True)
