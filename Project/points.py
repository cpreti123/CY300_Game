import pygame
from settings import Settings
from button import Button

class Points:
    '''Class to handle the game's points system.'''

    def __init__(self, sw_game):
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.points = self.settings.points

        #font and whatnot
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_points_img()

    def prep_points_img(self):
        '''Turn points into rendered img.'''
        points_str = str(self.points)
        self.points_img = self.font.render(points_str, True, self.text_color, self.settings.bg_color)
        self.points_rect = self.points_img.get_rect()
        self.points_rect.right = self.screen_rect.right - 20
        self.points_rect.top = 100
    
    def show_points(self):
        '''Draw to screen.'''
        self.screen.blit(self.points_img, self.points_rect)