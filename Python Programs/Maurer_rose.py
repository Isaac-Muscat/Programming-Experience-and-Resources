import pygame
import math
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 800
HEIGHT = 800

def update(win):
	global d, n
	win.fill(BLACK)
	i = 0
	k = i * d
	r = 150 * math.sin(n*k)
	x1 = (r * math.cos(k)) + OFFSET[0]
	y1 = (r * math.sin(k)) + OFFSET[1]

	for i in range(1, 361):
		k = i * d
		r = 150 * math.sin(n*k)
		x2 = (r * math.cos(k)) + OFFSET[0]
		y2 = (r * math.sin(k)) + OFFSET[1]

		pygame.draw.line(win, WHITE, [x1, y1], [x2, y2])
		x1 = x2
		y1 = y2
	d+=0.01
	n+=0.01
	time.sleep(0.5)
	pygame.display.update()


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maurer Rose')
RUN = True

OFFSET = [round(WIDTH/2), round(HEIGHT/2)]

d = 0
n = 0

while RUN:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			break
	update(win)

pygame.quit()