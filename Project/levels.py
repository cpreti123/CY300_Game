import pygame.font
from button import Button
from settings import Settings
from imagebutton import ImageButton
from gems import Gems


class Levels:
    '''A class to represent the levels.'''
    num_glock = 0
    num_plane = 0


    def __init__(self, cw_game):
        '''Initialize level attributes and whatnot.'''
        self.cw_game = cw_game
        self.screen = cw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.font = pygame.font.SysFont(None, 50)
        self.levels_active = False
        self.levels_button = Button(self, "LEVELS")
        self.level_num = self.settings.start_level
        self.updated_level = 1
        self.prep_levels()
        self.current_time = 0

    
    def prep_levels(self):
        '''Preps the levels.'''
        #self.levels_button.draw_button()
        #self.levels_button._position_button(350, 50)
        #self.levels_button._update_color_size_msg(0, 204, 102, 200, 50, f'Level {self.updated_level}')
        self.level_button = ImageButton(self, f"Project/images/level{str(self.updated_level)}_dark.png", pos=(675, -20))
        
        #print(self.settings.updated_level)

    def update_level(self, level_num):
        self.updated_level = level_num
    
    def show_levels(self):
        '''Draw levels and necessary components to screen!'''
        if self.levels_active:
            ##nothing rn
            self.prep_levels()
            self.level_button.draw_button()

    def run_level(self, difficulty):
        if difficulty == 1:
            self.num_glock = 3
            self.num_plane = 0
        elif difficulty == 2:
            self.num_glock = 6
            self.num_plane = 2
        elif difficulty == 3:
            self.num_glock = 10
            self.num_plane = 5
        elif difficulty == 4:
            self.num_glock = 15
            self.num_plane = 8
            

    def level_cycle(self, difficulty):
        self.current_time = pygame.time.get_ticks()
        if self.current_time % 1 > 0:
            self.current_time = 0
            self.rune_level(difficulty)
