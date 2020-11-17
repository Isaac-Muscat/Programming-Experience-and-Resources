from NeuralNetwork import NeuralNetwork
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pygame
#pygame.init()

AIRPLANE = 0
CAR = 1
BARN = 2

samples = [
np.load('Data/airplane_samples.npy'),
np.load('Data/car_samples.npy'),
np.load('Data/barn_samples.npy')
]

for i in range(len(samples)):
	for j in range(len(samples[i])):
		for k in range(len(samples[i][j])):
			samples[i][j][k] = samples[i][j][k]/255

train = []
test = []
for i in range(len(samples)):
	for j in range(1600):
		train.append(np.append(samples[i][j], i))
	for j in range(1600, 2000):
		test.append(np.append(samples[i][j], i))

random.shuffle(train)
random.shuffle(test)

X_train = []
y_train = []
for drawing in train:
	encoded = [0, 0, 0]
	encoded[drawing[784]] = 1
	y_train.append(encoded)
	X_train.append(np.delete(drawing, 784))

X_test = []
y_test = []
for drawing in test:
	encoded = [0, 0, 0]
	encoded[drawing[784]] = 1
	y_test.append(encoded)
	X_test.append(np.delete(drawing, 784))


nn = NeuralNetwork(784, 64, 3)


for i in range(1000):
	nn.train(X_train[i], y_train[i])
	print('epoch: ',i)

sum = 0
for i in range(500):
	y_pred = nn.feed_forward(X_test[i]).matrix
	if(y_pred[0].index(max(y_pred[0])) == y_test[i].index(1)):
		sum+=1
print('The accuracy is ', sum/500)
'''
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle_classifier")
run = True
def draw():
	global run
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		redrawWindow(win)

def redrawWindow(win):
    win.fill((255, 255, 255))
    pygame.display.update()

draw()
pygame.quit()
'''