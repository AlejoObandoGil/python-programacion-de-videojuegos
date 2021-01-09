import pygame

ANCHO=640
ALTO=480

pygame.init()
pantalla=pygame.display.set_mode([ANCHO,ALTO])

x=0
y=0

fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
    pygame.draw.line(pantalla, [0,255,0], [x,0], [x,ALTO], 2)
    pygame.draw.line(pantalla, [0,255,0], [0,y], [ANCHO,y], 2)
    pygame.display.flip()
    if x < ANCHO:
        x+=40
    if y < ALTO:
        y+=40
