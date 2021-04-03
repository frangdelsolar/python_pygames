from .constants import ROWS, COLS
import random
import pygame
import time

class AI():
	def __init__(self):
		self.ejecuciones = 0

	def get_valid_moves(self, snake):
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

		possible.pop(possible.index((snake.y_speed, snake.x_speed)))

		return possible

	def get_distance(self, snake, fruit):
		distance = (fruit.row - snake.row, fruit.col - snake.col)
		return distance

	def get_move(self, game):
		valid_moves = self.get_valid_moves(game.snake)
		distance = self.get_distance(game.snake, game.food)

		for move in valid_moves:
			new_distance = (distance[0] + move[0], distance[1] + move[1])

			print(new_distance[0] - distance[0], distance[0])
			print(new_distance[1] - distance[1], distance[1])
			if (new_distance[0] - distance[0] < distance[0] or
				new_distance[1] - distance[1] < distance[1]):
				print('acercandose')
				return move

		return move
