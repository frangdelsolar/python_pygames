import pygame
from .constants import BOARD_SIZE, BOMBS, ROWS, COLS, WHITE, SQUARE_SIZE, RED, GREEN, BLACK, FONTSIZE, GREY
import random


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.has_bomb = False
		self.has_flag = False
		self.hide = True
		self.vecinos = []
		self.vecinos_armados = 0
		self.build()

	def __repr__(self):
		# if self.has_bomb:
		# 	return "B"
		# else:
		# 	return '.'
		if self.hide:
			return "."
		else:
			return '0'
		# return f'{self.row}, {self.col}'

	def _crear_vecindad(self):

		if self.row == 0: 
			
			if self.col == 0:
				self.vecinos = [(self.row, self.col+1), (self.row+1, self.col), (self.row+1, self.col+1)]

			elif self.col == COLS-1:
				self.vecinos = [(self.row, self.col-1), (self.row+1, self.col), (self.row+1, self.col-1)]

			else:
				self.vecinos = [(self.row, self.col+1), (self.row+1, self.col), (self.row+1, self.col+1), 
								(self.row, self.col-1), (self.row+1, self.col-1)]


		elif self.row == ROWS-1:

			if self.col == 0:
				self.vecinos = [(self.row, self.col+1), (self.row-1, self.col), (self.row-1, self.col+1)]

			elif self.col == COLS-1:
				self.vecinos = [(self.row, self.col-1), (self.row-1, self.col), (self.row-1, self.col-1)]

			else:
				self.vecinos = [(self.row, self.col+1), (self.row-1, self.col), (self.row-1, self.col+1), 
								(self.row, self.col-1), (self.row-1, self.col-1)]

		else:

			if self.col == 0:
				self.vecinos = [(self.row-1, self.col), (self.row-1, self.col+1), 
														(self.row  , self.col+1),
								(self.row+1, self.col), (self.row+1, self.col+1)]

			elif self.col == COLS-1:
				self.vecinos = [(self.row-1, self.col-1), (self.row-1, self.col), 
								(self.row  , self.col-1),
								(self.row+1, self.col-1), (self.row+1, self.col)]

			else:
				self.vecinos = [(self.row-1, self.col-1), (self.row-1, self.col), (self.row-1, self.col+1), 
								(self.row  , self.col-1), 						  (self.row  , self.col+1),
								(self.row+1, self.col-1), (self.row+1, self.col), (self.row+1, self.col+1)]


	def build(self):
		self._crear_vecindad()

	def plantar_bomba(self):
		self.has_bomb = True

	def set_flag(self):
		if self.hide:
			self.has_flag = True

	def unset_flag(self):
		self.has_flag = False

	def revelar(self, board, screen):
		clock = pygame.time.Clock()
		self.hide = False
		self.draw(screen)
		pygame.display.update()
		clock.tick(200)
		if self.vecinos_armados == 0:
			self.mostrar_vecinos(board, screen)


	def mostrar_vecinos(self, board, screen):
		for r, c in self.vecinos:
			vec = board.grid[r][c]
			if vec.hide:
				vec.revelar(board, screen)

	def draw(self, screen):

		myfont = pygame.font.SysFont("monospace", FONTSIZE)
		myfont.set_bold(True)

  
		pygame.draw.rect(screen, WHITE, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
		
		if self.has_flag:
			pygame.draw.circle(screen, GREEN, (self.col*SQUARE_SIZE + SQUARE_SIZE//2, self.row*SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//3, 5)

		if not self.hide:
			pygame.draw.rect(screen, GREY, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
			if self.vecinos_armados > 0:
				label = myfont.render(str(self.vecinos_armados), 10, WHITE)
				screen.blit(label, (int(self.col*SQUARE_SIZE+SQUARE_SIZE/3), int(self.row*SQUARE_SIZE+ SQUARE_SIZE/3)))


			if self.has_bomb:
				pygame.draw.circle(screen, RED, (self.col*SQUARE_SIZE + SQUARE_SIZE//2, self.row*SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//3)
		else:
			if self.has_bomb:
				pygame.draw.circle(screen, RED, (self.col*SQUARE_SIZE + SQUARE_SIZE//2, self.row*SQUARE_SIZE + SQUARE_SIZE//2), 5)


class Board():
	def __init__(self):
		self.grid = []
		self.build()

	def _contar_bombas(self):
		for i in range(COLS):
			for j in range(ROWS):
				cell = self.grid[i][j]
				for row, col in cell.vecinos:
					vecino = self.grid[row][col]
					if vecino.has_bomb:
						cell.vecinos_armados += 1

	def build(self):
		for i in range(COLS):
			line = []

			for j in range(ROWS):
				line.append(Cell(i,j))

			self.grid.append(line)

		bombas_plantadas = 0
		while bombas_plantadas < BOMBS:
			rand_row = random.randint(0, ROWS-1)
			rand_col = random.randint(0, COLS-1)
			
			if not self.grid[rand_row][rand_col].has_bomb:
				self.grid[rand_row][rand_col].plantar_bomba()
				bombas_plantadas += 1

		self._contar_bombas()

	def draw(self, screen):
		screen.fill(BLACK)
		for i in range(COLS):
			for j in range(ROWS):
				self.grid[i][j].draw(screen)

	def click(self, button, pos, screen):
		"""
		Devuelve si el estado del juego debe continuar o no.
		"""

		x, y = pos
		col = x // SQUARE_SIZE
		row = y // SQUARE_SIZE

		cell = self.grid[row][col]

		if button == 3:
			if cell.has_flag:
				cell.unset_flag()
			else:
				cell.set_flag()

		if button == 1:
			if cell.has_bomb:
				cell.unset_flag()				
				return False
			else:
				cell.unset_flag()
				cell.revelar(self, screen)

		return True

	def revelar(self, screen):
		clock = pygame.time.Clock()

		for i in range(COLS):
			for j in range(ROWS):
				self.grid[i][j].revelar(self, screen)
				self.grid[i][j].draw(screen)
				pygame.display.update()
				clock.tick(200)