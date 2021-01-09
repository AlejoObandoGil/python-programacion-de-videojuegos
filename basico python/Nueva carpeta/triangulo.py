import pygame
from colors import *
from planeFunctions import *

ANCHO=640
ALTO=480

#LISTA QUE GUARDA LOS PUNTOS DIGITADOS
ls_ptos=[]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                #DIBUJAMOS PUNTOS
                print (event.pos, event.button)
                #ADICIONAMOS PUNTOS A LA LISTA
                ls_ptos.append(event.pos)
                print(ls_ptos[0])

        if len(ls_ptos)>0: #tamaño cadena = len
            a=ls_ptos[0]
            b=pygame.mouse.get_pos()#posicion del mouse
            pantalla.fill(BLACK)
            pygame.draw.line(pantalla, BLUE, a, b)
            pygame.display.flip()
        if len(ls_ptos) == 2:
            a=ls_ptos[0]
            b=ls_ptos[1]
            pygame.draw.line(pantalla, BLUE, a, b)
            pygame.display.flip()
            c=pygame.mouse.get_pos()
            pygame.draw.line(pantalla, BLUE, b, c)
            pygame.display.flip()
        if len(ls_ptos) == 3:
            b=ls_ptos[1]
            c=ls_ptos[2]
            pygame.display.flip()
            pygame.draw.line(pantalla, BLUE, a, b)
            pygame.draw.line(pantalla, BLUE, b, c)
            pygame.draw.line(pantalla, BLUE, a, c)
            pygame.display.flip()
            ls_ptos=[]