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
        self.x = np.random.uniform(-1, 1)
        self.y = np.random.uniform(-1, 1)
        if (f(self.x)>self.y):
            self.label = 1
        else:
            self.label = -1

def f(x):
    # y = mx + b
    return 0.89*x - 0.2

def guess(weights, inputs):
    return sine(np.matmul(weights, inputs))

def guessY(x, weights):
    return -(weights[0]/weights[2]) - (weights[1]/weights[2]) * x

def sine(n):
    if(n >= 0):
        return 1
    else:
        return -1

def map_range(value, start1, stop1, start2, stop2):
   return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2

def main():
    run = True
    win.fill((255, 255, 255))
    perceptron = Perceptron()
    points = [Point() for _ in range(200)]
    x1 = map_range(-1, -1, 1, 0, width)
    y1 = map_range(f(-1), -1, 1, height, 0)
    x2 = map_range(1, -1, 1, 0, width)
    y2 = map_range(f(1), -1, 1, height, 0)
    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 5)

    x1 = map_range(-1, -1, 1, 0, width)
    y1 = map_range(guessY(-1, perceptron.weights), -1, 1, height, 0)
    x2 = map_range(1, -1, 1, 0, width)
    y2 = map_range(guessY(1, perceptron.weights), -1, 1, height, 0)
    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 5)

    for point in points:
        px = map_range(point.x, -1, 1, 0, width)
        py = map_range(point.y, -1, 1, height, 0)
        target = point.label
        g = guess(perceptron.weights, [1, point.x, point.y])
        if(g == target):
            pygame.draw.ellipse(win, (0, 255, 0), (px, py, 8, 8))
        else:
            pygame.draw.ellipse(win, (255, 0, 0), (px, py, 8, 8))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                win.fill((255, 255, 255))
                x1 = map_range(-1, -1, 1, 0, width)
                y1 = map_range(f(-1), -1, 1, height, 0)
                x2 = map_range(1, -1, 1, 0, width)
                y2 = map_range(f(1), -1, 1, height, 0)
                pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 5)

                for point in points:
                    inputs = [1, point.x, point.y]
                    perceptron.train(inputs, point.label)

                for point in points:
                    px = map_range(point.x, -1, 1, 0, width)
                    py = map_range(point.y, -1, 1, height, 0)
                    target = point.label
                    g = guess(perceptron.weights, [1, point.x, point.y])
                    if(g == target):
                        pygame.draw.ellipse(win, (0, 255, 0), (px, py, 8, 8))
                    else:
                        pygame.draw.ellipse(win, (255, 0, 0), (px, py, 8, 8))

                x1 = map_range(-1, -1, 1, 0, width)
                y1 = map_range(guessY(-1, perceptron.weights), -1, 1, height, 0)
                x2 = map_range(1, -1, 1, 0, width)
                y2 = map_range(guessY(1, perceptron.weights), -1, 1, height, 0)
                pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 5)

        pygame.display.update()
    pygame.quit()

main()