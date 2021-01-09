#hacer un triangulo estatico y cambiarle de tamaño con la rueda del mouse
import pygame
from colors import *
from planeFunctions import *

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    origen=[600,350]
    #cartesianAxes(pantalla, origen)
    A=[300,300]
    B=[450,300]
    C=[350,350]
    ls=[A,B,C]
    vs=1
    s=[2,2]
    lse =[A,B,C]

    pygame.display.flip()

    fin = False
    while not fin:#bucle infinito
        for event in pygame.event.get():#para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:#eventos del mouse
                print(event.pos, event.button)

                if event.button == 4:
                     vs+=0.5
                     s[0] += vs
                     s[1] += vs
                     lse=[]
                if event.button == 5:
                     vs-=0,2
                     s[0] -= vs
                     s[1] -= vs
