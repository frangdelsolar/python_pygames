import pygame
import random
from buscaminas.constants import ROWS, COLS, OTRO, SQUARE_SIZE, WIDTH, HEIGHT, BOMBS

class Move():
	def __init__(self, r, c):
		self.row = r
		self.col = c
		self.vecinos = []
		self._crear_vecindad()
		self.hidden = True
		self.probability = 0
		self.visited = False
		self.flagged = []
		self.vecinos_armados = None

	def __str__(self):
		return f'({self.row}, {self.col}, {self.hidden})'

	def __repr__(self):
		return f'({self.row}, {self.col})'

	def __lt__(self, other):
		return self.probability < other.probability

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

	def get_sorrounding_bombs(self, moves, void_moves):
		count = []
		for i, j in self.vecinos:
			m = moves[i][j]
			if m in void_moves:
				count.append(m)
		return count

	def get_sorrounding_safe(self, moves, safe_moves):
		count = []
		for i, j in self.vecinos:
			m = moves[i][j]			
			if m in safe_moves:
				count.append(m)
		return count

	def get_influencers(self, moves):
		count = []
		for i, j in self.vecinos:
			if moves[i][j].vecinos_armados:
				count.append(moves[i][j])
		return count

	def get_libres(self, moves):
		count = []
		for i, j in self.vecinos:
			if moves[i][j].hidden:
				count.append(moves[i][j])
		return count	

	def get_status(self, void_moves, safe_moves, moves):
		print('.........................')
		print('MOVE', self.row, self.col)
		print('.........................')

		print('Oculta:', self.hidden)
		print('probability', self.probability)
		print('vecinos_armados', self.vecinos_armados)
		print('sorrounding_bombs', self.get_sorrounding_bombs(moves, void_moves))
		print('sorrounding_safe', self.get_sorrounding_safe(moves, safe_moves))
		print('influencers', self.get_influencers(moves))
		print('vecinos libres', self.get_libres(moves))
		print()

	def set_probability(self, moves, void_moves, safe_moves):
		if self.vecinos_armados:
			if self.vecinos_armados > 0:

				# 100% certeza				
				if self.vecinos_armados == len(self.get_libres(moves)):
					for m in self.get_libres(moves):
						m.probability = float('inf')

				# visitar vecinos y sumar puntos propios
				else:
					for m in self.get_libres(moves):

						if m in safe_moves:
							m.probability = -1
						else:
							# print(m)
							amenazas = self.vecinos_armados

							if m.get_sorrounding_bombs(moves, void_moves):
								amenazas -= len(m.get_sorrounding_bombs(moves, void_moves))

							# print('amenazas', amenazas)

							vacias = len(self.get_libres(moves))

							if m.get_sorrounding_safe(moves, safe_moves):
								vacias -= len(m.get_sorrounding_safe(moves, safe_moves))

							# print('vacías', vacias)
							try:
								m.probability += amenazas / vacias
							except ZeroDivisionError as e:
								# print(m, e)
								# m.get_status(void_moves, safe_moves, moves)
								m.probability += 999 


