import pygame
import random
import copy
from .constants import *
from .shapes import PIECE_SHAPES


class Piece():
    def __init__(self, row, col, game):
        self.shape = copy.deepcopy(random.choice(PIECE_SHAPES))
        self.rotation = random.randint(0, len(self.shape)-1)
        self.color = SHAPE_COLORS[PIECE_SHAPES.index(self.shape)]
        self.row = row
        self.col = col
        self.game = game

    def __repr__(self):
        return f'Pieza {self.row}, {self.col}'

    def max_col(self):
        shape = self.shape[self.rotation]
        max_col = 0     
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] == 1:
                    if j > max_col:
                        max_col = j
        return max_col

    def get_locations(self):
        shape = self.shape[self.rotation]
        locations = []
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] == 1:
                    row = self.row + i 
                    col = self.col + j 
                    locations.append((row, col))
        return locations

    def get_terminal_location(self):
        current_row = self.row
        is_valid = True
        
        while is_valid:
            self.row += 1
            for shape_pos in self.get_locations():
                if not shape_pos in self.game.board.get_valid_locations():
                    is_valid = False
                    break

        last_valid = self.row - 1

        self.row = last_valid
        terminal_locations = self.get_locations()

        score = self.game.get_pos_score(terminal_locations)['score']

        # Restore
        self.row = current_row 

        return {'terminal_locations': terminal_locations, 'score': score}    

    def draw(self, screen):
        if self.row == None: # Next Shape
            shape = self.shape[self.rotation]
            for i in range(len(shape)):
                for j in range(len(shape[i])):
                    if shape[i][j] == 1:
                        pygame.draw.rect(screen, self.color, ((PREV_X+j)*SQUARE_SIZE, (PREV_Y+i)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                        pygame.draw.rect(screen, GRAY, ((PREV_X+j)*SQUARE_SIZE, (PREV_Y+i)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

        else: # Current Shape
            for row, col in self.get_locations():
                pygame.draw.rect(screen, self.color, ((col+OFFSET_X)*SQUARE_SIZE, (row+OFFSET_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for row, col in self.get_terminal_location()['terminal_locations']:
                pygame.draw.rect(screen, self.color, ((col+OFFSET_X)*SQUARE_SIZE, (row+OFFSET_Y)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)


    def rotate(self, game):
        self.rotation += 1
        if self.rotation >= len(self.shape):
            self.rotation = 0

        is_valid = True
        for shape_pos in self.get_locations():
            if not shape_pos in game.board.get_valid_locations():
                is_valid = False
                break

        if not is_valid: # Reverse rotation
          self.rotation -= 1
          if self.rotation < 0:
              self.rotation =  len(self.shape)-1

    def fall(self):
        self.row += 1

    def move(self, x_dir, game):
        self.col += x_dir

        is_valid = True
        for shape_pos in self.get_locations():
            if not shape_pos in game.board.get_valid_locations():
                is_valid = False
                break

        if not is_valid: # Reverse 
            self.col -= x_dir
