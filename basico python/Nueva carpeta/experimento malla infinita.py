import pygame

ANCHO=1000
ALTO=700

pygame.init()
pantalla=pygame.display.set_mode([ANCHO, ALTO])

x=0
y=0

fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
        pygame.draw.line(pantalla, [0,255,0], [x,0], [x,400], 5)
        x=x+40
        pygame.draw.line(pantalla, [0,255,0], [0,y], [600,y], 5)
        y=y+40
        pygame.display.flip()
        
