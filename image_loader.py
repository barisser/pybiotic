import pygame
import os


def init():
    a = []
    path = os.getcwd() + "/images/a.png"
    b = pygame.image.load(path)
    a.append(b)
    return a

images = init()
