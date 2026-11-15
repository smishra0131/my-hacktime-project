class GameStats:
    """Class representing the stats of the game."""
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.points_scored = 0
        self.points_allowed = 0
        self.shots_attempted = 0
        self.shots_made = 0
        self.steals = 0
        self.rebounds = 0
        self.turnovers = 0

    def record_result(self, result, player_score, opponent_score):
        self.points_scored += player_score
        self.points_allowed += opponent_score
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        elif result == "tie":
            self.ties += 1
        

    def record_shot(self, made):
        self.shots_attempted += 1
        if made:
            self.shots_made += 1

    def record_rebound(self):
        self.rebounds += 1
    
    def record_steal(self):
        self.steals += 1

    def record_turnover(self):
        self.turnovers += 1

    def display_record(self):
        print(f"You have {self.wins} win(s), {self.losses} loss(es), and {self.ties} tie(s).")
        print(f"You scored {self.points_scored} point(s) and allowed {self.points_allowed} point(s).")
        print(f"You made {self.shots_made} out of {self.shots_attempted} shot(s).")
        print(f"You got {self.rebounds} rebound(s), {self.steals} steal(s), and {self.turnovers} turnover(s).")