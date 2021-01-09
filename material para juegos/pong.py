"""
 Muestra cómo rebotar una pelota usando una pala en Pygame.
 El programa asume que hay dos joysticks conectados.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
import pygame
import random
 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL =  (0, 0, 255)
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa sendas palas a cada lado de la pantalla.
        Deriva de la clase "Sprite" en Pygame """
 
    # Constructor. Pasa el color del bloque así como sus posiciones x e y
    def __init__(self, x, y, joystick_no):
        # Llama al constructor de la clase padre (Sprite)
        super().__init__() 
         
 
        # Variables que contienen el alto y largo del bloque
        self.largo = 10
        self.alto = 75
        self.mi_joystick = None
 
        # Crea una imagen de la pelota y rellénala de color.
        # También puedes usar una imagen guardada en el disco.
        self.image = pygame.Surface([self.largo, self.alto])
        self.image.fill(BLANCO)
 
        # Extrae el objeto rectángulo que posee las dimensiones de la imagen
        self.rect = self.image.get_rect()
         
        # Establece la ubicación inicial del sprite en las coordenadas 100,100
        self.rect.x = x
        self.rect.y = y
         
        # Cuenta el número de joysticks conectados al PC
        numero_de_joysticks = pygame.joystick.get_count()
        if numero_de_joysticks < joystick_no+1:
            # No hay joysticks!
            print("Error. No he encontrado suficientes joysticks. Solo hay ", numero_de_joysticks)
        else:
            # Usa joystick #0 e inicialízalo
            self.mi_joystick = pygame.joystick.Joystick(joystick_no)
            self.mi_joystick.init()
         
 
    def update(self):
        """ Actualiza la posición del protagonista. """
        # Mientras haya un joystick
        if self.mi_joystick != None:
         
            # Esto obtiene la posición del eje en el controlador de juego
            # Devuelve un número entre -1.0 y +1.0
            vert_axis_pos = self.mi_joystick.get_axis(1)   
             
             
            # Multiplicamos por 10 para acelerar el movimiento.
            self.rect.y = self.rect.y+vert_axis_pos*10
             
            # Si el jugador se mueve más allá de los límites de la pantalla, restablece la posición
            # sobre el borde.
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > alto_pantalla - self.alto:
                self.rect.y = alto_pantalla - self.alto
 
class Pared(pygame.sprite.Sprite):
    """ Esta clase representa las paredes en la partes superior e inferior de la
        pantalla. """
 
    # Función constructor
    def __init__(self, x, y, largo, alto):
        # Llama al constructor padre
        super().__init__()
 
        # Crea una pared AZUL con el tamaño especificado por los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill((AZUL))
 
        # Determina que la esquina superior izquierda sea la ubicación inicial.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
         
class Pelota(pygame.sprite.Sprite):
    """ Esta clase representa la pelota que rebota por ahí. """
 
    # Establece la velocidad del vector
    cambio_x = 0
    cambio_y = 0
    paredes = None
     
    # Función constructor
    def __init__(self, x, y, paredes):
        #  Llama al constructor de la clase padre
        super().__init__()
  
        # Establecemos el  alto, largo
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLANCO)
 
        # Determina que la esquina superior izquierda sea la ubicación inicial.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x        
        self.paredes = paredes
         
    def update(self):
        """ Actualiza la posición de la pelota. """
        # Obtiene la posición anterior para el caso que necesitemos volver a ella
        x_anterior = self.rect.x
        x_nueva = x_anterior + self.cambio_x
        self.rect.x = x_nueva
         
        # ¿Es que la última actualización hizo que la pelota chocara contra la pared?
        colisionar = pygame.sprite.spritecollide(self, self.paredes, False)
        if colisionar:
            # Ups! hemos dado contra la pared. Volvamos a la posición anterior
            self.rect.x = x_anterior
            self.cambio_x *= -1
 
        y_anterior = self.rect.y
        y_nueva = y_anterior + self.cambio_y
        self.rect.y = y_nueva
         
        #  ¿Es que la última actualización hizo que la pelota chocara contra la pared?
        colisionar = pygame.sprite.spritecollide(self, self.paredes, False)
        if colisionar:
            # Ups! hemos dado contra la pared. Volvamos a la posición anterior
            self.rect.y = y_anterior
            self.cambio_y *= -1
             
        if self.rect.x < -20 or self.rect.x > largo_pantalla + 20:
            self.cambio_x = 0
            self.cambio_y = 0
 
             
