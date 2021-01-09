import pygame
from libreria import *

ANCHO = 640
ALTO = 480

if __name__ == '__main__': #programa principal
    pygame.init()

    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    x = ANCHO / 2
    y = ALTO / 2
    ejeX = pygame.draw.line(pantalla, VERDE, [x, 0], [x, ALTO], 1)
    ejeY = pygame.draw.line(pantalla, VERDE, [0, y], [ANCHO, y], 1)
    #pygame.display.flip()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                 print(event.pos, event.button)
                 if event.button == 1:
                    Punto(pantalla, event.pos, ROJO)
                    punto = event.pos - (ANCHO,ALTO)
                    print (event.pos)
            pygame.display.flip()
        
