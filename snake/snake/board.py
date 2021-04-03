import pygame
from .constants import BOARD_SIZE, BOMBS, ROWS, COLS, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import random


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def __repr__(self):
		return f'{self.row}, {self.col}'

	def draw(self, screen):
		pygame.draw.rect(screen, WHITE, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
		

class Board():
	def __init__(self):
		self.grid = []
		self.build()

	def build(self):
		for r in range(ROWS):
			self.grid.append([Cell(r, c) for c in range(COLS)])

	def draw(self, screen):
		screen.fill(BLACK)
		# for r in range(ROWS):
		# 	for c in range(COLS):
		# 		self.grid[r][c].draw(screen)



