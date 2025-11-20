import pygame.font
from button import Button
from settings import Settings
from imagebutton import ImageButton
from gems import Gems

class Levels:
    '''A class to represent the levels.'''

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
        self.prep_levels()
        #self.level_number = self.settings.start_level
    
    def prep_levels(self):
        '''Preps the levels.'''
        self.levels_button.draw_button()
        self.levels_button._position_button(350, 50)
        self.levels_button._update_color_size_msg(0, 204, 102, 200, 50, f'Level {self.level_num}')
    
    def show_levels(self):
        '''Draw levels and necessary components to screen!'''
        self.levels_button.draw_button()
        if self.levels_active:
            ##nothing rn
            self.prep_levels()