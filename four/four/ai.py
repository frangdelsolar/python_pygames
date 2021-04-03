from .constants import ROWS, COLS
import random
import pygame
import time

class AI():
	def __init__(self):
		self.ejecuciones = 0

	def is_terminal_node(self, grid):
		# Revisar filas
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c].value != None:
					try:
						if (grid[r][c].value ==
							grid[r][c+1].value ==
							grid[r][c+2].value ==
							grid[r][c+3].value):
							return grid[r][c].value
					except Exception as e:
						# print(e)
						pass
		
		# Revisar Columnas
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c].value != None:
					try:
						if (grid[r][c].value ==
							grid[r+1][c].value ==
							grid[r+2][c].value ==
							grid[r+3][c].value):
							return grid[r][c].value
					except Exception as e:
						# print(e)
						pass

		# Revisar diagonal ascendente
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c].value != None:
					try:
						if (grid[r][c].value ==
							grid[r-1][c+1].value ==
							grid[r-2][c+2].value ==
							grid[r-3][c+3].value):
							return grid[r][c].value
					except Exception as e:
						# print(e)
						pass

		# Revisar diagonal descendente
		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c].value != None:
					try:
						if (grid[r][c].value ==
							grid[r+1][c+1].value ==
							grid[r+2][c+2].value ==
							grid[r+3][c+3].value):
							return grid[r][c].value
					except Exception as e:
						# print(e)
						pass

		# Revisar empate
		total_cells = ROWS * COLS
		count = 0

		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c].value != None:	
					count += 1

		if count == total_cells:
			print('Empate')
			return 'tie'

	def minimax(self, game, depth, alpha, beta, is_maxim):
		available = self.get_valid_locations(game.grid)

		self.ejecuciones += 1

		game.draw()
		pygame.display.update()


		is_terminal = self.is_terminal_node(game.grid)

		if depth == 0 or is_terminal:
			if is_terminal:
				if is_terminal == game.turno:
					return (None, 1000000)
				if is_terminal == game.other_player():
					return (None, -1000000)
				if is_terminal == 'tie':
					return (None, 0)
			else:
				return (None, self.get_score(game))

		if is_maxim:
			best_score = -float('inf')
			best_move = random.choice(available)

			for col in available:
				row = self.get_next_row(game.grid, col)
				if game.grid[row][col].value == None:
					game.grid[row][col].value = game.turno
					score = self.minimax(game, depth-1, alpha, beta, False)[1]
					game.grid[row][col].value = None
					if score > best_score:
						best_score = score
						best_move = col
					alpha = max(alpha, score)
					if alpha >= beta:
						break
			return (best_move, best_score)

		else:
			best_score = float('inf')
			best_move = random.choice(available)

			for col in available:
				row = self.get_next_row(game.grid, col)

				if game.grid[row][col].value == None:
					game.grid[row][col].value = game.other_player()
					score = self.minimax(game, depth-1, alpha, beta, True)[1]
					game.grid[row][col].value = None
					if score < best_score:
						best_score = score
						best_move = col
					beta = min(beta, score)
					if alpha >= beta:
						break

			return (best_move, best_score)



	def score_window(self, window, game):
		score = 0 

		if window.count(game.turno) == 4 and window.count(None) == 0:
			score += 100

		elif window.count(game.turno) == 3 and window.count(None) == 1:
			score += 5

		elif window.count(game.turno) == 2 and window.count(None) == 2:
			score += 2

		if window.count(game.other_player()) == 3 and window.count(None) == 1:
			score -= 4

		return score

	def get_score(self, game):
		WINDOW_LENGTH = 4
		score = 0

		# Centro
		centro = [game.grid[i][COLS//2].value for i in range(ROWS)]
		centro_count = centro.count(game.turno)
		score += centro_count * 3

		# Horizontal
		for r in range(ROWS):
			window = []
			for c in range(COLS-3):
				window = [game.grid[r][c+i].value for i in range(WINDOW_LENGTH)]				
				score += self.score_window(window, game)

		# Vertical
		for r in range(ROWS-3):
			window = []
			for c in range(COLS):
				window = [game.grid[r+i][c].value for i in range(WINDOW_LENGTH)]
				score += self.score_window(window, game)

		# positiva
		for r in range(ROWS-3):
			window = []
			for c in range(COLS-3):
				window = [game.grid[r+i][c+i].value for i in range(WINDOW_LENGTH)]
				score += self.score_window(window, game)

		# negativa
		for r in range(3, ROWS):
			window = []
			for c in range(COLS-3):
				window = [game.grid[r-i][c+i].value for i in range(WINDOW_LENGTH)]
				score += self.score_window(window, game)

		return score

	def get_next_row(self, grid, col):
		for row in range(ROWS-1, -1, -1):
			if grid[row][col].value == None:
				return row

	def get_valid_locations(self, grid):
		locations = []
		for r in range(ROWS-1, -1, -1):
			for c in range(COLS):
				if grid[r][c].value == None:					
					if c not in locations:
						locations.append(c)

		return locations

	def get_move(self, game):
		valid_locations = self.get_valid_locations(game.grid)

		self.ejecuciones = 0
		col = self.minimax(game, 3, -float('inf'), float('inf'), True)[0]
		print(self.ejecuciones)

		return col








