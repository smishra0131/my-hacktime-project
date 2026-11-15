import random
class BasketballGame:
    """Class representing the game play."""
    def __init__(self, player, opponent, stats):
        self.player = player
        self.opponent = opponent
        self.stats = stats
        self.time = 0
        self.player_score = 0
        self.opponent_score = 0
        self.possessions = 0
        self.current_possession = "player"
        self.player_rebounds = 0
        self.opponent_rebounds = 0
        self.player_steals = 0
        self.opponent_steals = 0
        self.player_shots = 0
        self.opponent_shots = 0
        self.attempted_shots = 0
        self.player_attempts = 0
        self.opponent_attempts = 0

    def start_game(self):
        print(f"Game starting between {self.player.name} and {self.opponent.name}")
        self.time = random.randint(15, 20)
        self.player_score = 0
        self.opponent_score = 0
        self.current_possession = random.choice(["player", "opponent"])
        while self.time > 0:
            self.simulate_possession()
            self.update_time()
        
        print("Game over!")
        self.display_final_score()
        self.determine_winner()
        

    def simulate_possession(self):
        if self.current_possession == "player":
            shooter = self.player
            defender = self.opponent
        else:
            shooter = self.opponent
            defender = self.player
        self.calculate_shot(shooter, defender)

    def calculate_shot(self, shooter, defender):
        self.attempted_shots += 1
        if shooter == self.player:
            self.player_attempts += 1
        else:
            self.opponent_attempts += 1
        
        if shooter == self.player:
            if self.player.shooting > self.opponent.defending:
                shot_chance = (self.player.shooting - self.opponent.defending) * 0.1
        
        if random.random() < shot_chance:
            if shooter == self.player:
                self.player_shots += 1
                self.update_score(2, self.player)
                self.current_possession = "opponent"
            else:
                self.opponent_shots += 1
                self.update_score(2, self.opponent)
                self.current_possession = "player"
        else:
            self.determine_rebound(shooter, defender)


    def determine_rebound(self, shooter, defender):
        rebound_chance = 0.6
        
        if random.random() < rebound_chance:
            rebounder = defender
        else:
            rebounder = shooter
            
        if rebounder == self.player:
            self.player_rebounds += 1
            self.current_possession = "player"
        else:
            self.opponent_rebounds += 1
            self.current_possession = "opponent"
        

    def update_score(self, points, scoring_player):
        if scoring_player == self.player:
            self.player_score += points
        else:
            self.opponent_score += points

    def update_time(self):
        self.time -= 1
        print(f"Time remaining: {self.time}")
        if self.time <= 0:
            print("Time's up!")

    def determine_winner(self):
        print(f"Player score: {self.player_score}")
        print(f"Opponent score: {self.opponent_score}")
        if self.player_score > self.opponent_score:
            print(f"{self.player.name} wins!")
        elif self.player_score < self.opponent_score:
            print(f"{self.opponent.name} wins!")
        else:
            print("It's a tie!")

    def display_final_score(self):
        print(f"\n ==== Final Score ====")
        print(f"Player score: {self.player_score}")
        print(f"Opponent score: {self.opponent_score}")
    