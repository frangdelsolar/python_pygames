from .board import Board
from .player import Player
from .snake import Snake
from .food import Food
from .ai import AI
from .constants import ROWS, COLS

class Game():
	def __init__(self, screen):
		self.board = Board()
		self.screen = screen
		self.player = Player('Francisco')
		self.snake = Snake()
		self.food = Food()
		self.ai = AI()
		self.run = True
		self.speed = 10

	def draw(self):
		self.update()
		self.board.draw(self.screen)
		self.snake.draw(self.screen)
		self.food.draw(self.screen)


	def ai_dirigir(self):
		direction = self.ai.get_move(self)
		self.dirigir(direction)

	def dirigir(self, direction):
		self.snake.mover(direction)

	def update(self):	
		self.snake.update()

		# eat itself
		if (self.snake.row, self.snake.col) in self.snake.tail:
			self.run = False

		# eat fruit
		if self.snake.row == self.food.row and self.snake.col == self.food.col:
			self.snake.eat(self.food)
			self.speed += 1 

		if self.speed >= 30:
			self.speed = 30

		# Screen limits
		if (self.snake.row < 0 or
			self.snake.row >= ROWS or
			self.snake.col < 0 or
			self.snake.col >= COLS):
			self.run = False