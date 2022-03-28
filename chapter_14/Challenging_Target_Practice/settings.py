class Settings:
    """Class for handling all settings for Target Practice game"""

    def __init__(self):
        """Initialize the game's static settings"""
        # screen settings 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # rectangle target settings 
        self.rect_width = 80
        self.rect_height = 80
        self.rectangle_color = (255, 255, 0)

        # bullet settings
        self.bullet_width = 20
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_left_in_game = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change throught the game"""
        self.rect_speed = 0.5
        self.bullet_speed = 1

        # rect direction of 1 represents moving down; -1 represents moving up
        self.rect_direction = 1

    def increase_speed(self):
        "Increase speed settings"
        self.rect_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale