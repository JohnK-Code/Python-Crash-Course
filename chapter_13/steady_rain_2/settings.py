class Settings:
    """Class used to store all settings for the steady raindrop game"""

    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # raindrop settings 
        self.raindrop_width = 25
        self.raindrop_height = 25
        self.raindrop_speed = 0.5