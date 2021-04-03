from chess.constants import SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT, WHITE
from .piece import Piece
from .rook import Rook
from .queen import Queen
from .knight import Knight
from .bishop import Bishop
import pygame


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

