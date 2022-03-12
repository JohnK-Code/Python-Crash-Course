#### TRY IT YOURSELF - Chapter 13 - Page 268 - Raindrops Game Settings

class Settings:
    """A class to store all settings for the Raindrop game."""

    def __init__(self):
        """Initialize game settings."""
        
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (200, 200, 200)

        # raindrop settings 
        self.raindrop_speed = 0.5