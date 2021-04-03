import pygame
import math
from vector import Vector

class Ray():
	def __init__(self, pos, angle):
		self.pos = pos
		self.dir = (math.cos(angle), math.sin(angle))

	def get_dir(self):
		return (self.pos[0]+self.dir[0]*20, self.pos[1]+self.dir[1]*20)

	def set_angle(self, angle):
		self.dir = (math.cos(angle), math.sin(angle))	

	def heading(self):
		return 	math.atan2(self.dir[0], self.dir[1])  

	def look_at(self, x, y):
		v = Vector(self.pos, (x, y))
		a, b = v.unit()
		self.dir = (a, b)

	def cast(self, wall):
		x1, y1 = wall.a
		x2, y2 = wall.b

		x3, y3 = self.pos
		x4, y4 = self.get_dir()

		den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
		if den == 0:
			return

		t =  ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
		u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

		if 0 < t < 1 and u > 0:
			x = x1 + t * (x2 - x1)
			y = y1 + t * (y2 - y1)
			return (x, y)
		return False


	def draw(self, screen):
		pygame.draw.line(screen, (255, 255, 0), self.pos, self.get_dir(), 1)
