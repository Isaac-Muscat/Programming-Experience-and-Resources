import pygame
import random
from NeuralNetwork import NeuralNetwork
from LinearAlgebra import Matrix
import copy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Pipe:
	def __init__(self):
		self.space = 125
		self.top = random.randint(100, height-(100+self.space))
		self.bottom = height-self.top-self.space
		self.x = width
		self.w = 70
		self.speed = 8
		self.passed = 0

	def hits(self, bird):
		if(bird.y - round(bird.size/2) < self.top or bird.y+round(bird.size/2) > height-self.bottom):
			if(bird.x+round(bird.size/2) > self.x and bird.x-round(bird.size/2) < self.x + self.w):
				return True

	def show(self, win):
		pygame.draw.rect(win, WHITE, (self.x, 0, self.w, self.top))
		pygame.draw.rect(win, WHITE, (self.x, height-self.bottom, self.w, self.bottom))

	def update(self):
		self.x -= self.speed
		if(self.x < 32 and self.passed <2):
			self.passed += 1




class Bird:
	def __init__(self, color):
		self.y = round(height/2)
		self.x = 64
		self.size = 18
		self.color = color
		self.gravity = 0.5
		self.lift = -10
		self.vel = 0

		self.score = 0
		self.fitness = 0
		self.brain = NeuralNetwork(5, 6, 2)

	def think(self, pipes):

		closest = pipes[0]
		closestD = 10000
		for i in range(len(pipes)):
			d = (pipes[i].x + pipes[i].w) - self.x
			if d<closestD and d > 0:
				closest = pipes[i]
				closestD = d

		inputs = []
		inputs.append(self.vel /10)
		inputs.append(self.y / height)
		inputs.append(closest.top / height)
		inputs.append(closest.bottom / height)
		inputs.append(closest.x / width)

		output = self.brain.predict(inputs)
		if(output.matrix[0][0] > output.matrix[1][0]):
			self.up()

	def up(self):
		self.vel += self.lift
 
	def show(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

	def update(self):
		self.score += 1
		self.vel += self.gravity
		self.vel *= 0.95
		self.y = round(self.vel + self.y)
			
def next_generation(saved_birds):
	calculate_fitness(saved_birds)

	for i in range(TOTAL_POP):
		birds.append(pick_one(saved_birds))
	saved_birds.clear()

def pick_one(saved_birds):
	index = 0
	r = random.random()
	while r>0:
		r = r - saved_birds[index].fitness
		index+=1
	index-=1

	child = copy.deepcopy(saved_birds[index])
	child.brain.mutate(0.1)
	return child

def calculate_fitness(saved_birds):
	s = 0
	for bird in saved_birds:
		s += bird.score

	for bird in saved_birds:
		bird.fitness = bird.score / s


def update_win(win, birds, saved_birds, pipes):
	win.fill(BLACK)
	
	for i in range(len(pipes)-1, -1, -1):
		pipes[i].show(win)
		pipes[i].update()
		for j in range(len(birds)-1, -1, -1):
			if(pipes[i].hits(birds[j])):
				saved_birds.append(birds[j])
				birds.remove(birds[j])

		if(pipes[i].x < 0-pipes[i].w):
			pipes.remove(pipes[i])
			
	for i in range(len(birds)-1, -1, -1):
		bird = birds[i]
		if bird.y >= height - round(bird.size/2) or bird.y <= round(bird.size/2):
			saved_birds.append(bird)
			birds.remove(bird)
		bird.think(pipes)
		bird.update()
		bird.show(win)

	if len(birds) == 0:
		next_generation(saved_birds)
		pipes.clear()
		pipes.append(Pipe())
		global frame_count
		frame_count = 0
	pygame.display.update()


pygame.init()
height = 800
width = 800
win = pygame.display.set_mode((width, height))

TOTAL_POP = 250
run = True
while run:
	restart = False
	score = 0
	frame_count = 0
	pipes = []
	birds = []
	saved_birds = []
	for i in range(TOTAL_POP):
		birds.append(Bird(WHITE))

	while not restart:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				restart = True

		if (frame_count % 75 == 0):
			frame_count = 0
			pipes.append(Pipe())
		update_win(win, birds, saved_birds, pipes)
		frame_count+=1
pygame.quit()


