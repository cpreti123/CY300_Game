class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (180, 176, 230)
        self.bg_start_color = (137, 67, 69)

        #currency settings
        self.points = 200

        #money settings
        self.start_money = 200
        self.money_time = 50 #money gained over time
        self.speed = 2

    
    def start_dynamic_settings(self):
        '''Settings that will change throughout the game.'''
