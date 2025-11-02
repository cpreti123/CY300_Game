class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (180, 176, 230)
        self.bg_start_color = (137, 67, 69)

    
    def start_dynamic_settings(self):
        '''Settings that will change throughout the game.'''
