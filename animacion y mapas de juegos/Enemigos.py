import pygame
from pygame.locals import *
from colors import *

#42 ancho columnas 1600 ancho imagen
#55 alto filas 600 alto imagen
class EnemigoZombie(pygame.sprite.Sprite):  # tipo de clase Sprite
    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)  # constructor
        self.m = m  # matriz para guardar cada sprite recortado
        self.direccion = 2
        self.con = 0  # contador para las transiciones de la animacion
        self.velocidad = 3
        self.image = zombie = self.m[self.direccion][self.con]  # la imagen cambia respecto a las posiciones de m
        self.rect = self.image.get_rect()  # obtiene un rectangulo en la pantalla
        # posicion del rectangulo que pertenece a el jugador en la pantalla
        self.rect.x = 100
        self.rect.y = 100

    def update(self):  # metodo que cambia la transicion de la animacion
        self.image = self.m[self.direccion][self.con]  # la imagen cambia respecto a las posiciones de m
        if self.con < 7:  # este sprite es de 3 imagenes
            self.con += 1
        else:
            self.con = 0  # reinicia el contador

    def movimiento(self):
        teclas = pygame.key.get_pressed()
        # asignamos las teclas en el atributo direccion
    #if teclas[K_LEFT]:
        self.direccion = 2
        self.update()
        if self.rect.x < 640:
            if self.rect.x > 0:
                self.rect.x += self.velocidad





