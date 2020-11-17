import pygame
import math
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 800
HEIGHT = 800

class Boundary:
	def __init__(self, x1, y1, x2, y2):
		self.a = [x1, y1]
		self.b = [x2, y2]

	def show(self, win):
		pygame.draw.line(win, WHITE, self.a, self.b, 2)

class Ray:
	def __init__(self, pos, angle):
		self.scale = 20
		self.pos = pos
		self.dir = [math.cos(angle), math.sin(angle)]


	def look_at(self, pos):
		self.dir[0] = pos[0] - self.pos[0]
		self.dir[1] = pos[1] - self.pos[1]
		m = math.sqrt(self.dir[0]**2 + self.dir[1]**2)
		if m > 0:
			self.dir[0]/=m
			self.dir[1]/=m

	def show(self, win):
		end_point = [round(self.pos[0] + self.dir[0]  * self.scale), round(self.pos[1] + self.dir[1]  * self.scale)]
		pygame.draw.line(win, WHITE, self.pos, end_point, 1)

	def cast(self, wall):
		x1 = wall.a[0]
		y1 = wall.a[1]
		x2 = wall.b[0]
		y2 = wall.b[1]

		x3 = self.pos[0]
		y3 = self.pos[1]
		x4 = self.pos[0] + self.dir[0]
		y4 = self.pos[1] + self.dir[1]

		den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
		if (den == 0):
			return
		t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
		u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

		if (t > 0 and t < 1 and u > 0):
			pt = [round(x1 + t * (x2 - x1)), round(y1 + t * (y2 - y1))]
			return pt
		else:
			return

class Particle:
	def __init__(self):
		self.pos = [round(WIDTH/2), round(HEIGHT/2)]
		self.rays = []
		for i in range(0, 720):
			self.rays.append(Ray(self.pos, math.radians(i/2)))

	def show(self, win):
		for ray in self.rays:
			ray.show(win)

	def update(self, pos):
		self.pos[0] = pos[0]
		self.pos[1] = pos[1]

	def look(self, win, walls):
		for ray in self.rays:
			closest = 0
			record = 100000
			for wall in walls:
				pt = ray.cast(wall)
				if pt:
					d = math.sqrt((self.pos[0] - pt[0])**2 + (self.pos[1] - pt[1])**2)
					if d < record:
						record = d
						closest = pt
			if closest:
				pygame.draw.line(win, WHITE, self.pos, closest, 1)

def update(win):
	win.fill(BLACK)
	for wall in walls:
		wall.show(win)
	particle.update(pygame.mouse.get_pos())
	particle.show(win)
	particle.look(win, walls)

	pygame.display.update()

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Casting Simulation')
RUN = True

particle = Particle()
walls = []
walls.append(Boundary(0, 0, WIDTH, 0))
walls.append(Boundary(0, 0, 0, HEIGHT))
walls.append(Boundary(0, HEIGHT, WIDTH, HEIGHT))
walls.append(Boundary(WIDTH, HEIGHT, WIDTH, 0))
for i in range(5):
	walls.append(Boundary(randint(0, WIDTH), randint(0, HEIGHT), 
						  randint(0, WIDTH), randint(0, HEIGHT)))

while RUN:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
			break
	update(win)

pygame.quit()



