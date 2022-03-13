import pygame

from settings import Settings

class Raindrop(pygame.sprite.Sprite):
    """Class for creating a single raindrop"""

    def __init__(self, sr_game):
        """Initialize the raindrop and set its starting position"""
        super().__init__() # initialize inherited clas
        self.settings = sr_game.settings
        self.screen = sr_game.screen # assign screen attribute from RaindropGame() class in main module to screen variable

        self.image = pygame.image.load("images/raindrop.png") # get pygame to load specified image
        self.image = pygame.transform.scale(self.image, (self.settings.raindrop_width, self.settings.raindrop_height)) # change size of image loaded above
        self.rect = self.image.get_rect() # get rectangle details of the image

        self.rect.x = self.rect.width # set x coordinates of the image to the width of the image
        self.rect.y = self.rect.height # set y coordinates of the image to the height of the image

        self.y = float(self.rect.y)

    def update(self):
        """Update the position of raindrop vertically"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def check_disappeared(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False