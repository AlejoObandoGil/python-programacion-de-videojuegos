import pygame
from libreria import *

ANCHO=640
ALTO=480

if __name__ == '__main__': #programa principal
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Punto(pantalla, [300,250], VERDE)#2 puntos al comenzar el programa
    Punto(pantalla, [250,100])
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event.pos, event.button)#imprime posicion del evento y numero del evento(1 o 3)
                if event.button == 1: #1 = click izquierdo
                    Punto(pantalla, event.pos , VERDE)
                    x=event.pos
                    print (x)
                if event.button == 3: #3 = click derecho
                    Punto(pantalla, event.pos, ROJO)
                    print (event.pos)
                    #dibuja linea(donde dibuja, color, posicion1, posicion2, ancho)
                    pygame.draw.line(pantalla, AZUL, [100,100], event.pos, 1)
            pygame.display.flip()
