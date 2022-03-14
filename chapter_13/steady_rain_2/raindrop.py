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

        self.y = float(self.rect.y) # assign class atribute with decimal value from image rect y coordinate

    def update(self):
        """Update the position of raindrop vertically"""
        self.y += self.settings.raindrop_speed # increase the deciaml value stored in variable - later used to update image rect y value
        self.rect.y = self.y # assign variable value to the images rect y value - this makes the image move vertically down screen

    def check_disappeared(self):
        """Check image has passed bottom of main screen surface"""
        if self.rect.top > self.screen.get_rect().bottom: # if top of image rect below bottom of screen rect, run indented code
            return True # return true to calling method/function
        else:
            return False # return false to calling method/function