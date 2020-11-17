from LinearAlgebra import Matrix
import math
import random

class NeuralNetwork():
	def __init__(self):
		'''
		self.input_nodes
		self.output_nodes
		self.lr
		'''
		self.hidden_layers = []
		self.weights = []
		self.biases = []


	def add_input_layer(self, numI):
		self.input_nodes = numI

	def add_hidden_layer(self, numH):
		self.hidden_layers.append(numH)

	def add_output_layer(self, numO):
		self.output_nodes = numO

	def initialize(self, lr):
		self.lr = lr

		self.biases.append(Matrix(self.hidden_layers[0], 1))
		self.weights.append(Matrix(self.hidden_layers[0], self.input_nodes))

		for i in range(len(self.hidden_layers)-1):
			self.weights.append(Matrix(self.hidden_layers[i], self.hidden_layers[i-1]))
			self.biases.append(Matrix(self.hidden_layers[i], 1))

		self.biases.append(Matrix(self.output_nodes, 1))
		self.weights.append(Matrix(self.output_nodes, self.hidden_layers[-1]))

		for w in self.weights:
			w.initialize(-1, 1)

		for b in self.biases:
			b.initialize(-1, 1)

	def predict(self, input_array):
		inputs = Matrix.from_array(input_array)
		next_inputs = inputs
		for i in range(len(self.weights)):
			current_layer = Matrix.mat_multi(self.weights[i], next_inputs)
			current_layer.add(self.biases[i])
			current_layer.f_map(NeuralNetwork.sigmoid)
			next_inputs = current_layer
		return next_inputs

	def train(self, input_array, target_array):
		inputs = Matrix.from_array(input_array)
		targets = Matrix.from_array(target_array)
		ds = lambda x: x*(1-x)

		next_inputs = []
		next_inputs.append(inputs)
		for i in range(len(self.weights)):
			current_layer = Matrix.mat_multi(self.weights[i], next_inputs[i])
			current_layer.add(self.biases[i])
			current_layer.f_map(NeuralNetwork.sigmoid)
			next_inputs.append(current_layer)
		
		errors = Matrix.subtract(targets, next_inputs[-1])
		for i in range(len(self.weights)-1, -1, -1):
			next_inputs[i+1].f_map(ds)
			next_inputs[i+1].multi(errors)
			next_inputs[i+1].multi(self.lr)
			d_weight = Matrix.mat_multi(next_inputs[i+1], Matrix.t(next_inputs[i]))
			self.weights[i].add(d_weight)
			self.biases[i].add(next_inputs[i+1])

			errors = Matrix.mat_multi(Matrix.t(self.weights[i]), errors)
			

	def sigmoid(x):
		return 1/(1+math.exp(-x))

def main():
	X = [[0,1],[1,0],[1,1],[0,0]]
	y = [[1], [1], [0], [0]]

	nn = NeuralNetwork()

	nn.add_input_layer(2)
	nn.add_hidden_layer(2)
	nn.add_output_layer(1)
	nn.initialize(0.1)

	for i in range(10000):
		j = random.randint(0, 3)
		nn.train(X[j], y[j])

	
	nn.predict([1,0]).log()
	nn.predict([0,1]).log()
	nn.predict([0,0]).log()
	nn.predict([1,1]).log()
	

main()