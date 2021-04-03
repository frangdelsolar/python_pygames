from .pac_man import Pacman
import random
from .constants import LEVEL_1, BLUE, BOMBS, ROWS, COLS, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import pygame
import time



class Ghost(Pacman):
	def __init__(self, row, col, x_speed, y_speed, color, juego, screen):
		super().__init__(row, col, x_speed, y_speed, color)
		self.path = []
		self.screen = screen
		self.end_pos = None
		self.status = 0

	def is_end(self, current_pos, end_pos):
		if  (current_pos[0], current_pos[1]) == end_pos:
			return True
		return False

	def find_path(self, board, path, end_pos):		
		for pos in path:			
			if self.is_end(pos, end_pos):
				return path

			else:
				for vecino in self.get_adjacents(pos, board):
					if not vecino in path:
						try:
							if board.level[vecino[0]][vecino[1]] != 1:
								# pygame.draw.rect(self.screen, self.color, (vecino[1]*SQUARE_SIZE, vecino[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
								# pygame.display.update()
								# # time.sleep(0.2)

								path.append(vecino)
								self.find_path(board, path, end_pos)

						except Exception as e:
							print(e)



	def get_adjacents(self, pos, board):
		row, col, count = pos
		count += 1
		vecinos = [
					(row-1, col, count),
					(row+1, col, count),
					(row, col-1, count),
					(row, col+1, count),
					]

		for row, col, count in vecinos:
			try:
				if board.level[row][col] == 1:
					vecinos.pop(vecinos.index((row, col, count)))
			except Exception as e:
				# print(e)
				vecinos.pop(vecinos.index((row, col, count)))

		return vecinos

	def get_neighbours(self, row, col, board):
		vecinos = [
					(row-1, col),
					(row+1, col),
					(row, col-1),
					(row, col+1),
					]

		for row, col in vecinos:
			if board.level[row][col]:
				if board.level[row][col] == 1:
					vecinos.pop(vecinos.index((row, col)))
			else:
				# vecinos.pop(vecinos.index((row, col)))	
				pass

		return vecinos

	def get_direccion(self, board, path):
		vecinos = self.get_neighbours(self.row, self.col, board)

		prox = None, None, float('inf')
		for row, col in vecinos:
			for i, j, c in path:
				if row == i and j == col:
					if c < prox[2]:
						prox = i, j, c

		if prox[0] != None and prox[1] != None:
			direccion = (prox[0]-self.row, prox[1]-self.col)
		else:
			direccion = (0, 0)

		return direccion

	def navigate(self, game):
		board = game.board
		end_pos = self.end_pos
		count = 0
		path = [(end_pos[0], end_pos[1], count)]
		path = self.find_path(board, path, (self.row, self.col))
		direccion = self.get_direccion(board, path)
		return direccion


	def update(self, game):
		super().update(game)

		if self.row == game.pacman.row and self.col == game.pacman.col:
			game.pacman.captured()


class Blinky(Ghost):
	def __init__(self, row, col, x_speed, y_speed, color, game, screen):
		super().__init__(row, col, x_speed, y_speed, color, game, screen)
		self.end_pos = (game.pacman.row, game.pacman.col)

	def update(self, game):
		super().update(game)
		self.end_pos = (game.pacman.row, game.pacman.col)



class Pinky(Ghost):
	def __init__(self, row, col, x_speed, y_speed, color, game, screen):
		super().__init__(row, col, x_speed, y_speed, color, game, screen)
		self.end_pos = (game.pacman.row, game.pacman.col)


	def update(self, game):
		super().update(game)

		end_row = game.pacman.row + game.pacman.y_speed*2
		end_col = game.pacman.col + game.pacman.x_speed*2
		self.end_pos = (end_row, end_col)


class Inky(Ghost):
	def __init__(self, row, col, x_speed, y_speed, color, game, screen):
		super().__init__(row, col, x_speed, y_speed, color, game, screen)


class Clyde(Ghost):
	def __init__(self, row, col, x_speed, y_speed, color, game, screen):
		super().__init__(row, col, x_speed, y_speed, color, game, screen)
