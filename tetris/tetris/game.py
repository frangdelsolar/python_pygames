from .board import Board
from .player import Player
from .piece import Piece
from .constants import *
import random
import pygame
import sys
import copy

class Game():
	def __init__(self, screen):
		self.board = Board()
		self.screen = screen
		self.player = Player('Francisco')
		self.next_piece = None
		self.falling_piece = None
		self.run = True
		self.speed = 2
		self.get_next()
		self.get_falling()

	def draw(self):
		self.screen.fill(WHITE)
		self.board.draw(self.screen)
		self.next_piece.draw(self.screen)
		self.falling_piece.draw(self.screen)

	def get_next(self):
		color = random.choice(SHAPE_COLORS)
		row = None
		col = None
		speed = 0
		is_prev = True
		self.next_piece = Piece(row, col, color, speed, is_prev)

	def get_falling(self):
		self.falling_piece = copy.deepcopy(self.next_piece)
		self.falling_piece.row = 0	
		self.falling_piece.y_speed = 1			
		self.falling_piece.is_prev = False	
		self.falling_piece.col = random.randint(0, BOARD_COLS - self.falling_piece.max_col()-1)

	def update(self):
		self.board.update(self.falling_piece, self)

	def listen(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.falling_piece.rotate(self)

				if event.key == pygame.K_DOWN:
					self.falling_piece.fall(self)

				if event.key == pygame.K_RIGHT:
					x_dir = 1
					self.falling_piece.move_x(x_dir, self)

				if event.key == pygame.K_LEFT:
					x_dir = -1
					self.falling_piece.move_x(x_dir, self)



