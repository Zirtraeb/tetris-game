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
    