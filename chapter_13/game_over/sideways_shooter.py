#### TRY IT YOURSELF - Chapter 12 - Page 253 - Sideways Shooter
import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""


    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideway Shooter")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._alien_grid()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)


    def _check_keydown(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet's group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().width:
                self.bullets.remove(bullet)

        self._check_bullets_aliens_collisions()

        
    def _check_bullets_aliens_collisions(self):
        """Respond to bulle-alien collisions"""
        # remove any bullets or aliens that have collided with each other
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # if no aliens left, delete all remaining bullets and start a new alien grid
        if not self.aliens:
            self.bullets.empty()
            self._alien_grid()


    def _alien_grid(self):
        """Create a grid of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width - ship_width - (4 * alien_width))
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - alien_height
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

        
    def _create_alien(self, alien_number, row):
        """Create alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien.rect.x - 2 * alien_width * alien_number
        alien.y = alien.rect.y + 2 * alien_height * row
        alien.rect.y = alien.y

        self.aliens.add(alien)


    def _update_aliens(self):
        """
        Check if grid is at top or bottom of screen, then 
        update the location of all aliens
        """
        self._check_grid_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the left side of the screen
        self._check_aliens_hit_left_wall()


    def _check_grid_edges(self):
        """Respond appropriately if alien reaches an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_grid_direction()
                break


    def _change_grid_direction(self):
        """move entire grid of aliens closer to the ship and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.grid_left_speed
        self.settings.grid_direction *= -1


    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left 
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._alien_grid()
            self.ship.center_ship()

            # Pause 
            sleep(0.5)
        else:
            self.stats.game_active = False


    def _check_aliens_hit_left_wall(self):
        """Check if aliens have hit the left side of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    ssg = SidewaysShooter()
    ssg.run_game()