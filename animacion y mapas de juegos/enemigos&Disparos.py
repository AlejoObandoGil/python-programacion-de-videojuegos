import pygame
from Jugador import *
from colors import *
from Enemigos import *


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

def recortarZombie(m, s):
    for j in range(3):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(8):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadroZombie = s.subsurface(i * 62, j * 66, 62, 66)  # variable que almacena cada sprite recortado
            ls.append(cuadroZombie)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load('fondoPsico.gif')  # cargamos la imagen con su extension
    spriteJugador = pygame.image.load('animals.png')  # cargamos la imagen con su extension
    spriteZombie = pygame.image.load('zombie 3.png')
    reloj = pygame.time.Clock()  # tiempo utilizado para la velocidad de animacion
    #listas
    jugadores = pygame.sprite.Group()  # sprite del tipo group
    zombies = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    # objetos
    matriz = []  # matriz para almacenar las animaciones de 3 x 4
    matrizZombie = []
    m = recortar(matriz, spriteJugador)
    mz = recortarZombie(matrizZombie, spriteZombie)
    jugador = Jugador(m)  # instanciamos un objeto de la clase Jugador
    zombie = EnemigoZombie(mz)  # instanciamos un objeto de la clase Jugador
    jugadores.add(jugador)  # agregamos a jugadores
    zombies.add(zombie)  # agregamos a jugadores


    fin = False
    while not fin:  # bucle infinito
        for event in pygame.event.get():  # para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Disparamos un proyectil si el usuario presiona el botón del ratón
                disparo = Disparo()
                # Configuramos el proyectil de forma que esté donde el protagonista
                disparo.rect.x = jugador.rect.x + 15
                disparo.rect.y = jugador.rect.y + 10
                disparos.add(disparo)

        # actualizacion grafica
        pantalla.blit(fondo, (0, 0))  # refrescamos la pantalla
        jugador.movimiento()
        disparos.update()
        zombie.movimiento()
        jugadores.draw(pantalla)  # dibujamos en pantalla
        zombies.draw(pantalla)
        disparos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)  # tiempo ajustado en 100 ms = 20 fps
    return 0


if __name__ == '__main__':  # programa principal
    main()
