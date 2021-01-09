import pygame
from colors import *

ANCHO = 1280
ALTO = 720
Xcentro = ANCHO / 2
Ycentro = ALTO / 2

#dibuja un patron de dos lineas con la posicion que se quiera
def patreon(p, origen, linea1, linea2):
    pygame.draw.line(p, LIME, [origen[0],origen[1]], [linea1[0], linea1[1]], 1)
    pygame.draw.line(p, LIME, [origen[0],origen[1]], [linea2[0], linea2[1]], 1)

def figure(p,listaPuntos):
    a = listaPuntos[0]
    b = listaPuntos[1]
    c = listaPuntos[2]
    d = listaPuntos[3]
    pygame.draw.line(p, BLUE, a, c)
    pygame.draw.line(p, BLUE, b, d)
    pygame.display.flip()
    p.fill(BLACK)
#trasnforma de 1 cuadrante al 4 cuadrante
def planeTransformation(pto, origen):
    xp = -pto[0] + origen[0]
    yp = pto[1] + origen[1]
    return [xp, yp]
#trasnforma de 3 cuadrante al 4 cuadrante
#def planeTransformation3a4(pto, origen):
 #   xp = -pto[0] + origen[0]
  #  yp = pto[1] + origen[1]
   # return [xp, yp]

