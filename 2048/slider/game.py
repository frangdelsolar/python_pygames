from .config import *
import random
import pygame
import copy
import time

class Tile():
	def __init__(self, r, c, value):
		self.r = r
		self.c = c
		self.value = value
		self.color = self.get_color()

	def get_color(self):

		if self.value == 0:
			return GRAY

		elif self.value == 2:
			return C2

		elif self.value == 4:
			return C4

		elif self.value == 8:
			return C8

		elif self.value == 16:
			return C16

		elif self.value == 32:
			return C32

		elif self.value == 64:
			return C64

		elif self.value == 128:
			return C128

		elif self.value == 256:
			return C256

		else:
			return C256

	def get_font_color(self):
		tile_color = self.get_color()
		font_color = LIGHT_FONT
		if (tile_color[0] + tile_color[0] + tile_color[0])//3 >= 230:
			font_color = DARK_FONT	
		return font_color
				
	def draw(self, screen):
		# Dibujar la baldoza
		pygame.draw.rect(screen, self.get_color(), (self.c*SQUARE_SIZE, self.r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

		# Dibujar texto
		if self.value != 0:
			myfont = pygame.font.SysFont("comicsans", FONTSIZE)

			# Elegir color
			font_color = self.get_font_color()			
			text = myfont.render(str(self.value), 10, font_color)
			text_rect = text.get_rect(center=(self.c*SQUARE_SIZE + SQUARE_SIZE//2, self.r*SQUARE_SIZE + SQUARE_SIZE//2))
			screen.blit(text, text_rect)
	
	def pop_animation(self, screen):
		self.draw(screen)

		pygame.draw.rect(screen, (0, 255, 255), (self.c*SQUARE_SIZE, self.r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 10)
		pygame.display.update()



class Game():
	def __init__(self, screen):
		self.grid = []
		self.screen = screen
		self.run = True
		self.build()

	def build(self):
		for r in range(ROWS):
			line = []
			for c in range(COLS):
				line.append(Tile(r, c, 0))
			self.grid.append(line)

		self.randomize()
		self.randomize()

	def randomize(self):
		zeros = []
		for r in range(len(self.grid)):
			for c in range(len(self.grid[r])):
				if self.grid[r][c].value == 0:
					zeros.append((r, c))

		rv = random.choice([2, 4])
		row, col = random.choice(zeros)
		self.grid[row][col].value = rv
		self.grid[row][col].pop_animation(self.screen)

	def combinar(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])-1, 0, -1):
				if self.grid[i][j].value == self.grid[i][j-1].value:
					self.grid[i][j].value = self.grid[i][j].value + self.grid[i][j-1].value
					self.grid[i][j-1].value = 0

	def slide_values(self):
		for i in range(len(self.grid[0])-1):
			for i in range(len(self.grid)):
				for j in range(len(self.grid[i])-1, 0, -1):
					if self.grid[i][j].value == 0:
						self.grid[i][j].value = self.grid[i][j-1].value
						self.grid[i][j-1].value = 0

	def rotar(self):
		grid_copia = copy.deepcopy(self.grid)

		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				row = j
				col = len(self.grid[i])-1-i
				grid_copia[row][col].value = self.grid[i][j].value

		self.grid = grid_copia

	def deslizar(self, button):

		prev_grid = copy.deepcopy(self.grid)

		# Rotar matriz
		if button == 'up':
			rt = 1

		elif button == 'down':
			rt = 3

		elif button == 'right':
			rt = 0

		elif button == 'left':
			rt = 2

		for _ in range(rt):
			self.rotar()

		# Aplicar cambios
		self.combinar()
		self.slide_values()

		# Devolver matriz a su posición original
		for _ in range(4-rt):
			self.rotar()

		next_grid = copy.deepcopy(self.grid)

		self.draw()
		pygame.display.update()
		
		self.slide_animation(prev_grid, next_grid, button)

		# Añadir un valor en posición aleatoria
		self.randomize()

	def slide_animation(self, prev, next, button):
		pass


	def draw(self):
		self.screen.fill(DARK_GRAY) 

		for r in range(len(self.grid)):
			for c in range(len(self.grid[r])):
				self.grid[r][c].draw(self.screen)

		for r in range(len(self.grid)):
			pygame.draw.line(self.screen, DARK_GRAY, (0, r*SQUARE_SIZE), (WIDTH, r*SQUARE_SIZE), 8)
			pygame.draw.line(self.screen, DARK_GRAY, (r*SQUARE_SIZE, 0), (r*SQUARE_SIZE, HEIGHT), 8)

