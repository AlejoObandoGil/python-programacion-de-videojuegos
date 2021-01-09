import pygame


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([640, 480])
    #posiciones para colocar el patron en X = 0
    fondo = pygame.image.load('terrenogen.png')

    m=[]
    for j in range(12):
        ls=[]
        for i in range(32): 
            cuadro = fondo.subsurface(i*32,j*32,32,32)
            ls.append(cuadro)
        m.append(ls)
    #ls=Recortar(fondo)
    pantalla.blit(m[4][0],[300,200])
    pygame.display.flip()
    
    fondo = pygame.image.load('animals.png')

    m=[]
    for j in range(8):
        ls=[]
        for i in range(12): 
            cuadro = fondo.subsurface(i*32,j*32,32,32)
            ls.append(cuadro)
        m.append(ls)
    #ls=Recortar(fondo)
    pantalla.blit(m[5][1],[320,240])
    pygame.display.flip()  
 
 
    fin = False
    while not fin:#bucle infinito
        for event in pygame.event.get():#para cualquier evento de entrada
            if event.type == pygame.QUIT:
                fin = True


if __name__ == '__main__': #programa principal
    main()
