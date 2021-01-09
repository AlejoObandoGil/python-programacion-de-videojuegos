import pygame
from libreria import *

ANCHO=640
ALTO=480
r=1

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
                if event.button == 4:
                    pygame.draw.circle(pantalla, AZUL, event.pos, r)
                    r+=10
                    pygame.display.flip()

   
