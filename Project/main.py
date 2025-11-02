import pygame
import sys
import time
from settings import Settings
from button import Button
from money import Money
from game_stats import GameStats
from cat_characters import GlockCat
from overlay_text import Overlay
from shop import Shop


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
        self.background = pygame.image.load("Project/images/game_bg.png").convert()
        #load elements of game
        self.money = Money(self)
        self.stats = GameStats(self)
        self.shop = Shop(self)

        #nts sprite group add glock cats to this
        self.all_sprites = pygame.sprite.Group()
        #creates first Glock Cat
        self.glock_cat = Button(self, "Glock Cat")

        #text things make cool fade yeah
        self.hover_text = None
        self.hover_start_time = 0
        self.hover_duration = 1000 #1 sec :smile:

        #creating play button AND making sure game is not running.
        self.game_active = False
        self.play_button = Button(self, "PLAY")


    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                # Update sprites
                self.all_sprites.update()
                self.shop._update_shop()
                mouse_pos = pygame.mouse.get_pos()
                self.check_hover(mouse_pos)
                if self.hover_text:
                    #https://stackoverflow.com/questions/61654510/how-to-use-pygame-time-get-ticks
                    '''I was using time.sleep here but that freezes the screen and that is no bueno'''
                    current_time = pygame.time.get_ticks()
                    if current_time - self.hover_start_time <= self.hover_duration:
                        overlay = Overlay(self, self.hover_text)
                        overlay.draw_text()
                    else:
                        self.hover_text = None  
            self._update_screen()
            self.clock.tick(60)

    
    def _check_play_button(self, mouse_pos):
        '''Start the game when user presses play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset necessary game settings/whatnot
            self.settings.start_dynamic_settings()
            ###RESET NECESSARY PARTS HERE###
            self.all_sprites.empty()
            self.game_active = True

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.game_active: #make sure game active to click buttons
                    self.check_glock_cat(mouse_pos)
                    self.check_hover(mouse_pos)
                    self.shop._checked_shop_clicked(mouse_pos)
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()


    def check_glock_cat(self, mouse_pos):
        """spawns glock cat when clicked"""
        button_clicked = self.glock_cat.rect.collidepoint(mouse_pos)
        spawn_coords = (100, 450)
        if button_clicked and self.money.amount >= 50:
            self.add_glock_cat(spawn_coords)
            self.money.spend_money(50)
        elif button_clicked:
            response = Overlay(self, "no cash hero")
            response.draw_text()
            pygame.display.flip()
            time.sleep(1)
            #self.hover_duration = pygame.time.get_ticks() # this is tech for smth else but works here :shrug:

    
    def check_hover(self, mouse_pos):
        '''see cat hp when hover over cat'''
        self.hover_text = None
        #https://stackoverflow.com/questions/41349635/how-to-detect-collision-mouse-over-between-the-mouse-and-a-sprite?
        for cats in self.all_sprites:
            if isinstance(cats, GlockCat) and cats.rect.collidepoint(mouse_pos):
                self.hover_text = f"HP: {cats.hp} Damage: {cats.damage}"
                self.hover_start_time = pygame.time.get_ticks()  
                break

    
    def add_glock_cat(self, pos):
        new_glock_cat = GlockCat(pos)
        self.all_sprites.add(new_glock_cat)

    
    def _update_screen(self):
        '''Redraw the screen each time through loop!'''
        if not self.game_active:
            self.screen.fill(self.settings.bg_start_color)
            self.play_button.draw_button()
            #changing button position~!
            self.play_button._position_button(400, 250)
        else:
            # Redraw the screen
            self.background = pygame.image.load("Project/images/game_bg.png").convert()
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.glock_cat.draw_button()
            self.money.show_money()
            self.shop.show_shop()

        #make most recent visible
        pygame.display.flip()

        


if __name__ == '__main__':
    game_object = CatWar()
    game_object.run_game()
