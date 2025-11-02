import pygame.font
from pygame.sprite import Group
from button import Button
from settings import Settings

class Shop:
    '''A class to represent the shop!'''

    def __init__(self, ai_game):
        '''Initialize shop attributes/methods.'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.font = pygame.font.SysFont(None, 50)
        self.shop_active = False
        self.shop_button = Button(self, "SHOP")
        self.background_button = Button(self, "")
        self.prep_background()
        self.prep_title()
        #self.prep_characters()
        #self.check_purchase_status()

    def _update_shop(self):
        '''Updating shop (empty rn)'''

    def _checked_shop_clicked(self, mouse_pos):
        '''Function to see if button clicked.'''
        shop_button_clicked = self.shop_button.rect.collidepoint(mouse_pos)
        if shop_button_clicked:
            self.shop_active = not self.shop_active #allows it to toggle

    def prep_background(self):
        '''Create a "button" for the shop to show.'''
        self.background_button._position_button(30, 100)
        self.background_button._update_color_size_msg(255, 153, 51, 850, 400)

    def prep_title(self):
        '''Create a "button" for the shop just to show.'''
        self.shop_txt_color = (100, 102, 100)

    def show_shop(self):
        '''Draw the shop and its componetns to the screen.'''
        self.shop_button.draw_button()
        self.shop_button._position_button(50, 20)
        self.shop_button._update_color_size_msg(204, 102, 0, 200, 50, "SHOP")

        if self.shop_active:
            self.background_button.draw_button()