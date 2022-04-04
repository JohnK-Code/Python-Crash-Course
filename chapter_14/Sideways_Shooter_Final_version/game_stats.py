from os import path

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ss_game):
        """Initialize statistics"""
        self.settings = ss_game.settings
        self.reset_stats()
        
        self.game_active = False

        # High score should never be reset 
        if path.exists("score.txt"):
            with open("score.txt", "r") as file:
                self.high_score = int(file.read())
        else:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1