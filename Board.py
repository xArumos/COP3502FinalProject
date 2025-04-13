import pygame, sys
from constants import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_size = self.width // 9

    def draw(self):
        self.screen.fill(WHITE)
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, BLACK, (0, i * self.cell_size), (self.width, i * self.cell_size), line_width)
            pygame.draw.line(self.screen, BLACK, (i * self.cell_size, 0), (i * self.cell_size, self.width), line_width)

        pygame.display.update()