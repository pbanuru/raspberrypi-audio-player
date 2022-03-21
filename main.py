from pygame import mixer
from time import sleep
import pygame
import os
import random


if __name__ == '__main__':
    print("Begin")
    pygame.init()
    mixer.init()

    # load a random song from audio/Genshin Impact [Music Box]/
    random_song = random.choice(os.listdir('audio/Genshin Impact [Music Box]/'))

    mixer.music.load('audio/Genshin Impact [Music Box]/' + random_song)
    mixer.music.play()
    print("Now playing: " + random_song)
    

    while mixer.music.get_busy():
        sleep(1)

    print("End")
    mixer.quit()
