#### Finished - Just need to add comments to each file explaining what code does
# Check Notes

import sys
import pygame

from settings import Settings
from raindrop import Raindrop

class RaindropGame:
    """Class used to handle game assests and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() # Initialize pygame
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # set the screen size
        pygame.display.set_caption("Steady Rain Game") # sets the caption/title for the game window

        self.raindrops = pygame.sprite.Group() # a container to hold and manage multiple sprite objects

        self._create_grid() # a helper function to define the drig of raindrops required

    def run_game(self): 
        """Start the main loop for the game"""
        while True:
            self._check_events() # helper function - Check for keyboard and mouse events
            self._update_raindrops() # helper function used to update the location of each raindrop
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
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size # assign width and height of raindrop to both variables specified
        available_space_x = self.settings.screen_width - (2 * raindrop_width) # get available space horizontally on the screen for raindrops
        
        self.number_raindrops_x = available_space_x // (2 * raindrop_width) # calculate the number of raindrops that will fit horizontally across the screen

        available_space_y = self.settings.screen_height # get available space vertically on the screen for raindrops
        number_rows = available_space_y // (2 * raindrop_height) # calculate the number of rows of raindrops that will fit the screen vertically

        for row_number in range(number_rows): # loop through each row
            self._create_row(row_number) # call helper function for defining a row - pass row number as well 

    def _create_row(self, row_number):
        """Create a row of raindrops"""
        for raindrop_number in range(self.number_raindrops_x): # loop through each raindrop in required raindrops horizontally
            self._create_raindrop(row_number, raindrop_number) # call function to create raindrop - pass both row number and raindrop number in row

    def _create_raindrop(self, row_number, raindrop_number):
        """Create raindrop"""
        raindrop = Raindrop(self) # create instance of Raindrop class
        raindrop_width, raindrop_height = raindrop.rect.size # get height and width of the rect from the Raindrop instance created above
        self.x = raindrop_width + 2 * raindrop_width * raindrop_number # get horizontal coordinates for each raindrop in row
        raindrop.rect.x = self.x # assign horizontal coordinates to Raindrop instances rectangle x attribute
        raindrop.y = 2 * raindrop_height * row_number # get vertical coordinates for each raindrop depending on its row
        raindrop.rect.y = raindrop.y # assign vertical coordinates to Raindrop instances rectangle y attribute
        self.raindrops.add(raindrop) # add Raindrop instance to pygame sprite group

    def _update_raindrops(self):
        """Make raindrop move vertically down the screen"""
        self.raindrops.update() # call update() method on all Raindrop instances in sprite group

        make_new_drop = False # set variable to false
        for raindrop in self.raindrops.copy(): # loop through all raindrop instances in sprite group copy
            if raindrop.check_disappeared(): # if method returns true, run indented code - method checks if raindrop instance is below bottom of screen
                self.raindrops.remove(raindrop) # remove raindrop instance from sprite group
                make_new_drop = True # change varible to True

        if make_new_drop: # if variable form above has been changed to true, run indented code
            self._create_row(0) # call create_row method and pass 0 as argument for row number - this makes new row appear at top of screen

    def _update_screen(self):
        """Update the screen"""
        self.screen.fill(self.settings.bg_color) # define color of main screen background
        self.raindrops.draw(self.screen) # draws all container sprite objects to the surface/main screen

        pygame.display.flip() # update the main screen/window 

if __name__ == '__main__': # if __name__ variable is equal to __main__ run indented code - this happens if module being called is the main module and not imported by another
    sr_game = RaindropGame() # create instance of Raindrop() class
    sr_game.run_game() # call method on instance created from class above 