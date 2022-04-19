from msilib.schema import Error
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

def speaktext(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate",150)
    engine.say(command)
    engine.runAndWait()
    

def main():
 
    r = sr.Recognizer() # To recongize the voice
    with sr.Microphone() as source: #To give a source of voice
        r.adjust_for_ambient_noise(source)
    
        print("Hello i am your Music Buddy, Created By dhrumil patel")
        speaktext("Hello i am your Music Buddy, Createrd by dhrumil patel")

        print("Tell me a song name you want to listen...")
        speaktext("Tell me a song name you want to listen...")

        audio = r.listen(source)
    
        try:
            speak = r.recognize_google(audio) #recognizing the provided audio on google
            print(speak)
            print("Searching..."+speak)
            # webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("https://open.spotify.com/search/"+speak) use this line if you want to open a song in perticular application
            speaktext("Playing"+speak+"On YouTube")
            print("Playing..." +speak+" on YouTube Tap Start Button to play")
            pywhatkit.playonyt(speak) #to play a song 

        except Error as er :
            print(f"Error:{er} \nTry Again...")

if __name__ == "__main__":
    main()

