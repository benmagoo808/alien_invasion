class Settings():
    """ A class to store all the settings for Alien Invasion """

    def __init__(self):
        """ Initialize the games static settings """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 15
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 10

        # fleet direction of 1 represents right of -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up at level up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """ Initialize the settings that change throughout the game """
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 4

        # Fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1


    def increase_speed(self):
        """ Increases the speed settings """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale