#### TRY IT YOURSELF - Chapter 12 - Page 246 - Rocket Settings
class Settings:
    """A class to store all settings for the Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings 
        self.ship_speed = 1.5