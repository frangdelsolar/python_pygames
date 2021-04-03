import pygame
import random
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, GREEN

class Snake():

	def __init__(self):
		self.row = None
		self.col = None
		self.x_speed = 0
		self.y_speed = 0
		self.tail = []
		self.build()

	def build(self):
		self.row = random.randint(1, ROWS-2)
		self.col = random.randint(1, COLS-2)
		self.x_speed = -1

	def draw(self, screen):
		# Dibujar cabeza
		pygame.draw.rect(screen, WHITE, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

		# Dibujar la cola
		for row, col in self.tail:
			pygame.draw.rect(screen, WHITE, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

	def update(self):
		for i in range(len(self.tail)-1, -1, -1):
			if i > 0:
				self.tail[i] = self.tail[i-1]	
			else:
				self.tail[i] = (self.row, self.col)

		self.row += self.y_speed
		self.col += self.x_speed

	def mover(self, direction):
		can_move = True
		if self.x_speed != 0 and direction[1] != 0:
			can_move = False
		if self.y_speed != 0 and direction[0] != 0:
			can_move = False

		if can_move:
			self.x_speed = direction[1]
			self.y_speed = direction[0]

	def eat(self, fruit):
		self.tail.append((fruit.row, fruit.col))

		fruit.row = random.randint(1, ROWS-2)
		fruit.col = random.randint(1, COLS-2)


