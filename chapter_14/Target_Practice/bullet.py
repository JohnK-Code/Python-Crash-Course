import pygame 

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage a bullet"""

    def __init__(self, tp_game):
        """"Initialize a bullet and set its starting position"""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color
        
        # create bullet rectangle and set starting position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = tp_game.ship.rect.midright

        # store x coordinate as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        "Update the position of the bullet on the screen"
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)