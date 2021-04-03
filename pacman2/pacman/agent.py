from .constants import SQUARE_SIZE, WIDTH, BLUE
import pygame


class Agent():
	def __init__(self, row, col, color):
		self.row = row
		self.col = col
		self.x = self.col * SQUARE_SIZE
		self.y = self.row * SQUARE_SIZE
		self.width = SQUARE_SIZE
		self.height = SQUARE_SIZE
		self.x_speed = 0
		self.y_speed = 0
		self.color = color
		self.radius = SQUARE_SIZE//3

	def get_pixels_ahead(self, ahead=1):
		rect = pygame.Rect(self.x, self.y, self.width, self.height)
		xy_ahead = []
		if self.x_speed > 0:
			xy_ahead = (rect.midright[0] + ahead, rect.midright[1])
		if self.x_speed < 0:
			xy_ahead = (rect.midleft[0] - ahead, rect.midleft[1])
		if self.y_speed < 0:
			xy_ahead = (rect.midtop[0], rect.midtop[1] - ahead)
		if self.y_speed > 0:
			xy_ahead = (rect.midbottom[0], rect.midbottom[1] + ahead)
		return xy_ahead

	def update(self, level, screen):
		self.x += self.x_speed
		if self.x == 0 and self.x_speed < 0:
			self.x = WIDTH-1
		elif self.x+self.width == WIDTH-1 and self.x_speed > 0:
			self.x = 0 - self.width

		self.y += self.y_speed

		self.col = self.x//SQUARE_SIZE
		self.row = self.y//SQUARE_SIZE

		if self.x_speed != 0 or self.y_speed != 0:
			xy_ahead = self.get_pixels_ahead()
			color_ahead = screen.get_at(xy_ahead)
			if color_ahead == BLUE:
				self.x_speed = 0
				self.y_speed=0

	def mover(self, vector):
		self.x_speed = vector[1]
		self.y_speed = vector[0]

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x+SQUARE_SIZE//2, self.y+SQUARE_SIZE//2), self.radius)
		# pygame.draw.rect(screen, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE), 1)


