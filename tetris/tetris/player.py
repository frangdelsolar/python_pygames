

class Player():
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.clicks = 0

	def __repr__(self):
		return f'Jugador {self.name} - {self.score} puntos'