# -*- coding: cp1252 -*-


# Jogo do macaco - Treino 1


# Primeiro, importe os modulos pygame, sys e os

import pygame, sys, os
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((468,60))
pygame.display.set_caption("Febre do MAcaco")
screen = pygame.display.get_surface()

monkey_head_file_name = os.path.join("data","chimp.bmp")
monkey_surface = pygame.image.load(monkey_head_file_name)

screen.blit(monkey_surface, (35,40))
pygame.display.flip()

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                screen.blit(monkey_surface, (0,0))
                pygame.display.update()
        else:
            print event
    
while True:
    input(pygame.event.get())
