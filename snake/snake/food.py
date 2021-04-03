import pygame
import random
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, RED

class Food():

	def __init__(self):
		self.row = None
		self.col = None
		self.build()

	def build(self):
		self.row = random.randint(0, ROWS-1)
		self.col = random.randint(0, COLS-1)

	def draw(self, screen):
		pygame.draw.rect(screen, RED, (self.col*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
		
	def pick_pos(self):
		row = random.randint(1, ROWS-2)
		col = random.randint(1, COLS-2)
		return (row, col)