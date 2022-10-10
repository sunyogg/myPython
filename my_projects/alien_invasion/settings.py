
class Settings:
    """A class to store all settings of Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # screen settings
        self.screen_width = 1250
        self.screen_height =730
        self.bg_color = (230, 230, 230)
        # ship settings
        
        self.ship_limit = 3

        # bullet settings
        
        self.bullet_width = 3.5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        # alien settings
        
        self.fleet_drop_speed = 10

        # How quickly the game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize game settings that throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 5
        self.alien_speed = 1
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # scoring
        self.alien_points = 5
        # How quickly the alien point value increases
        self.score_scale = 1.5


    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points =  int(self.alien_points * self.score_scale)
