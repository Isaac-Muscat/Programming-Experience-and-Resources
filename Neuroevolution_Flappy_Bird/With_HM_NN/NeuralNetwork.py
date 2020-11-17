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
		self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
		self.weights_ih.initialize(-1, 1)
		self.weights_ho.initialize(-1, 1)

		self.bias_h = Matrix(self.hidden_nodes, 1)
		self.bias_o = Matrix(self.output_nodes, 1)
		self.bias_h.initialize(-1, 1)
		self.bias_o.initialize(-1, 1)

	def predict(self, input_array):

		inputs = Matrix.from_array(input_array)
		hidden = Matrix.mat_multi(self.weights_ih, inputs)
		hidden.add(self.bias_h)
		hidden.f_map(NeuralNetwork.sigmoid)

		output = Matrix.mat_multi(self.weights_ho, hidden)
		output.add(self.bias_o)
		output.f_map(NeuralNetwork.sigmoid)
		return output

	def train(self, input_array, target_array):

		inputs = Matrix.from_array(input_array)
		hidden = Matrix.mat_multi(self.weights_ih, inputs)
		hidden.add(self.bias_h)
		hidden.f_map(NeuralNetwork.sigmoid)

		outputs = Matrix.mat_multi(self.weights_ho, hidden)
		outputs.add(self.bias_o)
		outputs.f_map(NeuralNetwork.sigmoid)

		targets = Matrix.from_array(target_array)

		output_errors = Matrix.subtract(targets, outputs)

		ds = lambda x: x*(1-x)
		outputs.f_map(ds)
		outputs.multi(output_errors)
		outputs.multi(self.lr)

		d_weight_ho = Matrix.mat_multi(outputs, Matrix.t(hidden))

		#Adjust weights and bias by there gradients
		self.weights_ho.add(d_weight_ho)
		self.bias_o.add(outputs)

		hidden_errors = Matrix.mat_multi(Matrix.t(self.weights_ho), output_errors)

		hidden.f_map(ds)
		hidden.multi(hidden_errors)
		hidden.multi(self.lr)
		d_weight_ih = Matrix.mat_multi(hidden, Matrix.t(inputs))

		self.weights_ih.add(d_weight_ih)
		self.bias_h.add(hidden)

	def mutate(self, rate):
		def mutate_func(val):
			if(random.random() < rate):
				#return random.random() * 2 - 1
			#elif(random.random() < rate):
				return val + random.gauss(0, 0.1)
			else:
				return val

		self.weights_ih.f_map(mutate_func)
		self.weights_ho.f_map(mutate_func)
		self.bias_h.f_map(mutate_func)
		self.bias_o.f_map(mutate_func)



	def sigmoid(x):
		return 1/(1+np.exp(-x))