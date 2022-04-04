#### TRY IT YOURSELF - Chapter 12 - Page 253 - Sideways Shooter Settings
## Settings
class Settings:
    """A class that stores all the settings for the game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings 
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        # Alien settings 
        self.grid_left_speed = 30

        # difficulty level 
        self.difficulty = "Medium"

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        if self.difficulty == "Easy":
            self.ship_limit = 5
            self.ship_speed = 0.75
            self.bullet_speed = 1.0
            self.alien_speed = 0.5
            self.bullets_allowed = 10
            self.alien_points = 25
        elif self.difficulty == "Medium":
            self.ship_limit = 4
            self.ship_speed = 1.0
            self.bullet_speed = 1.25
            self.alien_speed = 0.6
            self.bullets_allowed = 8
            self.alien_points = 75
        elif self.difficulty == "Hard":
            self.ship_limit = 3
            self.ship_speed = 1.25
            self.bullet_speed = 1.5
            self.alien_speed = 0.7
            self.bullets_allowed = 6
            self.alien_points = 125

        
        # fleet direction of 1 represents right; -1 represents left
        self.grid_direction = 1

    def increase_speed(self):
        """Increase speed settings alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        # decrease the amount of bullets allowed as game difficulty increases
        if self.bullets_allowed >= 3:
            self.bullets_allowed -= 1