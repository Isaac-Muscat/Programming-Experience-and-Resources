from LinearAlgebra import Matrix
import math
import random
import numpy as np

class NeuralNetwork():
	def __init__(self, numI, numH, numO):
		self.input_nodes = numI
		self.hidden_nodes = numH
		self.output_nodes = numO
		self.lr = 0.1

		self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes)
		self.weights_hh = Matrix(self.hidden_nodes, self.hidden_nodes)
		self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)

		self.weights_ih.initialize(-1, 1)
		self.weights_hh.initialize(-1, 1)
		self.weights_ho.initialize(-1, 1)

		self.bias_h = Matrix(self.hidden_nodes, 1)
		self.bias_hh = Matrix(self.hidden_nodes, 1)
		self.bias_o = Matrix(self.output_nodes, 1)

		self.bias_h.initialize(-1, 1)
		self.bias_hh.initialize(-1, 1)
		self.bias_o.initialize(-1, 1)

	def predict(self, input_array):
		inputs = Matrix.from_array(input_array)

		hidden = Matrix.mat_multi(self.weights_ih, inputs)
		hidden.add(self.bias_h)
		hidden.f_map(NeuralNetwork.sigmoid)

		hidden_h = Matrix.mat_multi(self.weights_hh, hidden)
		hidden_h.add(self.bias_hh)
		hidden_h.f_map(NeuralNetwork.sigmoid)

		output = Matrix.mat_multi(self.weights_ho, hidden_h)
		output.add(self.bias_o)
		output.f_map(NeuralNetwork.sigmoid)
		return output.to_array()

	def mutate(self, rate):
		def mutate_func(val):
			if(random.random() < rate):
				#return random.random() * 2 - 1
			#elif(random.random() < rate):
				answer = val + random.gauss(0, 0.2)
			else:
				answer = val

			if (answer>1):
				answer = 1
			if (answer<-1):
				answer = -1

			return answer

		self.weights_ih.f_map(mutate_func)
		self.weights_hh.f_map(mutate_func)
		self.weights_ho.f_map(mutate_func)
		self.bias_h.f_map(mutate_func)
		self.bias_hh.f_map(mutate_func)
		self.bias_o.f_map(mutate_func)

	def sigmoid(x):
		return 1/(1+np.exp(-x))
