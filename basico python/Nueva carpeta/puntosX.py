import pygame
from colors import *
from planeFunctions import *
from parcialFunctions import *

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption('¡Une los Puntos!')

    fuenteBásica = pygame.font.SysFont("Courier New", 20)
    # configurar el texto
    texto = fuenteBásica.render('¡4 clicks a la pantalla y mira la magia!:v', True, LIME)
    textRect = texto.get_rect()
    # dibujar rectangulo para el texto
    pygame.draw.rect(pantalla, BLACK, (textRect.left - 10, textRect.top - 10, textRect.width + 30, textRect.height + 30))
    # dibujar el texto sobre la superficie
    pantalla.blit(texto, textRect)
    #dibuja al iniciar el programa
    pygame.display.update()

    origenCentro = [Xcentro,Ycentro]#array centro de pantalla
    cartesianAxes(pantalla,origenCentro)#ejes X y Y al iniciar el programa

    listaPuntos=[]
    escala=[0.5,0.5]
    listaEscalado=[]
    i = 0

    fin = False
    while not fin:#bucle infinito
        for event in pygame.event.get():#para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:  # eventos del mouse
                pantalla.blit(texto, textRect)
                if event.button == 1:
                    cartesianAxes(pantalla, origenCentro)  # ejes X y Y al iniciar el programa
                    Point(pantalla, event.pos, RED)
                    #guardamos la posicion de los puntos en una lista
                    listaPuntos.append(event.pos)
                    if len(listaPuntos) > 3:
                        for l in listaPuntos:
                            escalar = Stairs(l,escala)
                            listaEscalado.append(escalar)
                            Point(pantalla,escalar,RED)

                        pygame.draw.line(pantalla, BLUE, listaPuntos[0], listaPuntos[2])
                        pygame.draw.line(pantalla, BLUE, listaPuntos[1], listaPuntos[3])
                        pygame.draw.line(pantalla, BLUE, listaEscalado[0], listaEscalado[2])
                        pygame.draw.line(pantalla, BLUE, listaEscalado[1], listaEscalado[3])
                        pygame.display.flip()
                        pantalla.fill(BLACK)
                        listaPuntos = []

if __name__ == '__main__':
    main()