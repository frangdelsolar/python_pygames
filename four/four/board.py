import pygame
from .constants import BOARD_SIZE, ROWS, COLS, BLUE, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import random


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.value = None

	def __repr__(self):
		return f'{self.row}, {self.col}'

	def draw(self, screen):
		if (self.row + self.col) % 2 == 0:
			pygame.draw.rect(screen, WHITE, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		else:		
			pygame.draw.rect(screen, BLACK, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

		if self.value:
			self.value.draw((self.row, self.col), screen)
	

class Board():
	def __init__(self):
		self.grid = []
		self._crear_grid()

	def _crear_grid(self):
		for r in range(ROWS):
			line = []
			for c in range(COLS):
				line.append(Cell(r, c))
			self.grid.append(line)

	def draw(self, screen):
		screen.fill(BLACK)
		for r in range(ROWS):
			for c in range(COLS):
				self.grid[r][c].draw(screen)

	def show(self):
		for r in range(ROWS):
			for c in range(COLS):
				print(self.grid[r][c].value, end='  ,')
			print()



