from config import SCREEN_SIZE
from arkanoid.game import Game
import sys
import pygame
import random


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)

game = Game(screen)



key_pressed = None
while game.run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				key_pressed = event.key
			
			if event.key == pygame.K_SPACE:
				game.disparar()


		if event.type == pygame.KEYUP:
			if event.key == key_pressed:
				key_pressed = None

	if not key_pressed:
		game.paddle.set_speed(0)
	else:
		if key_pressed == pygame.K_LEFT:
			game.paddle.set_speed(-1)
		elif key_pressed == pygame.K_RIGHT:
			game.paddle.set_speed(1)

	game.draw()
	pygame.display.update()
	# clock.tick(1)


	