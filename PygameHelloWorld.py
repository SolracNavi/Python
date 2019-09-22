import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the windows
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# Setear los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setear las fuentes
basicFont = pygame.font.SysFont(None, 48)

# Setear el texto
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Dibujar el fondo blanco
windowSurface.fill(WHITE)

# Dibujar un polígono verde
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Dibujar unas lineas azules
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# Circulo azul
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Elipse roja
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Rectangulo de fondo de texto
pygame.draw.rect(windowSurface, RED, (textRect.left -20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# dibujar el texto
windowSurface.blit(text, textRect)

# dibujar la ventana
pygame.display.update()

# ejecutar el loop de juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

