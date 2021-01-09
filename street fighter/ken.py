import pygame
from pygame.locals import *
from colors import *
#1470 ancho
#2400 alto
class Jugador(pygame.sprite.Sprite):  # tipo de clase Sprite
    def __init__(self, m):  # constructor
        pygame.sprite.Sprite.__init__(self)  # constructor
        self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 1
        self.limites = [3, 3, 2, 4, 1, 3, 4, 4, 6, 0]
        self.con = 0  # contador para las transiciones de la animacion
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # obtiene un rectangulo en la pantalla
        # posicion del rectangulo que pertenece a el jugador en la pantalla
        self.rect.x = 350
        self.rect.y = 435
        self.velx = 0
        self.vely = 0
        self.fric = 1
        self.muerto = 0

    def update(self):  # metodo que cambia la transicion de la animacion
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.velx < 0:
            self.velx += self.fric
        #if self.velx != 0 or self.vely != 0:
        if self.con < self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.accion = 1
            self.con = 0  # reinicia el contador


class Hadoken(pygame.sprite.Sprite):
    def __init__(self, m):
        super().__init__()
        self.m = m  # matriz para guardar cada sprite recortado
        self.accion = 4
        self.limites = [3, 3, 2, 4, 1, 3, 4, 4, 6, 0]
        self.con = 0  # contador para las transiciones de la animacion
        self.velx = 20
        self.vely = 0
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velx
        self.image = self.m[self.accion][self.con]  # la imagen cambia respecto a las posiciones de m
        #if self.velx != 0 or self.vely != 0:
        if self.con < self.limites[self.accion]:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            if self.accion == 5 and self.con == self.limites[self.accion]:  # este sprite es de 3 imagenes
                self.rect.x = 1400
            else:
                self.accion = 4
                self.con = 0  # reinicia el contador

class Barravida1(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("barravida1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(18, 4)

    def update(self, jugador, hadouken2):
        self.j = jugador
        self.h2 = hadouken2
        if self.rect.x <= -152:  # pierde toda la vida
            self.j.muerto = 1
        if self.h2.rect.y >= (self.j.rect.y - 100):
            if self.h2.rect.y <= (self.j.rect.y + 200):
                if self.h2.rect.x >= self.j.rect.x:
                    if self.h2.rect.x <= (self.j.rect.x + 40):
                        self.rect.x -= 15
                        self.h2.accion = 5
                        self.h2.velx = 0
                        self.j.velx = -7