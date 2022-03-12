#### Finish adding comment to raindrop.py module

#### Continue edititng _create_grid - This method should be used to calculate the number of raindrops
#-in a row and the number of rows required to fill the screen
#### Create a new method to create the row which should call another method to create the acual raindrop

import sys
import pygame

from raindrop import Raindrop

class RaindropGame:
    """Class used to handle game assests and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() # Initialize pygame

        self.screen = pygame.display.set_mode([1000, 600]) # set the screen size
        pygame.display.set_caption("Steady Rain Game") # sets the caption/title for the game window

        self.raindrops = pygame.sprite.Group() # a container to hold and manage multiple sprite objects

        self._create_grid() # a helper function to define the drig of raindrops required

    def run_game(self): 
        """Start the main loop for the game"""
        while True:
            self._check_events() # helper function - Check for keyboard and mouse events
            self._update_screen() # helper function - update the pygame window - main surface

    def _check_events(self):
        """Check for keypresses and mouse events"""
        for event in pygame.event.get(): # loop through all pygame events
            if event.type == pygame.QUIT: # check if event type is equal to QUIT
                sys.exit() # if true exit program
            elif event.type == pygame.KEYDOWN: # check for key presses
                if event.key == pygame.K_q: # if the key pressed is 'q' run indented code
                    sys.exit() # if true exit game

    def _create_grid(self):
        """Create a grid of raindrops"""
        
        # Make a raindrop
        #raindrop = Raindrop(self) # create instance of Raindrop class
        #self.raindrops.add(raindrop) # add Raindrop instance created above to sprite object container

    def _update_screen(self):
        """Update the screen"""
        self.screen.fill((230, 230, 230)) # define color of main screen background
        self.raindrops.draw(self.screen) # draws all container sprite objects to the surface/main screen

        pygame.display.flip() # update the main screen/window 

if __name__ == '__main__': # if __name__ variable is equal to __main__ run indented code - this happens if module being called is the main module and not imported by another
    sr_game = RaindropGame() # create instance of Raindrop() class
    sr_game.run_game() # call method on instance created from class above 