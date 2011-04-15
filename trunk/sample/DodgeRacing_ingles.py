
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
from random import randint
import time
imagenDeFondo = 'carretera1.jpg'
#.....................................................................#
pygame.init()
pygame.display.set_caption("Dodge Racing")
fps = 60
tiempo = 0
niveles = 'Level 1'
visor = pygame.display.set_mode((850, 480), 0, 32)
fondo = pygame.image.load(imagenDeFondo).convert()
imagenDeFondo = 'Cochecarrera.jpg'
imagenFinal = pygame.image.load('final.jpg').convert()
#.....................................................................#
#Coches

coche = pygame.image.load('cocheprincipal.jpg').convert()
coche.set_colorkey((127,127,127))
coche2 = pygame.image.load('coche222.jpg').convert()
coche2.set_colorkey((127,128,123))
coche3 = pygame.image.load('coche33.jpg').convert()
coche3.set_colorkey((127,127,127))
coche4 = pygame.image.load('coche4.jpg').convert()
coche4.set_colorkey((127,127,127))
#.....................................................................#
#Arboles

arbol1 = pygame.image.load('arbol1.jpg').convert()
arbol2 = pygame.image.load('arbol2.jpg').convert()
arbol3 = pygame.image.load('arbol3.jpg').convert()
arbol4 = pygame.image.load('arbol4.jpg').convert()
#.....................................................................#
#Senales

senal20 = pygame.image.load('20.jpg').convert()
senal20x = 120
senal20y = 50
senal40 = pygame.image.load('40.jpg').convert()
senal40x = 120
senal40y = -90
senal80 = pygame.image.load('80.jpg').convert()
senal80x = 120
senal80y = -90
senal100  = pygame.image.load('100.jpg').convert()
senal100x = 120
senal100y = -90
senal120  = pygame.image.load('120.jpg').convert()
senal120x = 120
senal120y = -90
#.....................................................................#
#Mancha

mancha = pygame.image.load('mancha.jpg').convert()
mancha.set_colorkey((127,127,127))
manchax = randint (224,530)
manchay = -1000
#.....................................................................#
#Estrella

estrella = pygame.image.load('star.jpg').convert()
estrella.set_colorkey((127,127,127))
estrellax = randint (224,530)
estrellay = -2000

#Estrella mala
estrella2 = pygame.image.load('estrella2.png').convert()
estrella2.set_colorkey((0,0,0))
estrella2x = randint (224,530)
estrella2y = -3000
#.....................................................................#
#Linea carretera.

linea = pygame.image.load('lineaCarretera.jpg').convert()
lineay = 0
lineax1 = 305
lineax2 = 406
lineax3 = 511
#.....................................................................#
#Explosion.

explosion1 = pygame.image.load('explosion1.jpg').convert()
explosion1.set_colorkey((0,0,0))
explosion2 = pygame.image.load('explosion2.jpg').convert()
explosion2.set_colorkey((0,0,0))
explosion3 = pygame.image.load('explosion3.jpg').convert()
explosion3.set_colorkey((0,0,0))
#.....................................................................#
#Puntos, marcador, niveles.

puntos = 0
marcador = pygame.image.load('marcador.png').convert()
marcador.set_colorkey((255,255,255))
reloj = pygame.image.load('reloj.png').convert()
reloj.set_colorkey((255,255,255))
pos = 100
#.....................................................................#
#Tipos de letras. 

tipoLetra = pygame.font.SysFont('arial', 70)
tipoLetra2 = pygame.font.SysFont('arial', 17)
tipoLetra3 = pygame.font.SysFont('arial', 40)
#.....................................................................#
BLANCO = (255,255,255)
#.....................................................................#
#Coches.

amarillox = randint (224,530)
amarilloy = 0
blancox = randint (224,530)
blancoy = 0
negrox = randint (224,530)
negroy = 0
#.....................................................................#
#Arboles.

arbol1x = randint(0,100)
arbol1y = 50
arbol2x = randint(630, 850)
arbol2y = 90
arbol3x = randint(0,100)
arbol3y = 0
arbol4x = randint(630, 850)
arbol4y = 0
#.....................................................................#
menu = pygame.image.load('menu1.jpg').convert()

#.....................................................................#
#Sonidos.

sonidoExplosion = pygame.mixer.Sound('Explosion.wav')
sonidoExplosion2 = pygame.mixer.Sound('Mario_Sounds(2).wav')
sonidoWiki = pygame.mixer.Sound('Mario_Sounds.wav')
pygame.mixer.music.load('od-endorfin.mod')


