import pygame
import random
import copy
from buscaminas.constants import ROWS, COLS, OTRO, SQUARE_SIZE, WIDTH, HEIGHT


class Cell():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.points = 0

	def __repr__(self):
		return f'{self.points}'


class AI():
	def __init__(self):
		self.grid = []
		self.moves_done = []
		self._build_grid()
		self.mines = []
		self.safe_moves = []
		self.void_moves = []


	def __str__(self):
		for i in range(ROWS):
			for j in range(COLS):
				print(self.grid[i][j], end=', ')
			print()
		return 'Juego'

	def _build_grid(self):
		for i in range(ROWS):
			self.grid.append([])
			for j in range(COLS):
				self.grid[i].append(Cell(i, j))


	def randomize_move(self):
		x = random.randint(0, WIDTH)
		y = random.randint(0, HEIGHT)
		return (x, y)

	def valid_move(self, pos, juego):
		x, y = pos

		col = x // SQUARE_SIZE
		row = y // SQUARE_SIZE

		cell = self.grid[row][col]
		if cell in self.mines:
			print('No debería hacer click allí')
			return False 

		if juego.board.grid[row][col].hide:
			return False
		return True

	def draw_move(self, pos, screen):
		x, y = pos
		col = x // SQUARE_SIZE
		row = y // SQUARE_SIZE
		pygame.draw.circle(screen, OTRO, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 5)


	def update_grid(self, juego):
		count = 0
		for i in range(ROWS):
			for j in range(COLS):
				if not juego.board.grid[i][j].hide:
					self.grid[i][j] = None
					count +=1
		return count


	def search_safe(self, juego):
		for mine in self.mines:
			for vr, vc in juego.board.grid[mine.row][mine.col].vecinos:
				vec1 = juego.board.grid[vr][vc]
				if not vec1.hide:
					# 1. conocer cantidad de vecinos_armados de la celda
					vec1_vec_armados = vec1.vecinos_armados

					# 2. Restarle la cantidad de infinitos y de celdas reveladas que la rodean
					vec1_vecs = juego.board.grid[vr][vc].vecinos
					vec1_cant_vecs = len(vec1_vecs)

					vecs_dispo = []
					for v1r, v1c in vec1_vecs:
						v1vec = juego.board.grid[v1r][v1c]
						if v1vec.hide:
							vecs_dispo.append(v1vec)

					v_minas = []
					for v in vecs_dispo:
						if self.grid[v.row][v.col] in self.mines:
							v_minas.append(v)

					rem = []
					for i in vecs_dispo:
						for j in v_minas:
							if i==j:
								if not i in self.void_moves:
									self.void_moves.append(i)
							else:
								rem.append(i)

					for c in rem:
						if not self.grid[c.row][c.col].points == float('inf'):
							if (c.row, c.col) not in self.safe_moves:
								self.safe_moves.append((c.row, c.col))

		for c in self.void_moves:
			if (c.row, c.col) in self.safe_moves:
				i = self.safe_moves.index((c.row, c.col))
				self.safe_moves.pop(i)


		return self.safe_moves


	def calc_points(self, juego):
		for i in range(ROWS):
			for j in range(COLS):
				if self.grid[i][j]:
					self.grid[i][j].points = 0

		# si la celda no está en la grilla, entonces, puedo conocer su número de vecinos armados
		for i in range(ROWS):
			for j in range(COLS):

				if not juego.board.grid[i][j].hide: # si esta celda ya ha sido revelada
					# calcular posibilidades de los vecinos
					# asegurarme cuántos vecinos están ocultos
					posibles = 0
					for vec in juego.board.grid[i][j].vecinos:
						r, c = vec
						if juego.board.grid[r][c].hide:
							posibles += 1
					
					for vec in juego.board.grid[i][j].vecinos:
						r, c = vec
						if self.grid[r][c]:
							prob = juego.board.grid[i][j].vecinos_armados/posibles
							if prob == 1.0:
								prob = float('inf')
								if not self.grid[r][c] in self.mines:
									self.mines.append(self.grid[r][c])
							self.grid[r][c].points += prob


	def next_move(self, juego):

		# Revisar seguros

		for m in self.void_moves:
			t = (m.row, m.col)
			if t in self.safe_moves:
				i = self.safe_moves.index(t)
				self.safe_moves.pop(i)

		for m in self.safe_moves:
			r, c = m
			if not juego.board.grid[r][c].hide:
				i = self.safe_moves.index(m)
				self.safe_moves.pop(i)		



		# 1. hay movimientos 100% seguros?
		if len(self.safe_moves) > 0:
			safe = self.safe_moves.pop(0)
			if safe:
				row, col = safe
				pos = row*SQUARE_SIZE, col*SQUARE_SIZE
				return pos

		else:
			print('No quedan movimientos seguros',self.safe_moves)
			# 2. Elegir movimiento con menor porcentaje de riesgo.
			# 3. Aleatorizar


			pos = self.randomize_move()

			if not self.valid_move(pos, juego):
				pos = self.randomize_move()	


			self.draw_move(pos, juego.screen)
			self.moves_done.append(pos)


			return pos		

	def print_grid(self):
		for i in range(ROWS):
			for j in range(COLS):
				if self.grid[i][j]:
					print( "{:.1f}".format(self.grid[i][j].points), end=', ')
				else:
					print('...', end=', ')
			print()
		print()

		print('Seguros:', self.safe_moves)

		print('Evitar:')
		for i in self.void_moves:
			print(f'({i.row}, {i.col})')



	def execute(self, juego):
		self.update_grid(juego)
		self.calc_points(juego)
		self.search_safe(juego)

		pos = self.next_move(juego)


		pygame.display.update()

		# for debugging
		self.print_grid()

		event = 1 # click izquierdo del mouse

		return (event, pos)