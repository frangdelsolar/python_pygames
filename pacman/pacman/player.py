

class Player():
	def __init__(self, name):
		self.name = name
		self.points = 0
		self.clicks = 0

	def __repr__(self):
		return f'Jugador {self.name} - {self.points} puntos'