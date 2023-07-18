# import pygame, sys 
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from secrets import choice
import pyttsx3 
import speech_recognition as sr
from PIL import Image
from secrets import choice
import pyttsx3 
import speech_recognition as sr
from PIL import Image
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


Assistance=pyttsx3.init('sapi5')
voices=Assistance.getProperty('voices')
rate=Assistance.getProperty('rate')
Assistance.setProperty('rate',130)
Assistance.setProperty('voices',voices[0].id)

fashion=['shirt','jeans',"t'shirt"]
games=['cricket','football','carrom']
foods=['cheez','burger','pizza']

def token(shopname): 
  word_data = shopname
  nltk_tokens = nltk.word_tokenize(word_data)
#   print (nltk_tokens)
  return nltk_tokens



def speak(audio):
    print("   ")
    Assistance.say(audio)
    print(f"{audio}")
    Assistance.runAndWait()

speak("welcome to pheonix mall")

speak("how may i assist you ")

def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        command.energy_threshold=10000
        command.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = command.listen(source)
        

        try:
            print("Recognizing..")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said:{query}")

        except Exception as Error:
            return "none"

        return query
inputs=takecommand()
print(inputs)
stores=['Mufti','Levis','Allen Solly','England','flying machine','Park avenue','Zara']
games=['cricket','football','games']
foods=['pizza','hotdog']

word_data = inputs
nltk_tokens = nltk.word_tokenize(word_data)
en_stops = set(stopwords.words('english'))
all_words = nltk_tokens
for word in all_words: 
    if word not in en_stops:
       if word in fashion:
           speak('which store do you want to visit  ')
           speak(stores)

           shopname=takecommand()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in stores:
              find=word
       if word in games:
           speak('which game you wish to Play ')
           speak(games)
           shopname=takecommand()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in games:
              find=word
        #    print("i want to play games")
       if word in foods:
           speak('from were you want to eat  ')

           speak(foods)
           shopname=takecommand()
           mytuple=(token(shopname))
           all_words = mytuple
           for word in all_words: 
             if word  in foods:
              find=word
        #    print("i want to eat somthing")

