import pygame
from .constants import (BOARD_SIZE, 
						BOARD_ROWS, 
						BOARD_COLS, 
						SQUARE_SIZE,
						BOARD_X,
						BOARD_X_MAX,
						BOARD_Y, 
						PREV_ROWS,
						PREV_COLS,
						PREV_X,
						PREV_Y,
						RED, GREEN, BLACK, GRAY, WHITE, BLUE, LIGHT_GRAY)
import random


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.value = 0
		self.color = LIGHT_GRAY

	def __repr__(self):
		return f'{self.value}'

	def draw(self, screen):
		# Dibuja celda en su lugar + offset
		pygame.draw.rect(screen, self.color, ((self.col+BOARD_X)*SQUARE_SIZE, (self.row+BOARD_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		pygame.draw.rect(screen, GRAY, ((self.col+BOARD_X)*SQUARE_SIZE, (self.row+BOARD_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
				

class Board():
	def __init__(self):
		self.grid = []
		self.build()

	def build(self):
		for r in range(0, BOARD_ROWS):
			self.grid.append([Cell(r, c) for c in range(0, BOARD_COLS)])

	def print(self):
		print('##############################')
		print()
		for i in self.grid:
			print(i)
		print()

	def draw(self, screen):
		self.print()

		### GRID SECTION ###
		pygame.draw.rect(screen, GRAY, (BOARD_X*SQUARE_SIZE, BOARD_Y*SQUARE_SIZE, BOARD_COLS*SQUARE_SIZE, BOARD_ROWS*SQUARE_SIZE), 2)

		for r in range(BOARD_ROWS):
			for c in range(BOARD_COLS):
				self.grid[r][c].draw(screen)

		# ### PREVIEW SECTION ###
		# pygame.draw.rect(screen, BLUE, (PREV_X*SQUARE_SIZE, PREV_Y*SQUARE_SIZE, PREV_COLS*SQUARE_SIZE, PREV_ROWS*SQUARE_SIZE), 2)

	def actualizar_grid(self, piece, game):
		for r in range(BOARD_ROWS):
			for c in range(BOARD_COLS):
				if not self.grid[r][c].value == 2:
					self.grid[r][c].value = 0
					self.grid[r][c].color = LIGHT_GRAY

		for row, col in piece.get_location(piece.rotation):
			if not self.grid[row][col].value == 2:
				self.grid[row][col].value = 1

			if row == BOARD_ROWS-1:
				piece.land(game)

			elif self.grid[row+1][col].value == 2:
				piece.land(game)


	def update(self, piece, game):
		piece.fall(game)
		self.actualizar_grid(piece, game)





		# # eliminar filas de iguales
		# for r in range(BOARD_ROWS-1, 0, -1):
		# 	count = 0
		# 	for c in range(BOARD_COLS):
		# 		if self.grid[r][c].value == 2:
		# 			count += 1
		# 	if count == 10:
		# 		for row in range(r, 0, -1):
		# 			for c in range(BOARD_COLS):
		# 				if row > 0:
		# 					self.grid[row][c].value = self.grid[row-1][c].value
		# 					self.grid[row][c].color = self.grid[row-1][c].color
		# 					pygame.display.update()
		# 				else: 
		# 					self.grid[row][c].value = 0
		# 					self.grid[row][c].color = LIGHT_GRAY


	def get_valid_locations(self):
		valid_locations = []
		for r in range(BOARD_ROWS):
			for c in range(BOARD_COLS):
				if not self.grid[r][c].value == 2:
					valid_locations.append((r, c))
		return valid_locations