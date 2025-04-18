import pygame, sys
from constants import *

class Cell:
    def __init__(self, value, row, col, screen, given=False):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.given = given

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        pass

    def draw(self):
        pass