import random
import pygame
import sys
from files.config import SCREEN_SIZE
from files.simulation import Simulation


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	clock = pygame.time.Clock()
	
	simulation = Simulation(screen)

	while simulation.run:
		simulation.draw()
		pygame.display.update()
		clock.tick(10)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# 	if event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_UP:
		# 			simulation.deslizar('up')

		# 		if event.key == pygame.K_DOWN:
		# 			simulation.deslizar('down')

		# 		if event.key == pygame.K_RIGHT:
		# 			simulation.deslizar('right')

		# 		if event.key == pygame.K_LEFT:
		# 			simulation.deslizar('left')

		# clock.tick(1)
main()
