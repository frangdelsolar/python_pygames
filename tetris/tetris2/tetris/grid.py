from .constants import *
import pygame


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.color = BASE_COLOR

	def __repr__(self):
		if self.color == BASE_COLOR:
			return '.'
		else:
			return str(1)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, ((self.col+OFFSET_X)*SQUARE_SIZE, (self.row+OFFSET_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



class Board():
	def __init__(self):
		self.grid = []
		self.build()

	def build(self):
		for r in range(0, BOARD_ROWS):
			self.grid.append([Cell(r, c) for c in range(0, BOARD_COLS)])

	def print(self):
		# print('##############################')
		print()
		for i in self.grid:
			print(i)
		print()

	def draw_cells(self, screen):
		pygame.draw.rect(screen, GRAY, (OFFSET_X*SQUARE_SIZE, OFFSET_Y*SQUARE_SIZE, BOARD_COLS*SQUARE_SIZE, BOARD_ROWS*SQUARE_SIZE), 2)

		for r in range(BOARD_ROWS):
			for c in range(BOARD_COLS):
				self.grid[r][c].draw(screen)

	def draw_grid(self, screen):
		for r in range(BOARD_ROWS):
			pygame.draw.line(screen, GRAY, (OFFSET_X*SQUARE_SIZE, (r+OFFSET_Y)*SQUARE_SIZE), (OFFSET_X_MAX*SQUARE_SIZE, (r+OFFSET_Y)*SQUARE_SIZE), 1) 

		for c in range(BOARD_COLS):
			pygame.draw.line(screen, GRAY, ((c+OFFSET_X)*SQUARE_SIZE, OFFSET_Y*SQUARE_SIZE), ((c+OFFSET_X)*SQUARE_SIZE, OFFSET_Y_MAX*SQUARE_SIZE), 1) 

	def get_valid_locations(self):
		locations = []
		for r in range(BOARD_ROWS):
			for c in range(BOARD_COLS):
				if self.grid[r][c].color == BASE_COLOR:
					locations.append((r, c))
		return locations

	def clear_rows(self):
		cleared = 0
		for r in range(BOARD_ROWS):
			count = 0
			for c in range(BOARD_COLS):
				if self.grid[r][c].color != BASE_COLOR:
					count += 1

			if count == BOARD_COLS:
				cleared += 1
				for row in range(r, 0, -1):
					for c in range(BOARD_COLS):
						if row > 0:
							self.grid[row][c].color = self.grid[row-1][c].color
							pygame.display.update()
						else: 
							self.grid[row][c].color = BASE_COLOR
		return cleared
