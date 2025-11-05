class Settings:
    """Class for storing settings for game."""

    def __init__(self):
        """Initialize settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (180, 176, 230)
        self.bg_start_color = (137, 67, 69)

        #currency settings
        self.points = 150

        #money settings
        self.start_money = 150
        self.money_time = 50 #money gained over time

    
    def start_dynamic_settings(self):
        '''Settings that will change throughout the game.'''
        #empty rn; will update time permitting
