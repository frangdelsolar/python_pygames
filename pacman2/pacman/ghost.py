from .agent import Agent
import pygame
import time
from .constants import SQUARE_SIZE



class Ghost(Agent):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def is_goal(self, step):
        row, col, count = step
        if self.row == row and self.col == col:
            return True
        return False

    def get_neighbours(self, step, grid):
        directions = [(1, 0),
                      (0, 1),
                      (-1, 0),
                      (0, -1)]

        row, col, count = step
        count += 1
        neighbours = []

        for i, j in directions:
            try:
                if grid[row+i][col+j] != 1:
                    neighbours.append((row+i, col+j, count))
            except Exception as e:
                # print(e)
                pass

        return neighbours

    def draw_path(self, path, game):
        for row, col, count in path:
            pygame.draw.rect(game.screen, self.color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
        
        pygame.display.update()    

    def get_path(self, path, game):
        for step in path:
            if self.is_goal(step):
                return path
            
            else:
                neighbours = self.get_neighbours(step, game.level.grid)
                for vecino in neighbours:
                    if not vecino in path:
                        path.append(vecino)

    def get_direction(self, grid, path):
        vecinos = self.get_neighbours((self.row, self.col, 0), grid)

        prox = None, None, float('inf')
        for row, col, count in vecinos:
            for i, j, c in path:
                if row == i and j == col:
                    if c < prox[2]:
                        prox = i, j, c


        if prox[0] != None and prox[1] != None:
            direccion = (prox[0]-self.col, prox[1]-self.row)
        else:
            direccion = (0, 0)

        return direccion
                
    def set_direction(self, game):
        firs_step = (game.pacman.row, game.pacman.col, 0)

        path = [firs_step]
        path = self.get_path(path, game)

        self.draw_path(path, game)
        
        direccion = self.get_direction(game.level.grid, path)

        self.mover(direccion)