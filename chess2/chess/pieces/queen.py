from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
import pygame


class Queen(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_queen.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_queen.png')

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

		#NW
		found = False
		for i in range(1, ROWS):

			if not(self.row-i > ROWS or
				   self.row-i < 0 or
				   self.col-i > COLS or 
				   self.col-i < 0):

				for piece in other_set:
					if piece.row == self.row-i and piece.col ==self.col-i :
						basic_moves.append((self.row-i, self.col-i))
						found = True

				for piece in self_set:
					if piece.row == self.row-i and piece.col == self.col - i:
						found = True

			if not found:
				basic_moves.append((self.row-i, self.col - i))
			else:
				break

		#NE
		found = False
		for i in range(1, ROWS):
			if not(self.row-i > ROWS or
				   self.row-i < 0 or
				   self.col+i > COLS or 
				   self.col+i < 0):
				for piece in other_set:
					if piece.row == self.row-i and piece.col ==self.col+i :

						basic_moves.append((self.row-i, self.col + i))
						found = True

				for piece in self_set:
					if piece.row == self.row-i and piece.col == self.col + i:
						found = True
				
				if not found:
					basic_moves.append((self.row-i, self.col + i))
				else:
					break

			#SE
		found = False
		for i in range(1, ROWS):
			if not(self.row+i > ROWS or
				   self.row+i < 0 or
				   self.col+i > COLS or 
				   self.col+i < 0):
				
				for piece in other_set:
					if piece.row == self.row + i and piece.col ==self.col + i :

						basic_moves.append((self.row + i, self.col + i))
						found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col + i:
						found = True
				
				if not found:
					basic_moves.append((self.row + i, self.col + i))
				else:
					break

			#SW
		found = False
		for i in range(1, ROWS):
			if not(self.row+i > ROWS or
				   self.row+i < 0 or
				   self.col-i > COLS or 
				   self.col-i < 0):
				
				for piece in other_set:
					if piece.row == self.row + i and piece.col ==self.col - i :

						basic_moves.append((self.row + i, self.col - i))
						found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col - i:
						found = True
				
				if not found:
					basic_moves.append((self.row + i, self.col - i))
				else:
					break

		# Remove Edges
		remove=[]
		for r, c in basic_moves:
			if not (0 <= r < ROWS and
				  0 <= c < COLS):
				remove.append((r, c))

		for r, c in remove:
			basic_moves.pop(basic_moves.index((r, c)))

		return basic_moves
