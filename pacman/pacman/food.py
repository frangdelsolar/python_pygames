import pygame
import random
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, YELLOW

class Food():
	def __init__(self, row, col, radius, is_superfood):
		self.row = row
		self.col = col
		self.radius = radius
		self.is_superfood = is_superfood

	def draw(self, screen):
		pygame.draw.circle(screen, YELLOW, ((self.col*SQUARE_SIZE)+SQUARE_SIZE//2, (self.row*SQUARE_SIZE)+SQUARE_SIZE//2), self.radius)
