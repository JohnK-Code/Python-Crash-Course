#### TRY IT YOURSELF - Chapter 12 - Page 253 - Sideways Shooter Bullet
import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ss_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ss_game.ship.rect.midright

        # Store the bullets positon as a deciaml value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen from left to right."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)