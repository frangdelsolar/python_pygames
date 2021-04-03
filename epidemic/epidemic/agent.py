from .constants import WHITE, RED, GRAY, DAYS_GONE, WIDTH, HEIGHT, YELLOW
import pygame
import random

class Agent():

	def __init__(self, x, y, community, status, color, radius):
		self.x = x
		self.y = y
		self.y_speed = None
		self.x_speed = None
		self.community = community
		self.color = color
		self.radius = self.community.width//100
		self.status = status
		self.day_zero = None
		self.r_sick = random.randint(0, 100)
		self.quarantined = False
		self.quar_det = False
		self.r_quar = random.randint(0, 100)
		self.asintomatico = False
		self.r_muerte = random.randint(0, 100)

	def update(self):
		self.update_position()
		if self.status == 'i':
			self.update_sick()

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 1)
		if self.status == 'i':
			pygame.draw.circle(screen, self.color, (self.x, self.y), 2)

	def iniciar_quarentena(self):
		import config
		config.QUARANTINED.append(self)

		self.quarantined = True
		self.x = random.randint(config.Q_X, config.Q_X+config.Q_S)
		self.y = random.randint(config.Q_Y, config.Q_Y+config.Q_S)

	def terminar_cuarentena(self):
		import config		
		config.QUARANTINED.pop(config.QUARANTINED.index(self))
		
		self.quarantined = False
		self.x = random.randint(self.community.x, self.community.x+self.community.width)
		self.y = random.randint(self.community.y, self.community.y+self.community.height)

	def get_dias_enfermo(self):
		import config
		return config.DAYS_GONE - self.day_zero

	def get_sick(self):
		self.status = 'i'
		self.color = RED
		self.radius = self.community.width//25
		if self.r_sick < self.community.sint_factor:
			self.asintomatico = True
			self.color = YELLOW

	def recuperarse(self):
		if self.quarantined:
			self.terminar_cuarentena()
		self.status = 'r'
		self.color = GRAY
		self.radius = self.community.width//90

	def morir(self):
		if self.quarantined:
			self.terminar_cuarentena()
		self.status = 'm'
		self.color = (0, 200, 200)
		self.radius = self.community.width//50

	def debe_hacer_cuarentena(self):
		return self.r_quar < self.community.quar_factor

	def debe_morir(self):
		return self.r_muerte < self.community.mortalidad

	def update_sick(self):
		import config
		
		if not self.day_zero:
			self.day_zero = config.DAYS_GONE


		if config.FRAMES % config.FRAMES_DAY_RATIO == 0:
			if self.debe_morir():
				self.morir()
				return

		else:
			if self.get_dias_enfermo() == 1:
				if not self.asintomatico:
					if not self.quar_det:
						self.quar_det = True
						if self.debe_hacer_cuarentena():
							self.iniciar_quarentena()

			elif self.get_dias_enfermo() >= 14:
				self.recuperarse()

	def update_position(self):
		if self.status == 'm':
			return 

		if not self.quarantined:
			self.x += random.randint(-self.community.freedom, self.community.freedom)
			self.y += random.randint(-self.community.freedom, self.community.freedom)

			if self.x <= self.community.x:
				self.x = self.community.x
			elif self.x >= self.community.x + self.community.width:
				self.x = self.community.x + self.community.width

			if self.y <= self.community.y:
				self.y = self.community.y
			elif self.y >= self.community.y + self.community.height:
				self.y = self.community.y + self.community.height

	def contagiar(self, other):
		if abs(other.x - self.x) <= self.radius and abs(other.y - self.y) <= self.radius:
			if random.randint(0, 100) < self.community.sick_prob:
				other.get_sick()



