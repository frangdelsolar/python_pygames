import pygame
import sys
from snake.constants import SCREEN_SIZE
from snake.game import Game

import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

juego = Game(screen)
clock = pygame.time.Clock()


while juego.run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direction = (-1, 0)
				juego.dirigir(direction)

			if event.key == pygame.K_DOWN:
				direction = (1, 0)
				juego.dirigir(direction)

			if event.key == pygame.K_RIGHT:
				direction = (0, 1)
				juego.dirigir(direction)

			if event.key == pygame.K_LEFT:
				direction = (0, -1)
				juego.dirigir(direction)

	# juego.ai_dirigir()

	juego.draw()

	pygame.display.update()

	clock.tick(juego.speed)


	