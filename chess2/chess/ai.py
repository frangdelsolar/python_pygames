from .constants import ROWS, COLS
import random
import pygame
import time

class AI():
	def __init__(self):
		self.ejecuciones = 0

	def is_terminal_node(self, game):
		player = game.turno
		if len(player.get_all_moves(game.other_player().set.pieces, game.log)) <= 0:
			if player.king_checked(game.other_player().set.pieces, game.log):
				print('jaque mate')
				return player
			return 'tie'


		elif len(game.other_player().get_all_moves(player.set.pieces, game.log)) <= 0:
			if game.other_player().king_checked(player.set.pieces, game.log):
				print('jaque mate')
				return game.other_player()
			return 'tie'


	def minimax(self, game, depth, alpha, beta, is_maxim):

		self.ejecuciones += 1

		game.draw()
		pygame.display.update()
		time.sleep(0.2)


		is_terminal = self.is_terminal_node(game)


		if depth == 0 or is_terminal:
			if is_terminal:
				if is_terminal == game.turno:
					return (None, 1000000)
				if is_terminal == game.other_player():
					return (None, -1000000)
				if is_terminal == 'tie':
					return (None, 0)
			else:
				return (None, self.get_score(game))


		if is_maxim:
			available = game.turno.get_all_moves(game.other_player().set.pieces, game.log)

			best_score = -float('inf')
			best_move = random.choice(available)

			for ai in available:
				
				piece = ai['pieza']
				col = piece.col
				row = piece.row

				player = game.turno
				other_player = game.other_player()
				
				valid_move = False

				player.hand = piece
				original_piece, original_row, original_col = player.hand, player.hand.row, player.hand.col
				move = ai['move']
				row = move[0]
				col = move[1]

				valid_move = player.release_piece(row, col, other_player.set.pieces, game.screen, game)


				captured = game.eat_piece(row, col)

				score = self.minimax(game, depth-1, alpha, beta, False)[1]

				# # Es promoción?

				# Reestablecer
				if captured:
					other_player.set.pieces.append(captured)
				original_piece.row, original_piece.col = original_row, original_col

				if score > best_score:
					best_score = score
					best_move = ai
				alpha = max(alpha, score)
				if alpha >= beta:
						break

			return (best_move, best_score)

		else:
			available = game.other_player().get_all_moves(game.turno.set.pieces, game.log)
			print(available)

			best_score = float('inf')
			best_move = random.choice(available)

			for ai in available:

				piece = ai['pieza']

				col = piece.col
				row = piece.row

				player = game.other_player()
				other_player = game.turno
				
				valid_move = False

				player.hand = piece
				original_piece, original_row, original_col = player.hand, player.hand.row, player.hand.col
				move = ai['move']
				row = move[0]
				col = move[1]
				valid_move = player.release_piece(row, col, other_player.set.pieces, game.screen, game)
				
				captured = game.eat_piece(row, col)
				score = self.minimax(game, depth-1, alpha, beta, True)[1]

				# # Es promoción?
				# Reestablecer
				if captured:
					other_player.set.pieces.append(captured)
				original_piece.row, original_piece.col = original_row, original_col

				if score < best_score:
					best_score = score
					best_move = ai
				beta = min(beta, score)
				if alpha >= beta:
					break
			return (best_move, best_score)


	def get_score(self, game):
		score = 0

		for piece in game.turno.set.pieces:
			if piece.name == 'King': 
				score += 900
			if piece.name == 'Queen': 
				score += 90
			if piece.name == 'Bishop': 
				score += 30
			if piece.name == 'Knight': 
				score += 30
			if piece.name == 'Rook': 
				score += 50
			if piece.name == 'Pawn': 
				score += 10

		for piece in game.other_player().set.pieces:
			if piece.name == 'King': 
				score -= 900
			if piece.name == 'Queen': 
				score -= 90
			if piece.name == 'Bishop': 
				score -= 30
			if piece.name == 'Knight': 
				score -= 30
			if piece.name == 'Rook': 
				score -= 50
			if piece.name == 'Pawn': 
				score -= 10

		return score

	def move(self, game):

		valid_moves = game.turno.get_all_moves(game.other_player().set.pieces, game.log)
		move = random.choice(valid_moves)

		self.ejecuciones = 0
		move = self.minimax(game, 3, -float('inf'), float('inf'), True)[0]
		print(self.ejecuciones)

		return move 








