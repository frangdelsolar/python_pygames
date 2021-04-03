from config import SCREEN_SIZE
from flappy.game import Game
import sys
import pygame
import random

def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(SCREEN_SIZE)

	game = Game(screen)

	while game.run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game.bird.volar()

		game.draw()
		pygame.display.update()
		clock.tick(100)

main()


	