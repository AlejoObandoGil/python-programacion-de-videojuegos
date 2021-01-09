import pygame

pygame.init()
pantalla=pygame.display.set_mode([640,480])#tamaño de la pantalla
pygame.display.flip()
fin=False
while not fin:
    for event in pygame.event.get():# para eventos en pygame windows

        if event.type == pygame.QUIT:
            fin=True
        if event.type == pygame.KEYDOWN:
            #print ( 'tecla' )
            if event.key == pygame.K_b:
                print ( 'tecla b' )
            if event.key == pygame.K_SPACE:
                print ( 'tecla espacio' )
        if event.type == pygame.MOUSEBUTTONDOWN:
            print (event.pos, event.button)
