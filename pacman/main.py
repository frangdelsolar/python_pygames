import pygame
import sys
from pacman.constants import SCREEN_SIZE
from pacman.game import Game
import time
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

			if event.key == pygame.K_SPACE:
				juego.pausar()

	for ghost in juego.ghosts:
		direccion = ghost.navigate(juego)
		ghost.mover(direccion)


	if not juego.pause:
		juego.draw()
		pygame.display.update()
		
		if juego.check_win():
			juego.run = False
			print('ganaste')
			time.sleep(3)
		clock.tick(juego.speed)


	