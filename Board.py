import pygame, sys
from constants import *
from Cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_size = self.width // 9
        self.selected = None

        self.rows = 9
        self.cols = 9

        self.grid = [[Cell(0, row, col, self.cell_size) for col in range(self.cols)] for row in range(self.rows)]

    def draw(self):
        self.screen.fill(WHITE)

        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, BLACK, (0, i * self.cell_size), (self.width, i * self.cell_size), line_width)
            pygame.draw.line(self.screen, BLACK, (i * self.cell_size, 0), (i * self.cell_size, self.width), line_width)

        pygame.display.update()

    def select(self, row, col) -> None:
        # marks a cell at (row, col) as a selected cell
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c].selected = False

        self.grid[row][col].selected = True
        self.selected = (row, col)

    def click(self, x, y):
        # returns a tuple of the (row, col) of the cell which was clicked.
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // self.cell_size
            col = x // self.cell_size
            return row, col
        return None



