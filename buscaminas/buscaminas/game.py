from .board import Board
from .player import Player
from .constants import ROWS, COLS

class Game():
	def __init__(self, screen):
		self.board = Board()
		self.screen = screen
		self.player = Player('Francisco')
		self.run = True

	def draw(self):
		self.board.draw(self.screen)

	def game_over(self):
		print('has perdido!!!')
		self.board.revelar(self.screen)
		self.run = False


	def click(self, button, pos, screen):
		run = self.board.click(button, pos, screen)

		if not run:
			self.game_over()

	def check_win(self):
		for i in range(ROWS):
			for j in range(COLS):
				if not self.board.grid[i][j].has_bomb:
					if self.board.grid[i][j].hide:
						return False
		print('has ganado!!!')
		self.run = False
		return True