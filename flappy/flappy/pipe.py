import config
import pygame

class Pipe():
	def __init__(self):
		self.x = config.WIDTH
		self.width = 40
		self.top = random.random(20, )
		self.xspeed = -3

	def update(self):
		self.x += self.xspeed

	def draw(self, screen):
		pygame.draw.rect(screen, config.WHITE, (self.x, 0, self.width, config.HEIGHT))
