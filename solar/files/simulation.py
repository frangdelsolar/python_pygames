from .config import *
from .planet import Planet
import pygame


class Simulation():
	def __init__(self, screen):
		self.run = True
		self.screen = screen
		
		self.sun = Planet(r=10)
		self.sun.spawn_moons(200)


	def update(self):
		pass

	def draw(self):
		self.screen.fill(BLACK)

		self.sun.draw(self.screen)