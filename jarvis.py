
# What is the use of Jarvis assistant ?
# --> These Assistants are created to automate our work.

# What are the Funtions can this assistant perform ?
# This assistant can perform the following tasks with your speech :- 
# 1. Say wikipedia
# 2. Say search "anything you wanted to search"
# 3. open youtube
# 4. open browser
# 5. open wikipedia article on our choice
# 6. open code
# 7. tells time
# 8. wish us according to time interval
# 9. play music
# 10. For general chatting :- How are you , fine , good , what is your name , who i am , who are you
# 11. Exit (to stop the assistant)
# 12. Joke 
# 13  Empty recycle bin  

# Modules needed to be imported 

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes

# Necessary funtions for the assistant 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
assistant = "Jarvis"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

# How the assistant work

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")		
            webbrowser.open(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?") 

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assistant)
            print("My friends call me", assistant)
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Disha Maini.")
			
        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "who i am" in query:
            speak("If you talk then definitely you are human.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Disha")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to disha' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "dishayourEmail@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Disha. I am not able to send this email")    