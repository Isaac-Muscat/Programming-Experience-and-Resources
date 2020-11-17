import pygame
import numpy as np
import random

pygame.init()

width = 800
height = 800

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Perceptron - Click for another epoch")

class Perceptron():
    def __init__(self):
        self.weights = [np.random.uniform(-1,1) for _ in range(3)]
        self.lr = 0.1

    def train(self, inputs, target):
        g = guess(self.weights, inputs)
        error = target - g
        self.weights = [self.weights[i] + self.lr*error*inputs[i] for i in range(0,len(self.weights))]

class Point():
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        if (self.x>self.y):
            self.label = 1
        else:
            self.label = -1

def guess(weights, inputs):
    return sine(np.matmul(weights, inputs))

def sine(n):
    if(n >= 0):
        return 1
    else:
        return -1

def main():
    run = True
    win.fill((255, 255, 255))
    perceptron = Perceptron()
    points = [Point() for _ in range(200)]
    pygame.draw.line(win, (0, 0, 0), (0, 0), (width, height), 5)

    for point in points:
            target = point.label
            g = guess(perceptron.weights, [1, point.x, point.y])
            if(g == target):
                pygame.draw.ellipse(win, (0, 255, 0), (point.x, point.y, 8, 8))
            else:
                pygame.draw.ellipse(win, (255, 0, 0), (point.x, point.y, 8, 8))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                for point in points:
                    inputs = [1, point.x, point.y]
                    perceptron.train(inputs, point.label)

                for point in points:
                    target = point.label
                    g = guess(perceptron.weights, [1,point.x, point.y])
                    if(g == target):
                        pygame.draw.ellipse(win, (0, 255, 0), (point.x, point.y, 8, 8))
                    else:
                        pygame.draw.ellipse(win, (255, 0, 0), (point.x, point.y, 8, 8))

        pygame.display.update()
    pygame.quit()

main()