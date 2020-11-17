from NeuralNetwork import NeuralNetwork
import pygame
import random
import time
import copy

WIDTH = 500
HEIGHT = 500
TS = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

class Cell:
	def __init__(self, x, y, color):
		self.pos = [x, y]
		self.color = color

	def show(self, win):
		rect = (self.pos[0]*TS, self.pos[1]*TS, TS, TS)
		pygame.draw.rect(win, self.color, rect)

class Snake:
	def __init__(self, c):
		self.alive = True
		self.fitness = 0
		self.score = 0
		self.lifetime = 0
		self.c = c
		start_pos = [round(WIDTH/(2*TS)), round(HEIGHT/(2*TS))]
		self.body = [Cell(start_pos[0], start_pos[1], self.c), 
					 Cell(start_pos[0], start_pos[1]+1, self.c),
					 Cell(start_pos[0], start_pos[1]+2, self.c),
					 Cell(start_pos[0], start_pos[1]+3, self.c)]
		self.head = self.body[0]
		self.vel = 0
		self.vision_size = 1
		self.brain = NeuralNetwork(4+self.vision_size**2-1, 64, 4)
		self.food = Food(self)

	def think(self):
		inputs = []
		inputs.append(self.head.pos[0]/(WIDTH/TS-1))
		inputs.append(self.head.pos[1]/(HEIGHT/TS-1))
		inputs.append(self.food.cell.pos[0]/(WIDTH/TS-1))
		inputs.append(self.food.cell.pos[1]/(HEIGHT/TS-1))

		head = self.head
		mid_point = int(self.vision_size/2)

		grid = [[0 for i in range(self.vision_size)] for j in range(self.vision_size)]
		grid[mid_point][mid_point] = 0

		for i in range(1, len(self.body)):
			seg = self.body[i]
			delta_x = seg.pos[0]-head.pos[0]
			delta_y = seg.pos[1]-head.pos[1]
			if(abs(delta_x) <= mid_point and abs(delta_y) <= mid_point):
				grid[mid_point + delta_y][mid_point + delta_x] = 1

		for i in range(self.vision_size):
			for j in range(self.vision_size):
				if(head.pos[0]-mid_point+j >= WIDTH or head.pos[0]-mid_point+j < 0 or head.pos[1]-mid_point+i >= HEIGHT or head.pos[1]-mid_point+i < 0):
					grid[i][j] = 1

				if(i != mid_point or j != mid_point):
					inputs.append(grid[i][j])

		outputs = self.brain.predict(inputs)
		output = outputs.index(max(outputs))
		if(output == 0):
			self.vel = UP
		elif(output == 1):
			self.vel = DOWN
		elif(output == 2):
			self.vel = LEFT
		elif(output == 3):
			self.vel = RIGHT


	def show(self, win):
		self.food.show(win)
		for cell in self.body:
			cell.show(win)

	def update(self):
		if self.food.cell.pos == self.head.pos:
			self.food.cell = Food.create_cell(self)
			growth = Cell(self.body[-1].pos[0], self.body[-1].pos[1], self.c)
			self.body.append(growth)
			self.lifetime = 0


		for i in range(len(self.body)-1, 0, -1):
			self.body[i].pos[0] = self.body[i-1].pos[0]
			self.body[i].pos[1] = self.body[i-1].pos[1]
		
		if self.vel == UP:
			self.head.pos[1] -= 1
		elif self.vel == DOWN:
			self.head.pos[1] += 1
		elif self.vel == LEFT:
			self.head.pos[0] -= 1
		else:
			self.head.pos[0] += 1

		for i in range(1, len(self.body)):
			if self.body[i].pos == self.head.pos:
				self.alive = False
				break

		if(self.lifetime >= 150 or self.head.pos[0] > WIDTH/TS or self.head.pos[0] < 0 or self.head.pos[1] > HEIGHT/TS or self.head.pos[1] < 0):
			self.alive = False

		self.score += 1
		self.lifetime += 1

class Food:
	def __init__(self, snake):
		self.cell = Food.create_cell(snake)

	def create_cell(snake):
		cell = Cell(random.randint(0, round(WIDTH/TS)-1),
					random.randint(0, round(HEIGHT/TS)-1), 
					snake.c)
		for seg in snake.body:
			if cell.pos == seg.pos:
				return Food.create_cell(snake)
		return cell

	def show(self, win):
		self.cell.show(win)
		
def next_gen(snakes, saved_snakes):
	calc_fit(saved_snakes)

	for i in range(TOTAL_POP):
		snakes.append(select(saved_snakes))
	saved_snakes.clear()

def calc_fit(saved_snakes):
	s = 0
	for snake in saved_snakes:
		snake.score = snake.score**2*((len(snake.body)-3)**2)
		s += snake.score

	for snake in saved_snakes:
		snake.fitness = snake.score / s

def select(saved_snakes):
	index = 0
	r = random.random()
	while r>0:
		r = r - saved_snakes[index].fitness
		index+=1
	index-=1
	snake = saved_snakes[index]
	child = Snake(COLORS[random.randint(0, 3)])
	child.brain = copy.deepcopy(snake.brain)
	child.brain.mutate(0.05)
	return child

def update_win(win, snakes, saved_snakes):
	win.fill(BLACK)
	for i in range(len(snakes)-1, -1, -1):
		snake = snakes[i]
		if(snake.alive == False):
			saved_snakes.append(snake)
			snakes.remove(snake)
		snake.think()
		snake.update()
		snake.show(win)

	if(len(snakes) == 0):
		next_gen(snakes, saved_snakes)
	pygame.display.update()


pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
RUN = True
TOTAL_POP = 25
COLORS = [GREEN, BLUE, RED, WHITE]
snakes = []
saved_snakes = []
for i in range(TOTAL_POP):
	snakes.append(Snake(COLORS[random.randint(0, 3)]))

while RUN:
	RESTART = False
	while not RESTART:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RUN = False
				RESTART = True
			'''
			snake = snakes[0]
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and snake.vel != -UP:
					snake.vel = UP
				elif event.key == pygame.K_s and snake.vel != -DOWN:
					snake.vel = DOWN
				elif event.key == pygame.K_a and snake.vel != -LEFT:
					snake.vel = LEFT
				elif event.key == pygame.K_d and snake.vel != -RIGHT:
					snake.vel = RIGHT
				'''
		update_win(win, snakes, saved_snakes)

pygame.quit()


