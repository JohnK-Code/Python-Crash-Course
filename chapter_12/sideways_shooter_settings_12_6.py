#### TRY IT YOURSELF - Chapter 12 - Page 253 - Sideways Shooter Settings
## Settings
class Settings:
    """A class that stores all the settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings 
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)