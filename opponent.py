import random
class Opponent:
    """Class representing the opponent in the game."""
    def __init__(self):
        self.random_characteristics()

    def random_characteristics(self):
        self.height = random.randint(60, 84)
        self.speed = random.randint(45, 75)
        self.stamina = random.randint(45, 75)
        self.strength = random.randint(45, 75)
        self.ball_handling = random.randint(45, 75)
        self.shooting = random.randint(45, 75)
        self.rebounding = random.randint(45, 75)
        self.defending = random.randint(45, 75)

    def display_stats(self):
        print(f"Height: {self.height} inches")
        print(f"Speed rating: {self.speed}")
        print(f"Stamina rating: {self.stamina}")
        print(f"Strength rating: {self.strength}")
        print(f"Ball handling rating: {self.ball_handling}")
        print(f"Shooting rating: {self.shooting}")
        print(f"Rebounding rating: {self.rebounding}")
        print(f"Defending rating: {self.defending}")