class GameStats:
    """Track money for SW."""

    def __init__(self, sw_game):
        """Initialize statistics."""
        self.settings = sw_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize money that can change during the game."""
        self.money = 100