import pygame
from colors import *
from ken import *
from ryu import *
from Bloques import *
from parcialFunctions import *

# GLOBALES
ANCHO = 1280
ALTO = 720
pantalla = pygame.display.set_mode([ANCHO, ALTO])


# FUNCIONES
def recortar(m, s):
    for j in range(10):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(7):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro = s.subsurface(i * 210, j * 240, 210, 240)  # variable que almacena cada sprite recortado
            ls.append(cuadro)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m
"""
def recortar2(m, s): #recorte de ryu
    ancho = 194
    for j in range(1):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(5):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro2 = s.subsurface(i * (4 + ancho), j * 299, ancho, 299)  # variable que almacena cada sprite recortado
            ls.append(cuadro2)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m
"""
def recortar2(m, s):
    for j in range(10):  # alto de imagen / 32 pixeles cada sprite = N de sprites en columnas de la imagen
        ls = []
        for i in range(7):  # ancho de imagen / 32 pixeles = N sprites filas
            cuadro = s.subsurface(i * 210, j * 240, 210, 240)  # variable que almacena cada sprite recortado
            ls.append(cuadro)  # agregamos esos cuadros a la lista filas
        m.append(ls)  # agregamos esas listas a la matriz
    return m

def colisionLucha(j1,j2,bv2,vel):
    jugador = j1
    jugadores2 = j2
    barravida2 = bv2
    dist = 20
    if jugador.accion == 2 or jugador.accion == 6 or jugador.accion == 7:
        ls_colision = pygame.sprite.spritecollide(jugador, jugadores2, False)
        for b in ls_colision:
            linf = b.rect.bottom - dist
            print(b.rect.bottom)
            lsup = b.rect.bottom + dist
            if (linf < jugador.rect.bottom) and (jugador.rect.bottom < lsup):
                # colision de desplazamiento x y Y
                if jugador.rect.right > b.rect.left:
                    b.velx = vel
                    barravida2.rect.x += vel
                    # pass
                    # jugador.rect.right = b.rect.left
                    # jugador.velx = 10

