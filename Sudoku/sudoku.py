
class Sudoku:

	def __init__(self):
		self.grid =   [[0, 0, 0,   0, 0, 0,   2, 0, 0],
				       [0, 8, 0,   0, 0, 7,   0, 9, 0],
				       [6, 0, 2,   0, 0, 0,   5, 0, 0],
     
				       [0, 7, 0,   0, 6, 0,   0, 0, 0],
				       [0, 0, 0,   9, 0, 1,   0, 0, 0],
				       [0, 0, 0,   0, 2, 0,   0, 4, 0],
     
				       [0, 0, 5,   0, 0, 0,   6, 0, 3],
				       [0, 9, 0,   4, 0, 0,   0, 7, 0],
				       [0, 0, 6,   0, 0, 0,   0, 0, 0]]


		self.solution = [[5, 3, 4,   6, 7, 8,   9, 1, 2],
				         [6, 7, 2,   1, 9, 5,   3, 4, 8],
				         [1, 9, 8,   3, 4, 2,   5, 6, 7],
     
				         [8, 5, 9,   7, 6, 1,   4, 2, 3],
				         [4, 2, 6,   8, 5, 3,   7, 9, 1],
				         [7, 1, 3,   9, 2, 4,   8, 5, 6],
     
				         [9, 6, 1,   5, 3, 7,   2, 8, 4],
				         [2, 8, 7,   4, 1, 9,   6, 3, 5],
				         [3, 4, 5,   2, 8, 6,   1, 7, 9]]

	def show(self):
		print('************************************')
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if (j+1) % 3 == 0:
					print(self.grid[i][j], end="    ")
				else:
					print(self.grid[i][j], end=" ")

			if (i+1) % 3 == 0:
				print()
			print()

	def buscar_cero(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == 0:
					return (i, j)
		return False

	def comprobar_fila(self, pos, valor):
		r, c = pos
		for i in self.grid[r]:
			if i == valor:
				return False
		return True

	def comprobar_columna(self, pos, valor):
		r, c = pos
		for i in self.grid:
			if i[c] == valor:
				return False
		return True

	def comprobar_box(self, pos, valor):
		r, c = pos
		rb = r//3
		cb = c//3
		for i in range(rb * 3, rb*3+3):
			for j in range(cb * 3, cb*3+3):
				if self.grid[i][j] == valor:
					return False

		return True

	def es_valido(self, pos, valor):
		if (self.comprobar_fila(pos, valor) and
			self.comprobar_columna(pos, valor) and
			self.comprobar_box(pos, valor) ):
			return True
		return False


	def resolver(self):
		pos = self.buscar_cero()

		if not pos:
			return True
		else:
			r, c = pos
			for i in range(1, 10):
				valido = self.es_valido(pos, i)
				if valido:
					self.grid[r][c] = i
					if self.resolver():
						return True
					self.grid[r][c] = 0
			self.show()
			return False




			





