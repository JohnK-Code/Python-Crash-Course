#### TRY IT YOURSELF - Chapter 12 - Page 246 - Keys
import sys
import pygame

class Keys:
    """Overall class for the game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Key Game")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    else:
                        print(event.key)
                
            # Make the most recently drawn screen visible.
            self.screen.fill((40, 160, 200))
            pygame.display.flip()

if __name__ == '__main__':
    kg = Keys()
    kg.run_game()