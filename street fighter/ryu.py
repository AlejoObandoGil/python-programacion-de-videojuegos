import pygame
from pygame.locals import *
from colors import *
from parcialFunctions import *

#1470 ancho
#2400 alto
class Jugador2(pygame.sprite.Sprite):  # tipo de clase Sprite
    def __init__(self, m):  # constructor
        pygame.sprite.Sprite.__init__(self)  # constructor
        self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 1
        self.limites = [3, 3, 4, 2, 5, 3, 2, 2, 0, 6]
        self.con = 6  # contador para las transiciones de la animacion
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # obtiene un rectangulo en la pantalla
        # posicion del rectangulo que pertenece a el jugador en la pantalla
        self.rect.x = 650
        self.rect.y = 435
        self.velx = 0
        self.vely = 0
        self.fric = 1
        self.muerto = 0

    def update(self):
        self.rect.x += self.velx
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.velx > 0:
            self.velx -= self.fric
        # if self.velx != 0 or self.vely != 0:
        if self.con > self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con -= 1
        else:
            self.accion = 1
            self.con = 6


class Hadoken2(pygame.sprite.Sprite):
    def __init__(self, m):
        super().__init__()
        self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 4
        self.limites = [3, 3, 4, 2, 5, 3, 2, 2, 0, 6]
        self.con = 0  # contador para las transiciones de la animacion
        self.velx = - 20
        self.vely = 0
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velx
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        #if self.velx != 0 or self.vely != 0:
        if self.con > self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con -= 1
        else:
            if self.accion == 5 and self.con == self.limites[self.accion]:  # este sprite es de 3 imagenes
                self.rect.x = 1400
            else:
                self.accion = 4
                self.con = 6  # reinicia el contador

class Barravida2(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("barravida2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(1092, 4)

    def update(self, jugador2, hadouken):
        self.j2 = jugador2
        self.h = hadouken
        if self.rect.x >= 782:
            self.j2.muerto = 1
        if self.h.rect.y >= (self.j2.rect.y - 100):
            if self.h.rect.y <= (self.j2.rect.y + 200):
                if self.h.rect.x >= self.j2.rect.x:
                    if self.h.rect.x <= (self.j2.rect.x + 30):
                        self.rect.x += 15
                        self.h.accion = 5
                        self.h.velx = 0
                        self.j2.velx = 7