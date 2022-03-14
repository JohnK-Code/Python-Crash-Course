import pygame

from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """Class for creating a single alien"""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.screen.get_rect().width - 100
        self.rect.y = 20

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if alien reaches top or bottom of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y += (self.settings.alien_speed * self.settings.grid_direction) 
        self.rect.y = self.y