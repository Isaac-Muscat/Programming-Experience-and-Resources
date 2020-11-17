from LinearAlgebra import Matrix
import math
import random

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

	def feed_forward(self, input_array):

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

	def sigmoid(x):
		return 1/(1+math.exp(-x))

def main():
	X = [[0,1],[1,0],[1,1],[0,0]]
	y = [[1], [1], [0], [0]]

	nn = NeuralNetwork(2, 2, 1)

	for i in range(50000):
		j = random.randint(0, 3)
		nn.train(X[j], y[j])

	nn.feed_forward([1,0]).log()
	nn.feed_forward([0,1]).log()
	nn.feed_forward([0,0]).log()
	nn.feed_forward([1,1]).log()

main()