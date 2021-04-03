from .pieces.chess_set import ChessSet
from .constants import GREEN,SQUARE_SIZE, BLUE, RED
import pygame 
import copy
from .ai import AI



class Player():
	def __init__(self, name, color, is_ai):
		self.name = name
		self.color = color
		self.points = 0
		self.clicks = 0
		self.is_ai = is_ai
		self.set = ChessSet(color)
		self.hand = None
		self.ai = AI()


	def __repr__(self):
		return f'Jugador {self.name} - {self.points} puntos'

	def draw(self, screen, self_set, other_set, log):
		self.set.draw(screen)

		# if self.hand:
		# 	pygame.draw.rect(screen, GREEN, (self.hand.col*SQUARE_SIZE, self.hand.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)
		# 	for move in self.get_all_moves(other_set, log):
		# 		if move['pieza'] == self.hand:
		# 			pygame.draw.rect(screen, BLUE, (move['move'][1]*SQUARE_SIZE, move['move'][0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)
		# else:
		# 	for move in self.get_all_moves(other_set, log):
		# 		pygame.draw.rect(screen, RED, (move['pieza'].col*SQUARE_SIZE, move['pieza'].row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)

	def king_checked(self, other_set, log):
		king = self.set.get_king()
		try:
			atacante = king.under_atack((king.row, king.col), self.set.pieces, other_set, log)
			if atacante:
				return True
		except Exception as e:
			print(e)

	def pop_piece(self, row, col, other_set):
		for piece in other_set:
			if piece.row == row and piece.col == col:
				if not piece.name == 'King':
					removed = other_set.pop(other_set.index(piece))
					return removed

	def restore_piece(self, piece, other_set):
		other_set.append(piece)

	def get_all_moves(self, other_set, log):

		all_moves = []

		for piece in self.set.pieces:
			for move in piece.get_valid_moves(self.set.pieces, other_set, log):
				all_moves.append({'pieza': piece, 'move': move})

		remover = []
		for move in all_moves:
			# Desempaquetar
			piece = move['pieza']
			move_r, move_c = move['move'][0], move['move'][1]

			# Estado actual del tablero
			actual_pos = piece.row, piece.col
			 
			# Simular
			removed = self.pop_piece(move_r, move_c, other_set)
			piece.row, piece.col = move_r, move_c
			if self.king_checked(other_set, log):
				remover.append(move)

			# reestablecer
			piece.row, piece.col = actual_pos
			if removed:
				self.restore_piece(removed, other_set)


		for move in remover:
			if move in all_moves:
				all_moves.pop(all_moves.index(move))

		return all_moves

	def grab_piece(self, row, col, other_set, log):
		moves = self.get_all_moves(other_set, log)
		for piece in self.set.pieces:
			for move in moves:
				if piece == move['pieza']:
					if piece.row == row and piece.col == col:
						self.hand = piece
						return True
		return False


	def release_piece(self, row, col, other_set, screen, game):


		# Soltar pieza en el mismo sitio:
		if self.hand.row == row and self.hand.col == col:
			self.hand = None
			return False

		# Verificar si es un movimiento válido
		moves = self.get_all_moves(other_set, game.log)
		intend = {'pieza': self.hand, 'move': (row, col)}
		if not intend in moves:
			return False

		# Hubo En Paessant?
		if len(game.log) >= 2:
			log_2 = game.log[-2]
			log_1 = game.log[-1]

			if log_2.piece.name == log_1.piece.name == 'Pawn':
				if (log_2.piece.col == log_1.piece.col + 1 or 
					log_2.piece.col == log_1.piece.col - 1):
					if abs(log_1.end_pos[0] - log_1.start_pos[0]) == 2:
						if log_2.piece.color == 'white':
							rb = 3
						else:
							rb = 4
						if log_2.end_pos[0] == rb:
							other_set.pop(other_set.index(log_1.piece))



		# Es enroque?
		if self.hand.name == 'King':
			if self.color == 'white':
				if ( (row, col) == (7, 2) or
					 (row, col) == (7, 6) ):

					self.hand.castle((row, col), self.set.pieces)

			elif self.color == 'black':
				if ( (row, col) == (0, 2) or
					 (row, col) == (0, 6) ):

					self.hand.castle((row, col), self.set.pieces)


		# Es promoción?
		if self.hand.name == 'Pawn':

			if self.color == 'white':
				if row == 0:
					self.hand.promote((row, col), self.set.pieces, screen)


			elif self.color == 'black':
				if row == 7:
					self.hand.promote((row, col), self.set.pieces, screen)

		game.log_move(self, self.hand, (self.hand.row, self.hand.col), (row, col))
		self.hand.move_count += 1
		self.hand.row = row
		self.hand.col = col
		self.hand = None
		return True