#### TRY IT YOURSELF - Chapter 13 - Page 268 - Raindrops Game
import sys, pygame

from raindrops_game_settings_13_3 import Settings
from raindrops_game_raindrop_13_3 import RainDrop

class RainDropGame:
    """Overall class to manage game behavior and assets"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")

        self.raindrops = pygame.sprite.Group()
        self._create_raindrop_grid()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self.raindrops.update()
            self._update_screen()

    def _create_raindrop_grid(self):
        """Create a row of raindrops"""
        # Create a raindrop and find the number of raindrops in a row
        # Spacing between each raindrop is equal to one raindrop width
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - raindrop_width
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen
        available_space_y = self.settings.screen_height
        number_of_rows = available_space_y // (2 * raindrop_height)

        # Create full grid of raindrops
        for row_number in range(number_of_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
            """Create raindrop and place it in the row"""
            raindrop = RainDrop(self)
            raindrop_width = raindrop.rect.width
            raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
            raindrop.y = 2 * raindrop.rect.height * row_number
            raindrop.rect.y = raindrop.y
            self.raindrops.add(raindrop)

    def _update_screen(self):
        """Update images on screen and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    rg = RainDropGame()
    rg.run_game()