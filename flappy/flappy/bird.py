import config
import pygame

class Bird():
	def __init__(self):
		self.x = (config.WIDTH//5) 
		self.y = config.HEIGHT//2
		self.r = 10
		self.yspeed = 0
		self.lift = -30

	def update(self):
		self.yspeed += config.GRAVITY
		self.yspeed *= 0.9
		self.y += self.yspeed

		if self.y > config.HEIGHT:
			self.y = config.HEIGHT
			self.yspeed = 0

		if self.y < 0:
			self.y = 0
			self.yspeed = 0

		self.y = int(self.y//1)

	def volar(self):
		self.yspeed += self.lift

	def draw(self, screen):
		pygame.draw.circle(screen, config.YELLOW, (int(self.x), int(self.y)), self.r)
