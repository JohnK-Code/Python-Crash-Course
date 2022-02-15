#### TRY IT YOURSELF - Chapter 12 - Page 238 - Game Character
import sys
import pygame

from game_character_alien_12_2 import Alien
from game_character_settings_12_1 import Settings

class GameCharacter:
    """Overall class to manage game assets and behaviors."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Game Character")

        self.alien = Alien(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass thorugh the loop - Pass background color.
            self.screen.fill(self.settings.bg_color)
            self.alien.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    gc = GameCharacter()
    gc.run_game()