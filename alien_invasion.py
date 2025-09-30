import sys
import pygame

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.clock = pygame.time.Clock() #setting up framerate
        self.screen = pygame.display.set_mode((1200,800)) #dims of window (pix)
        pygame.display.set_caption("Alien Invasion")

        #set background color!
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            #Watch for keyboard and mouse events!
            for event in pygame.event.get(): #event loop (listens...)
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through loop
            self.screen.fill(self.bg_color) #fills background with color

            #Make the most recently drawn screen visible!
            pygame.display.flip()
            self.clock.tick(60)#frame rate is arg here!

if __name__ == '__main__':
    #make game instance, run game!
    ai = AlienInvasion()
    ai.run_game()