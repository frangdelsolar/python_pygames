import math

class Vector():
	def __init__(self, list1, list2):
		self.diff = (list2[0]-list1[0], list2[1]-list1[1])

	def distance(self):
		self.a = self.diff[0]
		self.b = self.diff[1]
		return math.sqrt(self.a**2 + self.b**2)

	def unit(self):
		distance = self.distance()
		if distance != 0:
			self.aunit = self.a/distance
		else:
			self.aunit = 0

		if distance != 0:
			self.bunit = self.b/distance
		else:
			self.bunit = 0
		return self.aunit, self.bunit 

	def add(self, one, two):
		self.sum =(one[0]+two[0], one[1]+two[1])
		return self.sum

	def multiply(self, v, num):
		self.product =(v[0]*num, v[1]*num)
		return self.product