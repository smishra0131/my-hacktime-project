class Player:
    """Class representing a player in the game."""
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.height = 0
        self.speed = 50
        self.stamina = 50
        self.strength = 50
        self.shooting = 50
        self.passing = 50
        self.rebounding = 50
        self.defending = 50
    
    def display_stats(self):
        pass

    def can_afford(self, price):
        pass

    def purchase_upgrade(self, upgrade_name, price):
        pass

    def earn_money(self, amount):
        pass

    def loose_money(self, amount):
        pass