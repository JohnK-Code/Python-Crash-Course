import pygame

class Raindrop(pygame.sprite.Sprite):
    """Class for creating a single raindrop"""

    def __init__(self, sr_game):
        super().__init__() # initialize inherited clas
        self.screen = sr_game.screen # assign screen attribute from RaindropGame() class in main module to screen variable

        self.image = pygame.image.load("images/raindrop.png") # get pygame to load specified image
        self.image = pygame.transform.scale(self.image, (25, 25)) # change size of image loaded above
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)