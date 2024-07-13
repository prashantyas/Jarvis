import requests
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


newsapi="47fb77baad9648f98c424ff961c845d1"

recognizer = sr.Recognizer
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #phrase the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #speak the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let openai handle the rerquest
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #listen for the wake word Jarvis
        #obtain audio from the microphone
        r= sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listning...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen to command
                with sr.Microphone() as source:
                    print("Listning...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}", format(e))        


    #recognize speech using S
