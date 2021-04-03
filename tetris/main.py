import pygame
import sys
from tetris.constants import SCREEN_SIZE
from tetris.game import Game

import random


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

run = True

juego = Game(screen)
clock = pygame.time.Clock()


while juego.run:



	juego.listen()
	
	juego.update()


	juego.draw()
	pygame.display.update()
	clock.tick(juego.speed*2)


	