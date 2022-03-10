import random
from msilib.schema import Error
import webbrowser
import speech_recognition as sr
import wikipedia
import pyttsx3
import time
import pywhatkit
import calendar
import pyjokes


class Alpha:

    def __init__(self,name,bday):
        self.name = name
        self.bday = bday

    def change_name(self):
        self.voice_Speak("Tell me your new name...")
        newname = self.voice_data()
        self.voice_Speak(f"Your new name is:{newname}")
        self.voice_Speak("is it correct?")
        corrction = self.voice_data()
        if 'yes' in corrction:
            self.name = newname
            self.voice_Speak(f"Your new name is:{newname}")
            
    def wikipedia_eng(self,search_wiki):
        try:
            page = wikipedia.page(search_wiki)
            summary = wikipedia.summary(search_wiki , sentences = 50)
            print(search_wiki+f"page:{page.original_title}")
            print(search_wiki+f"Sufmmary:{summary}")
        except:
            print(f"Error:{Error}")

    def link(self,link):
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(link)

    def voice_Speak(self,command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.setProperty('rate',150)
        print(f"{command}")
        engine.say(command)
        engine.runAndWait()

    def voice_data(self):
        try:
            print("Listening...")
            voice_c = sr.Recognizer()
            with sr.Microphone() as source:
                voice_c.adjust_for_ambient_noise(source)
                audio = voice_c.listen(source)
                audio_google = voice_c.recognize_google(audio)
                print(f"{audio_google}\n")
        except:
            self.voice_Speak("Speak louder and properly...")
        
        return audio_google

    def voice_Com(self):
        
        self.voice_Speak("Hello, I am Alpha...")
        self.voice_Speak("say Hello Alpha to start me...")
        
        while 'hello alpha' in self.voice_data():
       
            self.voice_Speak(f"{self.name} How may i help you?")

                voice_command = self.voice_data()
             
            if 'how are you' in voice_command:
                self.voice_Speak(f'I am awesome...{self.name}')

            elif 'you do' in voice_command:
                self.voice_Speak("I can do all these things...")
                self.voice_Speak("You can ask me for your Name and Birthday")
                self.voice_Speak("I can create Contacts for you.")
                self.voice_Speak("I can play music for you, on YouTube , spotify , Apple music and Amazon music")
                self.voice_Speak("I can send a whatsapp message for you!!!")
                self.voice_Speak("I can tell you the current time and date!!!")
                self.voice_Speak("I can search anything on web.")
                self.voice_Speak("I can search music for you on your favorite platform.")
                self.voice_Speak("I can tell you jokes...")
                self.voice_Speak("I can choose Random Number for you...")
                

            elif 'made you' in voice_command:
                self.voice_Speak("Dhrumil Patel made me, he is studying diploma in computer engineering from parul university gujarat, he is working on python programming , java programming and c programming. he made me in python programming language.")
            elif 'name' in voice_command:
                self.voice_Speak(self.name)
            
            elif 'do you like my name' in voice_command:
                self.voice_Speak("i like your name")

            elif 'birthday' in voice_command:
                self.voice_Speak(f'your birthday is {self.bday}')
                
            elif 'song' in voice_command:
                self.voice_Speak("On which platform you want to listen a song?")
                print("Youtube\nSpotify\nApple music\nAmazon music")
                print("Choose your Platfrom: ")
                choice = self.voice_data()

                if 'YouTube' in choice:
                    self.voice_Speak("Tell me a song name...")
                    song = self.voice_data()
                    self.voice_Speak(f"Playing...{song} on YouTube")
                    pywhatkit.playonyt(song)

                elif 'spotify' in choice:
                    self.voice_Speak("Tell me a song name...")
                    song = self.voice_data()
                    self.voice_Speak(f"Playing...{song} on Spotify")

                    self.link(f"https://open.spotify.com/search/{song}")

                elif 'Apple music' in choice:
                    self.voice_Speak("Tell me a song name...")
                    song = self.voice_data()
                    self.voice_Speak(f"Playing...{song} on Apple Music")

                    self.link(f"https://music.apple.com/us/search?term={song}")
                
                elif 'Amazon Music' in choice:
                    self.voice_Speak("Tell me a song name...")
                    song = self.voice_data()
                    self.voice_Speak(f"Playing...{song} on Amazon Music")
                    self.link(f"https://music.amazon.in/search/{song}?filter=IsLibrary%7Cfalse&sc=none")
                
                else:
                    print(f"Error:{Error}")
                
        
            elif 'feeling sad' in voice_command:
                self.voice_Speak("Dont Worry everything will be okay!!!")
            
            elif 'time' in voice_command:
                lctime = time.time()
                curtime = time.ctime(lctime)
                self.voice_Speak(curtime)

            elif 'message' in voice_command:
                self.voice_Speak("Ready to send your message on whatsapp!")

                self.voice_Speak("Enter your mobile number correctly, otherwise the message will be send to another person!!!")

                self.voice_Speak("Type Your country code:")
                ccode = input("")
                self.voice_Speak("Type Mobile Number: ")
                num = input("")
            
                self.voice_Speak("Type your message: ")
                msg = input("")

                self.voice_Speak("Enter a time, you want to send message")

                self.voice_Speak("Type Time in hour:")
                time_hour = input("")

                self.voice_Speak("Type Time in minute: ")
                time_min = input("")

                self.voice_Speak("I will send your message on your given time...")
                if int(time_min) < 10:
                    pywhatkit.sendwhatmsg(f"{ccode}+{num}",f"{msg}" , int(time_hour) , f"0{int(time_min)}" )

                else:
                    pywhatkit.sendwhatmsg(f"{ccode}+{num}",f"{msg}" , int(time_hour) ,int(time_min) )

            elif 'google' in voice_command:
                self.voice_Speak("Ready to search anyhing on Google!!!")
                self.voice_Speak("What do you want to search?")
                search = self.voice_data()
                self.voice_Speak(f"Searching... {search} on Google.")
                self.link(f"https://www.google.com/search?q={search}")

            elif 'Wikipedia' in voice_command:
                self.voice_Speak("Ready to search anyhing on wikipedia!!!")
                self.voice_Speak("What do you want to search?")
                searchwiki  = self.voice_data()
                self.wikipedia_eng(searchwiki)

                self.voice_Speak("\nTo read full article, say Read in wikipedia")
                openwiki = self.voice_data()

                if 'read' in openwiki:
                    self.voice_Speak("Opening in wikipedia")
                    self.link(f"https://en.wikipedia.org/w/index.php?search={searchwiki}&title=Special:Search&profile=advanced&fulltext=1&ns0=1")
                    break

            elif 'change' in voice_command:
                self.change_name()
            
            elif 'thank you' in voice_command:
                self.voice_Speak("You're welcome")

            elif 'contact' in voice_command:
                self.voice_Speak("Opening contacts")
                self.voice_Speak("To Add new contact, say Create contact")
                self.voice_Speak("To Open contact list, say View Contact list")
                choice  = self.voice_data()

                if 'create' in choice:
                    contact = {}
                    self.voice_Speak("Enter Name:")
                    name = input("")
                    self.voice_Speak("Enter Number:")
                    num = input("")
                    contact_lst = contact.update({name:num})
                    with open("Contacts.txt",'a') as r:
                       r = r.write(str(contact_lst))

                    self.voice_Speak("Contact is added.")

                if 'view' in choice:
                    with open("Contacts.txt",'r') as r:
                       r = r.read(contact_lst)

            elif 'calendar' in voice_command:
                self.voice_Speak("Opening Calendar")
                print(calendar.calendar(2022,2,1,6))

            elif 'joke' in voice_command:
                my_joke = pyjokes.get_joke(language="en",category="all")
                self.voice_Speak("Here is one joke for you...")
                self.voice_Speak(my_joke)
                
            elif 'I love you' in voice_command:
                self.voice_Speak("Sorry this is not possible, i have crush on siri...")

            elif 'random number' in voice_command:

                try:
                    
                    self.voice_Speak("Choosing random number for you...")
                    rand = random.randint(0,1000)
                    self.voice_Speak(rand)

                except:

                    self.voice_Speak("Unable to choose random number... try again...")

            elif 'bye' in voice_command:
                self.voice_Speak("See you later... Bye Bye")
                exit()
        
            else:
                self.voice_Speak("I am still improving my self, so i can not perform this task temporarily... but i will try my best next time!!!")
                exit()
            
            i+=1
     

dhrumil = Alpha("Dhrumil","30 july 2004")
dhrumil.voice_Com()


'''
Modules needed
Subprocess:- This module is used for getting system subprocess details which are used in various commands i.e Shutdown, Sleep, etc. This module comes built-in with Python. 
 
Ecapture:- To capture images from your Camera. To install this module type the below command in the terminal.
pip install ecapture

'''
