from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
import pygame


class King(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.jaque = False
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_king.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_king.png')

	def under_atack(self, pos, self_set, other_set, log):
		row, col = pos
		for piece in other_set:
			if piece.name == 'King':
				other_king_moves = [
					(piece.row - 1, piece.col - 1),
					(piece.row - 1, piece.col),
					(piece.row - 1, piece.col + 1),
					(piece.row , piece.col - 1),
					(piece.row , piece.col + 1),
					(piece.row + 1, piece.col - 1),
					(piece.row + 1, piece.col),
					(piece.row + 1, piece.col + 1)
				]
				if pos in other_king_moves:
					return piece


			elif piece.name == 'Pawn':
				if self.color == 'white':

					if (piece.row == row - 1 and
						(piece.col == col + 1 or piece.col == col-1) ):
						return piece
				elif self.color == 'black':
					if ( piece.row == row + 1 and 
						(piece.col == col + 1 or piece.col == col-1) ):
						return piece

			else:
				if pos in piece.get_valid_moves(other_set, self_set, log):
					return piece

	def is_empty(self, celdas, self_set, other_set):
		for r, c in celdas:
			for piece in self_set:
				if piece.row == r and piece.col == c:
					return False
			for piece in self_set:
				if piece.row == r and piece.col == c:
					return False
		return True

	def get_valid_moves(self, self_set, other_set, log):
		posible_moves = [
			(self.row - 1, self.col - 1),
			(self.row - 1, self.col),
			(self.row - 1, self.col + 1),
			(self.row , self.col - 1),
			(self.row , self.col + 1),
			(self.row + 1, self.col - 1),
			(self.row + 1, self.col),
			(self.row + 1, self.col + 1)
		]

		for piece in self_set:
			for r, c in posible_moves:
				if piece.row == r and piece.col == c:
					posible_moves.pop(posible_moves.index((r, c)))

		remover = []
		for pos in posible_moves:
			if self.under_atack(pos, self_set, other_set, log):
				remover.append(pos)

		for pos in remover:
			posible_moves.pop(posible_moves.index(pos))

		# Remove Edges
		remove=[]
		for r, c in posible_moves:
			if not (0 <= r < ROWS and
				  0 <= c < COLS):
				remove.append((r, c))

		for r, c in remove:
			posible_moves.pop(posible_moves.index((r, c)))

		# castling
		if self.move_count == 0:

			for piece in self_set:
				if  piece.name == 'Rook':
					
					if piece.move_count == 0:
					
						# Rook castling
						if piece.col == 7:
							if self.color == 'white':
								boxes = [(7, 5), (7, 6)]
							else:
								boxes = [(0, 5), (0, 6)]

							amenazadas = False
							for box in boxes:
								if self.under_atack(box, self_set, other_set, log):
									amenazadas = True

							if not amenazadas:
								if self.is_empty(boxes, self_set, other_set):
									if self.color == 'white':
										posible_moves.append((7, 6))
									else:
										posible_moves.append((0, 6))
							

						# Queen castling
						if piece.col == 0:
							if self.color == 'white':
								boxes = [(7, 1), (7, 2), (7, 3)]
							else:
								boxes = [(0, 1), (0, 2), (0, 3)]

							amenazadas = False
							for box in boxes:
								if self.under_atack(box, self_set, other_set, log):
									amenazadas = True

							if not amenazadas:
								if self.is_empty(boxes, self_set, other_set):
									if self.color == 'white':
										posible_moves.append((7, 2))
									else:
										posible_moves.append((0, 2))

		return posible_moves

	def castle(self, pos, self_set):

		if self.color == 'white':
			if  pos == (7, 2):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 0:
							piece.col = 3

			elif pos == (7, 6):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 7:
							piece.col = 5


		elif self.color == 'black':
			if pos == (0, 2):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 0:
							piece.col = 3

			elif pos == (0, 6):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 7:
							piece.col = 5
