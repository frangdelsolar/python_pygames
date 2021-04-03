
import sys
import pygame
import random
from perceptron import Perceptron


WIDTH, HEIGHT = 600, 600

class Point():
	x = None
	y = None
	label = None
	color = (255, 255, 255)

	def __init__(self, x, y):
		self.x = x
		self.y = y

		if x < y:
			self.label = 1
			self.color = (255, 255, 255)
		else:
			self.label = -1
			self.color = (100, 70, 255)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), 4)


class Line():
	def __init__(self, pos1, pos2):
		self.pos1 = pos1
		self.pos2 = pos2


	def draw(self, screen):
		pygame.draw.line(screen, (0, 255, 255), self.pos1, self.pos2, 1)


def train(brain, points, screen):
	for point in points:
		point.draw(screen)

		inputs = [point.x, point.y]
		target = point.label
		brain.train(inputs, target)
		guess = brain.guess(inputs)
		if guess == target:
			pygame.draw.circle(screen, (255,255,0), (point.x, point.y), 10, 1)


def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	# line = Line((0, random.randint(0, HEIGHT) ), (WIDTH, random.randint(0, HEIGHT)))

	line = Line((0, 0), (WIDTH, HEIGHT))

	points = []
	for i in range(100):
		points.append(Point(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

	

	brain = Perceptron()

	# inputs = [-1, 0,5]
	# output = brain.guess(inputs)
	# print(output)
	training_index = 0

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# if event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_SPACE:
			# 		train(brain, points, screen)

		line.draw(screen)
		for point in points:
			point.draw(screen)

		for point in points:
			inputs = [point.x, point.y]
			target = point.label
			guess = brain.guess(inputs)
			if guess == target:
				pygame.draw.circle(screen, (255,255,0), (point.x, point.y), 10, 1)
				pygame.display.update()

		print(training_index)
		point = points[training_index]
		inputs = [point.x, point.y]
		target = point.label
		brain.train(inputs, target)
		guess = brain.guess(inputs)
		# if guess == target:
			# pygame.draw.circle(screen, (255,255,0), (point.x, point.y), 10, 1)
		training_index += 1
		if training_index >= len(points):
			training_index=0

		points.append(Point(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
		pygame.display.update()
		clock.tick(1)




main()


	