import pygame

from codes.const import GRID_HEIGHT, GRID_WIDTH
from codes.display import Display
from codes.tetronimo import Tetromino

class Game:
    
    def __init__(self,):
        self.display = Display()
        self.field = [[(0, 0, 0) for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
        self.current_tetromino = Tetromino(5, 0)
        self.state = "Start"