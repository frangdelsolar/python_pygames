from config import *
from ray import Ray
from vector import Vector
import math
import pygame


class Particle():
	def __init__(self):
		self.pos = (WIDTH//2, HEIGHT//2)
		self.rays = []
		self.heading = 0
		self.fov = 30

		for i in range(-self.fov, self.fov, 1):
			self.rays.append(Ray(self.pos, math.radians(i)))

	def rotate(self, angle):
		self.heading += angle
		for i in range(-self.fov, self.fov, 1):
			self.rays[i].set_angle(math.radians(i+self.heading))

	def move(self, amt):
		a, b = (math.cos(self.heading)*amt, math.sin(self.heading)*amt)
		# print(a, b)
		# print(self.pos)
		# self.pos = (int(self.pos[0]+a), int(self.pos[1]+b))
		# print(self.pos)
		# for i in range(-self.fov, self.fov, 1):
		# 	self.rays[i].set_angle(math.radians(i+self.heading))

	def look(self, walls, screen):
		scene = []
		for ray in self.rays:
			# print(ray.pos, ray.dir)
			closest = None
			record = float('inf')
			for wall in walls:
				pt = ray.cast(wall)
				if pt:
					d = Vector(self.pos, pt).distance()					
					if d < record:
						record = d
						closest = pt					
			if closest:
				pygame.draw.line(screen, (0, 255, 255), self.pos, closest, 1)			
			scene.append(record)

		return scene

	def update(self, x, y):
		self.pos = (x, y)
		for r in self.rays:
			r.pos=self.pos

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 0), self.pos, 4)

		for r in self.rays:
			r.draw(screen)