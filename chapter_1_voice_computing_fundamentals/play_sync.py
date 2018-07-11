'''
play_sync.py

Play back an audio file synchronously.
'''

import pygame

def sync_playback(filename):
    # takes in a file and plays it back 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

sync_playback('one.wav')
