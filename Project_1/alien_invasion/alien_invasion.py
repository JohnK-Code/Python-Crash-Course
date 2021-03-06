#### Check Notes!!!!!!!!!!!

import sys
from time import sleep

import pygame 

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from level_button import Level_button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings() # create Settings() instance

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # create screen/surface/window
        self.settings.screen_width = self.screen.get_rect().width # get the screen width and assign it to the screen_width attribute in the settings.py module
        self.settings.screen_height = self.screen.get_rect().height # get the screen height and assign it to the screen_height attribute in the settings.py module
        pygame.display.set_caption("Alien Invasion") # assign a caption to the game window

        self.stats = GameStats(self) # create GameStats() instance 
        self.sb = Scoreboard(self) # create Scoreboard instance
        self.ship = Ship(self) # create ship instance

        self.bullets = pygame.sprite.Group() # create sprite group for bullets
        self.aliens = pygame.sprite.Group() # create sprite group for aliens

        self._create_fleet() # call helper method to create fleet of aliens

        self.play_button = Button(self, "Play") # create a Button() instance and pass 'Play' as the messsage to be displayed

        self.L1 = Level_button(self, self.play_button.x + 50, self.play_button.y + 60, "Easy") # create Level_button instance and pass all the required arguments/parameters
        self.L2 = Level_button(self, self.play_button.x + 50, self.L1.y + 110, "Medium") # create Level_button instance and pass all the required arguments/parameters
        self.L3 = Level_button(self, self.play_button.x + 50, self.L2.y + 110, "Hard") # create Level_button instance and pass all the required arguments/parameters

    def run_game(self):
        """Start the main loop for the game."""
        while True: # run indented code while True
            self._check_events() # call helper method - checks for keyboard and mouse events 

            if self.stats.game_active: # game_stats.py attribute is set to True, run indented code
                self.ship.update() # call update() method on ship instance - update() method used to update the ships location
                self._update_bullets() # call helper method _update_bullets() - used to update bullet location, check for collisions and remove old bullets
                self._update_aliens() # call helper method _update_aliens - used to update alien position and check for collisions

            self._update_screen() # call helper method - used to update game screen/window

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get(): # loop through pygame events
            if event.type == pygame.QUIT: # if event equals QUIT, run indented code
                f = open("score.txt", "w") # open file for writing
                f.write(self.stats.high_score) # write string to open file - writes game_stats attribute highscore to file
                f.close() # close file 
                sys.exit() # exit interpreter 
            elif event.type == pygame.KEYDOWN: # if pygame event equals KEYDOWN, run indented code 
                self._check_keydown_events(event) # call helper function and pass event variable from for loop 
            elif event.type == pygame.KEYUP: # if pygame event equals KEYUP, run indented code 
                self._check_keyup_events(event) # call helper function and pass event variable from for loop
            elif event.type == pygame.MOUSEBUTTONDOWN: # if pygame event equals MOUSEBUTTONDOWN, run indented code 
                mouse_pos = pygame.mouse.get_pos() # get mouse position when clicked
                self._check_button_clicked(mouse_pos) # call helper function and pass mouse position

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            f = open("score.txt", "w")
            f.write(str(self.stats.high_score))
            f.close()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_button_clicked(self, mouse_pos):
        """Start a new game when the player clicks play"""
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        L1_button_clicked = self.L1.rect.collidepoint(mouse_pos)
        L2_button_clicked = self.L2.rect.collidepoint(mouse_pos)
        L3_button_clicked = self.L3.rect.collidepoint(mouse_pos)
        if play_button_clicked and not self.stats.game_active:
            self._start_game()
        elif L1_button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.pick_game_speed(1.2)
        elif L2_button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.pick_game_speed(1.3)
        elif L3_button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.pick_game_speed(1.4)

    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets 
        self.aliens.empty()
        self.bullets.empty()

        # create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)

        # Play background music
        self.background_sound = pygame.mixer.Sound("sounds/background.wav")
        self.background_sound.set_volume(0.5)
        self.background_sound.play(-1)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            bullet_sound = pygame.mixer.Sound("sounds/shoot.wav")
            bullet_sound.set_volume(0.2)
            bullet_sound.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet) 

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

            self._start_new_level()

    def _start_new_level(self):
        """Star a new level"""
        if not self.aliens:
            # Detroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """
           Check if the fleet is at the edge,
           then update the position of all the aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respind appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Play sound for ship getting hit 
            self.explosion = pygame.mixer.Sound("sounds/explosion.wav")
            self.explosion.play()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.background_sound.stop()
            self.explosion.play()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw buttons if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.L1.draw_level_button()
            self.L2.draw_level_button()
            self.L3.draw_level_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()