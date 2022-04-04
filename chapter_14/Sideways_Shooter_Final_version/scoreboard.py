import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ss_game):
        """Initialize scorekeeping attributes"""
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # font setting for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self._prep_images()

    def _prep_images(self):
        # prepare the initial score and high score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_difficulty()

    def prep_score(self):
        """turn the score into the a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score: " + score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        rounded_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render("High Score " + high_score_str, True, self.text_color, self.settings.bg_color)

        # display the high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render("Level: " + level_str, True, self.text_color, self.settings.bg_color)

        # display the level below the score on the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ss_game)
            ship.rect.x = 100 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_difficulty(self):
        """Turn difficulty into a rendered image"""
        self.difficulty_image = self.font.render("Difficulty: " + self.settings.difficulty, True, self.text_color, self.settings.bg_color)

        # display the difficulty next to the high score
        self.difficulty_rect = self.difficulty_image.get_rect()
        self.difficulty_rect.centerx = self.screen_rect.centerx
        self.difficulty_rect.bottom = self.screen_rect.bottom - 10

    def show_score(self):
        """Draw scores, level, and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.difficulty_image, self.difficulty_rect)

    def check_high_score(self):
        """Check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()