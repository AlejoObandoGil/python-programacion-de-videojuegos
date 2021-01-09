import pygame

pygame.init()
pantalla=pygame.display.set_mode([640,480])
y=50
x1=100
x2=250
pygame.draw.line(pantalla, [0,255,0], [x1,y], [x2,y], 1) #rectangulo - lineas: color, posicion, tamaño
pygame.draw.circle(pantalla, [255,255,255], [300,250], 40, 1)#circulo: color, posicion, tamaño

pygame.display.flip()
fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:#Si hay evento tecla arriba
                y-=20 #Auemnta o disminuye posicion en pantalla
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla, [0,255,0], [x1,y], [x2,y], 15)
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                y+=20
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla, [0,255,0], [x1,y], [x2,y], 15)
                pygame.draw.circle(pantalla, [255, 255, 255], [300, 250], 40, 1)#circulo
                pygame.display.flip()                   
            if event.key == pygame.K_RIGHT:
                x1+=20
                x2+=20
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla, [0,255,0], [x1,y], [x2,y], 15)
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                x1-=20
                x2-=20
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla, [0,255,0], [x1,y], [x2,y], 15)
                pygame.display.flip() 
