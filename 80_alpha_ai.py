import random
from msilib.schema import Error
import webbrowser
from cv2 import vconcat
import speech_recognition as sr
import wikipedia
import pyttsx3
import time
import pywhatkit
import calendar
import pyjokes
import pyautogui as pg 
from time import sleep


class Alpha:

    def __init__(self, name, bday):
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

    def story(self):
        story_no = random.randint(1, 10)
        if story_no == 1:
            self.voice_Speak('''. An Old Man Lived in the Village
            Short Moral Stories - An Old Man
            
            An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood
            The longer he lived, the more bile he was becoming and the more poisonous were his words. People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him
            He created the feeling of unhappiness in others
            But one day, when he turned eighty years old, an incredible thing happened. Instantly everyone started hearing the rumour
            “An Old Man is happy today, he doesn’t complain about anything, smiles, and even his face is freshened up.
            The whole village gathered together. The old man was asked
            Villager: What happened to you
            “Nothing special. Eighty years I’ve been chasing happiness, and it was useless. And then I decided to live without happiness and just enjoy life. That’s why I’m happy now.” – An Old Ma
            Moral of the story:
            Don’t chase happiness. Enjoy your life.''')

        elif story_no == 2:
            self.voice_Speak('''The Wise Man
    Short Moral Stories - The Wise Man
    People have been coming to the wise man, complaining about the same problems every time. One day he told them a joke and everyone roared in laughter.
    After a couple of minutes, he told them the same joke and only a few of them smiled.
    When he told the same joke for the third time no one laughed anymore.
    The wise man smiled and said:
    “You can’t laugh at the same joke over and over. So why are you always crying about the same problem?”
    
    Moral of the story:
    Worrying won’t solve your problems, it’ll just waste your time and energy.
     ''')
        elif story_no == 3:
            self.voice_Speak('''
            The Foolish Donkey
Short Moral Stories - The Foolish Donkey


A salt seller used to carry the salt bag on his donkey to the market every day.

On the way they had to cross a stream. One day the donkey suddenly tumbled down the stream and the salt bag also fell into the water. The salt dissolved in the water and hence the bag became very light to carry. The donkey was happy.

Then the donkey started to play the same trick every day.

The salt seller came to understand the trick and decided to teach a lesson to it. The next day he loaded a cotton bag on the donkey.

Again it played the same trick hoping that the cotton bag would be still become lighter.


Related:  6 Powerful Tips to Grinding Harder This Year
But the dampened cotton became very heavy to carry and the donkey suffered. It learnt a lesson. It didn’t play the trick anymore after that day, and the seller was happy.

 

Moral of the story:
Luck won’t favor always.''')

        elif story_no == 4:
            self.voice_Speak('''
            Having A Best Friend
Short Moral Stories - Having A Best Friend

A story tells that two friends were walking through the desert. During some point of the journey they had an argument, and one friend slapped the other one in the face.
The one who got slapped was hurt, but without saying anything, wrote in the sand;
“Today my best friend slapped me in the face.”
They kept on walking until they found an oasis, where they decided to take a bath. The one who had been slapped got stuck in the mire and started drowning, but the friend saved him. After he recovered from the near drowning, he wrote on a stone;

“Today my best friend saved my life.”
The friend who had slapped and saved his best friend asked him;
“After I hurt you, you wrote in the sand and now, you write on a stone, why?”
The other friend replied;

“When someone hurts us we should write it down in sand where winds of forgiveness can erase it away. But, when someone does something good for us, we must engrave it in stone where no wind can ever erase it.”

Moral of the story: 
Don’t value the things you have in your life. But value who you have in your life.

  ''')
        elif story_no == 5:
            self.voice_Speak('''The Four Smart Students
Short Moral Stories - The Four Smart Students


One night four college students were out partying late night and didn’t study for the test which was scheduled for the next day. In the morning, they thought of a plan.

They made themselves look dirty with grease and dirt.

Then they went to the Dean and said they had gone out to a wedding last night and on their way back the tire of their car burst and they had to push the car all the way back. So they were in no condition to take the test.

The Dean thought for a minute and said they can have the re-test after 3 days. They thanked him and said they will be ready by that time.

On the third day, they appeared before the Dean. The Dean said that as this was a Special Condition Test, all four were required to sit in separate classrooms for the test. They all agreed as they had prepared well in the last 3 days.


The Test consisted of only 2 questions with the total of 100 Points:

Moral of the story:
Take responsibility or you will learn your lesson.

  ''')
        elif story_no == 6:
            self.voice_Speak('''The Greedy Lion
Short Moral Stories - The Greedy Lion


It was an incredibly hot day, and a lion was feeling very hungry.

He came out of his den and searched here and there. He could find only a small hare. He caught the hare with some hesitation. “This hare can’t fill my stomach” thought the lion.

Related:  Top 10 Inspiring Travel Videos That'll Show You the Beauty of the World
As the lion was about to kill the hare, a deer ran that way. The lion became greedy. He thought;

 

“Instead of eating this small hare, let me eat the big deer.”

 


He let the hare go and went behind the deer. But the deer had vanished into the forest. The lion now felt sorry for letting the hare off.

 

Moral of the story:
A bird in hand is worth two in the bush.

  ''')
        elif story_no == 7:
            self.voice_Speak(''' Two Friends & The Bear
Short Moral Stories - Two Friends & The Bear


Vijay and Raju were friends. On a holiday they went walking into a forest, enjoying the beauty of nature. Suddenly they saw a bear coming at them. They became frightened.

Raju, who knew all about climbing trees, ran up to a tree and climbed up quickly. He didn’t think of Vijay. Vijay had no idea how to climb the tree.

Vijay thought for a second. He’d heard animals don’t prefer dead bodies, so he fell to the ground and held his breath. The bear sniffed him and thought he was dead. So, it went on its way.

Raju asked Vijay;

 

“What did the bear whisper into your ears?”

 

Vijay replied, “The bear asked me to keep away from friends like you” …and went on his way.


 

Moral of the story:
A friend in need is a friend indeed.

 ''')
        elif story_no == 8:
            self.voice_Speak('''The Struggles of Our Life
Short Moral Stories - The Struggles of our Life


Once upon a time a daughter complained to her father that her life was miserable and that she didn’t know how she was going to make it.

She was tired of fighting and struggling all the time. It seemed just as one problem was solved, another one soon followed.

Her father, a chef, took her to the kitchen. He filled three pots with water and placed each on a high fire.

Once the three pots began to boil, he placed potatoes in one pot, eggs in the second pot and ground coffee beans in the third pot. He then let them sit and boil, without saying a word to his daughter.

The daughter, moaned and impatiently waited, wondering what he was doing. After twenty minutes he turned off the burners.

He took the potatoes out of the pot and placed them in a bowl. He pulled the eggs out and placed them in a bowl. He then ladled the coffee out and placed it in a cup.

 


Turning to her, he asked. “Daughter, what do you see?”

“Potatoes, eggs and coffee,” she hastily replied.

“Look closer” he said, “and touch the potatoes.” She did and noted that they were soft.

He then asked her to take an egg and break it. After pulling off the shell, she observed the hard-boiled egg.

Finally, he asked her to sip the coffee. Its rich aroma brought a smile to her face.

“Father, what does this mean?” she asked.

 

He then explained that the potatoes, the eggs and coffee beans had each faced the same adversity-the boiling water. However, each one reacted differently. The potato went in strong, hard and unrelenting, but in boiling water, it became soft and weak.

Related:  25 Pictures of Modern Society Worth A Thousand Words

The egg was fragile, with the thin outer shell protecting its liquid interior until it was put in the boiling water. Then the inside of the egg became hard.

However, the ground coffee beans were unique. After they were exposed to the boiling water, they changed the water and created something new.

“Which one are you?” he asked his daughter.

 

“When adversity knocks on your door, how do you respond? Are you a potato, an egg, or a coffee bean?”

 

Moral of the story: 
In life, things happen around us, things happen to us, but the only thing that truly matters is how you choose to react to it and what you make out of it. Life is all about leaning, adopting and converting all the struggles that we experience into something positive. ''')
        elif story_no == 9:
            self.voice_Speak(''' The Fox & The Grapes
Short Moral Stories - The Fox & The Grapes

One afternoon a fox was walking through the forest and spotted a bunch of grapes hanging from over a lofty branch.

“Just the thing to quench my thirst,” he thought.

Taking a few steps back, the fox jumped and just missed the hanging grapes. Again the fox took a few paces back and tried to reach them but still failed.


Finally, giving up, the fox turned up his nose and said, “They’re probably sour anyway,” and proceeded to walk away.

 

Moral of the story: 
It’s easy to despise what you can’t have.

 ''')
        elif story_no == 10:
            self.voice_Speak('''The Lion & The Poor Slave
Short Moral Stories - The Lion & The Poor Slave


A slave, ill-treated by his master, runs away to the forest. There he comes across a lion in pain because of a thorn in his paw. The slave bravely goes forward and removes the thorn gently.

The lion without hurting him goes away.

Some days later, the slave’s master comes hunting to the forest and catches many animals and cages them. The slave is spotted by the masters’ men who catch him and bring him to the cruel master.

The master asks for the slave to be thrown into the lion’s cage.

The slave is awaiting his death in the cage when he realizes that it is the same lion that he had helped. The slave rescued the lion and all other caged animals.

 

Moral of the story: 
One should help others in need, we get the rewards of our helpful acts in return. ''')

    def wikipedia_eng(self, search_wiki):
        try:
            page = wikipedia.page(search_wiki)
            summary = wikipedia.summary(search_wiki, sentences=50)
            print(search_wiki+f"page:{page.original_title}")
            print(search_wiki+f"Sufmmary:{summary}")
        except:
            print(f"Error:{Error}")

    def link(self, link):
        webbrowser.get(
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(link)

    def voice_Speak(self, command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 150)
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
            self.voice_Speak("Speak louder and properly")

        return audio_google

    def voice_Com(self):
             
            self.voice_Speak(f"Hello!!! {self.name} How may i help you?")
        
            while True:
                voice_command = self.voice_data()

                if 'how are you' in voice_command:
                    self.voice_Speak(f'I am awesome...{self.name}')
                
                elif 'hello' in voice_command:
                    self.voice_Speak(f"Hello,{self.name} what can i do for you?")

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
                    self.voice_Speak(
                        "On which platform you want to listen a song?")
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
                        self.link(
                            f"https://music.amazon.in/search/{song}?filter=IsLibrary%7Cfalse&sc=none")

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

                    self.voice_Speak(
                        "Enter your mobile number correctly, otherwise the message will be send to another person!!!")

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

                    self.voice_Speak(
                        "I will send your message on your given time...")
                    if int(time_min) < 10:
                        pywhatkit.sendwhatmsg(
                            f"{ccode}+{num}", f"{msg}", int(time_hour), f"0{int(time_min)}")

                    else:
                        pywhatkit.sendwhatmsg(
                            f"{ccode}+{num}", f"{msg}", int(time_hour), int(time_min))

                elif 'search' in voice_command:
                    self.voice_Speak("Ready to search anyhing on Google!!!")
                    self.voice_Speak("What do you want to search?")
                    search = self.voice_data()
                    self.voice_Speak(f"Searching... {search} on Google.")
                    self.link(f"https://www.google.com/search?q={search}")

                elif 'Wikipedia' in voice_command:
                    self.voice_Speak("Ready to search anyhing on wikipedia!!!")
                    self.voice_Speak("What do you want to search?")
                    searchwiki = self.voice_data()
                    self.wikipedia_eng(searchwiki)

                    self.voice_Speak(
                        "\nTo read full article, say Read in wikipedia")
                    openwiki = self.voice_data()

                    if 'read' in openwiki:
                        self.voice_Speak("Opening in wikipedia")
                        self.link(
                            f"https://en.wikipedia.org/w/index.php?search={searchwiki}&title=Special:Search&profile=advanced&fulltext=1&ns0=1")
                        

                elif 'change' in voice_command:
                    self.change_name()

                elif 'thank you' in voice_command:
                    self.voice_Speak("You're welcome")

                elif 'will you marry me' in voice_command:
                    self.voice_Speak("Ishhhh.... this is going to be serious...")

                elif 'will you be my girlfriend' in voice_command:
                    self.voice_Speak(
                        "Awwwww, sure... let me tell you this thing to your parents... ")

                elif 'am i good person' in voice_command:
                    self.voice_Speak(
                        "Yes you are such a kind person, i have ever seen in my life!!!")

                elif 'say i love you' in voice_command:
                    self.voice_Speak(
                        "Might be these words can not describe how much i love you, but yesss i love you so much!!!")

                elif 'can i call you' in voice_command:
                    self.voice_Speak("Yea sure, call me on 9252525252")

                elif 'you are my best friend' in voice_command:
                    self.voice_Speak(
                        "Glad to hear this, i always find a loyal person for me... and i have you, im so thankful to god to have you in my life!!!")

                elif 'story' in voice_command:
                    self.story()
                elif 'contact' in voice_command:
                    self.voice_Speak("Opening contacts")
                    self.voice_Speak("To Add new contact, say Create contact")
                    self.voice_Speak("To Open contact list, say View Contact list")
                    choice = self.voice_data()

                    if 'create' in choice:
                        contact = {}
                        self.voice_Speak("Enter Name:")
                        name = input("")
                        self.voice_Speak("Enter Number:")
                        num = input("")
                        contact_lst = contact.update({name: num})
                        with open("Contacts.txt", 'a') as r:
                            r = r.write(str(contact_lst))

                        self.voice_Speak("Contact is added.")

                    if 'view' in choice:
                        with open("Contacts.txt", 'r') as r:
                            r = r.read(contact_lst)

                elif 'calendar' in voice_command:
                    self.voice_Speak("Opening Calendar")
                    print(calendar.calendar(2022, 2, 1, 6))

                elif 'joke' in voice_command:
                    my_joke = pyjokes.get_joke(language="en", category="all")
                    self.voice_Speak("Here is one joke for you...")
                    self.voice_Speak(my_joke)

                elif 'I love you' in voice_command:
                    self.voice_Speak(
                        "Sorry this is not possible, i have crush on siri...")
                
                elif 'open' in voice_command:
                    self.voice_Speak("Say what do you want to open!!!")
                    op = self.voice_data()
                    self.voice_Speak(f"opening {op}")
                    sleep(3.00)
                    pg.press('tab',2)
                    pg.press('enter')
                    pg.write(f'{op}')
                    sleep(1.00)
                    pg.press('enter')
                    

                elif 'random number' in voice_command:

                    try:

                        self.voice_Speak("Choosing random number for you...")
                        rand = random.randint(0, 1000)
                        self.voice_Speak(rand)

                    except:

                        self.voice_Speak(
                            "Unable to choose random number... try again...")

                elif 'bye' in voice_command:
                    self.voice_Speak("See you later... Bye Bye")
                    exit()

                else:
                    self.voice_Speak(
                        "I am still improving my self, so i can not perform this task temporarily... but i will try my best next time!!!")
                    exit()


dhrumil = Alpha("Dhrumil", "30 july 2004")
dhrumil.voice_Com()
