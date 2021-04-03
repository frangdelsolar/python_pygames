from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
import pygame
from . import King
from . import Queen
from . import Bishop
from . import Knight
from . import Rook
from . import Pawn



class ChessSet():

	def __init__(self, color):
		self.color = color
		self.pieces = []
		self.build()


	def build(self):

		if self.color == 'white':
			self.pieces.append(King('King', self.color, (7, 4)))
			self.pieces.append(Queen('Queen', self.color, (7, 3)))
			self.pieces.append(Bishop('Bishop', self.color, (7, 2)))
			self.pieces.append(Bishop('Bishop', self.color, (7, 5)))
			self.pieces.append(Knight('Knight', self.color, (7, 1)))
			self.pieces.append(Knight('Knight', self.color, (7, 6)))
			self.pieces.append(Rook('Rook', self.color, (7, 0)))
			self.pieces.append(Rook('Rook', self.color, (7, 7)))
			
			for i in range(0, 8):
				self.pieces.append(Pawn('Pawn', self.color, (6, i)))

		if self.color == 'black':
			self.pieces.append(King('King', self.color, (0, 4)))
			self.pieces.append(Queen('Queen', self.color, (0, 3)))
			self.pieces.append(Bishop('Bishop', self.color, (0, 2)))
			self.pieces.append(Bishop('Bishop', self.color, (0, 5)))
			self.pieces.append(Knight('Knight', self.color, (0, 1)))
			self.pieces.append(Knight('Knight', self.color, (0, 6)))
			self.pieces.append(Rook('Rook', self.color, (0, 0)))
			self.pieces.append(Rook('Rook', self.color, (0, 7)))

			for i in range(0, 8):
				self.pieces.append(Pawn('Pawn', self.color, (1, i)))

	def draw(self, screen):
		for p in self.pieces:
			p.draw(screen)

	def get_king(self):
		for piece in self.pieces:
			if piece.name == 'King':
				return piece
