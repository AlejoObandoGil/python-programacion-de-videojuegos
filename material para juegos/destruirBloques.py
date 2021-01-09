""" 
 Juego tipo Breakout
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
# --- Importamos las bibliotecas que usaremos en este programa
 
import math
import pygame
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
 
# Tamaño de los bloques break-out
largo_bloque = 23
alto_bloque = 15
 
class Bloque(pygame.sprite.Sprite):
    """Esta clase representa a cada bloque que será golpeado por la pelota.
    Deriva de la clase "Sprite" en Pygame """
 
    def __init__(self, color, x, y):
        """ Constructor. Pasa el color del bloque y su 
            posición x, y. """
         
        # Llama al constructor de la clase padre (Sprite)
        super().__init__()
         
        # Crea una imagen del bloque de tamaño apropiado
        # El largo y alto son enviados como una lista al primer parámetro.
        self.image = pygame.Surface([largo_bloque, alto_bloque])
         
        # Rellenamos la imagen con el color apropiado
        self.image.fill(color)
         
        # Extraemos el objeto rectángulo que posee las dimensiones de la imagen
        self.rect = self.image.get_rect()
         
        # Movemos la esquina superior izquierda del rectángulo a las coordenadas x,y.
        # Aquí es donde aparecerá nuestro bloque.
        self.rect.x = x
        self.rect.y = y
 
 
class Pelota(pygame.sprite.Sprite):
    """ Esta clase representa la pelota       
        Deriva de la clase "Sprite" en Pygame """
     
    # Velocidad en píxeles por ciclo
    velocidad = 10.0
     
    # Representación en coma flotante de la ubicación de la pelota
    x = 0.0
    y = 180.0
     
    # Rumbo de la pelota (en grados)
    rumbo = 200
 
    largo = 10
    alto = 10
     
    # Constructor. Pasa el color del bloque así como su posición x e y
    def __init__(self):
        # Llama al constructor de la clase padre (Sprite)
        super().__init__()
         
        # Crea la imagen de la pelota
        self.image = pygame.Surface([self.largo, self.alto])
         
        # Color de la pelota
        self.image.fill(BLANCO)
         
        # Obtiene un objeto rectángulo que muestra dónde se encuentra nuestra imagen
        self.rect = self.image.get_rect()
         
        # Obtiene los atributos para alto/largo de la pantalla
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
     
    def botar(self, diff):
        """ Está función hará botar la pelota 
            desde una superficie horizontal (no de una vertical) """
         
        self.rumbo = (180 - self.rumbo) % 360
        self.rumbo -= diff
     
    def update(self):
        """ Actualiza la posición de la pelota. """
        # Seno y Coseno trabajan con grados, por eso debemos convertirlos a radianes
        rumbo_radianes = math.radians(self.rumbo)
         
        # Cambia la posición (x e y) según la velocidad y el rumbo
        self.x += self.velocidad * math.sin(rumbo_radianes)
        self.y -= self.velocidad * math.cos(rumbo_radianes)
         
        # Mueve la imagen hacia las coordenadas x e y
        self.rect.x = self.x
        self.rect.y = self.y
         
        # ¿Hemos botado por fuera del borde superior de la pantalla?
        if self.y <= 0:
            self.botar(0)
            self.y = 1
             
        # ¿Hemos botado por fuera de la izquierda de la pantalla?
        if self.x <= 0:
            self.rumbo = (360 - self.rumbo) % 360
            self.x = 1
             
        # ¿Hemos botado por fuera de la derecha de la pantalla?
        if self.x > self.largo_pantalla - self.largo:
            self.rumbo = (360 - self.rumbo) % 360
            self.x = self.largo_pantalla - self.largo - 1
         
        # ¿Hemos botado por fuera del borde inferior de la pantalla?
        if self.y > 600:
            return True
        else:
            return False
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra de la parte inferior que controla el protagonista. """
     
    def __init__(self):
        """ Constructor para Protagonista. """
        # Llama al constructor padre
        super().__init__()
         
        self.largo = 75
        self.alto = 15
        self.image = pygame.Surface([self.largo, self.alto])
        self.image.fill((BLANCO))
         
        # Hacemos que la esquina superior izquierda se la ubicación a pasar.
        self.rect = self.image.get_rect()
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = self.alto_pantalla-self.alto
     
    def update(self):
        """ Actualiza la posición del protagonista. """
        # Obtenemos la posición del ratón
        pos = pygame.mouse.get_pos()
        # Sitúa la barra del lado izquierdo del jugador en la posición del ratón
        self.rect.x = pos[0]
        # Asegúrate de que no empujamos la pala del protagonista 
        # por fuera del borde derecho de la pantalla 
        if self.rect.x > self.largo_pantalla - self.largo:
            self.rect.x = self.largo_pantalla - self.largo
 
