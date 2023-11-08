import struct
import pyaudio
import pvporcupine
from pydub.playback import play
from pydub import AudioSegment
import time
import speech_recognition as sr
import pyttsx3
import testin2
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty("rate",rate-30)
def speak(text):
    print("Terminator:",text)
    engine.say(text)
    engine.runAndWait()

porcupine=None
pyaud=None
audio_stream=None
def startsound():
    audio=AudioSegment.from_wav("start up sound.wav")
    play(audio)

def endsound():
    audio=AudioSegment.from_wav("end up sound.wav")
    play(audio)

#porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
porcupine=pvporcupine.create(access_key="11WB/Mx1h/RTT0V3uSs8AKnoGc8cCEXmFxCPGMXhoszlmQm2IMgM5g==", keywords=["jarvis","bumblebee","terminator"])
paud=pyaudio.PyAudio()
audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            startsound()
            speak("I am terminator how can i help you")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                    print("Listening..")
                    audio = r.listen(source) 

            try:
                    print("Recognizing..")
                    query = r.recognize_google(audio,language = 'en-in')   
                    print( f"user said:{query}\n")
                    testin2.command(query)
            except Exception as e:
                    print("Say that again please") 
                    query= None
            
            # startsound()
            # recognize=sr.Recognizer()
            # with sr.Microphone() as source:
            #     audio=recognize.listen(source,3,3)
            #     endsound()
            # try:
            #     query=recognize.recognize_google(audio,language='en-in')
            #     # jarvis_command.command(query)
            # except sr.UnknownValueError:
            #     speak("not recognize")
            



# import struct
# import pyaudio
# import pvporcupine
# from pydub.playback import play
# from pydub import AudioSegment
# import speech_recognition as sr
# import pyttsx3
# engine=pyttsx3.init("sapi5")
# voices=engine.getProperty("voices")
# engine.setProperty("voice",voices[0].id)
# rate=engine.getProperty('rate')
# engine.setProperty("rate",rate-30)
# def speak(text):
#     print("Jarvis:",text)
#     engine.say(text)
#     engine.runAndWait()

# porcupine=None
# pyaud=None
# audio_stream=None
# def startsound():
#     audio=AudioSegment.from_wav("start up sound.wav")
#     play(audio)

# def endsound():
#     audio=AudioSegment.from_wav("end up sound.wav")
#     play(audio)
# try:
#     porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
#     paud=pyaudio.PyAudio()
#     audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
#     while True:
#         keyword=audio_stream.read(porcupine.frame_length)
#         keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
#         keyword_index=porcupine.process(keyword)
#         if keyword_index>=0:
#             startsound()
#             recognize=sr.Recognizer()
#             with sr.Microphone() as source:
#                 audio=recognize.listen(source,3,3)
#                 endsound()
#             try:
#                 query=recognize.recognize_google(audio,language='en-in')
#                 #jarvis_command.command(query)
#             except sr.UnknownValueError:
#                 speak("not recognize")
            

# finally:
#     if porcupine is not None:
#         porcupine.delete()
#     if audio_stream is not None:
#         audio_stream.close()
#     if paud is not None:
#         paud.terminate()