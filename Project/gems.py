import pygame
from settings import Settings
from button import Button

class Gems:
    '''Class to handle the game's gems system.'''

    def __init__(self, sw_game):
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.gems = self.settings.gems

        #font and whatnot
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_gems_img()

    def prep_gems_img(self):
        '''Turn gems into rendered img.'''
        gems_str = str(self.gems)
        self.gems_img = self.font.render(gems_str, True, self.text_color, self.settings.bg_color)
        self.gems_rect = self.gems_img.get_rect()
        self.gems_rect.right = self.screen_rect.right - 425
        self.gems_rect.top = 170
        
    def updated_gems(self, amount):
        '''updates gem amount'''
        self.gems += amount

    def show_gems(self):
        '''Draw to screen.'''
        self.prep_gems_img()
        self.screen.blit(self.gems_img, self.gems_rect)