import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, tp_game):
        """Initialize the ship and set its starting position"""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()

        # Load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Set ships starting position
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value of the ships horizontal position
        self.y = float(self.rect.y)

        # movement flags 
        self.move_up = False
        self.move_down = False

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the location of the ship using arrow keys"""
        if self.move_up and self.rect.y >= 0:
            self.y -= 1
            self.rect.y = self.y
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 1
            self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)