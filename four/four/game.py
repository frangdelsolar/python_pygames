from .board import Board
from .player import Player
from .constants import ROWS, COLS, SQUARE_SIZE

class Move():
	def __init__(self, player, pos):
		self.player = player
		self.pos = pos

	def __str__(self):
		return f'player: {self.player}. {self.pos}'

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
		self.players.append(Player('P1', 'blue', True))
		self.players.append(Player('P2', 'red', False))
		self.turno = self.players[0]

	@property
	def grid(self):
		return self.board.grid

	def check_win(self):
		# Revisar filas
		for r in range(ROWS):
			for c in range(COLS):
				if self.board.grid[r][c].value != None:
					try:
						if (self.board.grid[r][c].value ==
							self.board.grid[r][c+1].value ==
							self.board.grid[r][c+2].value ==
							self.board.grid[r][c+3].value):
							print('Tenemos un ganador', self.board.grid[r][c].value)
							# self.run = False
							return True
					except Exception as e:
						# print(e)
						pass
		
		# Revisar Columnas
		for r in range(ROWS):
			for c in range(COLS):
				if self.board.grid[r][c].value != None:
					try:
						if (self.board.grid[r][c].value ==
							self.board.grid[r+1][c].value ==
							self.board.grid[r+2][c].value ==
							self.board.grid[r+3][c].value):
							print('Tenemos un ganador', self.board.grid[r][c].value)
							# self.run = False
							return True
					except Exception as e:
						# print(e)
						pass

		# Revisar diagonal ascendente
		for r in range(ROWS):
			for c in range(COLS):
				if self.board.grid[r][c].value != None:
					try:
						if (self.board.grid[r][c].value ==
							self.board.grid[r-1][c+1].value ==
							self.board.grid[r-2][c+2].value ==
							self.board.grid[r-3][c+3].value):
							print('Tenemos un ganador', self.board.grid[r][c].value)
							# self.run = False
							return True
					except Exception as e:
						# print(e)
						pass

		# Revisar diagonal descendente
		for r in range(ROWS):
			for c in range(COLS):
				if self.board.grid[r][c].value != None:
					try:
						if (self.board.grid[r][c].value ==
							self.board.grid[r+1][c+1].value ==
							self.board.grid[r+2][c+2].value ==
							self.board.grid[r+3][c+3].value):
							print('Tenemos un ganador', self.board.grid[r][c].value)
							# self.run = False
							return True
					except Exception as e:
						# print(e)
						pass

		# Revisar empate
		total_cells = ROWS * COLS
		count = 0

		for r in range(ROWS):
			for c in range(COLS):
				if self.board.grid[r][c].value != None:	
					count += 1

		if count == total_cells:
			print('Empate')
			return False

	def log_move(self, player, pos):
		move = Move(player, pos)
		self.log.append(move)
		print(move)

	def other_player(self):
		if self.turno == self.players[0]:
			return self.players[1]
		else:
			return self.players[0]

	def draw(self):
		self.board.draw(self.screen)

	def cambiar_de_turno(self):
		if self.turno == self.players[0]:
			self.turno = self.players[1]
		else:
			self.turno = self.players[0]

	def poner_ficha(self, col):
		for r in range(ROWS-1, -1, -1):
			if self.board.grid[r][col].value == None:
				self.board.grid[r][col].value = self.turno
				break

	def click(self, button, pos):

		if not self.turno.is_ai:
			x, y = pos
			col = x // SQUARE_SIZE
			row = y // SQUARE_SIZE

		else:
			col = self.turno.ai.get_move(self)

		self.poner_ficha(col)
		self.cambiar_de_turno()
		return True