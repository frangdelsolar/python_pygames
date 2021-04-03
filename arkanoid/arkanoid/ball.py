import pygame
import config
import math
import random

class Ball():
	def __init__(self, paddle, r):
		self.r = r
		# self.x = paddle.x + (paddle.width//2)
		# self.y = paddle.y - self.r
		self.x = 40
		self.y = 40
		self.x_speed = 0
		self.y_speed = 0
		self.speed = 1
		self.degree = 45
		self.angle = self.degree*(math.pi/180)

	def set_speed(self, xs, ys):
		self.x_speed = xs
		self.y_speed = ys

	def update(self):
		self.x += self.x_speed
		self.y += self.y_speed

		if self.x - self.r <= 0 or self.x + self.r >= config.WIDTH:
			self.x_speed *= -1

		if self.y - self.r <= 0 or self.y + self.r >= config.HEIGHT:
			self.y_speed *= -1

	def hit_x(self, other):
		if ( (int(self.x) == int(other.x) or int(self.x) == int(other.x) + int(other.width)) and 
			 (int(self.y) >= int(other.y) and int(self.y) <= int(other.y) + int(other.height)) ):
			return True
		return False

	def hit_y(self, other):
		if ( (int(self.y) == int(other.y) or int(self.y) == int(other.y) + int(other.height)) and 
			 (int(self.x) >= int(other.x) and int(self.x) <= int(other.x) + int(other.width)) ):
			return True
		return False

	def draw(self, screen):
		pygame.draw.circle(screen, config.YELLOW, (int(self.x), int(self.y)), self.r)
