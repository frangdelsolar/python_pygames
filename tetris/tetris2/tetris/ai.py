import pygame
import random
import time
from .constants import *

class AI:
    current_status = None
    next_status = None
    best_move = None

    def __init__(self, game):
        self.game = game
        self.evaluation = None

    def save_status(self):
        self.current_status = {
            'rot': self.game.current.rotation,
            'row': self.game.current.row,
            'col': self.game.current.col,
        }

        self.next_status = {
            'rot': self.game.next.rotation,
            'row': self.game.next.row,
            'col': self.game.next.col,
        }


    def restore(self):
        self.game.current.rotation = self.current_status['rot']
        self.game.current.row = self.current_status['row']
        self.game.current.col = self.current_status['col']
        
        self.game.next.rotation = self.next_status['rot']
        self.game.next.row = self.next_status['row']
        self.game.next.col = self.next_status['col']

        self.current_status = None
        self.next_status = None


    def evaluate(self):

        self.save_status()

        current = self.game.current
        preview = self.game.next

        best_move = {
            'shape': current,
            'rot': current.rotation,
            'col': current.col,       
        }
        best_score = -float('inf')


        # iterar sobre cada posición posible de la forma
        current_rots = len(current.shape)
        for current_rot in range(current_rots):
            current.rotation = current_rot
            is_valid = True
            for current_shape_pos in current.get_locations():
                if not current_shape_pos in self.game.board.get_valid_locations():
                    is_valid = False
                    continue
                    
            if is_valid:
                # iterar sobre cada columna
                for current_col in range(BOARD_COLS - current.max_col()):
                    current.col = current_col

                    # preview_rots = len(preview.shape)
                    # self.game.next.row = 0 
                    # self.game.next.col = 0
                    # for preview_rot in range(preview_rots):
                    #     preview.rotation = preview_rot
                    #     is_valid = True
                    #     for preview_shape_pos in preview.get_locations():
                    #         if not preview_shape_pos in self.game.board.get_valid_locations():
                    #             is_valid = False
                    #             continue
                                
                    #     if is_valid:
                    #         # iterar sobre cada columna
                    #         for preview_col in range(BOARD_COLS - preview.max_col()):
                    #             preview.col = preview_col

                    score = current.get_terminal_location()['score']

                    if score > best_score:
                        best_score = score
                        best_move = {
                            'shape': current,
                            'rot': current_rot,
                            'col': current_col,     
                        }

        # Reestablecer
        self.restore()

        # devolver instrucciones
        self.evaluation = best_move
        # return best_move

    def get_event(self):

        while not self.evaluation or self.evaluation['shape'] != self.game.current:
            self.evaluate()

        best_move = self.evaluation
        # best_move = self.evaluate()
        

        if self.game.current.rotation != best_move['rot']:
            return {
                'type': 'KEYDOWN',
                'key' : 'K_UP'
            }

        elif (self.game.current.rotation == best_move['rot'] and 
              self.game.current.col < best_move['col']): 
            return {
                'type': 'KEYDOWN',
                'key' : 'K_RIGHT'
            }
        
        elif (self.game.current.rotation == best_move['rot'] and 
              self.game.current.col > best_move['col']): 
            return {
                'type': 'KEYDOWN',
                'key' : 'K_LEFT'
            }

        elif (self.game.current.rotation == best_move['rot'] and 
              self.game.current.col == best_move['col']):            
            return {
                'type': 'KEYDOWN',
                'key' : 'K_DOWN'
            }

        else:
            print('Se me escapó alguna alternativa')


        # time.sleep(1)



