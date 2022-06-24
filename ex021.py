#faça um prog em python que abra e reproduza o audio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
