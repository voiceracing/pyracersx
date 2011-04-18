# -*- coding: cp1252 -*-


# Jogo do macaco - Treino 1


# Primeiro, importe os modulos pygame, sys e os

import pygame, sys, os
from pygame.locals import *

if not pygame.font: print "Fontes desabilitadas"
if not pygame.mixer: print "Sons desabilitados"


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image: ", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound: pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print "Cannot load sound: ", name
        raise SystemExit, message
    return sound

class Fist(pygame.sprite.Sprite):
    """Move um punho pela tela, seguindo o mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("fist.bmp", -1)
        self.punching = 0

    def update(self):
        "Move o punho baseado na posição do mouse"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5 , 10)

    def punch(self, target):
        "Retorna True se o punho colidir com o alvo"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        "só para colocar o punho de volta no jogo"
        self.punching = 0

class Chimp(pygame.sprite.Sprite):
    """ Move o macaco sobre a tela e o para quando leva um soco"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0

    def update(self):
        "Anda ou Para, dependendo do estado do macaco"
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        "move o macaco sobre a tela, retornando nos cantos"
        newpos = self.rect.move((self.move,0))
        if self.rect.left < self.area.left or self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pugame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        "para a imagem do macaco"
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def punched(self):
        "faz com que o macaco começe a girar"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image

pygame.init()
screen = pygame.display.set_mode((468, 60))
pygame.display.set_caption("Febre do macaco")
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)








whiff_sound = load_sound('whiff.wav')
punch_sound = load_sound('punch.wav')
chimp = Chimp()
fist = Fist()
allsprites = pygame.sprite.RenderPlain((fist, chimp))
clock = pygame.time.Clock()

while 1:
    clock.tick(60)

for event in pygame.event.get():
    if event.type == QUIT:
        sys.exit()
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
        if fist.punch(chimp):
            punch_sound.play() #punch
            chimp.punched()
        else:
            whiff_sound.play() #miss
    elif event.type == MOUSEBUTTONUP:
        fist.unpunch()


allsprites.update()

screen.blit(background, (0, 0))
allsprites.draw(screen)
pygame.display.flip()
