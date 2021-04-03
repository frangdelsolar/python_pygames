import config
import pygame

class Paddle():
	def __init__(self):
		self.width = config.WIDTH//10
		self.height = self.width
		self.x = (config.WIDTH//2) - (self.width//2)
		self.y = config.HEIGHT - (config.HEIGHT//10)
		self.speed = 0

	def set_speed(self, speed):
		self.speed = speed

	def is_colliding(self, ball):
		return(ball.x > self.x and 
			   ball.x < self.x+self.width and
			   ball.y > self.y and
			   ball.y < self.y + self.height)

	def update(self, ball):
		self.x += self.speed

		if self.x <= 0:
			self.x = 0
		elif self.x + self.width >= config.WIDTH :
			self.x = config.WIDTH - self.width

		if ball.hit_x(self):
			ball.x_speed *= -1

		if ball.hit_y(self):
			ball.y_speed *= -1
		# if self.is_colliding(ball):
		# 	ball.x_speed *= -1
		# 	ball.y_speed *= -1

	def draw(self, screen):
		pygame.draw.rect(screen, config.WHITE, (self.x, self.y, self.width, self.height))
