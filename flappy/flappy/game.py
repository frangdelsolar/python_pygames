import pygame
import config
import random
from .bird import Bird
from .pipe import Pipe

class Game():
	def __init__(self, screen):
		self.screen = screen
		self.run = True
		self.bird = Bird()
		self.pipes = [Pipe()]
		self.loop_count = 0

	def draw(self):
		self.loop_count += 1

		if self.loop_count % 80 == 0:
			self.pipes.append(Pipe())

		self.screen.fill(config.BLACK)
		
		self.bird.update()
		self.bird.draw(self.screen)

		for pipe in self.pipes:
			pipe.update()
			pipe.draw(self.screen)
