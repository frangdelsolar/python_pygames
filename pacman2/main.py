import pygame
import sys
from pacman.constants import SCREEN_SIZE
from pacman.game import Game
import time
import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

game = Game(screen)
clock = pygame.time.Clock()


while game.run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				direction = (-1, 0)
				game.dirigir(direction)

			if event.key == pygame.K_DOWN:
				direction = (1, 0)
				game.dirigir(direction)

			if event.key == pygame.K_RIGHT:
				direction = (0, 1)
				game.dirigir(direction)

			if event.key == pygame.K_LEFT:
				direction = (0, -1)
				game.dirigir(direction)

			if event.key == pygame.K_SPACE:
				game.pausar()

	if not game.pause:
		game.draw()
		pygame.display.update()
		
		# if game.check_win():
		# 	game.run = False
		# 	print('ganaste')
		# 	time.sleep(3)

		# clock.tick(game.speed)

