class GameStats:
    """Class representing the stats of the game."""
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.points = 0
        self.points_allowed = 0
        self.shots_attempted = 0
        self.steals = 0
        self.rebounds = 0
        self.turnovers = 0

    def record_stat(self, result, player_score, opponent_score):
        pass

    def record_player_shots(self, made):
        pass

    def record_rebounds(self):
        pass
    
    def record_steals(self):
        pass

    def record_turnovers(self):
        pass

    def display_record(self):
        pass
