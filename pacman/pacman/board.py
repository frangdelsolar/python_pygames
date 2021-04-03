import pygame
from .constants import LEVEL_1, BLUE, BOMBS, ROWS, COLS, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import random


class Cell():
	def __init__(self, row, col, color):
		self.row = row
		self.col = col
		self.color = color

	def __str__(self):
		if self.color == BLUE:
			return str(1)
		if self.color == RED:
			return str(2)
		else:
			return ' '

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		

class Board():
	def __init__(self):
		self.grid = []
		self.level = LEVEL_1
		self.build()

	def build(self):
		for r in range(len(self.level)):
			line = []
			for c in range(len(self.level[r])):				
				if self.level[r][c] == 1:
					line.append(Cell(r, c, BLUE))
				
				elif self.level[r][c] == 2:
					line.append(Cell(r, c, RED))
				
				else:
					line.append(Cell(r, c, BLACK))
			
			self.grid.append(line)

	def print(self):
		for r in range(len(self.level)):
			for c in range(len(self.level[r])):
				print(self.grid[r][c], end=', ')
			print()

	def draw(self, screen):
		screen.fill(BLACK)
		for r in range(len(self.level)):
			for c in range(len(self.level[r])):
				self.grid[r][c].draw(screen)




