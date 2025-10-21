import pygame
import sys
from settings import Settings
from button import Button
from money import Money
from game_stats import GameStats



class Unit(pygame.sprite.Sprite):
    def __init__(self, pos):
        cat_png = "cat_glock.png"
        super().__init__()
        self.image = pygame.image.load(cat_png).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
            


class sw:
    '''holds things for stick war eske game'''
   
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #screen things
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("sw")

        #load background
        self.background = pygame.image.load("game_bg.png").convert()
        self.money = Money(self)
        self.stats = GameStats(self)

        #nts sprite group add units to this
        self.all_sprites = pygame.sprite.Group()
        self.player = Unit((self.settings.screen_width // 2, self.settings.screen_height // 2))  
        #creates first unit Glock Cat
        self.unit_one = Button(self, "Unit1")


    def run_game(self):
        while True:
            self._check_events()
            
            # Update sprites
            self.all_sprites.update()

            # Redraw the screen
            
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.unit_one.draw_button()
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
                self.check_unit_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()


    def check_unit_button(self, mouse_pos):
        """spawns unit when clicked"""
        button_clicked = self.unit_one.rect.collidepoint(mouse_pos)
        spawn_coords = (100, 450)
        if button_clicked and self.money.amount > 50:
            self.add_unit(spawn_coords)
            self.money.spend_money(50)
    
    def add_unit(self, pos):
        new_unit = Unit(pos)
        self.all_sprites.add(new_unit)
            

            
        
        

if __name__ == '__main__':
    game_object = sw()
    game_object.run_game()