# Llamamos a esta función para que la biblioteca Pygame pueda inicializarse.
pygame.init()
 
# Creamos una pantalla de 800x600
largo_pantalla = 800
alto_pantalla = 600
 
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
 
# Establecemos el título de la ventana
pygame.display.set_caption('Test')
 
# Creamos una superficie sobre la que podamos dibujar
fondo_pantalla = pygame.Surface(pantalla.get_size())
 
# Usado para convertir cosas como mapa de colores
fondo_pantalla = fondo_pantalla.convert()
 
# Rellenamos la pantalla con color NEGRO
fondo_pantalla.fill(NEGRO)
 
# Listas de todos los sprites
lista_paredes = pygame.sprite.Group()
todos_los_sprites = pygame.sprite.Group()
sprites_en_movimiento = pygame.sprite.Group()
 
# Creamos a los protagonistas
protagonista1 = Protagonista(10, alto_pantalla/2, 0)
todos_los_sprites.add(protagonista1)
lista_paredes.add(protagonista1)
sprites_en_movimiento.add(protagonista1)
 
protagonista2 = Protagonista(largo_pantalla - 20, alto_pantalla/2, 1)
todos_los_sprites.add(protagonista2)
lista_paredes.add(protagonista2)
sprites_en_movimiento.add(protagonista2)
 
# Construimos las paredes. (x_pos, y_pos, largo, alto)
# Pared superior
pared = Pared(0, 0, largo_pantalla, 10) 
lista_paredes.add(pared)
todos_los_sprites.add(pared)
 
# Pared inferior
pared = Pared(0, alto_pantalla - 10, largo_pantalla, alto_pantalla) 
lista_paredes.add(pared)
todos_los_sprites.add(pared)
 
# Creamos la pelota
pelota = Pelota(-50, -50, lista_paredes )
sprites_en_movimiento.add(pelota)
todos_los_sprites.add(pelota)
 
reloj = pygame.time.Clock()
 
hecho = False
 
# Bucle principal
while not hecho:
     
    # Itera a través de cualquier evento de la ventana
    for evento in pygame.event.get():
        # El usuario hizo click sobre 'cerrar' o apretó las teclas Alt-F4
        if evento.type == pygame.QUIT:
            hecho = True
             
        # El usuario apretó un botón del ratón
        # o presionó una tecla
        elif evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
             
            # ¿No se está moviendo la pelota?
            if pelota.cambio_y == 0:
                 
                # Empieza en la mitad de la pantalla sobre una ubicación y aleatoria
                pelota.rect.x = largo_pantalla/2
                pelota.rect.y = random.randrange(10, alto_pantalla - 0)
                 
                # Establecemos un vector aleatorio
                pelota.cambio_y = random.randrange(-5, 6)
                pelota.cambio_x =  random.randrange(5, 10)
                 
                # ¿La pelota se dirige a la izquierda o a la derecha? Selecciona aleatoriamente
                if( random.randrange(2) == 0 ):
                    pelota.cambio_x *= -1
 
                 
    # Actualiza la posición de la pelota. Le pasamos la lista de objetos con los que puede rebotar
    sprites_en_movimiento.update()
     
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
     
    # Dibujamos los sprites
    todos_los_sprites.draw(pantalla)
 
    # Mostramos la pantalla
    pygame.display.flip()
 
    reloj.tick(30)
 
# Trabajo hecho, apagamos Pygame            
pygame.quit()