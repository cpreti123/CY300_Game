import pygame
import sys
from settings import Settings
from button import Button
from money import Money
from game_stats import GameStats
from cat_characters import CatCharacters


class CatWar:
    '''holds things for stick war eske game'''
   
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #screen things
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("CatWar")

        #load background
        self.background = pygame.image.load("Project/game_bg.png").convert()
        self.money = Money(self)
        self.stats = GameStats(self)

        #nts sprite group add glock cats to this
        self.all_sprites = pygame.sprite.Group()
        self.player = CatCharacters((self.settings.screen_width // 2, self.settings.screen_height // 2))  
        #creates first Glock Cat
        self.glock_cat = Button(self, "Glock Cat")


    def run_game(self):
        while True:
            self._check_events()
            
            # Update sprites
            self.all_sprites.update()

            # Redraw the screen
            
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.glock_cat.draw_button()
            self.money.show_money()

            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_glock_cat(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()


    def check_glock_cat(self, mouse_pos):
        """spawns glock cat when clicked"""
        button_clicked = self.glock_cat.rect.collidepoint(mouse_pos)
        spawn_coords = (100, 450)
        if button_clicked and self.money.amount > 50:
            self.add_glock_cat(spawn_coords)
            self.money.spend_money(50)
    
    def add_glock_cat(self, pos):
        new_glock_cat = CatCharacters(pos)
        self.all_sprites.add(new_glock_cat)
            

            
        
        

if __name__ == '__main__':
    game_object = CatWar()
    game_object.run_game()
