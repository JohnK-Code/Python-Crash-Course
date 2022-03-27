# Game complete :-)

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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

        self.stats = GameStats(self) # create instance to store game stats
        self.rectangle = Rectangle(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            
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
        if self.stats.game_active:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        

    def _update_bullets(self):
        """Update the bullet location and remove old bullets"""
        self.bullets.update()
        self._remove_old_bullet()
        self._check_bullet_collision()

    
    def _remove_old_bullet(self):
        """Remove bullet if it reaches the end of the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().width:
                self.bullets.remove(bullet)
                self.stats.bullets_left -= 1
                self._bullets_run_out()

    
    def _bullets_run_out(self):
        """Check if bullets have run out"""
        if self.stats.bullets_left == 0:
                    self._end_game()


    def _check_bullet_collision(self):
        """Check if bullet collides with the rect/target"""
        if pygame.sprite.spritecollideany(self.rectangle, self.bullets):
            self._end_game()


    def _update_rect(self):
        """Update the rectangle"""
        self._check_rect_edges()
        self.rectangle.update_position()


    def _check_rect_edges(self):
        """Check rectangle reached edge of screen"""
        if self.rectangle.check_edges():
            self.settings.rect_direction *= -1


    def _end_game(self):
        """End the game if bullets run out or rect hit by bullet"""
        # get rid of remaining bullets
        self.bullets.empty()

        # center the ship and relocate the rectangle in a random location
        self.ship.center_ship()
        self.rectangle.relocate_rect()

        # Pause
        sleep(0.5)

        self.stats.game_active = False
        self.stats.reset_stats()

    def _check_play_button(self, mouse_pos):
        """Starts a new game when the player clicks play"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.game_active = True


    def _update_screen(self):
        """Update game screen"""
        # set background color
        self.screen.fill(self.settings.bg_color)

        self.rectangle.draw_rectangle()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # reload screen
        pygame.display.flip()


if __name__ == '__main__':
    tp_game = Target_practice()
    tp_game.run_game()