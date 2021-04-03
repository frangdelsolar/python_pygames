from .constants import ROWS, COLS
import random
import pygame
import time

class AI():
	def __init__(self):
		self.ejecuciones = 0

	def get_valid_moves(self, pacman):
		possible = [
			# UP
			(-1, 0),

			# DOWN:
			(1, 0),

			# RIGHT
			(0, 1),

			# LEFT
			(0, -1)
		]

		possible.pop(possible.index((pacman.y_speed, pacman.x_speed)))

		return possible

	def get_distance(self, pacman, fruit):
		distance = (fruit.row - pacman.row, fruit.col - pacman.col)
		return distance

	def get_move(self, game):
		valid_moves = self.get_valid_moves(game.pacman)
		distance = self.get_distance(game.pacman, game.food)

		for move in valid_moves:
			new_distance = (distance[0] + move[0], distance[1] + move[1])

			print(new_distance[0] - distance[0], distance[0])
			print(new_distance[1] - distance[1], distance[1])
			if (new_distance[0] - distance[0] < distance[0] or
				new_distance[1] - distance[1] < distance[1]):
				print('acercandose')
				return move

		return move
