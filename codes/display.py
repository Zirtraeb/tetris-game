
import pygame

from codes.const import *


class Display:
    def display(self):
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris Game")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Arial", 24)
        title_font = pygame.font.SysFont("Arial", 48, bold=True)
        
    def grid(self):
        background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        background.fill(COLOR_BLACK)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(background, COLOR_WHITE,  
                                (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
        return background
    
    def draw_tetromino(self, surface, tetromino):
        shape_rotations = SHAPES[tetromino.shape]
        current_grid = shape_rotations[tetromino.rotation % len(shape_rotations)]
        
        for row_index, row in enumerate(current_grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    x = (tetromino.x + col_index) * GRID_SIZE
                    y = (tetromino.y + row_index) * GRID_SIZE
                    pygame.draw.rect(surface, tetromino.color, (x, y, GRID_SIZE, GRID_SIZE))