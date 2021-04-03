import pygame
from vector import Vector

class Boundary():
	def __init__(self, x1, y1, x2, y2):
		self.a = (x1, y1)
		self.b = (x2, y2)

	def draw(self, screen):
		pygame.draw.line(screen, (255, 255, 255), self.a, self.b, 1)