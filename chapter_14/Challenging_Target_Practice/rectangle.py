import pygame
import random

class Rectangle:
    """A class to manage the rectangle being shot at"""

    def __init__(self, tg_game):
        """Initialize the rectangle and it's starting position"""
        self.screen = tg_game.screen
        self.settings = tg_game.settings
        self.screen_rect = tg_game.screen.get_rect()

        # Create rectangle and set position
        self.rect = pygame.Rect((self.screen.get_width() - self.settings.rect_width - 10), 10, self.settings.rect_width, self.settings.rect_height)

        self.y = float(self.rect.y)

    def draw_rectangle(self):
        """Draw the rectangle to the screen"""
        pygame.draw.rect(self.screen, self.settings.rectangle_color, self.rect)

    def check_edges(self):
        """Check if rectangle has reached the top or bottom of the screen"""
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            return True

    def update_position(self):
        """Move rectangle up and down the screen"""
        self.y += (self.settings.rect_speed * self.settings.rect_direction)
        self.rect.y = self.y

    def relocate_rect(self):
        """Relocate the rect to a random position on the right side of the screen"""
        self.y = random.randint(2, self.settings.screen_height - self.settings.rect_height)
        self.rect.y = self.y