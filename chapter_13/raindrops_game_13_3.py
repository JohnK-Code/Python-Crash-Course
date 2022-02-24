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
        self._create_raindrop()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

            self._update_screen()

    def _create_raindrop(self):
        """Create a raindrop"""
        raindrop = RainDrop(self)
        self.raindrops.add(raindrop)

    def _update_screen(self):
        """Update images on screen and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    rg = RainDropGame()
    rg.run_game()