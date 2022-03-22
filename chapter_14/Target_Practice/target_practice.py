#### Add play button and detect collisions between bullet and target 
#### Restart game if player misses the target 3 time - hint count how many times bullet goes of screen

import sys

import pygame

from settings import Settings
from rectangle import Rectangle
from bullet import Bullet
from ship import Ship

class Target_practice:
    """Class for managing game atttributes and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        self.rectangle = Rectangle(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_rect()
            self._update_screen()

    def _check_events(self):
        """Check for keyboard or mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _fire_bullets(self):
        """Fire bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the bullet location"""
        self.bullets.update()

        # check for bullet and rectangle collisions
        if pygame.sprite.spritecollideany(self.rectangle, self.bullets):
            print("Hit rectangle!!!")

        # if bullet reaches the end of the screen, remove it
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().width:
                self.bullets.remove(bullet)

    def _update_rect(self):
        """Update the rectangle"""
        self._check_rect_edges()
        self.rectangle.update_position()

    def _check_rect_edges(self):
        """Check rectangle reached edge of screen"""
        if self.rectangle.check_edges():
            self.settings.rect_direction *= -1

    def _update_screen(self):
        """Update game screen"""
        # set background color
        self.screen.fill(self.settings.bg_color)

        self.rectangle.draw_rectangle()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # reload screen
        pygame.display.flip()

if __name__ == '__main__':
    tp_game = Target_practice()
    tp_game.run_game()