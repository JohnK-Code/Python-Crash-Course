#################### Check Notes

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # create an instance to store game statistics 
        # and create a scoreboard 
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._alien_grid()

        # Make a play button
        self.play_button = Button(self, "Play")

        self._make_difficulty_buttons()


    def _make_difficulty_buttons(self):
        """Create level difficulty buttons"""
        self.easy_button = Button(self, "Easy")
        self.easy_button.rect.top = self.play_button.rect.bottom + 10
        self.easy_button.position_msg()

        self.medium_button = Button(self, "Medium")
        self.medium_button.rect.top = self.easy_button.rect.bottom + 10
        self.medium_button.position_msg()
        self.medium_button.button_color = (0, 100, 0) # set button color - medium is the default difficulty for the game

        self.hard_button = Button(self, "Hard")
        self.hard_button.rect.top = self.medium_button.rect.bottom + 10
        self.hard_button.position_msg()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active: # check if game active
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                f = open("score.txt", "w")
                f.write(str(self.stats.high_score))
                f.close()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_level(mouse_pos)


    def _check_keydown(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            f = open("score.txt", "w")
            f.write(str(self.stats.high_score))
            f.close()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()


    def _check_keyup(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        
    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    
    def _check_difficulty_level(self, mouse_pos):
        """Check difficulty level"""
        easy = self.easy_button.rect.collidepoint(mouse_pos)
        medium = self.medium_button.rect.collidepoint(mouse_pos)
        hard = self.hard_button.rect.collidepoint(mouse_pos)

        selected = (0, 100, 0) # change button background color if selected
        not_selected = (0, 255, 0) # change button background color if not selected

        if easy:
            self.settings.difficulty = "Easy"
            self.easy_button.button_color = selected
            self.medium_button.button_color = not_selected
            self.hard_button.button_color = not_selected
        elif medium:
            self.settings.difficulty = "Medium"
            self.easy_button.button_color = not_selected
            self.medium_button.button_color = selected
            self.hard_button.button_color = not_selected
        elif hard:
            self.settings.difficulty = "Hard"
            self.easy_button.button_color = not_selected
            self.medium_button.button_color = not_selected
            self.hard_button.button_color = selected

        self.sb.prep_difficulty()


    def _start_game(self):
        # Reset the game statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._alien_grid()
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)

        # play background music
        self.background_music = pygame.mixer.Sound("sounds/background.wav")
        self.background_music.play(-1)


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet's group."""
        if len(self.bullets) < self.settings.bullets_allowed and self.stats.game_active:
            bullet_sound = pygame.mixer.Sound("sounds/shoot.wav")
            bullet_sound.play()
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

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.aliens:
            self._start_new_level()


    def _start_new_level(self):
        # destroy existing bullets and create new fleet
        self.bullets.empty()
        self._alien_grid()
        self.settings.increase_speed()

        # increase level
        self.stats.level += 1
        self.sb.prep_level()


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
        self._check_aliens_hit_left()

    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien or aliens hitting the left side of the screen"""
        if self.stats.ships_left > 0:
            # play sound if ship hit or alien reaches left wall 
            explosion = pygame.mixer.Sound("sounds/explosion.wav")
            explosion.play()

            # Decrement ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new grid of aliens and center the ship
            self._alien_grid()
            self.ship.center_ship()

            # pause game for 0.5 seconds when ship hit by alien
            sleep(0.5)
            explosion.stop()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.background_music.stop()


    def _check_aliens_hit_left(self):
        """Check if any aliens have reached the left side of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                # Treat this the same as if the shi got hit by an alien
                self._ship_hit()
                break


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


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive 
        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    ssg = SidewaysShooter()
    ssg.run_game()