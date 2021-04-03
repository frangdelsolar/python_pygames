from tetris.shapes import PIECE_SHAPES
from .constants import *
import pygame
import random
import copy

class Piece():
	def __init__(self, row, col, color, speed, is_prev):
		self.shape = copy.deepcopy(random.choice(PIECE_SHAPES))
		self.rotation = None
		self.color = color
		self.row = row
		self.col = col
		self.y_speed = speed
		self.is_prev = is_prev
		self.landed = False
		self.pick_rotation()

	def draw(self, screen):
		shape = self.shape[self.rotation]
		if self.is_prev:
			locations = []
			for i in range(len(shape)):
				for j in range(len(shape[i])):
					if shape[i][j] == 1:
						pygame.draw.rect(screen, self.color, ((PREV_X+j)*SQUARE_SIZE, (PREV_Y+i)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
						pygame.draw.rect(screen, WHITE, ((PREV_X+j)*SQUARE_SIZE, (PREV_Y+i)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
		else:
			# self.fall()
			for i in range(len(shape)):
				for j in range(len(shape[i])):
					if shape[i][j] == 1:
						pygame.draw.rect(screen, self.color, ((self.col+j+BOARD_X)*SQUARE_SIZE, (self.row+i+BOARD_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
						pygame.draw.rect(screen, WHITE, ((self.col+j+BOARD_X)*SQUARE_SIZE, (self.row+i+BOARD_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

	
	def get_location(self, rotation):
		shape = self.shape[rotation]
		locations = []
		for i in range(len(shape)):
			for j in range(len(shape[i])):
				if shape[i][j] == 1:
					row = self.row + i 
					col = self.col + j 
					locations.append((row, col))
		return locations

	def max_col(self):
		shape = self.shape[self.rotation]
		max_col = 0		
		for i in range(len(shape)):
			for j in range(len(shape[i])):
				if shape[i][j] == 1:
					if j > max_col:
						max_col = j
		return max_col

	def pick_rotation(self):
		self.rotation = random.randint(0, len(self.shape)-1)

	def rotate(self, game):
		mover = True		

		rotation = self.rotation
		rotation += 1
		if rotation > len(self.shape)-1:
			rotation = 0

		valid_locations = game.board.get_valid_locations()
		for loc in self.get_location(self.rotation):
			if not loc in valid_locations:
				mover = False

		if mover:
			self.rotation = rotation

	def fall(self, game):
		mover = True		
		self.row += self.y_speed
		
		valid_locations = game.board.get_valid_locations()

		for loc in self.get_location(self.rotation):
			if not loc in valid_locations:
				mover = False

		if not mover:
			self.row -= self.y_speed

	def land(self, game):
		self.landed = True
		self.y_speed = 0
		for r, c in self.get_location(self.rotation):
			game.board.grid[r][c].value = 2
			game.board.grid[r][c].color = self.color

		game.get_falling()
		game.get_next()

	def move_x(self, direction, game):
		mover = True
		self.col += direction

		valid_locations = game.board.get_valid_locations()

		for loc in self.get_location(self.rotation):
			if not loc in valid_locations:
				mover = False

		if not mover:
			self.col -= direction


