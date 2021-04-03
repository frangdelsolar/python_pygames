from .board import Board
from .player import Player
from .pac_man import Pacman
from .ghost import Blinky, Pinky, Inky, Clyde
from .food import Food
from .constants import ROWS, COLS, SQUARE_SIZE, YELLOW, BLUE, RED, GREEN, PINK

class Game():
	def __init__(self, screen):
		self.board = Board()
		self.screen = screen
		self.player = Player('Francisco')
		self.pacman = Pacman(11, 10, 0, -1, YELLOW)
		self.ghosts = []
		self.food = []
		self.run = True
		self.speed = 1
		self.pause = False
		self.build()

	def build(self):
		for r in range(len(self.board.level)):
			for c in range(len(self.board.level[r])):				
				if self.board.level[r][c] == 0:
					self.food.append(Food(r, c, SQUARE_SIZE//10, False))
				if self.board.level[r][c] == 4:
					self.food.append(Food(r, c, SQUARE_SIZE//5, True))

		self.ghosts.append(Blinky(7, 10, 1, 1, RED, self, self.screen))
		# self.ghosts.append(Pinky(9, 9, 1, 1, PINK, self, self.screen))
		# self.ghosts.append(Inky(9, 10, 1, 1))
		# self.ghosts.append(Clyde(9, 11, 1, 1))

	def draw(self):
		self.update()

		self.board.draw(self.screen)
		for food in self.food:
			food.draw(self.screen)
		for ghost in self.ghosts:
			ghost.draw(self.screen)

		self.pacman.draw(self.screen)

	def pausar(self):
		if self.pause == False:
			self.pause = True
		else:
			self.pause = False

	def dirigir(self, direction):
		self.pacman.mover(direction)

	def check_win(self):
		return len(self.food) == 0

	def update(self):	
		self.pacman.update(self)

		for ghost in self.ghosts:
			ghost.update(self)

		for food in self.food:
			if food.row == self.pacman.row and food.col == self.pacman.col:
				self.food.pop(self.food.index(food))
				if food.is_superfood:
					print('ohh!')


