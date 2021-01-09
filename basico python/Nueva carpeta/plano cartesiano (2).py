import pygame
from colors import *
from planeFunctions import *

ANCHO = 640
ALTO = 480
Xcentro = ANCHO / 2
Ycentro = ALTO / 2

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    origenCentro = [Xcentro,Ycentro]#array centro de pantalla
    cartesianAxes(pantalla,origenCentro)#ejes X y Y al iniciar el programa
    triangulo = [[50,150],[50,50],[150,50]] #cordenadas del triangulo
    triangle(pantalla,triangulo)
    vectorA = [100,100]
    vectorB = [50,70]
    unitVector(pantalla,vectorA,[0,0])
    unitVector(pantalla,vectorB,[0,0])
    pygame.display.flip()

    fin = False
    while not fin:#bucle infinito
        for event in pygame.event.get():#para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:#eventos del mouse
                print(event.pos, event.button)
                if event.button == 1:
                    Point(pantalla, event.pos, RED)
                if event.button == 3:
                    pantalla.fill(BLACK)#refrescar pantalla
                    cartesianAxes(pantalla,event.pos)
                    triangle(pantalla, triangulo)
                    unitVector(pantalla, vectorA,[0,0])
                    unitVector(pantalla, vectorB, [0,0])

                    triangulito = [[0, 0], [0, 0], [0, 0]]#nueva lista auxiliar
                    a = planeTransformation(triangulo[0], event.pos)
                    b = planeTransformation(triangulo[1], event.pos)
                    c = planeTransformation(triangulo[2], event.pos)
                    triangulito[0] = a
                    triangulito[1] = b
                    triangulito[2] = c
                    triangle(pantalla, triangulito)

                    vectorcitoA = [[0, 0], [0, 0]]
                    vectorcitoB = [[0, 0], [0, 0]]
                    vectoresA = planeTransformation (vectorA, event.pos)
                    vectoresB = planeTransformation (vectorB, event.pos)
                    unitVector(pantalla, vectoresA, event.pos)
                    unitVector(pantalla, vectoresB, event.pos)
                    suma = [[0,0],[0,0]]
                    suma[0] = vectoresA[0] + vectoresB[0]
                    suma[1] = vectoresA[1] + vectoresB[1]
                    unitVector (pantalla, suma, event.pos)
                    pygame.display.flip()
                    print (event.pos)

if __name__ == '__main__': #programa principal
    main()