# PRINCIPAL
def main():
    pygame.init()
    reloj = pygame.time.Clock()  # tiempo utilizado para la velocidad de animacion

    # BACKGROUNDS & SPRITES
    fondo = pygame.image.load('background-egypt.png')  # cargamos la imagen con su extension
    logo = pygame.image.load('SF_Logo.png')  # cargamos la imagen con su extension
    vs = pygame.image.load('vs2.png')  # cargamos la imagen con su extension
    spriteJugador = pygame.image.load('ken2.png')  # cargamos la imagen con su extension
    spriteJugador2 = pygame.image.load('ken2-ConvertImage.png')  # cargamos la imagen con su extension
    cuadrovida1 = pygame.image.load("cuadrovida1.png").convert_alpha()
    cuadrovida2 = pygame.image.load("cuadrovida2.png").convert_alpha()

    # BANDA SONORA
    pygame.mixer.music.load('Los Turros-Faltan 5 Pe.mp3')
    pygame.mixer.music.play()

    # GRUPOS & VARIABLES
    jugadores = pygame.sprite.Group()  # sprite del tipo group
    jugadores2 = pygame.sprite.Group()  # sprite del tipo group
    disparos = pygame.sprite.Group()
    matriz = []  # matriz para almacenar las animaciones
    matriz2 = []  # matriz para almacenar las animaciones
    punto = [700,400]
    vel1 = 7
    vel2 = -7

    # OBJETOS y FUNCIONES
    m = recortar(matriz, spriteJugador)
    m2 = recortar2(matriz2, spriteJugador2)
    jugador = Jugador(m)  # instanciamos un objeto de la clase Jugador
    jugador2 = Jugador2(m2)  # instanciamos un objeto de la clase Jugador
    hadoken = Hadoken(m)
    hadoken2 = Hadoken2(m2)
    barravida1 = Barravida1()
    barravida2 = Barravida2()
    jugadores.add(jugador)  # agregamos a jugadores
    jugadores2.add(jugador2)  # agregamos a jugadores

    # LOOP
    fin = False
    while not fin:
        for event in pygame.event.get():  # para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.velx = 15
                if event.key == pygame.K_LEFT:
                    jugador.velx = -15
                if event.key == pygame.K_DOWN:
                    jugador.vely = +15
                    jugador.accion = 9
                    jugador.con = 0
                if event.key == pygame.K_UP:
                    jugador.velx = 0
                    jugador.vely = -15
                if event.key == pygame.K_l:
                    jugador.accion = 2
                    jugador.con = 0
                if event.key == pygame.K_m:
                    jugador.accion = 6
                    jugador.con = 0
                if event.key == pygame.K_j:
                    jugador.accion = 7
                    jugador.con = 0
                if event.key == pygame.K_d:
                    jugador2.velx = 15
                if event.key == pygame.K_a:
                    jugador2.velx = -15
                if event.key == pygame.K_s:
                    jugador2.vely = -15
                    jugador2.accion = 9
                    jugador2.con = 6
                if event.key == pygame.K_w:
                    jugador2.velx = 0
                    jugador2.vely = +15
                if event.key == pygame.K_x:
                    jugador2.accion = 2
                    jugador2.con = 6
                if event.key == pygame.K_c:
                    jugador2.accion = 6
                    jugador2.con = 6
                if event.key == pygame.K_v:
                    jugador2.accion = 7
                    jugador2.con = 6
                if event.key == pygame.K_SPACE:
                    jugador2.accion = 0
                    jugador2.con = 6
                    hadoken2 = Hadoken2(m2)
                    hadoken2.rect.x = jugador2.rect.x - 100  # Configuramos el proyectil de forma que esté donde el protagonista
                    hadoken2.rect.y = jugador2.rect.y - 10
                    hadoken2.velx = -20
                    hadoken2.accion = 4
                    disparos.add(hadoken2)
                # Eliminamos los disparos que sobrepasan la pantalla
                if hadoken2.rect.x > 1280:
                    disparos.remove(hadoken2)
            if event.type == pygame.KEYUP:
                jugador.velx = 0
                jugador.vely = 0
                jugador2.velx = 0
                jugador2.vely = 0

            #HADOUKEN
            if event.type == pygame.MOUSEBUTTONDOWN:  # Disparamos un proyectil si el usuario presiona el botón del ratón
                jugador.accion = 0  # animacion hadouken
                jugador.con = 0
                hadoken = Hadoken(m)
                hadoken.rect.x = jugador.rect.x + 100# Configuramos el proyectil de forma que esté donde el protagonista
                hadoken.rect.y = jugador.rect.y - 10
                hadoken.velx = 20
                hadoken.accion = 4
                disparos.add(hadoken)
            # Eliminamos los disparos que sobrepasan la pantalla
            if hadoken.rect.x > 1280:
                disparos.remove(hadoken)

        # COLISIONES LUCHA
        colisionLucha(jugador, jugadores2, barravida2,vel1)
        colisionLucha(jugador2, jugadores, barravida1,vel2)

        # ACTUALIZACION GRAFICA
        pantalla.blit(fondo, (0, 0))  # refrescamos la pantalla
        pantalla.blit(logo, (460, 50))  # refrescamos la pantalla
        pantalla.blit(vs, (600, 10))  # refrescamos la pantalla
        jugadores.update()
        jugadores2.update()
        disparos.update()
        barravida1.update(jugador, hadoken2)
        barravida2.update(jugador2, hadoken)
        jugadores.draw(pantalla)  # dibujamos en pantalla
        jugadores2.draw(pantalla)  # dibujamos en pantalla
        disparos.draw(pantalla)
        pantalla.blit(barravida1.image, barravida1.rect)
        pantalla.blit(barravida2.image, barravida2.rect)
        pantalla.blit(cuadrovida1, (0, 0))
        pantalla.blit(cuadrovida2, (1088, 0))
        pygame.display.flip()

        reloj.tick(12)  # tiempo ajustado en 100 ms = 20 fps
    return 0


if __name__ == '__main__':  # programa principal
    main()
