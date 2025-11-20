import pygame.font
from settings import Settings

#this is basically a reworked "button.py code fyi"
class Overlay:
    def __init__(self, cw_game, text):
        """Prepare transparent overlay text."""
        self.screen = cw_game.screen
        self.screen_rect = self.screen.get_rect()

        # Text settings
        self.text_color = (255, 0, 0) # im no genius but I thin this is red 
        self.font = pygame.font.SysFont(None, 48)


        #do the thing on call
        self._prep_msg(text)

        #settings
        self.settings = Settings()


    def _prep_msg(self, text):
        """Render text with transparent background and center it."""
        self.text_image = self.font.render(text, True, self.text_color, None)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.screen_rect.center


    def draw_text(self):
        """Blit transparent text directly to the screen."""
        self.screen.blit(self.text_image, self.text_image_rect)
    
    
    def draw_health(self, hp:int, max_hp:int):
        "Draws health for the cat!"
        #https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/scoring-health-bars
        buffer = 20
        x = self.settings.health_x
        y = self.settings.health_y
        if max_hp > 100:
            buffer = 0
        
        ratio = hp / max_hp
        pygame.draw.rect(self.screen, "red", (x, y, max_hp + buffer, 20))
        pygame.draw.rect(self.screen, "green", (x, y, (max_hp + buffer) * ratio, 20))
        self.screen.blit(self.text_image, self.text_image_rect)