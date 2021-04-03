import pygame
import sys
from tetris.constants import SCREEN_SIZE
from tetris.game import Game

import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

game = Game(screen)
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 0.27
level_time = 0


while game.run:

	fall_time += clock.get_rawtime()
	level_time += clock.get_rawtime()
	clock.tick(100000)

	game.listen()
	# game.listen_ai()

	if not game.pause:

		if fall_time/1000 > fall_speed:
			fall_time = 0
			game.current.fall()
			game.draw()
			pygame.display.update()


	