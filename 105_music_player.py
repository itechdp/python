'''
This program will help the user to find out the best songs realted to their mood and find out the songs of thier fav 
singer

step: program will take a input from the user and ask the question about users mood
step: the list of singer will be provided to the user and program will sort some musics related to mood 
step: then after the selelction of the singer the songs will be given to the user in form
step: program will be associated with the youtube and spotify
step: after selecting the mood of the user the program will ask about the format of the song video or audio
step: program will take a song number from the user and play that song on the respective platform 

'''

class Main_int:
    def mood_type(self):
        mood = input("Enter Your Mood: ")
        song_type = input("Enter song category: ")
        self.song_type = song_type
        self.mood = mood

    
class Mood(Main_int):
    def mood_music(self):
        if self.mood == self.happy:
            pass
        elif self.mood == self.sad:
            pass
        elif self.mood == self.relax:
            pass
        elif self.mood == self.excited:
            pass
        elif self.mood == self.hiphop:
            pass
    
    def platform(self):
        pass

class Singer(Mood):
    def singer_music(self):
        pass



dhrumil = Main_int()
dhrumil.mood_type()