import pygame

from codes.const import GRID_HEIGHT, GRID_WIDTH, SHAPES
from codes.display import Display
from codes.tetronimo import Tetromino

class Game:
    
    def __init__(self,):
        self.display = Display()
        self.field = [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_tetromino = Tetromino(5, 0)
        self.state = "Start"
        
    def valid_move(self, piece):
        shape_rotation = SHAPES[piece.shape]
        current_grid = shape_rotation[piece.rotation % len(shape_rotation)]
        
        for row_index, row in enumerate(current_grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    new_x = piece.x + col_index
                    new_y = piece.y + row_index
                    
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    
                    if new_y >= 0:
                        if self.field[new_y][new_x] != (0, 0, 0):
                            return False
        return True
        
    def lock_piece(self, piece):
        print("Locking piece")
        shape_rotation = SHAPES[piece.shape]
        current_grid = shape_rotation[piece.rotation % len(shape_rotation)]
            
        for row_index, row in enumerate(current_grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    grid_y = piece.y + row_index
                    grid_x = piece.x + col_index
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        self.field[grid_y][grid_x] = piece.color
                    else:
                        print(f"Skipping out-of-bounds write at {grid_x}, {grid_y}")
            
        self.current_tetromino = Tetromino(GRID_WIDTH // 2, 1) #spawn new piece