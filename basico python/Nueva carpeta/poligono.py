import pygame
from libreria import *

ANCHO=640
ALTO=480

#LISTA QUE GUARDA LOS PUNTOS DIGITADOS
ptos=[]

if __name__ == '__main__':    
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event.pos, event.button)
                ptos.append(event.pos)#Guardar posiciones en la lista
        
        if len(ptos) == 5:#recorre toda la lista
            a=ptos[0]#guardamos las posciones en variables
            b=ptos[1]
            c=ptos[2]
            d=ptos[3]
            e=ptos[4]
            pantalla.fill(NEGRO)#borrar a color negro
            pygame.draw.polygon(pantalla, ROJO, [a,b,c,d,e], 2)#dibujamos el poligono
            pygame.display.flip()
            ls_ptos=[]#lista vacia

