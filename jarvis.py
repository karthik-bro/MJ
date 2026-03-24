import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import requests

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help you?")

wish()

while True:

    command = input("Enter command: ").lower()

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        webbrowser.open("https://google.com")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)
        print("Time:", time)

    elif "open code" in command:
        os.system("code")

    elif "search" in command:
        query = input("What do you want to search? ")
        webbrowser.open("https://google.com/search?q=" + query)

    elif "exit" in command:
        speak("Goodbye")
        break
    
    elif "wikipedia" in command:
        try:
            query = command.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)

            print(result)
            speak(result)

        except:
            print("No result found")
            speak("Sorry, I could not find anything")
            
    elif "note" in command:
         note = input("Write your note: ")

         with open("notes.txt", "a") as file:
          file.write(note + "\n")

         print("Note saved")
         speak("Note saved successfully")

    else:
       print("Command not recognized")