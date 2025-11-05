#could be a sublass
import pygame


class ImageButton:
        """beacuse I want to use this image i made instead of just words man"""
        def __init__(self, cw_game, image_path, pos=(0,0)):
            self.screen = cw_game.screen
            self.image = pygame.image.load(image_path).convert_alpha() 
            self.rect = self.image.get_rect()
            self.rect.topleft = pos

        def _position_button(self, x:int, y:int) -> None:
            '''Positions the button on the screen!'''
            self.rect.topleft = (x, y)

        def draw_button(self):
            """Draw image button."""
            self.screen.blit(self.image, self.rect)