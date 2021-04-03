import pygame
class AI:
    pass

    def move(self, piece, grid):
        from main import valid_space, draw_next_shape
        # print(piece)
        # print(grid)

        for rotation in range(len(piece.shape)):
            print(rotation)
            piece.rotation += 1
            if not(valid_space(piece, grid)):
                piece.rotation -= 1

            pygame.display.update()
