#### TRY IT YOURSELF - Chapter 13 - Page 264 - Stars Game
import sys, pygame

from random import randint
from stars_game_settings_13_1 import Settings
from stars_game_star_13_1 import Star

class StarGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.stars = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars Game")

        self._create_grid()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen through each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.stars.draw(self.screen)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _create_grid(self):
        """Create a grid of stars."""
        # Create a star and find the number of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        available_space_y = (self.settings.screen_height - (2 * star_height))
        number_rows = available_space_y // (2 * star_height)

        # Create a full grid of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number

########### Random stars - Added for exercise 13-2 (Better stars) #######################
        star.rect.x += randint(-10, 10)
        star.rect.y += randint(-10, 10)
        self.stars.add(star)

if __name__ == '__main__':
    # Make a game instance, and run game.
    sg = StarGame()
    sg.run_game()