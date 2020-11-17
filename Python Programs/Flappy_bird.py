import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Pipe():
	def __init__(self):
		self.space = 90
		self.top = random.randint(self.space, height-self.space*2)
		self.bottom = height-self.top-self.space
		self.x = width
		self.w = 70
		self.speed = 4
		self.highlight = False
		self.passed = 0

	def hits(self, bird):
		global restart
		if(bird.y - round(bird.size/2) < self.top or bird.y+round(bird.size/2) > height-self.bottom):
			if(bird.x+round(bird.size/2) > self.x and bird.x-round(bird.size/2) < self.x + self.w):
				restart = True
				return True

	def show(self, win):
		color = WHITE
		if (self.highlight):
			color = RED
		pygame.draw.rect(win, color, (self.x, 0, self.w, self.top))
		pygame.draw.rect(win, color, (self.x, height-self.bottom, self.w, self.bottom))

	def update(self):
		self.x -= self.speed
		self.highlight = False
		if(self.x < 32 and self.passed <2):
			self.passed += 1




class Bird():
	def __init__(self, color):
		self.y = round(height/2)
		self.x = 64
		self.size = 18
		self.color = color
		self.gravity = 0.6
		self.lift = -15
		self.vel = 0

	def up(self):
		self.vel += self.lift
 
	def show(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

	def update(self):
		self.vel += self.gravity
		self.vel *= 0.95
		self.y = round(self.vel + self.y)

		if self.y > height:
			self.y = height
			self.vel = 0

		if self.y < 0:
			self.y = 0
			self.vel = 0
			


def update_win(win, bird, pipes, font):
	global score
	global high_score
	win.fill(BLACK)
	for i in range(len(pipes)-1, -1, -1):
		pipes[i].show(win)
		pipes[i].update()
		if(pipes[i].passed == 1):
			score +=1
		if(pipes[i].hits(bird)):
			score = 0
			pipes[i].highlight = True
		if(pipes[i].x < 0-pipes[i].w):
			pipes.remove(pipes[i])

	bird.update()
	bird.show(win)

	if(score > high_score):
		high_score = score

	text = font.render("Score: {0}".format(score), 1, BLUE)
	win.blit(text, (round(width/2), 50))
	text = font.render("High score: {0}".format(high_score), 1, BLUE)
	win.blit(text, (round(width/2), height-50))
	pygame.display.update()


pygame.init()
height = 800
width = 800
win = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 40)

high_score = 0

run = True
while run:
	restart = False
	score = 0
	frame_count = 0

	pipes = []
	bird = Bird(GREEN)
	while not restart:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				restart = True
			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						bird.up()
		if (frame_count % 100 == 0):
			frame_count = 0
			pipes.append(Pipe())
		update_win(win, bird, pipes, font)
		frame_count+=1
pygame.quit()


