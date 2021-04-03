from .agent import Agent
from .constants import WHITE, WIDTH, HEIGHT
from .quadtree import QuadTree, Rectangle, Point, Circle
import random
import pygame
import csv
import os

class Community():

	def __init__(self, x, y, width, height, population, sick_prob, quar_factor, sint_factor, mortalidad, freedom):
		self.agents = []
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.sick_prob = sick_prob
		self.quar_factor = quar_factor
		self.sint_factor = sint_factor
		self.mortalidad = mortalidad
		self.freedom = freedom
		self.qt = None
		self.is_saved = False
		self.build(population)

	def build(self, population):
		for i in range(population):
			agent = Agent(
						  x=random.randint(self.x, self.x+self.width),
						  y=random.randint(self.y, self.y+self.height),
						  community=self, 
						  status='s',
						  color=WHITE,
						  radius=2,
						  )
			self.agents.append(agent)

		for i in range(5):
			self.agents[i].get_sick()

	def contagiar(self):
		boundary = Rectangle(self.x, self.y, self.width, self.height)
		self.qt = QuadTree(boundary, 1)

		for agent in self.agents:
			if agent.status == 's':
				point = Point(agent.x, agent.y, agent)
				self.qt.insert(point)


		for infected in self.get_condition('i'):
			rango = Circle(infected.x, infected.y, infected.radius)
			points = self.qt.query(rango, [])

			for point in points:
				agent = point.user_data
				infected.contagiar(agent)


	def get_condition(self, condition):
		group = []
		for agent in self.agents:
			if agent.status == condition:
				group.append(agent)
		return group

	def update(self):
		self.contagiar()
		for agent in self.agents:
			agent.update()	

		if len(self.get_condition('i')) == 0:
			if not self.is_saved:
				data = self.get_data()
				self.dump_data(data)
				print(data)
				self.is_saved = True

	def draw(self, screen):

		# self.qt.draw(screen)
		pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 3)

		for agent in self.agents:
			if not agent.quarantined:
				agent.draw(screen)

		self.draw_score(screen)

	def draw_score(self, screen):

		font = pygame.font.SysFont('comicsans', 25)
		x = self.x

		labels = {
		'S: ': str(len(self.get_condition('s'))),
		'I: ': str(len(self.get_condition('i'))),
		'R: ': str(len(self.get_condition('r')) + len(self.get_condition('m'))),
		'M: ': str(len(self.get_condition('m'))),
		'Contagio: ': f'{self.sick_prob}%',
		'Cuarentena: ': f'{self.quar_factor}%',
		'Asintomáticos: ': f'{self.sint_factor}%',
		'Mortalidad: ': f'{self.mortalidad}%',
		'Libertad: ': f'{self.freedom} px',
		}

		y = self.y + self.height + 15
		for key in labels:
			label = font.render(key + " " + labels[key], 0, (255,255,255))
			screen.blit(label, (x, y))
			y += 15

	def get_data(self):
		import config
		
		return {
				'poblacion': len(self.agents),
				'Probabilidad de contagio': self.sick_prob, 
				'Probabilidad de cuarentena': self.quar_factor, 
				'Asintomáticos': self.sint_factor, 
				'Mortalidad': self.mortalidad, 
				'Libertad': self.freedom, 
				'Susceptibles': str(len(self.get_condition('s'))),
				'Infectados': str(len(self.get_condition('i'))),
				'Removidos': str(len(self.get_condition('r')) + len(self.get_condition('m'))),
				'Muertos': str(len(self.get_condition('m'))),
				'Días transcurrridos': config.DAYS_GONE
				}

	def dump_data(self, data):

		headers = [
				'poblacion',
				'Probabilidad de contagio', 
				'Probabilidad de cuarentena', 
				'Asintomáticos', 
				'Mortalidad', 
				'Libertad', 
				'Susceptibles',
				'Infectados',
				'Removidos',
				'Muertos',
				'Días transcurrridos'
			]

		filename = 'data.csv'
		file_exists = os.path.isfile(filename)

		with open(filename, "a") as csvfile:
			
			writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
			if not file_exists:
				writer.writeheader()
				writer.writerow(data)

			else:
				writer.writerow(data)

