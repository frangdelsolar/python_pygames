import pygame
import random
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, GREEN, YELLOW, BLACK




class Pacman():

	def __init__(self, row, col, x_speed, y_speed, color):
		self.row = row
		self.col = col
		self.color = color
		self.radius = SQUARE_SIZE//3
		self.x_speed = x_speed
		self.y_speed = y_speed

	def draw(self, screen):
		x = (self.col*SQUARE_SIZE)+SQUARE_SIZE//2
		y = (self.row*SQUARE_SIZE)+SQUARE_SIZE//2
		pygame.draw.circle(screen, self.color, (x, y), self.radius)

	def animar_y(self, screen, origen, destino):
		x = (origen [1]*SQUARE_SIZE)+SQUARE_SIZE//2
		y1 = (origen [0]*SQUARE_SIZE)+SQUARE_SIZE//2
		y2 = (destino [0]*SQUARE_SIZE)+SQUARE_SIZE//2

		for y in range(y1, y2):
			pygame.draw.circle(screen, self.color, (x, y), self.radius)
			pygame.display.update()

	def animar_x(self, screen, origen, destino):
		y = (origen [0]*SQUARE_SIZE)+SQUARE_SIZE//2
		x1 = (origen [1]*SQUARE_SIZE)+SQUARE_SIZE//2
		x2 = (destino [1]*SQUARE_SIZE)+SQUARE_SIZE//2

		for x in range(x1, x2):
			pygame.draw.circle(screen, self.color, (x, y), self.radius)
			pygame.display.update()

	def update(self, game):
		# if game.board.level[self.row+self.y_speed][self.col+self.x_speed]:
			if game.board.level[self.row+self.y_speed][self.col+self.x_speed] != 1:
				or_row = self.row
				or_col = self.col
				self.row += self.y_speed
				self.col += self.x_speed

				if self.col == 0 and self.x_speed != 0:
					self.col = 19
				elif self.col == 19 and self.x_speed != 0:
					self.col = 0

				# if self.y_speed > 0:
				# 	self.animar_y(game.screen, (or_row, self.col), (self.row, self.col))
				# elif self.y_speed < 0:
				# 	self.animar_y(game.screen, (self.row, self.col), (or_row, self.col))
				# elif self.x_speed > 0:
				# 	self.animar_x(game.screen, (self.row, or_col), (self.row, self.col))
				# elif self.x_speed < 0:
				# 	self.animar_x(game.screen, (self.row, self.col), (self.row, or_col))


	def mover(self, direction):
		self.x_speed = direction[1]
		self.y_speed = direction[0]

	def captured(self):
		self.row = 11
		self.col = 10
		self.x_speed = 0
		self.y_speed = 0

