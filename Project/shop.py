import pygame.font
from pygame.sprite import Group
from button import Button
from settings import Settings
from imagebutton import ImageButton
from points import Points

class Shop:
    '''A class to represent the shop!'''

    def __init__(self, sw_game):
        '''Initialize shop attributes/methods.'''
        self.sw_game = sw_game
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.font = pygame.font.SysFont(None, 50)
        self.shop_active = False
        self.shop_button = Button(self, "SHOP")
        self.background_button = Button(self, "")
        self.plane_cat = ImageButton(self, "Project/images/biplane_cat.png", pos=(100, 100))
        self.plane_cat_button = Button(self, "Plane Cat ($100)")
        self.plane_cat_purchased = False
        self.prep_characters()
        self.points = Points(self.sw_game)

    def _update_shop(self):
        '''Updating shop (nothing rn)'''

    def _check_clicked(self, mouse_pos):
        '''Function to check all events clicked.'''
        self._checked_shop_clicked(mouse_pos)
        self._checked_plane_clicked(mouse_pos)

    def _checked_shop_clicked(self, mouse_pos):
        '''Function to see if button clicked.'''
        shop_button_clicked = self.shop_button.rect.collidepoint(mouse_pos)
        if shop_button_clicked:
            self.shop_active = not self.shop_active #allows it to toggle
    
    def _checked_plane_clicked(self, mouse_pos):
        '''Function to see if plane clicked.'''
        plane_button_clicked = self.plane_cat_button.rect.collidepoint(mouse_pos)
        if plane_button_clicked and self.points.points >= 100 and not self.plane_cat_purchased:
            self.points.points -= 100
            self.points.prep_points_img()
            self.points.show_points()
            self.plane_cat_purchased = True
            self._check_character_status()

    def _check_character_status(self):
        if self.plane_cat_purchased:
            self.plane_cat_button._update_color_size_msg(0, 182, 24, 275, 75, "Plane Cat")

    def prep_plane_cat(self):
        '''Create a button for plane cat.'''
        self.plane_cat_button._position_button(80, 220)
        self.plane_cat_button._update_color_size_msg(238, 33, 18, 275, 75, "Plane Cat ($100)")
    
    def prep_shop_button(self):
        '''Preps the shop button.'''
        self.shop_button.draw_button()
        self.shop_button._position_button(50, 20)
        self.shop_button._update_color_size_msg(204, 102, 0, 200, 50, "SHOP")

    def prep_background(self):
        '''Create a "button" for the shop to show.'''
        self.background_button._position_button(30, 100)
        self.background_button._update_color_size_msg(255, 153, 51, 850, 400)

    def prep_title(self):
        '''Create a "button" for the shop just to show.'''
        self.shop_txt_color = (100, 102, 100)

    def prep_characters(self):
        '''Preps all characters to be called by show_shop'''
        self.prep_plane_cat()
        self.prep_background()
        self.prep_title()
        self.prep_shop_button()

    def show_shop(self):
        '''Draw the shop and its componetns to the screen.'''
        self.shop_button.draw_button()
        if self.shop_active:
            self.background_button.draw_button()
            self.plane_cat.draw_button()
            self.plane_cat_button.draw_button()
            self.points.show_points()