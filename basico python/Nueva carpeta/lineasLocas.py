import pygame
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
        #LEN: MEDIDA DE LA CADENA
        if len(ls_ptos)>0:
            a=ls_ptos[0]
            #TOMA LA POSICION DEL MOUSE
            b=pygame.mouse.get_pos()
            pantalla.fill(BLACK)
            pygame.draw.line(pantalla, BLUE, a, b)
            pygame.display.flip()
        if len(ls_ptos) == 2:
            a=ls_ptos[0]
            b=ls_ptos[1]
            pantalla.fill(BLACK)
            pygame.draw.line(pantalla, BLUE, a, b)
            pygame.display.flip()
            c=pygame.mouse.get_pos()
            pantalla.fill(BLACK)
            pygame.draw.line(pantalla, BLUE, b, c)
            pygame.display.flip()