#Llamamos a esta función para que la biblioteca Pygame pueda inicializarse.
pygame.init()
 
#Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])
 
# Establecemos el título de la ventana
pygame.display.set_caption('Breakout')
 
# Haz esto para que el ratón desaparezca cuando se encuentre sobre nuestra ventana
pygame.mouse.set_visible(0)
 
# Esta es la fuente que usaremos para dibujar texto sobre pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Creamos una superficie sobre la que podamos dibujar
fondo_pantalla = pygame.Surface(pantalla.get_size())
 
# Listas de todos los sprites
bloques = pygame.sprite.Group()
pelotas = pygame.sprite.Group()
todos_los_sprites = pygame.sprite.Group()
 
# Creamos el objeto pala del protagonista
protagonista = Protagonista()
todos_los_sprites.add(protagonista)
 
# Creamos las pelotas
pelota = Pelota()
todos_los_sprites.add(pelota)
pelotas.add(pelota)
 
# La parte superior del bloque (posición y)
top = 80
 
# Número de bloques a crear
numero_de_bloques = 32
 
# --- Creamos los bloques
 
# Cinco filas de bloques
for fila in range(5):
    # 32 columnas de bloques
    for columna in range(0, numero_de_bloques):
        # Crea un bloque (color,x,y)
        bloque = Bloque(AZUL, columna * (largo_bloque + 2) + 1, top)
        bloques.add(bloque)
        todos_los_sprites.add(bloque)
    # Mueve  hacia abajo el borde superior de la siguiente fila
    top += alto_bloque + 2
 
# Reloj para limitar la velocidad
reloj = pygame.time.Clock()
 
# ¿Se acabó el juego?
game_over = False
 
# ¿Salir del programa?
salir_programa = False
 
# Bucle principal
while not salir_programa:
 
    # Limitamos a 30 fps
    reloj.tick(30)
 
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
     
    # Procesamos los eventos en el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salir_programa = True
     
    # Mientras que el juego no acabe, actualizamos las posiciones del protagonista 
    # y las pelotas.
    if not game_over:
        #actualizamos las posiciones del protagonista y las pelotas.
        protagonista.update()
        game_over = pelota.update()
     
    # Si terminamos, imprimir game over
    if game_over:
        texto = fuente.render("Game Over", True, BLANCO)
        textopos = texto.get_rect(centerx=fondo_pantalla.get_width()/2)
        textopos.top = 300
        pantalla.blit(texto, textopos)
     
    # Observamos si las pelotas chocan contra la pala del protagonista.
    if pygame.sprite.spritecollide(protagonista, pelotas, False):
        # El 'diff' te permite intentar botar las pelotas hacia la izquierda o derecha 
        # dependiendo por que parte de la pala las golpees
        diff = (protagonista.rect.x + protagonista.largo/2) - (pelota.rect.x+pelota.largo/2)
         
        # Establece la posición 'y' de la pelota en caso la golpees 
        # con el borde la pala
        pelota.rect.y = pantalla.get_height() - protagonista.rect.alto - pelota.rect.alto - 1
        pelota.botar(diff)
     
    # Comprueba las colisiones entre las pelotas y los bloques
    bloquesmuertos = pygame.sprite.spritecollide(pelota, bloques, True)
     
    # Si le damos a un bloque, botamos las pelotas
    if len(bloquesmuertos) > 0:
        pelota.botar(0)
         
        # El juego se termina si todos los bloques desaparecen.
        if len(bloques) == 0:
            game_over = True
     
    # Dibujamos Todo
    todos_los_sprites.draw(pantalla)
 
    # Actualizamos la pantalla para mostrar todo lo dibujado
    pygame.display.flip()
 
pygame.quit()