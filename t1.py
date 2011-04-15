# -*- coding: cp1252 -*-
#teste1 - Apenas mover o carro no cenário com as setas, sem pretenções de OO

import pygame, sys, os
from pygame.locals import *

pygame.init()
pygame.display.set_caption("try1")
screen = pygame.display.set_mode((480,320))
background = pygame.image.load("gp.png")
car = pygame.image.load("gto.png")

scree.blit(car,(300,50))
pygame.display.flip()

def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      else: 
         print event 
 
while True: 
   input(pygame.event.get()) 
