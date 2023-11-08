import pyttsx3 #speech to text
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import mysql.connector
from tabulate import tabulate

con= mysql.connector.connect(host="127.0.0.1",port='3306',user="root",password="Samurai@42#",database="darkangel")

print("Initializing Dark Angel")

MASTER="Mam..."
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#speak("Hi Mam... This is Dark Angel...Your..Destop..Assistant")
#speak function will pronounce the string
def speak(text):
    engine.say(text)
    engine.runAndWait()

def insert(name,regno):
    res = con.cursor()
    sql ="insert into users (Name,Regno) values (%s,%s)"
    user = (name,regno)
    res.execute(sql,user)
    con.commit()
    print("Inserted")
def update(name,regno,id):
    res = con.cursor()
    sql ="update users set Name=%s,Regno=%s where ID=%s"
    user = (name,regno,id)
    res.execute(sql,user)
    con.commit()
    print("Updated")
def delete(id):
    res = con.cursor()
    sql ="delete from users where id=%s"
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print("Data Deleted")
def select():
    res = con.cursor()
    sql="SELECT ID,Name,Regno from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","Name","Regno"]))

def sendemail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rv1545@srmist.edu.in' , 'Srlkannan123@')
    # server.sendmail("sumer18@gamil.com", content)
    server.close()
# def wishme():
#     hour= int(datetime.datetime.now().hour)
      

#     if hour>=0 and hour<12:
#         speak("Good morning"+ MASTER)
#     elif hour>=12 and hour<18:
#         speak("Good afternoon"+ MASTER) 
#     else:
#         speak("Good evening"+ MASTER)
#     speak("How can i help you")           
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening..")
#         audio = r.listen(source) 

#     try:
#         print("Recognizing..")
#         query = r.recognize_google(audio,language = 'en-in')   
#         print( f"user said:{query}\n")
        
#     except Exception as e:
#         print("Say that again please") 
#         query= None

#     return query    

# speak("Intializing.. Dark..Angel..")
# wishme()
#takecommand()
# query = takecommand()

#logic for answering
def command(query):
    
    if 'wikipedia' in query.lower():
     speak('Wait for a while..')
     query= query.replace("wikipedia", "")
     results= wikipedia.summary(query, sentences=2)
     speak(results)

    elif 'open youtube' in query.lower():
             webbrowser.open("youtube.com")
    elif 'open google'  in query.lower():
        webbrowser.open("google.com")   
    elif 'open whatsapp web'  in query.lower():
        webbrowser.open("web.whatsapp.com")   
    elif 'open gmail'  in query.lower():
        webbrowser.open("gmail.com")   
    elif 'open facebook'  in query.lower():
        webbrowser.open("facebook.com")   
    elif 'open github'  in query.lower():
        webbrowser.open("github.com")   


    elif 'play music'  in query.lower():
      songs=os.listdir()



    elif 'the time' in query.lower():
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"(MASTER) the time is {strTime}")
    
    elif 'who is your master' in query.lower():
        speak("MY master is Sumresh..")

    elif 'insert data' in query.lower():
        name=command()
        regno=input("Enter regno: ")
        insert(name,regno)
    elif 'update data' in query.lower():
        id=int(input("Enter id: "))
        name=input("Enter name: ")
        regno=input("Enter regno: ")
        update(name,regno,id)
    elif 'select data' in query.lower():
        print("  ")
        select()
    elif 'delete' in query.lower():
        id=input("Enter the value to be deleted: ")
        delete(id)
    elif 'quit' in query.lower():
        quit()
    elif 'email' in query.lower():
        try:
         speak("what should i send")
         content= command()
         to = "sumresh18@gmail.com" 
         sendemail(to,content)  
         speak("email is sent")
        except Exception as e :
            print(e)

    elif 'notepad' in query.lower():
        webbrowser.open('notepad')
    else:
        speak("Invalid selection try again")

