import pygame
import sys
from four.constants import SCREEN_SIZE
from four.game import Game

import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

juego = Game(screen)
clock = pygame.time.Clock()


while juego.run:

	juego.check_win()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			juego.click(event.button, event.pos)


	juego.draw()


	pygame.display.update()

	clock.tick(1)


	