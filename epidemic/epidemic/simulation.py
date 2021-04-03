from .constants import *
from .community import Community
import pygame
import random


class Simulation():
	def __init__(self, screen):
		self.run = True
		self.speed = 1
		self.screen = screen
		self.communities = []
		self.build()

	def build(self):
		margin = 10
		cols = 5
		rows = 2
		communities = cols * rows
		width = (WIDTH-margin * (cols + 2)) // cols 
		height = width

		for r in range(rows):
			for c in range(cols):
				x = margin * (c+1) + width * c
				y = margin * (r+1) + height * 2 * r
				com = Community(x=x, 
								y=y, 
								width=width, 
								height=height, 
						 		population=random.randint(10,width*2), 
						 		sick_prob=random.randint(0,100), 
						 		quar_factor=random.randint(0,100),
						 		sint_factor=random.randint(0,100),
						 		mortalidad=random.randint(0,100),
						 		freedom=random.randint(0,width//10))
				self.communities.append(com)

	def update(self):
		import config

		config.FRAMES += 1
		if config.FRAMES % config.FRAMES_DAY_RATIO == 0:
			config.DAYS_GONE += 1
			print('Days gone:', config.DAYS_GONE)

		self.run = False
		for c in self.communities:
			if len(c.get_condition('i')) > 0:
				self.run = True

		for com in self.communities:
			com.update()

	def draw(self):

		self.screen.fill(BLACK)
		for com in self.communities:
			com.draw(self.screen)

		self.draw_score()
		self.draw_quarantined()


	def draw_score(self):	
		import config

		font = pygame.font.SysFont('comicsans', 30)

		label4 = font.render('Frames: ' + str(config.FRAMES), 1, (255,255,255))
		sx = 20
		sy = config.HEIGHT-60
		self.screen.blit(label4, (sx, sy))

		label4 = font.render('Days: ' + str(config.DAYS_GONE), 1, (255,255,255))
		sx = 20
		sy = config.HEIGHT-40
		self.screen.blit(label4, (sx, sy))


	def draw_quarantined(self):
		import config
		pygame.draw.rect(self.screen, WHITE, (config.Q_X, config.Q_Y, config.Q_S, config.Q_S), 3)

		for agent in config.QUARANTINED:
			agent.draw(self.screen)