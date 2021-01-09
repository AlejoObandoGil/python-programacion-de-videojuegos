import pygame
from pygame.locals import *
from colors import *
from parcialFunctions import *


# 80 ancho columnas 326 ancho imagen
# 110 alto filas 94 alto imagen
class Jugador2(pygame.sprite.Sprite):  # tipo de clase Sprite
    def __init__(self, m, pto):
        pygame.sprite.Sprite.__init__(self)
        self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 0
        self.limites = [3, 0]
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # obtiene un rectangulo en la pantalla
        # posicion del rectangulo que pertenece a el jugador en la pantalla
        self.rect.x = pto[0]
        self.rect.y = pto[1]
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
        if self.con < self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.accion = 1
            self.con = 0


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
                    if self.h.rect.x <= (self.j2.rect.x + 100):
                        self.rect.x += 15
                        self.h.accion = 5
                        self.h.velx = 0
                        self.j2.velx = 7