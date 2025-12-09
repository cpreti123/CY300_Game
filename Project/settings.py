class Settings:
    """Class for storing settings for game."""

    def __init__(self):
        """Initialize settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (180, 176, 230)
        #self.bg_start_color = (137, 67, 69)
        self.bg_start_image = "Project/images/InactiveBG.png"
        self.bg_start_color2 = (150, 200, 20)

        #currency settings
        self.gems = 0

        #money settings
        self.start_money = 150
        self.money_time = 50 #money gained over time
        self.speed = 1

        #attack stuff
        self.stop_range = 100
        self.tower_stop_range = 200
        self.plane_stop_range = 400

        #health stuff
        self.max_glock_hp = 100
        #self.health_x = 400
        #self.health_y = 250

        #levels stuff
        self.start_level = 1

    
    def start_dynamic_settings(self):
        '''Settings that will change throughout the game.'''
        #empty rn; will update time permitting
        self.level_increment = 1
    