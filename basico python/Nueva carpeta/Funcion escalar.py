import pygame
from planeFunctions import *
from colors import *
#type()saber el tipo de dato

#ANCHO = 640 ya viene defininida de planeFunctions
#ALTO = 480

if __name__ == '__main__':  # programa principal
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    origen=[600,350]
    cartesianAxes(pantalla, origen)
    A=[100,100]
    B=[250,100]
    C=[150,150]
    ls=[A,B,C]
    s=[2,2]
    lse=[]
    lsc=[]
    lsec=[]
    for e in ls:
        print(e)
        Point(pantalla,e,RED)
        ee=Stairs(e,s) # ee=escalar
        Point(pantalla, ee,RED)
        lse.append(ee)
        ec = planeTransformation(ee,origen)
        Point(pantalla,ec,GREEN)
        lsc.append(ec)
        eec = planeTransformation(e,origen)
        Point(pantalla,eec,GREEN)
        lsec.append(eec)
    pygame.draw.polygon(pantalla,WHITE,ls,1)
    pygame.draw.polygon(pantalla,WHITE,lse, 1)
    #pygame.draw.polygon(pantalla, WHITE, ls, 1)
    pygame.draw.polygon(pantalla,WHITE,lsc, 1)
    pygame.draw.polygon(pantalla,WHITE,lsec, 1)
    pygame.display.flip()
    fin = False
    while not fin:#bucle infinito
        for event in pygame.event.get():#para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:  # eventos del mouse
                print(event.pos, event.button)
                pygame.display.flip()