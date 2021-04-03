from .constants import WIDTH, HEIGHT, WHITE, GREEN
import random 
import pygame

class Point():
	def __init__(self, x, y, user_data=None):
		self.x = x
		self.y = y
		self.user_data = user_data

	def draw(self, screen):
		pygame.draw.circle(screen, WHITE, (self.x, self.y), 3)


class Circle():
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
		self.rsq = self.r * self.r

	def contains(self, point):
		d = (point.x - self.x) ** 2 + (point.y - self.y) ** 2
		return d <= self.rsq

	def intersects(self, rango):
		x_dist = abs(rango.x - self.x)
		y_dist = abs(rango.y - self.y)

		r = self.r

		w = rango.w
		h = rango.h

		edges = (x_dist - w) ** 2 + (y_dist - h) ** 2

		if x_dist > r + w or y_dist > r + h:
			return False

		if x_dist <= w or y_dist <= h:
			return True

		return edges <= self.rsq


class Rectangle():
	def __init__(self, x, y, w, h):
		self.x = x 
		self.y = y
		self.w = w
		self.h = h

	def contains(self, point):
		return (point.x >= self.x and 
				point.x <= self.x + self.w and
				point.y >= self.y and
				point.y <= self.y + self.h)

	def intersects(self, rango):
		return not (rango.x > self.x + self.w or
				    rango.x + rango.w < self.x or
				    rango.y > self.y + self.h or
				    rango.y + rango.h < self.y)


class QuadTree():
	def __init__(self, boundary, n):
		self.boundary = boundary
		self.capacity = n
		self.points = []
		self.divided = False
		self.northeast = None
		self.northwest = None
		self.southeast = None
		self.southwest = None

	def subdivide(self):
		x = self.boundary.x
		y = self.boundary.y
		w = self.boundary.w
		h = self.boundary.h
		ne = Rectangle(x + w/2, y,       w/2, h/2)
		nw = Rectangle(x,       y,       w/2, h/2)
		se = Rectangle(x + w/2, y + h/2, w/2, h/2)
		sw = Rectangle(x,       y + h/2, w/2, h/2)
		self.northeast = QuadTree(ne, self.capacity)
		self.northwest = QuadTree(nw, self.capacity)
		self.southeast = QuadTree(se, self.capacity)
		self.southwest = QuadTree(sw, self.capacity)
		self.divided = True

	def insert(self, point):
		if not self.boundary.contains(point):
			return 

		if len(self.points) < self.capacity:
			self.points.append(point)
		else:
			if not self.divided:
				self.subdivide()

			self.northeast.insert(point)
			self.northwest.insert(point)
			self.southeast.insert(point)
			self.southwest.insert(point)

	def draw(self, screen):
		pygame.draw.rect(screen, WHITE, (self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h), 1)

		for point in self.points:
			point.draw(screen)

		if self.divided:
			self.northeast.draw(screen)
			self.northwest.draw(screen)
			self.southeast.draw(screen)
			self.southwest.draw(screen)

	def query(self, rango, found):

		if not rango.intersects(self.boundary):
			return

		else:
			for p in self.points:
				if not p in found:
					if rango.contains(p):
						found.append(p)

			if self.divided:
				self.northwest.query(rango, found)
				self.northeast.query(rango, found)
				self.southwest.query(rango, found)
				self.southeast.query(rango, found)

		return found			
