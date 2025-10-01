import pygame

class Ship:
    '''A class to manage ship'''

    def __init__(self, ai_game): #METHOD
        '''Initialize the ship and set its starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #kinda like hibox!

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for ship's exact horizontal position
        self.x = float(self.rect.x)

        #movement flags; start with ship that is NOT moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self): #METHOD
        '''Update ship's position based on movement flag'''
        #update ship's x value, not rect!
        #if both held down, will stay in mid!
        #also makes sure it does not go PAST screen edge!
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        #update rect object from self.x!!
        self.rect.x = self.x

    def blitme(self): #METHOD
        '''Draw the ship at current location'''
        self.screen.blit(self.image, self.rect)