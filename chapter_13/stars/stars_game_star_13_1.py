#### TRY IT YOURSELF - Chapter 13 - Page 264 - Stars Game Star
import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the grid."""

    def __init__(self, s_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = s_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)