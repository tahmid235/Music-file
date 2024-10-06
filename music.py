import pygame


pygame.mixer.init()

songs = ["music 1.mp3","music 2.mp3","music 3.mp3"]

def Playmusic(mymusic):
    pygame.mixer.music.load(mymusic)
    pygame.mixer.music.play()
    print(f"Now playing {mymusic}")
    
    

print("Welcome to simple music player")
print("Available songs")

for song in songs:
    print(song)

choice = int(input("Enter your choice 1/2/3"))

if choice == 1:
    Playmusic(songs[0])
if choice == 2:
    Playmusic(songs[1])
if choice == 3:
    Playmusic(songs[2])

input("Press enter to stop")
pygame.mixer.music.stop()