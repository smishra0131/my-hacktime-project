class BasketballGame:
    """Class representing the game play."""
    def __init__(self, player, opponent, stats):
        self.player = player
        self.opponent = opponent
        self.stats = stats

    def start_game(self):
        pass

    def simulate_possession(self):
        pass

    def calculate_shot(self, shooter, defender):
        pass

    def determine_rebound(self):
        pass

    def update_score(self, points, scoring_player):
        pass

    def update_time(self):
        pass

    def determine_winner(self):
        pass

    def display_final_score(self):
        pass