from abc import ABC, abstractmethod 
from .constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
import pygame

class Piece(ABC):

	def __init__(self, name, color, pos):
		self.name = name
		self.base = pos
		self.color = color
		self.move_count = 0		
		self.image = None
		self.row, self.col = pos
		self.valid_moves = []

	def __repr__(self):
		return f'{self.name}' #, {self.row}, {self.col}'

	def draw(self, screen):
		self.rect = self.image.get_rect()
		x = self.col * SQUARE_SIZE
		y = self.row * SQUARE_SIZE
		self.rect.topleft = x, y
		screen.blit(self.image, self.rect)

	def get_valid_moves(self, self_set, other_set, log):
		pass


class Pawn(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_pawn.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_pawn.png')

	def get_valid_moves(self, self_set, other_set, log):
		basic_moves = []

		# Avance doble desde posición inicial
		if self.move_count == 0:
			if self.color == 'white':
				r, c = self.row - 2, self.col
				r2 = self.row - 1
			else:
				r, c = self.row + 2, self.col
				r2 = self.row + 1
			
			empty = True
			for piece in self_set:
				if piece.row == r2 and piece.col == c:
					empty = False

			for piece in other_set:
				if piece.row == r2 and piece.col == c:
					empty = False

			if empty:
				basic_moves.append((r, c))

		# Avance simple
		if self.color == 'white':
			basic_moves.append((self.row - 1, self.col))

		if self.color == 'black':
			basic_moves.append((self.row + 1, self.col))

		# Comer al paso
		if self.color == 'white':
			if self.row == 3:
				pieza = log[-1].piece
				if pieza.name == 'Pawn':
					if pieza.col == self.col - 1 or pieza.col == self.col + 1:
						basic_moves.append((2, pieza.col))

		if self.color == 'black':
			if self.row == 4:
				pieza = log[-1].piece
				if pieza.name == 'Pawn':
					if pieza.col == self.col - 1 or pieza.col == self.col + 1:
						basic_moves.append((5, pieza.col))

		# Quitar casilleros ocupados por piezas del mismo set			
		for piece in self_set:
			for r, c in basic_moves:
				if piece.row == r and piece.col == c:
					basic_moves.pop(basic_moves.index((r, c)))

		# Quitar piezas ocupadas por piezas equipo contrario
		for piece in other_set:
			for r, c in basic_moves:
				if piece.row == r and piece.col == c:
					basic_moves.pop(basic_moves.index((r, c)))

			if self.color == 'white':
				if (piece.row == self.row - 1 and 
						(piece.col == self.col - 1 or 
							piece.col == self.col + 1 )):
				
								basic_moves.append((piece.row, piece.col))

			if self.color == 'black':
				if (piece.row == self.row + 1 and 
						(piece.col == self.col - 1 or 
							piece.col == self.col + 1 )):
				
							basic_moves.append((piece.row, piece.col))	

		return basic_moves

	def display_options(self, screen):

		if self.color == 'white':
			rook_image = pygame.image.load('chess/img/w_tower.png')
			queen_image = pygame.image.load('chess/img/w_queen.png')
			knight_image = pygame.image.load('chess/img/w_knight.png')
			bishop_image = pygame.image.load('chess/img/w_bishop.png')

		else:
			rook_image = pygame.image.load('chess/img/b_tower.png')
			queen_image = pygame.image.load('chess/img/b_queen.png')
			knight_image = pygame.image.load('chess/img/b_knight.png')
			bishop_image = pygame.image.load('chess/img/b_bishop.png')



		continuar = True

		while continuar:

			pygame.draw.rect(screen, (255,255,255), (0, 0, WIDTH, HEIGHT))

			# Rook
			rook_rect = rook_image.get_rect()
			x = 200
			y = 350
			rook_rect.topleft = x, y
			screen.blit(rook_image, rook_rect)

			# Queen
			queen_rect = queen_image.get_rect()
			x = 300
			y = 350
			queen_rect.topleft = x, y
			screen.blit(queen_image, queen_rect)

			# Knight
			knight_rect = knight_image.get_rect()
			x = 400
			y = 350
			knight_rect.topleft = x, y
			screen.blit(knight_image, knight_rect)

			# Bishop
			bishop_rect = bishop_image.get_rect()
			x = 500
			y = 350
			bishop_rect.topleft = x, y
			screen.blit(bishop_image, bishop_rect)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					if y >= 350 and y <= 450:
						if x >= 200 and x < 300:
							return 'Rook'
						elif x >= 300 and x < 400:
							return 'Queen'
						elif x >= 400 and x < 500:
							return 'Knight' 
						elif x >= 500 and x < 600:
							return 'Bishop'
						else: 
							pass  


	def promote(self, pos, self_set, screen):

		option = self.display_options(screen)

		if self.color == 'white':
			row = 0
		else:
			row = 7
		
		if option == 'Rook':
			self_set.append(Rook('Rook', self.color, pos))

		elif option == 'Queen':
			self_set.append(Queen('Queen', self.color, pos))

		elif option == 'Knight':
			self_set.append(Knight('Knight', self.color, pos))

		elif option == 'Bishop':
			self_set.append(Bishop('Bishop', self.color, pos))

		self_set.pop(self_set.index(self))



class Rook(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_tower.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_tower.png')

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

		return basic_moves


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


class King(Piece):

	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.jaque = False
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_king.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_king.png')

	def under_atack(self, pos, self_set, other_set, log):
		row, col = pos
		for piece in other_set:
			if piece.name == 'King':
				other_king_moves = [
					(piece.row - 1, piece.col - 1),
					(piece.row - 1, piece.col),
					(piece.row - 1, piece.col + 1),
					(piece.row , piece.col - 1),
					(piece.row , piece.col + 1),
					(piece.row + 1, piece.col - 1),
					(piece.row + 1, piece.col),
					(piece.row + 1, piece.col + 1)
				]
				if pos in other_king_moves:
					return piece


			elif piece.name == 'Pawn':
				if self.color == 'white':

					if (piece.row == row - 1 and
						(piece.col == col + 1 or piece.col == col-1) ):
						return piece
				elif self.color == 'black':
					if ( piece.row == row + 1 and 
						(piece.col == col + 1 or piece.col == col-1) ):
						return piece

			else:
				if pos in piece.get_valid_moves(other_set, self_set, log):
					return piece

	def is_empty(self, celdas, self_set, other_set):
		for r, c in celdas:
			for piece in self_set:
				if piece.row == r and piece.col == c:
					return False
			for piece in self_set:
				if piece.row == r and piece.col == c:
					return False
		return True

	def get_valid_moves(self, self_set, other_set, log):
		posible_moves = [
			(self.row - 1, self.col - 1),
			(self.row - 1, self.col),
			(self.row - 1, self.col + 1),
			(self.row , self.col - 1),
			(self.row , self.col + 1),
			(self.row + 1, self.col - 1),
			(self.row + 1, self.col),
			(self.row + 1, self.col + 1)
		]

		for piece in self_set:
			for r, c in posible_moves:
				if piece.row == r and piece.col == c:
					posible_moves.pop(posible_moves.index((r, c)))

		remover = []
		for pos in posible_moves:
			if self.under_atack(pos, self_set, other_set, log):
				remover.append(pos)

		for pos in remover:
			posible_moves.pop(posible_moves.index(pos))

		# Remove Edges
		remove=[]
		for r, c in posible_moves:
			if not (0 <= r < ROWS and
				  0 <= c < COLS):
				remove.append((r, c))

		for r, c in remove:
			posible_moves.pop(posible_moves.index((r, c)))

		# castling
		if self.move_count == 0:

			for piece in self_set:
				if  piece.name == 'Rook':
					
					if piece.move_count == 0:
					
						# Rook castling
						if piece.col == 7:
							if self.color == 'white':
								boxes = [(7, 5), (7, 6)]
							else:
								boxes = [(0, 5), (0, 6)]

							amenazadas = False
							for box in boxes:
								if self.under_atack(box, self_set, other_set, log):
									amenazadas = True

							if not amenazadas:
								if self.is_empty(boxes, self_set, other_set):
									if self.color == 'white':
										posible_moves.append((7, 6))
									else:
										posible_moves.append((0, 6))
							

						# Queen castling
						if piece.col == 0:
							if self.color == 'white':
								boxes = [(7, 1), (7, 2), (7, 3)]
							else:
								boxes = [(0, 1), (0, 2), (0, 3)]

							amenazadas = False
							for box in boxes:
								if self.under_atack(box, self_set, other_set, log):
									amenazadas = True

							if not amenazadas:
								if self.is_empty(boxes, self_set, other_set):
									if self.color == 'white':
										posible_moves.append((7, 2))
									else:
										posible_moves.append((0, 2))

		return posible_moves

	def castle(self, pos, self_set):

		if self.color == 'white':
			if  pos == (7, 2):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 0:
							piece.col = 3

			elif pos == (7, 6):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 7:
							piece.col = 5


		elif self.color == 'black':
			if pos == (0, 2):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 0:
							piece.col = 3

			elif pos == (0, 6):
				for piece in self_set:
					if piece.name == "Rook":
						if piece.col == 7:
							piece.col = 5


class Knight(Piece):
	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()

	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_knight.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_knight.png')

	def get_valid_moves(self, self_set, other_set, log):
		posible_moves = [
			(self.row - 2, self.col - 1),
			(self.row - 2, self.col + 1),
			(self.row - 1, self.col - 2),
			(self.row - 1, self.col + 2),
			(self.row + 2, self.col - 1),
			(self.row + 2, self.col + 1),
			(self.row + 1, self.col - 2),
			(self.row + 1, self.col + 2), 
		]

		for piece in self_set:
			for r, c in posible_moves:
				if piece.row == r and piece.col == c:
					posible_moves.pop(posible_moves.index((r, c)))

		# Remove Edges
		remove=[]
		for r, c in posible_moves:
			if not (0 <= r < ROWS and
				  0 <= c < COLS):
				remove.append((r, c))

		for r, c in remove:
			posible_moves.pop(posible_moves.index((r, c)))


		return posible_moves
		

class Bishop(Piece):
	def __init__(self, name, color, pos):
		super().__init__(name, color, pos)
		self.set_image()


	def set_image(self):
		if self.color == 'white':
			self.image = pygame.image.load('chess/img/w_bishop.png')

		if self.color == 'black':
			self.image = pygame.image.load('chess/img/b_bishop.png')

	def get_valid_moves(self, self_set, other_set, log):
		basic_moves = []


		#NW
		found = False
		for i in range(1, ROWS):
			for piece in other_set:
				if piece.row == self.row-i and piece.col == self.col-i:
					if (0 <= self.row-i < ROWS and
						0 <= self.col-i < COLS):
						basic_moves.append((self.row-i, self.col-i))
						found = True

			for piece in self_set:
				if piece.row == self.row-i and piece.col == self.col - i:
					found = True

			if not found:
				if (0 <= self.row-i < ROWS and
					0 <= self.col-i < COLS):
					basic_moves.append((self.row-i, self.col - i))
			else:
				break

		#NE
		found = False
		for i in range(1, ROWS):
				for piece in other_set:
					if piece.row == self.row-i and piece.col ==self.col+i :
						if (0 <= self.row-i < ROWS and
							0 <= self.col+i < COLS):

							basic_moves.append((self.row-i, self.col + i))
							found = True

				for piece in self_set:
					if piece.row == self.row-i and piece.col == self.col + i:
						found = True
				
				if not found:
					if (0 <= self.row-i < ROWS and
						0 <= self.col+i < COLS):
						basic_moves.append((self.row-i, self.col + i))
				else:
					break

			#SE
		found = False
		for i in range(1, ROWS):				
				for piece in other_set:
					if piece.row == self.row + i and piece.col == self.col + i :
						if (0 <= self.row + i < ROWS and
							0 <= self.col + i < COLS):
							basic_moves.append((self.row + i, self.col + i))
							found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col + i:
						found = True
				
				if not found:
					if (0 <= self.row + i < ROWS and
						0 <= self.col + i < COLS):
						basic_moves.append((self.row + i, self.col + i))
				else:
					break

		#SW
		found = False
		for i in range(1, ROWS):
			
				for piece in other_set:
					if piece.row == self.row + i and piece.col ==self.col - i :
						if (0 <= self.row+i < ROWS and
							0 <= self.col-i < COLS):
							basic_moves.append((self.row + i, self.col - i))
							found = True

				for piece in self_set:
					if piece.row == self.row + i and piece.col == self.col - i:
						found = True
				
				if not found:
					if (0 <= self.row+i < ROWS and
						0 <= self.col-i < COLS):
						basic_moves.append((self.row + i, self.col - i))
				else:
					break

		return basic_moves


class ChessSet():

	def __init__(self, color):
		self.color = color
		self.pieces = []
		self.build()


	def build(self):

		if self.color == 'white':
			self.pieces.append(King('King', self.color, (7, 4)))
			self.pieces.append(Queen('Queen', self.color, (7, 3)))
			self.pieces.append(Bishop('Bishop', self.color, (7, 2)))
			self.pieces.append(Bishop('Bishop', self.color, (7, 5)))
			self.pieces.append(Knight('Knight', self.color, (7, 1)))
			self.pieces.append(Knight('Knight', self.color, (7, 6)))
			self.pieces.append(Rook('Rook', self.color, (7, 0)))
			self.pieces.append(Rook('Rook', self.color, (7, 7)))
			
			for i in range(0, 8):
				self.pieces.append(Pawn('Pawn', self.color, (6, i)))

		if self.color == 'black':
			self.pieces.append(King('King', self.color, (0, 4)))
			self.pieces.append(Queen('Queen', self.color, (0, 3)))
			self.pieces.append(Bishop('Bishop', self.color, (0, 2)))
			self.pieces.append(Bishop('Bishop', self.color, (0, 5)))
			self.pieces.append(Knight('Knight', self.color, (0, 1)))
			self.pieces.append(Knight('Knight', self.color, (0, 6)))
			self.pieces.append(Rook('Rook', self.color, (0, 0)))
			self.pieces.append(Rook('Rook', self.color, (0, 7)))

			for i in range(0, 8):
				self.pieces.append(Pawn('Pawn', self.color, (1, i)))

	def draw(self, screen):
		for p in self.pieces:
			p.draw(screen)

	def get_king(self):
		for piece in self.pieces:
			if piece.name == 'King':
				return piece
