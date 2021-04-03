from .board import Board
from .player import Player
from .constants import ROWS, COLS, SQUARE_SIZE

class Move():
	def __init__(self, player, piece, start_pos, end_pos):
		self.player = player
		self.piece = piece
		self.start_pos = start_pos
		self.end_pos = end_pos

	def __str__(self):
		return f'player: {self.player}. piece: {self.piece}. from: {self.start_pos}. to: {self.end_pos}'

class Game():
	def __init__(self, screen):
		self.board = Board()
		self.screen = screen
		self.players = []
		self.turno = None
		self.run = True
		self.log = []
		self.build()

	def build(self):
		self.players.append(Player('P1', 'white', False))
		self.players.append(Player('P2', 'black', True))
		self.turno = self.players[0]

	def check_win(self):
		player = self.turno
		if len(player.get_all_moves(self.other_player().set.pieces, self.log)) <= 0:
			if player.king_checked(self.other_player().set.pieces, self.log):
				print('jaque mate')
				self.run = False
				return

			print('empate')
			self.run = False
			return
		return


	def log_move(self, player, piece, start_pos, end_pos):
		move = Move(player, piece, start_pos, end_pos)
		self.log.append(move)
		# print(move)

	def other_player(self):
		if self.turno == self.players[0]:
			return self.players[1]
		else:
			return self.players[0]

	def draw(self):
		self.board.draw(self.screen)
		for p in self.players:
			p.draw(self.screen, self.turno.set.pieces, self.other_player().set.pieces, self.log)

	def cambiar_de_turno(self):
		if self.turno == self.players[0]:
			self.turno = self.players[1]
		else:
			self.turno = self.players[0]

	def eat_piece(self, row, col):
		for p in self.other_player().set.pieces:
			if p.row == row and p.col == col:
				piece = self.other_player().set.pieces.pop(self.other_player().set.pieces.index(p))
				return piece

	def click(self, button, pos):
		if not self.turno.is_ai:
			x, y = pos
			col = x // SQUARE_SIZE
			row = y // SQUARE_SIZE

			player = self.turno
			other_player = self.other_player()
			
			valid_move = False

			if not player.hand:
				player.grab_piece(row, col, other_player.set.pieces, self.log)

			else:
				valid_move = player.release_piece(row, col, other_player.set.pieces, self.screen, self)


			if valid_move:
				self.eat_piece(row, col)
				self.cambiar_de_turno()


		else:
			ai = self.turno.ai.move(self)
			piece = ai['pieza']

			col = piece.col
			row = piece.row

			player = self.turno
			other_player = self.other_player()
			
			valid_move = False


			player.hand = piece
			move = ai['move']
			row = move[0]
			col = move[1]
			valid_move = player.release_piece(row, col, other_player.set.pieces, self.screen, self)


			if valid_move:
				self.eat_piece(row, col)
				self.cambiar_de_turno()


		return True