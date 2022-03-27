class GameStats:
    """Track statistics for target practice game"""

    def __init__(self, tp_game):
        """Initialize statistics"""
        self.settings = tp_game.settings
        self.reset_stats()

        # game only plays when game_active True
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.bullets_left = self.settings.bullets_left_in_game