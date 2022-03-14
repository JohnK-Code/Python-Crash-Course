class Settings:
    """Class used to store all settings for the steady raindrop game"""

    def __init__(self):
        # screen settings
        self.screen_width = 1000 # assign class atribute with value for screen width
        self.screen_height = 600 # assign class atribute with value for screen height
        self.bg_color = (230,230,230) # assign class atribute with value for screen/surface color

        # raindrop settings 
        self.raindrop_width = 25 # assign class atribute with value for raindrop surface/rect width
        self.raindrop_height = 25 # assign class atribute with value forraindrop /surface/rect height
        self.raindrop_speed = 0.5 # assign class atribute with value for raindrop speed - this is used to change the rect y value to make the raindrop move down screen