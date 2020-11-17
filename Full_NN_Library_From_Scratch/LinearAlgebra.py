import random

class Matrix():
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]

	def log(self):
		print(self.matrix)

	def transpose(self):
		result = Matrix(self.cols, self.rows)
		for i in range(self.rows):
				for j in range(self.cols):
					result.matrix[j][i] = self.matrix[i][j]
		self.matrix = result.matrix
		self.cols = result.cols
		self.rows = result.rows

	def multi(self, n):
		if (isinstance(n, Matrix)):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] *= n.matrix[i][j]
		else:		
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] *= n

	def add(self, n):
		if(isinstance(n, Matrix)):
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] += n.matrix[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.matrix[i][j] += n

	def initialize(self, start, stop):
		for i in range(self.rows):
			for j in range(self.cols):
				self.matrix[i][j] = random.uniform(start, stop)

	def f_map(self, fn):
		for i in range(self.rows):
			for j in range(self.cols):
				self.matrix[i][j] = fn(self.matrix[i][j])

	def to_array(self):
		arr = []
		for i in range(self.rows):
			for j in range(self.cols):
				arr.append(self.matrix[i][j])
		return arr

	def from_array(arr):
		m = Matrix(len(arr), 1)
		for i in range(len(arr)):
			m.matrix[i][0] = arr[i]
		return m

	def subtract(a, b):
		result = Matrix(a.rows, a.cols)
		for i in range(result.rows):
			for j in range(result.cols):
				result.matrix[i][j] = a.matrix[i][j] - b.matrix[i][j]
		return result

	def t(matrix):
		result = Matrix(matrix.cols, matrix.rows)
		for i in range(matrix.rows):
				for j in range(matrix.cols):
					result.matrix[j][i] = matrix.matrix[i][j]
		return result

	def mat_multi(a, b):
		if(a.cols != b.rows):
			print("Error: Dimensions don't match;", a.cols, "!=", b.rows)
		result = Matrix(a.rows, b.cols)
		for i in range(result.rows):
			for j in range(result.cols):
				_sum_ = 0
				for k in range(a.cols):
					_sum_ += a.matrix[i][k]*b.matrix[k][j]
					result.matrix[i][j] = _sum_
		return result
