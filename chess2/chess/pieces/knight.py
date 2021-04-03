from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
import pygame


class Knight(Piece):
	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()

	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_knight.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_knight.png')

	def get_valid_moves(self, self_set, other_set, log):
		posible_moves = [
			(self.row - 2, self.col - 1),
			(self.row - 2, self.col + 1),
			(self.row - 1, self.col - 2),
			(self.row - 1, self.col + 2),
			(self.row + 2, self.col - 1),
			(self.row + 2, self.col + 1),
			(self.row + 1, self.col - 2),
			(self.row + 1, self.col + 2), 
		]

		for piece in self_set:
			for r, c in posible_moves:
				if piece.row == r and piece.col == c:
					posible_moves.pop(posible_moves.index((r, c)))

		# Remove Edges
		remove=[]
		for r, c in posible_moves:
			if not (0 <= r < ROWS and
				  0 <= c < COLS):
				remove.append((r, c))

		for r, c in remove:
			posible_moves.pop(posible_moves.index((r, c)))


		return posible_moves
		
