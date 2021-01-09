import pygame


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([640, 480])

    # imagen con sprites del personaje
    fondo = pygame.image.load('animals.png')
    # algoritmo de recorte de sprites, en imagenes con una matriz de sprites
    m=[]
    for j in range(8):
        ls=[]
        for i in range(12):
            cuadro = fondo.subsurface(i*32,j*32,32,32)
            ls.append(cuadro)
        m.append(ls)
    # ls=Recortar(fondo)

    fin = False
    con =0
    direccion = 0
    # variable que almacena los fps del juego
    reloj=pygame.time.Clock()
    while not fin:  # bucle infinito
        # esta condicion cambia la transicion de la animacion
        if con <2:
            con+=1
        else:
             con= 0
        reloj.tick(10)
        for event in pygame.event.get():  # para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direccion = 2  # direccion cambia el sentido de la animacion(ariba, abajo, etc)
                if event.key == pygame.K_LEFT:
                    direccion = 1
                if event.key == pygame.K_DOWN:
                    direccion = 0
                if event.key == pygame.K_UP:
                    direccion = 3
        #actualizacion grafica
        pantalla.fill([0,0,0])
        pantalla.blit(m[direccion][con],[320,240])
        pygame.display.flip()


if __name__ == '__main__': #programa principal
    main()
