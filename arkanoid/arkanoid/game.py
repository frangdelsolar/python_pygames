import pygame
import config
import random
from .paddle import Paddle
from .ball import Ball
from .vector import Vector

class Game():
	def __init__(self, screen):
		self.screen = screen
		self.run = True
		self.paddle = Paddle()
		self.ball = Ball(self.paddle, self.paddle.width//10)

	def update(self):
		self.ball.update()
		self.paddle.update(self.ball)

	def draw(self):
		self.update()

		self.screen.fill(config.BLACK)
		self.paddle.draw(self.screen)
		self.ball.draw(self.screen)

	def disparar(self):
		rpos = (random.randint(0, config.WIDTH), random.randint(0, self.paddle.y))
		xs, ys = Vector((self.ball.x, self.ball.y), rpos).unit()
		self.ball.set_speed(xs, ys)

