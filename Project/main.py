import pygame
import sys
import random
from settings import Settings
from button import Button
from imagebutton import ImageButton
from money import Money
from game_stats import GameStats
from cat_characters import GlockCat, EnemyCat
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
        #Used Copilot for downloading background (needed 'convert()')
        self.background = pygame.image.load("Project/images/game_bg.png").convert()
        #load elements of game
        self.money = Money(self)
        self.stats = GameStats(self)
        self.shop = Shop(self)

        #nts sprite group add glock cats to this
        self.all_sprites = pygame.sprite.Group()
        #creates first Glock Cat Button
        self.glock_cat_button = ImageButton(self, "Project/images/glock_cat_icon.png", pos=(300, 500))

        #creates first biplane cat button
        self.plane_cat_button = ImageButton(self, "Project/images/biplane_cat.png", pos=(475, 495))

        self.glock_cat = None

        #text things make cool fade yeah
        self.hover_text = None
        self.hover_start_time = 0
        self.hover_duration = 1000 #1 sec :smile:

        #no cash overlay
        self.no_cash_showing = False
        self.no_cash_start = 0
        self.no_cash_duration = 1000  # 1 second

        #creating play button AND making sure game is not running.
        self.game_active = False
        self.play_button = Button(self, "PLAY")

        #initialize money update-system
        self.money.update_money()


    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                # Update sprites
                self.all_sprites.update()
                self.shop._update_shop()
                mouse_pos = pygame.mouse.get_pos()
                self.check_hover(mouse_pos)
                self.sprite_movement()
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
                    self.shop._check_clicked(mouse_pos)
                self._check_play_button(mouse_pos)
            elif event.type == self.money.timer:
                #https://runebook.dev/en/articles/pygame/ref/time/pygame.time.set_timer
                self.money.update_money()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_p:
            self.spawn_enemy()
            #here so I can spawn enemy cats for testing
            

    def check_glock_cat(self, mouse_pos):
        """spawns glock cat when clicked"""
        button_clicked = self.glock_cat_button.rect.collidepoint(mouse_pos)
        spawn_y = random.randint(400, 550) 
        spawn_coords = (100, spawn_y)
        if button_clicked and self.money.amount >= 50:
            self.add_glock_cat(spawn_coords)
            self.money.spend_money(50)
        elif button_clicked:
            self.no_cash_showing = True
            self.no_cash_start = pygame.time.get_ticks()



    #not a fan of this rn will rewrite later
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
        self.glock_cat = GlockCat(pos)
        self.all_sprites.add(self.glock_cat)


    def spawn_enemy(self):
        y_pos = random.randint(400, 550)  #i gotta mess w/ this range but its cool not having them all ontop of eachother
        enemy = EnemyCat((self.settings.screen_width, y_pos))
        self.all_sprites.add(enemy)



    def sprite_movement(self):
        '''ik this says movement but its also combat''' #its ez to stop them then fight this way
        #https://stackoverflow.com/questions/56210758/how-to-create-narrow-collision-detection-between-a-players-melee-weapon-and-an
        #https://coderslegacy.com/python/pygame-rpg-enemy-ranged-attacks/
        #https://stackoverflow.com/questions/66624936/pygame-i-want-to-calculate-the-distance-between-the-player-sprite-and-enemy1
        for cat in self.all_sprites:
            if not cat._alive:
                continue
            move = True
            stop_range = 100
            ###Copilot helped with creating both of these 'isinstance' blocks.
            if isinstance(cat, GlockCat):
                for enemy in self.all_sprites:
                    if isinstance(enemy, EnemyCat) and enemy._alive:
                        dx = enemy.rect.centerx - cat.rect.centerx
                        dy = enemy.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5
                        if distance <= stop_range:
                            cat.attack(enemy)
                            move = False
                            break
                if move:
                    cat.rect.x += 1  
            elif isinstance(cat, EnemyCat): #This one too!
                for friendly in self.all_sprites:
                    if isinstance(friendly, GlockCat) and friendly._alive:
                        dx = friendly.rect.centerx - cat.rect.centerx
                        dy = friendly.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5
                        if distance <= stop_range:
                            cat.attack(friendly)
                            move = False
                            break
                if move:
                    cat.rect.x -= 1  # Move left
                    #via testing 100 is a good stop point for glock cats


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
            self.screen.blit(self.background, (0, 0)) #Used Copilot for this line here!
            self.all_sprites.draw(self.screen)
            self.glock_cat_button.draw_button()
            self.plane_cat_button.draw_button()
            self.money.show_money()
            self.shop.show_shop()

            # draw "No cash hero" overlay if needed
            if self.no_cash_showing:
                overlay = Overlay(self, "No cash hero")
                overlay.draw_text()
                current_time = pygame.time.get_ticks()
                if current_time - self.no_cash_start >= self.no_cash_duration:
                    self.no_cash_showing = False

        #make most recent visible
        pygame.display.flip()

        


if __name__ == '__main__':
    game_object = CatWar()
    game_object.run_game()
