import pygame
import random
from codes.const import COLORS, SHAPES


class Tetromino:
    def __init__(self, x, y, shape=None, color=None):
        self.x = x
        self.y = y
        self.shape = shape if shape is not None else random.randint(0, len(SHAPES) - 1)
        self.color = color if color is not None else COLORS[random.randint(0, len(COLORS) - 1)]
        self.rotation = 0
        
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(SHAPES[self.shape])
    
    ''' def get_position(self):
        blocks = []
        for i in range(len(SHAPES[self.shape][self.rotation])):
            for j in range(len(SHAPES[self.shape][self.rotation][i])):
                if SHAPES[self.shape][self.rotation][i][j] == 1:
                    blocks.append((self.x + j, self.y + i))
        return blocks'''