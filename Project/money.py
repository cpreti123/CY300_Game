import pygame.font

class Money:
    '''a class to handle money'''

    def __init__(self, sw_game):
        '''initialize scoreboard attributes'''
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_game.settings

        #starting amount ** add this to setting later but am lazy rn
        self.amount = 1000

        #font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_money_image()

    def prep_money_image(self):
        """Turn the money into a rendered image."""
        money_str = str(self.amount)
        self.money_image = self.font.render(money_str, True, self.text_color, self.settings.bg_color)
        self.money_rect = self.money_image.get_rect()
        self.money_rect.right = self.screen_rect.right - 20
        self.money_rect.top = 20


    def add_money(self, amount):
        '''add money'''
        self.amount += amount
        self.prep_money_image()

    def spend_money(self, amount):
        '''put it all on red'''
        self.amount -= amount
        self.prep_money_image()


    def show_money(self):
        """Draw money to the screen."""
        self.screen.blit(self.money_image, self.money_rect)