def explosiones():
    sonidoExplosion.play()
    visor.blit(explosion1, (pos+ 40,385))
    time.sleep(0.2)
    pygame.display.update()
    visor.blit(explosion2, (pos+30,400))
    time.sleep(0.2)
    pygame.display.update()
    visor.blit(explosion1, (pos+10,390))
    time.sleep(0.2)
    time.sleep(1)
    sonidoExplosion2.play()
    pygame.display.update()
#.....................................................................#
def pausa():
    # Esta funcion hace que se espera hasta que se pulse una tecla
    esperar = True
    while esperar:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                esperar = False
#.....................................................................#
def pausa2():
    global coche
    global menu
    esperar = True
    while esperar:
        
        teclasPulsadas2 = pygame.key.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x >483 and x<600 and y>370 and y<452:
            menu = pygame.image.load('menu_salir2.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
        
        if x >450 and x<620 and y>266 and y<315:
            menu = pygame.image.load('menu_ayuda.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
            
        if x >545 and x<593 and y>136 and y<220:
            menu = pygame.image.load('menu_coche2.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
            
        if x >361 and x<413 and y>136 and y<220:
            menu = pygame.image.load('menu_coche1.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
            
        if x>1 and x<2 and y>1 and y<2:
            menu = pygame.image.load('menu1.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
        else:
            menu = pygame.image.load('menu1.jpg').convert()
            visor.blit(menu,(0,0))
            pygame.display.update()
            
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x>483 and x<600:
                    if y>370 and y<452:
                        pygame.quit()
                        sys.exit()
                        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x>450 and x<620:
                    if y>266 and y<315:
                        sonidoWiki.play()
                        ayuda= pygame.image.load('ayuda.jpg').convert()
                        visor.blit(ayuda, (0,0))
                        pygame.display.update()
                        time.sleep (6)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x>545 and x<593:
                    if y>136 and y<220:
                        sonidoWiki.play()
                        coche = pygame.image.load('cocheprincipal2.jpg').convert()
                        visor.blit(fondo, (0,0))
                        esperar = False
                        pygame.display.update()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x>361 and x<413:
                    if y>136 and y<220:
                        sonidoWiki.play()
                        coche = pygame.image.load('cocheprincipall.jpg').convert()
                        visor.blit(fondo, (0,0))
                        esperar = False
                        pygame.display.update()
                        

                
#.....................................................................#
def mostrarIntro():
           
    pygame.display.toggle_fullscreen()


    pygame.mixer.music.play(-1)

    fondo = pygame.image.load(imagenDeFondo).convert()
    visor.blit(fondo, (0,0))
    pygame.display.update()
    pausa()
   
#.....................................................................#
def mostrarMenu():
    
    visor.blit(menu, (0,0))
    pygame.display.update()
    pausa2()

#.....................................................................#
def mostrarFinal():

    creditosy = -1000
    creditosx = 0
    esperar = True
    while esperar:
        
            
            niveles = 'Level 1'
            puntos = 0
            final = pygame.image.load('creditos.jpg').convert()
            visor.blit(final, (0,0))
            creditos = pygame.image.load('creditos2.jpg').convert()

            visor.blit(creditos, (creditosx,creditosy))
            creditosy += 2
            pygame.display.update()
            
            senal20y=50
            senal40y= -90
            senal80y= -90
            senal100y=-90
            senal120y=-90
    
            

            if creditosy >420:
                esperar = False
                mostrarMenu()
                pygame.display.update()
mostrarIntro()
mostrarMenu()


while True:
    
    if pygame.time.get_ticks()-tiempo < 1000/fps:
        continue
    tiempo = pygame.time.get_ticks()

    
    # Mirar los eventos y si es QUIT terminar el programa
    for evento in pygame.event.get():
        if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        if evento.type == KEYDOWN: 
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif evento.unicode == 'f':
                pygame.display.toggle_fullscreen()

#.....................................................................#
#Velocidad mancha.
    if manchay > 365 and manchay < 440 and abs (pos-manchax) < 45:
        amarilloy = amarilloy + 10
        blancoy = blancoy + 10
        negroy = negroy + 10
        arbol1y = arbol1y + 10
        arbol2y = arbol2y + 10
        arbol3y = arbol3y + 10
        arbol4y = arbol4y + 10
    
    
#.....................................................................#
#Suma de puntos estrella.
    
    if estrellay >365 and estrellay < 440 and abs (pos-estrellax) < 20 :
        puntos = puntos + 1000
        estrellay = -1500
        
    if estrella2y >365 and estrella2y < 440 and abs (pos-estrella2x) < 20 :
        puntos = puntos -1000
        estrella2y = -2500
         
#...................................................................#
#Choques.

    if amarilloy > 365  and amarilloy < 440 and abs (pos-amarillox) < 45 :
        niveles = 'Level 1'
        amarilloy = 0
        negroy = 0
        blancoy = 0
        senal20y = -90
        senal40y = -90
        senal80y = -90
        senal100y = -90
        senal120y = -90
        estrellay = -1500
        estrella2y = -2500
        manchay = -1000
        manchax = randint (214,550)
        amarillox = randint(214,550)
        blancox = randint (214,550)
        negrox = randint (214,550)
        explosiones()
        time.sleep(1)
        mostrarMenu()
       
        puntos= puntos - puntos

    if blancoy > 400 and blancoy < 440 and abs (pos- blancox) < 45:
        niveles = 'Level 1'
        amarilloy = 0
        negroy = 0
        blancoy = 0
        senal20y = -90
        senal40y = -90
        senal80y = -90
        senal100y = -90
        senal120y = -90
        estrellay = -1500
        estrella2y = -2500
        manchay = -1000
        manchax = randint (214,550)
        amarillox = randint(214,550)
        blancox = randint (214,550)
        negrox = randint (214,550)
        explosiones()
        time.sleep(1)
        mostrarMenu()
        puntos= puntos - puntos
#.....................................................................#
#Explosiones.

    if negroy > 500 and negroy < 580 and abs (pos- negrox) < 45:
        niveles = 'Level 1'
        amarilloy = 0
        negroy = 0
        blancoy = 0
        senal20y = -90
        senal40y = -90
        senal80y = -90
        senal100y = -90
        senal120y = -90
        estrellay = -1500
        estrella2y = -2500
        manchay = -1000
        manchax = randint (214,550)
        amarillox = randint(214,550)
        blancox = randint (214,550)
        negrox = randint (214,550)
        
        explosiones()
        time.sleep(1)
        mostrarMenu()
        puntos= puntos - puntos
#.....................................................................#
            
#Modificar la posicion en funcion de la tecla pulsada
    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[K_LEFT]:
        pos = pos - 10
    if teclasPulsadas[K_RIGHT]:
        pos = pos + 10
    pygame.display.update()
    
#.....................................................................#
#No salirse de la carretera.
    if pos < 210:
        pos = 210
    elif pos > 555:
        pos = 555
    
    if estrellax < 210:
        estrellax  = 210
    elif estrellax > 555:
        estrellax = 555
        
    if estrella2x < 210:
        estrella2x  = 210
    elif estrella2x > 555:
        estrella2x = 555
        
    if amarilloy > 600:
        amarilloy = 0 
        amarillox = randint (214, 550)
    
    if manchay > 2000:
        manchay = -200
        manchax = randint (214, 550)
        
    if blancoy > 1000:
        blancoy = 0
        blancox = randint (214, 550)
    
    if negroy > 1000:
        negroy = 0
        negrox = randint (214, 550)
        
    if arbol1y > 900:
        arbol1y = 0
        arbol1x = randint(0, 120)
    
    if arbol2y > 900:
        arbol2y = 0
        arbol2x = randint(630, 850)
        
    if arbol3y > 2000:
        arbol3y = 0
        arbol3x = randint(0,120)
        
    if arbol4y > 2000:
        arbol4y = 0
        arbol4x = randint(630,850)
        
    if estrellay > 3000:
        estrellax = randint (214, 550)
        estrellay = -2000
        
    if estrella2y > 3000:
        estrella2x = randint (214, 550)
        estrella2y = -3000
        
    if linea > 2000:
        lineay = 0
        lineax1 = 305
#contador puntos:
    if amarilloy > 480 and amarilloy < 488:
        puntos = puntos + 100
    if blancoy > 480 and blancoy < 488:
        puntos = puntos +100
    if negroy > 400 and negroy < 405:
        puntos = puntos + 100
    if puntos > 2500 and amarilloy > 480 and amarilloy < 495:
        puntos = puntos +100
    if puntos > 2500 and blancoy > 480 and blancoy < 495:
        puntos = puntos +100
    if puntos > 2500 and negroy > 480 and negroy < 495:
        puntos = puntos +100
    
#control de puntos:
    if puntos > 700:
        amarilloy = amarilloy + 2
        blancoy = blancoy + 2
        negroy = negroy + 2
        senal40y += 4
        arbol1y = arbol1y + 2
        arbol2y = arbol2y + 2
        arbol3y = arbol3y + 2
        arbol4y = arbol4y + 2
        manchay = manchay + 2 
        
    if puntos > 2500:
        amarilloy = amarilloy + 2
        blancoy = blancoy + 2
        negroy = negroy + 2
        senal80y += 6
        arbol1y = arbol1y + 2
        arbol2y = arbol2y + 2
        arbol3y = arbol3y + 2
        arbol4y = arbol4y + 2
        manchay = manchay + 2 
    if puntos > 5000:
        amarilloy = amarilloy + 2
        blancoy = blancoy + 2
        negroy = negroy + 2
        senal100y += 8
        arbol1y = arbol1y + 2
        arbol2y = arbol2y + 2
        arbol3y = arbol3y + 2
        arbol4y = arbol4y + 2
        manchay = manchay + 2 
    if puntos > 10000:
        amarilloy = amarilloy + 2
        blancoy = blancoy + 2
        negroy = negroy + 2
        senal120y += 10
        arbol1y = arbol1y + 2
        arbol2y = arbol2y + 2
        arbol3y = arbol3y + 2
        arbol4y = arbol4y + 2
        manchay = manchay + 2 
    # cambio nivel
    
    if puntos > 700:
        niveles = 'Level 2'
        
    if puntos > 2500:
        niveles = 'Level 3'

    if puntos > 5000:
        niveles = 'Level 4'

    if puntos > 10000:
        niveles = 'Level 5'

    if puntos > 12499:
        niveles = 'Level 1'
        puntos= puntos - puntos
        mostrarFinal()
        senal20y = -90
        senal40y = -90
        senal80y = -90
        senal100y = -90
        senal120y = -90
        estrellay = -1500
        estrella2y = -2500
        manchay = -1000
        amarilloy = -100
        negroy = 0
        blancoy = -250
        pygame.display.update()

#Dibujar el color de fondo
    visor.blit(fondo, (0,0))

    #.....................................................................#
    
#Dibujar
    visor.blit(linea, (lineax1,lineay))
    visor.blit(linea, (406,lineay))
    visor.blit(linea, (511,lineay))
    visor.blit(mancha, (manchax, manchay))
    visor.blit(estrella, (estrellax, estrellay))
    visor.blit(estrella2, (estrella2x, estrella2y))
    visor.blit(coche, (pos,380))
    visor.blit(coche2, (amarillox,amarilloy-50))
    visor.blit(coche3, (blancox,blancoy-100))
    visor.blit(coche4, (negrox,negroy-200))
    visor.blit(arbol1, (arbol1x,arbol1y- 100))
    visor.blit(arbol2, (arbol2x,arbol2y- 250))
    visor.blit(arbol3, (arbol3x,arbol3y- 400))
    visor.blit(arbol4, (arbol4x,arbol4y- 600))
    visor.blit(senal20, (senal20x,senal20y))
    visor.blit(senal40, (senal40x,senal40y))
    visor.blit(senal80, (senal80x,senal80y))
    visor.blit(senal100, (senal100x,senal100y))
    visor.blit(senal120, (senal120x,senal120y))
    visor.blit(marcador, (615,10))
    visor.blit(reloj, (15,10))
    

    #.....................................................................#
    lineay += 2
    manchay += 2
    estrellay += randint (1,6)
    estrellax += randint (-50,50)
    estrella2y += randint (1,6)
    estrella2x += randint (-50,50)
    amarilloy += 4
    blancoy += 4
    negroy += 4
    arbol1y += 2
    arbol2y += 2
    arbol3y += 2
    arbol4y += 2
    senal20y += 2
    #.....................................................................#
    marcador1 = tipoLetra.render(str(puntos), True, BLANCO)
    visor.blit(marcador1, (630, 20, 30, 50))
    reloj1 = tipoLetra3.render(str(niveles), True, BLANCO)
    visor.blit(reloj1, (40, 40, 30, 50))
    pygame.display.update()
#.....................................................................#
