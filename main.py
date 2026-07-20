import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import requests
from gtts import gTTS
import pygame
import os
from ai import ask_ai
from urllib.parse import quote


recognizer = sr.Recognizer()
engine = pyttsx3.init() 


# def speak(text):
#      engine.say(text)
#      engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com") 

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")    

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")    

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")    

  




    elif c.lower().startswith("play"):
     song = c.lower().replace("play", "", 1).strip()

     if song in musiclibrary.music:
       webbrowser.open(musiclibrary.music[song])
     else:
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(song)}"
        )


    else:
     reply = ask_ai(command)
     speak(reply)
     




    
               


   
if __name__ == "__main__":
        
   speak("Initializing Jarvis .....")


   while True:
        r = sr.Recognizer()
            # Listen for the wake word"Jarvis"
            # Obtain audio from the microphone
        print("Recognizing") 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("YES SIR HOW MAY I HELP YOU")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

       
        except Exception as e:
         print("Error; {0}".format(e))
        