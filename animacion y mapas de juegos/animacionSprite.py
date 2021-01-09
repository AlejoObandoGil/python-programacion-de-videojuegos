import pygame
from Jugador import *
from colors import *


ANCHO = 800
ALTO = 600

def recortar(m, s):
    for j in range(8):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(12):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro = s.subsurface(i * 32, j * 32, 32, 32)  # variable que almacena cada sprite recortado
            ls.append(cuadro)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load('fondoPsico.gif')  # cargamos la imagen con su extension
    sprite = pygame.image.load('animals.png')  # cargamos la imagen con su extension
    reloj = pygame.time.Clock()  # tiempo utilizado para la velocidad de animacion
    # objetos
    jugadores = pygame.sprite.Group()  # sprite del tipo group
    matriz = []  # matriz para almacenar las animaciones de 3 x 4
    m = recortar(matriz,sprite)
    j = Jugador(m)  # instanciamos un objeto de la clase Jugador
    jugadores.add(j)  # agregamos a jugadores
    disparo = Disparo()

    fin = False
    while not fin:  # bucle infinito
        for event in pygame.event.get():  # para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
        # actualizacion grafica
        pantalla.blit(fondo,(0,0))  # refrescamos la pantalla
        j.movimiento()
        disparo.update(j)
        jugadores.draw(pantalla)  # dibujamos en pantalla
        pantalla.blit(disparo.image, disparo.rect)
        pygame.display.flip()
        reloj.tick(j.velocidad)  # tiempo ajustado en 100 ms
    return 0

if __name__ == '__main__':  # programa principal
    main()
