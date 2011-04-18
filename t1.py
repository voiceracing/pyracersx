# -*- coding: cp1252 -*-
#teste1 - Apenas mover o carro no cenário com as setas, sem pretenções de OO

import pygame, sys, os
from pygame.locals import *

pos = 157

pygame.init()


window = pygame.display.set_mode((350,400))
pygame.display.set_caption("try1")
screen = pygame.display.get_surface()
car_fn = os.path.join("img","gto.png")
car_surface = pygame.image.load(car_fn)
#car_surface.set_colorKey((0,0,0))
screen.blit(car_surface,(pos,337))
#pygame.display.flip()


def input(events):
   for event in events:
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
         os.exit()
      if event.type == KEYDOWN:
         if event.type == K_ESCAPE:
            pygame.quit()
            sys.exit()
            os.exit()
         if event.type == K_RIGHT:
            pos += 10
            screen.blit(car_surface,(pos,337))
            pygame.display.update()
            
         if event.type == K_LEFT:
            pos -= 10
            screen.blit(car_surface,(pos,337))
            pygame.display.update()
   
         
            
while True:
   input(pygame.event.get())
   if event.type == KEYDOWN:
         if event.type == K_ESCAPE:
            pygame.quit()
            sys.exit()
            os.exit()
         if event.type == K_RIGHT:
            pos += 10
            screen.blit(car_surface,(pos,337))
            pygame.display.update()
            
         if event.type == K_LEFT:
            pos -= 10
            screen.blit(car_surface,(pos,337))
            pygame.display.update()
   pygame.display.update()
   


   


