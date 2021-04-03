from .constants import *
from .piece import Piece
from .grid import Board
from .ai import AI
import pygame
import sys
import random
import copy


class Game():
	def __init__(self, screen):
		self.run = True
		self.screen = screen
		self.speed = 1
		self.board = None
		self.next = None
		self.current = None
		self.score = 0
		self.ai = None
		self.pause = False
		self.build()

	def build(self):
		self.next = Piece(None, None, self)
		self.current = Piece(0, 5, self)
		self.board = Board()
		self.ai = AI(self)

	def draw_score(self):
		font = pygame.font.SysFont('comicsans', 30)
		label = font.render('Score: ' + str(self.score), 1, (255,255,255))
		sx = 3 * SQUARE_SIZE
		sy = 3 * SQUARE_SIZE
		self.screen.blit(label, (sx + 20, sy + 160))

	def draw_pos_score(self):
		font = pygame.font.SysFont('comicsans', 30)
		label = font.render('Position score: ' + str(self.current.get_terminal_location()['score']), 1, (255,0,255))
		sx = 2 * SQUARE_SIZE
		sy = 5 * SQUARE_SIZE
		self.screen.blit(label, (sx + 20, sy + 160))


	def draw(self):
		self.screen.fill(WHITE)
		self.draw_score()
		self.draw_pos_score()
		self.board.draw_cells(self.screen)
		self.current.draw(self.screen)
		self.next.draw(self.screen)
		self.board.draw_grid(self.screen)
		self.update()

	def get_current(self):
		self.current = self.next
		self.current.row = -1
		self.current.col = 5
		self.next = Piece(None, None, self)

	def set_pause(self):
		if self.pause == False:
			self.pause = True
		else:
			self.pause = False

	def get_pos_score(self, shape_pos):
		score = 0

		grid_copy = copy.deepcopy(self.board.grid)

		for row, col in shape_pos:
			grid_copy[row][col].color = self.current.color

		# calcular puntos

		# Sumar filas completas
		filas_score = 0

		for r in range(BOARD_ROWS):
			count = 0
			for c in range(BOARD_COLS):
				if grid_copy[r][c].color != BASE_COLOR:
					count += 1
			if count == BOARD_COLS:
				filas_score = count * 150

		# Calcular alturas
		heights = []
		for c in range(BOARD_COLS):
			for r in range(BOARD_ROWS):				
				if grid_copy[r][c].color != BASE_COLOR:
					height = BOARD_ROWS - r
					break
				else:
					height = 0
			heights.append(height) 				
					
		# Penalizar alturas
		count = 0
		for h in heights:
			count += h
		height_score = -count * 5

		# Bumpiness
		bumps = []
		for i in range(len(heights)-1):
			bumps.append(abs(heights[i]-heights[i+1]))

		count = 0
		for b in bumps:
			count += b
		bump_score = -count * 15

		# Penalizar huecos
		holes = 0
		for c in range(BOARD_COLS):
			count_holes = False
			for r in range(BOARD_ROWS):			
				if grid_copy[r][c].color != BASE_COLOR:
					count_holes = True
				else:
					if count_holes:
						holes += 1 
		
		hole_score = -holes * 50

		score += filas_score
		score += height_score 
		score += bump_score  
		score += hole_score  

		total_score = {
			'filas_score': filas_score,
			'height_score': height_score ,
			'bump_score': bump_score ,
			'hole_score': hole_score,
			'score': score,
			}

		# print(total_score)

		return total_score

	def update(self):
		stop = False
		for row, col in self.current.get_locations():

			# if row == BOARD_ROWS-1:
			# 	stop = True
			# 	break
			try:
				if self.board.grid[row+1][col].color != BASE_COLOR:
					stop = True
					break
			except Exception as e:
				stop = True
				break

		if stop:
			for row, col in self.current.get_locations():
				self.board.grid[row][col].color = self.current.color

			self.score += self.board.clear_rows()

			self.get_current()

	def listen(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					self.current.fall()

				if event.key == pygame.K_UP:
					self.current.rotate(self)

				if event.key == pygame.K_RIGHT:
					x_dir = 1
					self.current.move(x_dir, self)

				if event.key == pygame.K_LEFT:
					x_dir = -1
					self.current.move(x_dir, self)

				if event.key == pygame.K_SPACE:
					self.set_pause()

	def listen_ai(self):
		event = self.ai.get_event()
		if event['type'] == 'KEYDOWN':
			if event['key'] == 'K_DOWN':
				# self.current.fall()
				pass


			if event['key'] == 'K_UP':
				self.current.rotate(self)

			if event['key'] == 'K_RIGHT':
				x_dir = 1
				self.current.move(x_dir, self)

			if event['key'] == 'K_LEFT':
				x_dir = -1
				self.current.move(x_dir, self)