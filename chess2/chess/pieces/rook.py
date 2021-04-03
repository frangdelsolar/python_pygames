from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
import pygame


class Rook(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_tower.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_tower.png')

	def get_valid_moves(self, self_set, other_set, log):
		basic_moves = []

		found = False
		for i in range(self.col + 1, COLS):

			for piece in other_set:
				if piece.row == self.row and piece.col == i:
					basic_moves.append((self.row, i))
					found = True

			for piece in self_set:
				if piece.row == self.row and piece.col == i:
					found = True
			
			if not found:
				basic_moves.append((self.row, i))
			else:
				break


		found = False
		for i in range(self.col-1, -1, -1):

			for piece in other_set:
				if piece.row == self.row and piece.col == i:
					basic_moves.append((self.row, i))
					found = True

			for piece in self_set:
				if piece.row == self.row and piece.col == i:
					found = True
			
			if not found:
				basic_moves.append((self.row, i))
			else:
				break


		found = False
		for i in range(self.row + 1, ROWS):

			for piece in other_set:
				if piece.col == self.col and piece.row == i:
					basic_moves.append((i, self.col))
					found = True

			for piece in self_set:
				if piece.col == self.col and piece.row == i:
					found = True
			
			if not found:
				basic_moves.append((i, self.col))
			else:
				break

		found = False
		for i in range(self.row-1, -1, -1):

			for piece in other_set:
				if piece.col == self.col and piece.row == i:
					basic_moves.append((i, self.col))
					found = True

			for piece in self_set:
				if piece.col == self.col and piece.row == i:
					found = True
			
			if not found:
				basic_moves.append((i, self.col))
			else:
				break

		return basic_moves

