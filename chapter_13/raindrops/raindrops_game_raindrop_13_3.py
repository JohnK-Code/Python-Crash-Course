#### TRY IT YOURSELF - Chapter 13 - Page 268 - Raindrops Game Raindrop
import pygame 
from pygame.sprite import Sprite

class RainDrop(Sprite):
    """A class representing a single raindrop in the grid"""

    def __init__(self, r_game):
        """Initialize the raindrop and set it's starting position."""
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings

        self.image = pygame.image.load('images/raindrop.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y