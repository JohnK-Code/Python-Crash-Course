#### TRY IT YOURSELF - Chapter 12 - Page 238 - Game Character
## Alien image class
import pygame

class Alien:
    """Class to manage the alien."""

    def __init__(self, gc_game):
        """Initialize the alien and its starting position."""
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()

        # Load the alien image and get it's rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the alien at it's current location"""
        self.screen.blit(self.image, self.rect)