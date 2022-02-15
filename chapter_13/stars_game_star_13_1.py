#### TRY IT YOURSELF - Chapter 13 - Page 264 - Stars Game Star
import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the grid."""

    def __init__(self, s_game):
        