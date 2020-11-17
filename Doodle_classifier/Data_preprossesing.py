import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def display_sample(data):
	imgs = []
	for k in range(64):
		l = random.randint(0, len(data))
		img = []
		for i in range(28):
			drawing = []
			for j in range(28):
				drawing.append(data[l][j+(i*28)])
			img.append(drawing)
		imgs.append(img)

	fig=plt.figure(figsize=(8, 8))
	for i in range(1, len(imgs)+1):
		fig.add_subplot(8, 8, i)
		plt.imshow(imgs[i-1])

	plt.show()

airplanes = np.load('Data/airplane_samples.npy')
cars = np.load('Data/car_samples.npy')
barns = np.load('Data/barn_samples.npy')

display_sample(barns)

'''
def create_samples(data, num_samples):
	samples = []
	for i in range(num_samples):
		l = random.randint(0, len(data))
		samples.append(data[l])
	return samples

airplanes = np.load('Data/airplanes.npy')
cars = np.load('Data/cars.npy')
barns = np.load('Data/barns.npy')

airplane_samples = create_samples(airplanes, 2000)
car_samples = create_samples(cars, 2000)
barn_samples = create_samples(barns, 2000)

np.save('Data/airplane_samples', airplane_samples)
np.save('Data/car_samples', car_samples)
np.save('Data/barn_samples', barn_samples)
'''