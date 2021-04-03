import pygame
from .constants import BOARD_SIZE, ROWS, COLS, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import random


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def __repr__(self):
		return f'{self.row}, {self.col}'

	def draw(self, screen):
		if (self.row + self.col) % 2 == 0:
			pygame.draw.rect(screen, WHITE, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		else:		
			pygame.draw.rect(screen, BLACK, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


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
		for i in range(COLS):
			for j in range(ROWS):
				self.grid[i][j].draw(screen)



