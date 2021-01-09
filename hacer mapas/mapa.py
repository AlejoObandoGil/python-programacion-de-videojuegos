import configparser
import pygame

pygame.init()
pantalla=pygame.display.set_mode([600,400])


mapa=configparser.ConfigParser()
mapa.read('mapa.map')
archivo=mapa.get('info','imagen')
fondo=pygame.image.load(archivo)
m=[]
for j in range(12):
    ls=[]
    for i in range(32):
        cuadro=fondo.subsurface(i*32,j*32,32,32)
        ls.append(cuadro)
    m.append(ls)

'''
print(mapa.sections())
print(mapa.get('info','imagen'))
mp=mapa.get('info','mapa')
print(mp)
print(mapa.get('#','tipo'), mapa.get('#','fil'))
'''
for s in mapa.sections():
    if s == 'info':
        print ('archivo: ', mapa.get('info','imagen'))
        print ('mapa: ', mapa.get('info','mapa'))
    else:
        print ('objeto y tipo: ', s,mapa.get(s,'tipo'))
        f=int(mapa.get(s,'fil'))
        c=int(mapa.get(s,'col'))
        print('filas:  ',f, type(f))
        pantalla.blit(m[f][c],[100,100])

mp=mapa.get('info','mapa')
mp=mp.split('\n')
print(mp,type(mp))
print (mp[0])
for e in mp[0]:
    print (e,mapa.get(e,'tipo'), mapa.get(e,'fil'))

pygame.display.flip()
fin=False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
