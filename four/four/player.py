from .constants import GREEN,SQUARE_SIZE, BLUE, RED, MARGIN
from .ai import AI
import pygame 

class Player():
	def __init__(self, name, color, ai):
		self.name = name
		self.color = color
		self.points = 0
		self.clicks = 0
		self.is_ai = ai
		self.image = None
		self.set_image()
		self.ai = AI()


	def draw(self, pos, screen):
		self.rect = self.image.get_rect()
		y = pos[0] * SQUARE_SIZE + MARGIN
		x = pos[1] * SQUARE_SIZE + MARGIN
		self.rect.topleft = x, y
		screen.blit(self.image, self.rect)


	def set_image(self):
		if self.color == 'blue':
			self.image = pygame.image.load('four/img/b_ficha.png')

		if self.color == 'red':
			self.image = pygame.image.load('four/img/r_ficha.png')

		self.image = pygame.transform.scale(self.image, (SQUARE_SIZE-MARGIN*2, SQUARE_SIZE-MARGIN*2))

	def __repr__(self):
		return f'{self.color}'
