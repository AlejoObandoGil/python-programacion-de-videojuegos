import pygame
from pygame.locals import *
from colors import *


class Jugador(pygame.sprite.Sprite):  # tipo de clase Sprite
    def __init__(self, m):  # constructor
        pygame.sprite.Sprite.__init__(self)  # constructor
        self.m = m  # matriz para guardar cada sprite recortado
        self.direccion = 4
        self.con = 7  # contador para las transiciones de la animacion
        self.velocidad = 5
        self.image = self.m[self.direccion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # obtiene un rectangulo en la pantalla
        # posicion del rectangulo que pertenece a el jugador en la pantalla
        self.rect.x = 370
        self.rect.y = 300

    def update(self):  # metodo que cambia la transicion de la animacion
        self.image = self.m[self.direccion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.con > 6:  # este sprite es de 3 imagenes
            self.con -= 1
        else:
            self.con = 8  # reinicia el contador

    def movimiento(self):
        teclas = pygame.key.get_pressed()
        # asignamos las teclas en el atributo direccion
        if teclas[K_LEFT]:
            self.direccion = 5
            self.update()
            if self.rect.x > 0:
                self.rect.x -= self.velocidad
        if teclas[K_RIGHT]:
            self.direccion = 6
            self.update()
            if self.rect.x < 768:
                self.rect.x += self.velocidad
        if teclas[K_DOWN]:
            self.direccion = 4
            self.update()
            if self.rect.y < 568:
                self.rect.y += self.velocidad
        if teclas[K_UP]:
            self.direccion = 7
            self.update()
            if self.rect.y > 0:
                self.rect.y -= self.velocidad

class Disparo(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.velocidad = 25
        self.image = pygame.image.load("disparo.gif").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocidad

