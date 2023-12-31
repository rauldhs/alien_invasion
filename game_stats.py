class GameStats:
    """class to track game stats"""

    def __init__(self,ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1