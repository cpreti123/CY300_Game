import pygame
import sys
import random
from settings import Settings
from button import Button
from imagebutton import ImageButton
from money import Money
from game_stats import GameStats
from cat_characters import GlockCat, EnemyCat, PlaneCat, EnemyPlaneCat
from overlay_text import Overlay
from shop import Shop
from towers import FriendlyTower, EnemyTower
from levels import Levels
#from pygame import mixer ima do this later

#NEW !! start screen images / UI images from: https://copilot.microsoft.com/shares/DpEcTf5AwJ17rPQWSLjZR & reminded me how to image transparency


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
        self.levels = Levels(self)

        #nts sprite group add glock cats to this
        self.all_sprites = pygame.sprite.Group()

        #tower group
        self.friendly_tower = pygame.sprite.Group()
        self.enemy_tower = pygame.sprite.Group()


        #creates first Glock Cat Button
        self.glock_cat_button = ImageButton(self, "Project/images/glock_cat_icon.png", pos=(300, 500))

        #creates first biplane cat button
        self.plane_cat_button = ImageButton(self, "Project/images/biplane_cat.png", pos=(475, 495))

        self.glock_cat = None
        self.plane_cat = None


        #text things make cool fade yeah
        self.hover_text = None
        self.hover_start_time = 0
        self.hover_duration = 1000 #1 sec :smile:

        #no cash overlay
        self.no_cash_showing = False
        self.no_cash_start = 0
        self.no_cash_duration = 1000  # 1 second

        #health overlay
        self.health_showing = False
        self.health_showing_start = 0
        self.health_showing_duration = 1000

        #creating play button AND making sure game is not running.
        self.game_active = False
        self.play_button = ImageButton(self, "Project/images/play_button.png", pos=(10, 0))

        #initialize money update-system
        self.money.update_money()

        #setting init
        self.settings = Settings()


    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                # Update sprites
                self.all_sprites.update()
                self.friendly_tower.update()
                self.enemy_tower.update()
                self.shop._update_shop()
                mouse_pos = pygame.mouse.get_pos()
                self.check_hover(mouse_pos)
                self.sprite_movement()
                #self.tower_handle()
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
            #i added this here because im sure we are going to want to reset it but also it makes sense to spawn it on game start :)
            self.friendly_tower.empty()
            self.enemy_tower.empty()
            self.spawn_friendly_tower()
            self.spawn_enemy_tower()
            self.game_active = True
            self.levels.levels_active = True


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.game_active: #make sure game active to click buttons
                    self.check_glock_cat(mouse_pos)
                    self.check_plane_cat(mouse_pos)
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
        if event.key == pygame.K_o:
            self.spawn_enemy_plane()
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

    def check_plane_cat(self, mouse_pos):
        """spawns plane cat when clicked"""
        button_clicked = self.plane_cat_button.rect.collidepoint(mouse_pos)
        spawn_y = random.randint(100, 200) 
        spawn_coords = (100, spawn_y)
        if button_clicked and self.money.amount >= 100 and self.shop.plane_cat_purchased:
            self.add_plane_cat(spawn_coords)
            self.money.spend_money(100)
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
                #self.hover_text = f"HP: {cats.hp} Damage: {cats.damage}"
                #self.hover_start_time = pygame.time.get_ticks()  
                self.update_health(True, cats.hp, self.settings.max_glock_hp)
                break
            else:
                self.health_showing = False

    
    def add_glock_cat(self, pos):
        self.glock_cat = GlockCat(pos)
        self.all_sprites.add(self.glock_cat)

    def add_plane_cat(self, pos):
        self.plane_cat = PlaneCat(pos)
        self.all_sprites.add(self.plane_cat)


    def spawn_enemy(self):
        y_pos = random.randint(400, 550)  #i gotta mess w/ this range but its cool not having them all ontop of eachother
        enemy = EnemyCat((self.settings.screen_width, y_pos))
        self.all_sprites.add(enemy)

    
    def spawn_enemy_plane(self):
        y_pos = random.randint(100, 200) 
        enemy = EnemyPlaneCat((self.settings.screen_width, y_pos))
        self.all_sprites.add(enemy)


    def spawn_friendly_tower(self):
        friendly_tower = FriendlyTower((50, 450))
        self.friendly_tower.add(friendly_tower)

    
    def spawn_enemy_tower(self):
        enemy_tower = EnemyTower((850, 450))
        self.enemy_tower.add(enemy_tower)


    def sprite_movement(self): #Copilot helped here!
        '''ik this says movement but its also combat''' #its ez to stop them then fight this way
        #https://stackoverflow.com/questions/56210758/how-to-create-narrow-collision-detection-between-a-players-melee-weapon-and-an
        #https://coderslegacy.com/python/pygame-rpg-enemy-ranged-attacks/
        #https://stackoverflow.com/questions/66624936/pygame-i-want-to-calculate-the-distance-between-the-player-sprite-and-enemy1
        #NEW https://realpython.com/what-does-isinstance-do-in-python/
        for cat in self.all_sprites:
            if not cat._alive:
                continue
            move = True
            ###Copilot helped with creating both of these 'isinstance' blocks.
            if isinstance(cat, GlockCat) or isinstance(cat, PlaneCat):
                for enemy in self.all_sprites:
                    if (isinstance(enemy, EnemyCat) or isinstance(enemy, EnemyPlaneCat)) and enemy._alive:
                        dx = enemy.rect.centerx - cat.rect.centerx
                        dy = enemy.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5


                        if isinstance(cat, PlaneCat) and distance < 300:
                            cat.attack(enemy)
                            move = False
                            break


                        elif distance <= self.settings.stop_range:
                            cat.attack(enemy)
                            move = False
                            break


                for towers in self.enemy_tower:
                    if (isinstance(towers, EnemyTower)) and towers._alive:
                        dx = towers.rect.centerx - cat.rect.centerx
                        dy = towers.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5
                        if distance <= self.settings.tower_stop_range:
                            cat.attack(towers)
                            towers.attack(cat)
                            move = False
                            break
                if move:
                    cat.rect.x += self.settings.speed 
            elif isinstance(cat, EnemyCat) or isinstance(cat, EnemyPlaneCat):
                for friendly in self.all_sprites:
                    #group before check alive
                    if (isinstance(friendly, GlockCat) or isinstance(friendly, PlaneCat)) and friendly._alive:
                        dx = friendly.rect.centerx - cat.rect.centerx
                        dy = friendly.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5


                        if isinstance(cat, EnemyPlaneCat) and distance < 300:
                            cat.attack(friendly)
                            move = False
                            break


                        elif distance <= self.settings.stop_range:
                            cat.attack(friendly)
                            move = False
                            break


                for towers in self.friendly_tower:
                    if (isinstance(towers, FriendlyTower)) and towers._alive:
                        dx = towers.rect.centerx - cat.rect.centerx
                        dy = towers.rect.centery - cat.rect.centery
                        distance = (dx**2 + dy**2)**0.5
                        if distance <= self.settings.tower_stop_range:
                            cat.attack(towers)
                            towers.attack(cat)
                            move = False
                            break
                if move:
                    cat.rect.x -= self.settings.speed  # Move left
                    #via testing 100 is a good stop point for glock cats
    

    def update_health(self, toggle:bool, hp:int, max_hp:int):
        '''Updates health.'''
        if toggle:
            self.health_showing = True
        if self.health_showing:
            self.hp = hp
            self.max_hp = max_hp
        

    def _update_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        '''Redraw the screen each time through loop!'''
        if not self.game_active:
            #self.screen.fill(self.settings.bg_start_color)
            self.inactive_background = pygame.image.load("Project/images/InactiveBG.png").convert()
            self.screen.blit(self.inactive_background, (0, 0))
            if self.play_button.rect.collidepoint(mouse_pos):
                self.play_button.image = pygame.image.load("Project/images/play_button_hovered.png").convert_alpha()
            else:
                self.play_button.image = pygame.image.load("Project/images/play_button.png").convert_alpha()
            self.play_button.draw_button()
            #changing button position~!
            self.play_button._position_button(325, 230)
        else:
            # Redraw the screen
            self.background = pygame.image.load("Project/images/game_bg.png").convert()
            #self.ui = pygame.image.load("Project/images/test_ui.png").convert_alpha() # to be worked with
            self.screen.blit(self.background, (0, 0)) #Used Copilot for this line here!
            #self.screen.blit(self.ui, (0, 0)) tbww
            self.all_sprites.draw(self.screen)
            self.friendly_tower.draw(self.screen)
            self.enemy_tower.draw(self.screen)
            self.glock_cat_button.draw_button()
            self.plane_cat_button.draw_button()
            self.money.show_money()
            self.shop.show_shop()
            self.levels.show_levels()


            # draw "No cash hero" overlay if needed
            if self.no_cash_showing:
                overlay = Overlay(self, "No cash hero")
                overlay.draw_text()
                current_time = pygame.time.get_ticks()
                if current_time - self.no_cash_start >= self.no_cash_duration:
                    self.no_cash_showing = False
            #call for updating health bar
            if self.health_showing:
                overlay = Overlay(self, "HEALTH")
                overlay.draw_health(self.hp, self.max_hp)
                current_time = pygame.time.get_ticks()
                if current_time - self.health_showing_start >= self.health_showing_duration:
                    self.health_showing = False
        #make most recent visible
        pygame.display.flip()

        
#buff talon
#nerf jax
if __name__ == '__main__':
    game_object = CatWar()
    game_object.run_game()
