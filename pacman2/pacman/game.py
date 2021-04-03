from .pac_man import Pacman
from .level import Level
from .ghost import Ghost
from .constants import YELLOW, RED, BLACK

class Game():
    def __init__(self, screen):
        self.pause = False
        self.run = True
        self.screen = screen
        self.speed = 1
        self.level = None
        self.pacman = None
        self.ghosts = []
        self.build()

    def build(self):
        self.level = Level()
        self.pacman = Pacman(11, 10, YELLOW)
        self.ghosts.append(Ghost(7, 10, RED))

    def update(self):
        self.pacman.update(self.level, self.screen)
        
        for ghost in self.ghosts:
            ghost.set_direction(self)
            ghost.update(self.level, self.screen)


    def dirigir(self, direction):
        self.pacman.mover(direction)

    def draw(self):
        self.update()
        self.screen.fill(BLACK)        
        self.level.draw(self.screen)
        self.pacman.draw(self.screen)

        for ghost in self.ghosts:
            ghost.draw(self.screen)

    def pausar(self):
        if self.pause == False:
            self.pause = True
        else:
            self.pause = False
