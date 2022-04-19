from playsound import playsound

link = "https://open.spotify.com/search/"
song = input("Enter song name")
url = link + song
print(url)
playsound(f'open {link}'.format(url))
