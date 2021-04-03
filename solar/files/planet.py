import pygame
from .config import YELLOW, HEIGHT, WIDTH
import math
import random


class Planet():
	def __init__(self, x=0, y=0, d=0, a=0, r=0, speed=0):
		self.x = x
		self.y = y
		self.r = r
		self.d = d
		self.a = a
		self.speed = speed
		self.planets = []

	def update(self):
		self.x = (self.d * math.cos(math.radians(self.a)))
		self.y = (self.d * math.sin(math.radians(self.a)))

		self.a += self.speed

	def spawn_moons(self, total):
		for i in range(total):
			x = self.x
			y = self.y
			a = random.randint(0, 360)
			r = random.randint(self.r//10, self.r//2)
			gap = 3
			speed = random.randint(1, 3) * random.choice([1, -1])
			d = random.randint(self.r + r + gap, self.r*20)
			p = Planet(x=x, y=y, d=d, a=a, r=r, speed=speed)
			self.planets.append(p)
			

	def draw(self, screen):
		pygame.draw.circle(screen, YELLOW, (int(self.x+WIDTH//2), int(self.y+HEIGHT//2)), self.r)

		for p in self.planets:
			p.update()
			p.draw(screen)
			# print(p.pos_to_coord())
