import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 800
HEIGHT = 800

def update(win):
	win.fill(BLACK)
	pygame.display.update()


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pygame_template')
RUN = True

while RUN:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			break
	update(win)

pygame.quit()