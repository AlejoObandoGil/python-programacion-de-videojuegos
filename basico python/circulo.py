import pygame
from libreria import *

ANCHO=640
ALTO=480

if __name__ == '__main__':    
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Punto(pantalla, [300,250], VERDE)
    Punto(pantalla, [250,100])
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event.pos, event.button)
                if event.button == 1:
                    Punto(pantalla, event.pos , VERDE)
                    x=event.pos
                    print (x)
                if event.button == 3:
                    Punto(pantalla, event.pos, ROJO)
                    print (event.pos)
                    pygame.draw.line(pantalla, AZUL, x, event.pos, 5)
            pygame.display.flip()
