# ------------------------ 1 ----------------- IMPORTS
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# ------------------------ 2 ---------------- OUTPUT VOICE OR SPEAK
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices) #list of aud of 3 types of voices
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# ------------------------ 3 ---------------- WISH FUNC
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<12:
        speak("Good Morning Buddy...")
    elif hour>12 and hour<17:
        speak("Good Afternoon Buddy...")
    else:
        speak("Good Evening Buddy...")
    
    speak("I'm Melaa! How can I help you?")

# ------------------------ 4 ---------------- LISTEN AND RECOGNIZE VOICE + other funcs
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"Input : {query}")
    except Exception as e:
        print(e)
        print("Can't reached at the moment...Please Repeat!")
        return "not found"
    return query

def sendEmail(to, sub, msg):
    gmailId = 'your-gmail-id'
    gmailPwd = 'your-gmail-pwd'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmailId, gmailPwd)
    s.sendmail(gmailId, to, f"Subject: {sub}\n\n{msg} ")
    s.quit()


# ------------------------ 5 ---------------- RUN
if __name__ == "__main__":
    wishMe()
    while True:
        # query = takeCommand().lower()
        print("\nListening...")
        query = input().lower()

        if 'open' in query:
            query = query.replace('open ', '')
            speak(f"Opening {query}")
            webbrowser.open(f"{query}.com")
            print('Opening...')
            break

        elif 'play' in query:
            query = query.replace('play ', '')
            musicDir = "D:\\users\Music"
            songs = os.listdir(musicDir)
            for song in songs:
                if query in song.lower():         
                    speak(f"Playing {query}")
                    os.startfile(os.path.join(musicDir, song))
                    break
            else:
                speak("No such song found!")
            break

        elif 'wiki' in query:
            query = query.replace('wiki', '')
            speak(f"Searching Wikipedia for {query}")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'time' in query:
            query = query.replace('time ', '')
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            speak(f'The time is {time}')

        elif 'send email' in query:
            print('To send emails first turn less secure apps from web ON')
            speak('Say Email Address!')
            # to = takeCommand()
            to = input()
            speak('Say Subject!')
            # subject = takeCommand()
            subject = input()
            speak('Say Content!')
            # content = takeCommand()
            content = input()
            try:
                sendEmail(to, subject, content)
            except Exception as e:
                print(e)
            else:
                speak(f"Email to {to} with subject {subject} sent!")

        elif 'quit' or 'exit' in query:
            exit()
        

