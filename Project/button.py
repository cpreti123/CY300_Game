import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, sw_game, msg):
        """Initialize button attributes."""
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 100, 100
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = (100, 500)

        # The button message needs to be prepped only once.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def _position_button(self, x:int, y:int) -> None:
        '''Positions the button on the screen!'''
        self.rect.topleft = (x, y)
        self.msg_image_rect.center = self.rect.center


    def _update_color_size_msg(self, a:int, b:int, c:int, x:int, y:int, msg:str = "") -> None:
        '''Updates the color and size of buttons.'''
        self.button_color = (a, b, c)
        self.width, self.height = x, y
        self.rect = pygame.Rect(self.rect.topleft[0], self.rect.topleft[1], self.width, self.height)
        self._prep_msg(msg)

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)