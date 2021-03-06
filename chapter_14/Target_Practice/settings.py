class Settings:
    """Class for handling all settings for Target Practice game"""

    def __init__(self):
        """Initialize the game's settings"""
        # screen settings 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # rectangle target settings 
        self.rect_width = 80
        self.rect_height = 80
        self.rectangle_color = (255, 255, 0)
        self.speed = 0.5
        self.rect_direction = 1

        # bullet settings
        self.bullet_width = 20
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1
        self.bullets_left_in_game = 3