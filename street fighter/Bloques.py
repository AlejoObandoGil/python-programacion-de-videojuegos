import pygame
from pygame.locals import *
from colors import *


class Bloque(pygame.sprite.Sprite):
    def __init__(self, pto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 80])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx = 0
        self.fric = 1

    def update(self):
        self.rect.x += self.velx
        if self.velx > 0:
            self.velx -= self.fric
