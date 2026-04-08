import pygame
from codes.const import WINDOW_HEIGHT, WINDOW_WIDTH
from codes.const import *
from codes.game import Game

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.show_splash = True 
        self.game_instance = Game()#initial screen

    def text_menu(self, text_size, text, text_color, text_center_pos):
        font = pygame.font.SysFont('arial', text_size, bold=True)
        image = font.render(text, True, text_color)
        rect = image.get_rect(center=text_center_pos)
        self.screen.blit(image, rect)

    def run(self):
        pygame.mixer_music.load('assets/autumn.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.fill(COLOR_BLACK)

            if self.show_splash:
                # initial screen
                self.text_menu(100, "TETRIS", COLOR_ORANGE, 
                               (WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 -100))
                self.text_menu(15, "CONTROLS", COLOR_WHITE, 
                               (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +75))
                self.text_menu(15, K_CONTROLS, COLOR_WHITE, 
                               (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +100))
                self.text_menu(20, "PRESS ANY KEY TO START", COLOR_YELLOW, 
                               (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +300))
            else:
                
                grid_surface = self.game_instance.display.grid()
                self.screen.blit(grid_surface, (0, 0))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                
                if event.type == pygame.KEYDOWN:
                    if self.show_splash:
                        self.show_splash = False