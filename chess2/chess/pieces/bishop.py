from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
import pygame


class Bishop(Piece):
	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_bishop.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_bishop.png')

	def get_valid_moves(self, self_set, other_set, log):
		basic_moves = []


		#NW
		found = False
		for i in range(1, ROWS):
			for piece in other_set:
				if piece.row == self.row-i and piece.col == self.col-i:
					if (0 <= self.row-i < ROWS and
						0 <= self.col-i < COLS):
						basic_moves.append((self.row-i, self.col-i))
						found = True

			for piece in self_set:
				if piece.row == self.row-i and piece.col == self.col - i:
					found = True

			if not found:
				if (0 <= self.row-i < ROWS and
					0 <= self.col-i < COLS):
					basic_moves.append((self.row-i, self.col - i))
			else:
				break

		#NE
		found = False
		for i in range(1, ROWS):
				for piece in other_set:
					if piece.row == self.row-i and piece.col ==self.col+i :
						if (0 <= self.row-i < ROWS and
							0 <= self.col+i < COLS):

							basic_moves.append((self.row-i, self.col + i))
							found = True

				for piece in self_set:
					if piece.row == self.row-i and piece.col == self.col + i:
						found = True
				
				if not found:
					if (0 <= self.row-i < ROWS and
						0 <= self.col+i < COLS):
						basic_moves.append((self.row-i, self.col + i))
				else:
					break

			#SE
		found = False
		for i in range(1, ROWS):				
				for piece in other_set:
					if piece.row == self.row + i and piece.col == self.col + i :
						if (0 <= self.row + i < ROWS and
							0 <= self.col + i < COLS):
							basic_moves.append((self.row + i, self.col + i))
							found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col + i:
						found = True
				
				if not found:
					if (0 <= self.row + i < ROWS and
						0 <= self.col + i < COLS):
						basic_moves.append((self.row + i, self.col + i))
				else:
					break

		#SW
		found = False
		for i in range(1, ROWS):
			
				for piece in other_set:
					if piece.row == self.row + i and piece.col ==self.col - i :
						if (0 <= self.row+i < ROWS and
							0 <= self.col-i < COLS):
							basic_moves.append((self.row + i, self.col - i))
							found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col - i:
						found = True
				
				if not found:
					if (0 <= self.row+i < ROWS and
						0 <= self.col-i < COLS):
						basic_moves.append((self.row + i, self.col - i))
				else:
					break

		return basic_moves
