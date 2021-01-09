import pygame
from colors import *

ANCHO = 1200
ALTO = 700
Xcentro = ANCHO / 2
Ycentro = ALTO / 2

def Point(p, posicion, cl=[255,255,255]):
    pygame.draw.circle(p,cl,posicion,2)
    pygame.display.flip()

def cartesianAxes(p, origen = []):
    pygame.draw.line(p, LIME, [origen[0], 0], [origen[0], ALTO], 1)
    pygame.draw.line(p, LIME, [0, origen[1]], [ANCHO, origen[1]], 1)
    pygame.display.flip()

#crea un vector unitario posOrigen=(0,0)
def unitVector(p, posCabeza,posCola):
    Point(p, posCabeza, RED)
    pygame.draw.line(p, CYAN, posCola, posCabeza, 2)

def triangle(p,coordenadas):
    pygame.draw.line(p, CYAN, coordenadas[0], coordenadas[1], 2)
    pygame.draw.line(p, CYAN, coordenadas[1], coordenadas[2], 2)
    pygame.draw.line(p, CYAN, coordenadas[2], coordenadas[0], 2)

def planeTransformation(pto,origen):
    xp = pto[0]+origen[0]
    yp = -pto[1]+origen[1]
    return [xp, yp]

def Stairs(pto,s):
    xp = pto[0] * s[0]
    yp = pto[1] * s[1]
    return [int (xp), int (yp)]

#def triangleTransfor(triangulo):

