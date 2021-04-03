import pygame
import sys
from buscaminas.constants import SCREEN_SIZE
from buscaminas.game import Game
# from ai.ai import AI
from ai2.ai2 import AI

import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

juego = Game(screen)
ai = AI()
clock = pygame.time.Clock()


while juego.run:


	juego.check_win()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# if event.type == pygame.MOUSEBUTTONDOWN:
		# 	# juego.click(event.button, event.pos, screen)

		# 	if event.button == 1:
		event, pos = ai.execute(juego)			
		juego.click(event, pos, screen)

		ai.update(juego)


	juego.draw()


	pygame.display.update()

	clock.tick(1)


	