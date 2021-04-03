import random
import pygame
import sys
from slider.config import SCREEN_SIZE
from slider.game import Game


def main():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	clock = pygame.time.Clock()
	
	game = Game(screen)

	while game.run:
		game.draw()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					game.deslizar('up')

				if event.key == pygame.K_DOWN:
					game.deslizar('down')

				if event.key == pygame.K_RIGHT:
					game.deslizar('right')

				if event.key == pygame.K_LEFT:
					game.deslizar('left')

		# clock.tick(1)
main()
