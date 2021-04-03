from abc import ABC, abstractmethod 
from chess.constants import SQUARE_SIZE

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