class AI():
	def __init__(self):
		self.moves = []
		self.available_moves = []
		self.safe_moves = []
		self.void_moves = []
		self.moves_done = []
		self.flag_moves = []
		self.objetivos = None
		self.build_moves()

	def show(self):
		print('//////////////////////////////////////////////////////////////')

		for i in range(ROWS):
			for j in range(COLS):
				if self.moves[i][j].probability:
						print("{:.1f}".format(self.moves[i][j].probability), end=', ')

					# if self.moves[i][j].probability == float('inf'):
					# 	print('BoB', end=', ')
					# else:
					# 	print("{:.1f}".format(self.moves[i][j].probability), end=', ')
				else:
					if self.moves[i][j].hidden:
						print(' ? ', end=', ')
					else:
						print('   ', end=', ')

			print()

		# print('available_moves', self.available_moves)		
		print('safe_moves', self.safe_moves)		
		print('void_moves', self.void_moves)		
		print('flag_moves', self.flag_moves)		

		print('Detalle:')
		print('Movimientos totales', (ROWS * COLS))
		print('available_moves', len(self.available_moves))
		print('void_moves', len(self.void_moves))		
		print('safe_moves', len(self.safe_moves))		
		print('flag_moves', len(self.flag_moves))		
		print('moves_done', self.moves_done)

	def build_moves(self):
		for i in range(ROWS):
			self.moves.append([])
			for j in range(COLS):
				self.moves[i].append(Move(i, j))

	def get_info(self, juego):
		self.objetivos = BOMBS
		self.available_moves = []

		for r in range(ROWS):
			for c in range(COLS):
				self.moves[r][c].hidden = juego.board.grid[r][c].hide
				self.moves[r][c].flagged = juego.board.grid[r][c].has_flag

				# Si la celda ya ha sido revelada
				if self.moves[r][c].hidden:
					# Agregar a la lista de movimientos posibles
					self.available_moves.append(self.moves[r][c])

				else:
					# Actualizar info sobre amenazas
					self.moves[r][c].vecinos_armados = juego.board.grid[r][c].vecinos_armados

	def print_known_facts(self):
		for r in range(ROWS):
			for c in range(COLS):
				self.moves[r][c].get_status(self.void_moves, self.safe_moves, self.moves)

	def resetear_prob(self):
		# probability = bombas_restantes / ocultas

		# Resetear valores
		for r in range(ROWS):
			for c in range(COLS):
				celda = self.moves[r][c]
				celda.probability = 0

	def calcular_probabilidades(self, void_moves, safe_moves):	

		for r in range(ROWS):
			for c in range(COLS):

				self.moves[r][c].set_probability(self.moves, void_moves, safe_moves)
						
	def update_void(self):
		self.void_moves = []
		for r in range(ROWS):
			for c in range(COLS):
				if self.moves[r][c].probability == float('inf'):
					self.void_moves.append(self.moves[r][c])

	def bomb_neighbouring(self):
		for m in self.void_moves:
			for r, c in m.vecinos:
				v = self.moves[r][c]
				if v.vecinos_armados == len(v.get_sorrounding_bombs(self.moves, self.void_moves)):
					for l in v.get_libres(self.moves):
						if not l in self.void_moves:
							if not l in self.safe_moves:
								if not l.probability == float('inf'):
									self.safe_moves.append(l)

	def inferir(self):
		for r, c in self.void_moves:
			celda = self.moves[r][c]

			# conocer los vecinos de la mina
			v_ocupados = celda.vecinos.copy()
			
			vl = []
			for i, j in celda.vecinos:
				if self.moves[i][j].hidden:
					vl.append((i,j))

			for v in vl:
				if v in v_ocupados:
					v_ocupados.pop(v_ocupados.index(v))
			
			# comparar vecinos armados y estimaciones
			for i, j in v_ocupados:

				ref = self.moves[i][j]

				minas_circundantes = []
				for o, p in ref.vecinos:
					v = self.moves[o][p]
					if v.probability == float('inf'):
						minas_circundantes.append(v)

				if len(minas_circundantes) == ref.vecinos_armados:
					for o, p in ref.vecinos:
						v = self.moves[o][p]
						if not  v.probability == float('inf'):
							# self.moves[o][p].probability = -1
							if v.hidden:
								if (o, p) in self.available_moves:
									if not (o, p) in self.safe_moves and not (o, p) in self.void_moves:
										if not self.moves[o][p].probability == float('inf'):
											self.safe_moves.append((o, p))

	def update(self, juego):
		# Recibir info del estado del juego y actualizar representación interna
		self.get_info(juego)

		# self.print_known_facts()

		# Calcular probabilidades		
		self.resetear_prob()
		self.calcular_probabilidades(self.void_moves, self.safe_moves)

		# Actualizar listas
		self.update_void()

		# Inferir
		# self.inferir()
		self.bomb_neighbouring()

		self.available_moves.sort()
		self.void_moves.sort()
		self.safe_moves.sort()

		# Imprimir parámetros
		# self.show()

	def choose_move(self):
		if self.safe_moves:
			m = self.safe_moves.pop(0)
		else:
			# if not self.moves_done:
			m = random.choice(self.available_moves)
			# else:
			# 	m = self.available_moves[0]
		return m
	
	def execute(self, juego):

		self.update(juego)

		# Poner banderas
		for m in self.void_moves:
			if not m in self.flag_moves:
				self.flag_moves.append(m)
				r, c = m.row, m.col
				event = 3
				pos = (c*SQUARE_SIZE, r*SQUARE_SIZE)
				return event, pos

		
		# Elegir un movimiento posible
		m = self.choose_move()
		self.moves_done.append(m)
		r, c = m.row, m.col
		event = 1
		pos = (c*SQUARE_SIZE, r*SQUARE_SIZE)
		return event, pos