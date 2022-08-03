from pygame import mixer
import pygame

background = "pixel-perfect-112527.wav"
eat = "eatingsfxwav-14588.wav"
spawn = "moody-blip-43107.wav"
death = "pixel-death-66829.wav"
pygame.init()


# Backgroud Music
def bg_music():
    mixer.music.load(background)
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)


# Food spawn sound
def food_spawn():
    fd_spawn = mixer.Sound(spawn)
    fd_spawn.play()


# Food eating sound
def eaten():
    eat_food = mixer.Sound(eat)
    eat_food.play()


# Snake dead sound
def dead():
    died = mixer.Sound(death)
    died.play()
