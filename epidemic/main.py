import pygame
import sys
from epidemic.constants import SCREEN_SIZE
from epidemic.simulation import Simulation
import config
import random

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

config.DAYS_GONE = 0
config.FRAMES = 0
simulation = Simulation(screen)
clock = pygame.time.Clock()

while simulation.run:
	simulation.update()
	simulation.draw()
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()