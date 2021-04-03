import random

WEIGHTS_AMOUNT = 2

class Perceptron:
	weights = []
	lr = 0.1

	def __init__(self):
		for i in range(WEIGHTS_AMOUNT):
			r = random.random() * random.choice([1, -1])
			self.weights.append(r)

	def sign(self, n):
		"""
		Activation function
		"""
		if n >= 0:
			return 1
		return -1

	def guess(self, inputs):
		suma = 0
		for i in range(len(self.weights)):
			suma += inputs[i] * self.weights[i]

		output = self.sign(suma)
		return output

	def train(self, inputs, target):
		guess = self.guess(inputs)
		error = target - guess

		for i in range(len(self.weights)):
			self.weights[i] += error * inputs[i] * self.lr