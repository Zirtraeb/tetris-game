import pygame
from codes.const import WINDOW_HEIGHT, WINDOW_WIDTH
from codes.const import *
from codes.game import Game

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.show_splash = True 
        self.game_instance = Game()  # initial screen
        self.fall_time = 0
        self.fall_speed = 500
        self.clock = pygame.time.Clock()

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
                self.text_menu(20, "PRESS ANY KEY TO START", COLOR_GREEN, 
                               (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +250))
            else:
                grid_surface = self.game_instance.display.grid()
                self.screen.blit(grid_surface, (0, 0))
                self.game_instance.display.draw_field(self.screen, self.game_instance.field)
                self.game_instance.display.draw_tetromino(self.screen, self.game_instance.current_tetromino)

                score_text = f"Score: {self.game_instance.score}"
                self.text_menu(25, score_text, COLOR_GREEN, (WINDOW_WIDTH - SIDEBAR_WIDTH // 2, 30))

            pygame.display.flip()

            if not self.show_splash:
                self.fall_time += self.clock.get_rawtime()
                self.clock.tick()
                
                if self.fall_time >= self.fall_speed:
                    self.fall_time = 0
                    self.game_instance.current_tetromino.y += 1
                    if not self.game_instance.valid_move(self.game_instance.current_tetromino):
                        self.game_instance.current_tetromino.y -= 1
                        self.game_instance.lock_piece(self.game_instance.current_tetromino)  # lock piece in place if it can't move down

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if self.show_splash:
                        self.show_splash = False
                        self.fall_time = 0 # reset fall time when starting game
                        
                    else:                        
                        if event.key == pygame.K_UP:  # rotate
                            self.game_instance.current_tetromino.rotate()
                            if not self.game_instance.valid_move(self.game_instance.current_tetromino):
                                for _ in range(3):
                                    self.game_instance.current_tetromino.rotate()  # Rotate back if hits a wall or another piece
                                    
                        if event.key == pygame.K_DOWN: # soft drop
                            self.game_instance.current_tetromino.y += 1
                            if not self.game_instance.valid_move(self.game_instance.current_tetromino):
                                self.game_instance.current_tetromino.y -= 1
                                self.game_instance.lock_piece(self.game_instance.current_tetromino) #lock piece in place if it can't move down
                        
                        if event.key == pygame.K_LEFT: # move
                            self.game_instance.current_tetromino.x -= 1
                            if not self.game_instance.valid_move(self.game_instance.current_tetromino):
                                self.game_instance.current_tetromino.x += 1
                                
                        if event.key == pygame.K_RIGHT: # move
                            self.game_instance.current_tetromino.x += 1
                            if not self.game_instance.valid_move(self.game_instance.current_tetromino):
                                self.game_instance.current_tetromino.x -= 1    
                        
                        if event.key == pygame.K_SPACE: # hard drop 
                            while self.game_instance.valid_move(self.game_instance.current_tetromino): #keep going until it hits something
                                self.game_instance.current_tetromino.y += 1
                            self.game_instance.current_tetromino.y -= 1
                            
                            
            if self.game_instance.state == "Game Over":
                self.screen.fill(COLOR_BLACK)
                self.text_menu(50, "GAME OVER", COLOR_RED, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
                self.text_menu(25, f"Final Score: {self.game_instance.score}", COLOR_YELLOW, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
                self.text_menu(20, "PRESS ANY KEY TO RESTART", COLOR_WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100))
                pygame.display.flip()
                
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN: #reset game on key press
                            self.game_instance = Game()
                            self.fall_time = 0
                            waiting = False
                continue