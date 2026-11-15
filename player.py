class Player:
    """Class representing a player in the game."""
    def __init__(self, name):
        self.name = name
        self.money = 500
        self.height = 69
        self.speed = 50
        self.stamina = 50
        self.strength = 50
        self.ball_handling = 50
        self.shooting = 50
        self.rebounding = 50
        self.defending = 50
    
    def display_stats(self):
        print(f"Player name: {self.name}")
        print(f"Amount of money you have: {self.money}")
        print(f"Height in inches of {self.name}: {self.height}")
        print(f"Speed rating of {self.name}: {self.speed}")
        print(f"Stamina rating of {self.name}: {self.stamina}")
        print(f"Strength rating of {self.name}: {self.strength}")
        print(f"Ball handling rating of {self.name}: {self.ball_handling}")
        print(f"Shooting rating of {self.name}: {self.shooting}")
        print(f"Rebounding rating of {self.name}: {self.rebounding}")
        print(f"Defending rating of {self.name}: {self.defending}")

    def can_afford(self, price):
        if self.money >= price:
            return True
        else:
            return False

    def purchase_upgrade(self, stat, price, increase):
        if not self.can_afford(price):
            print("Not enough money to purchase this upgrade.")
            print(f"You currently have ${self.money}. You need ${price - self.money} more.")
            return False

        if stat == "height" and getattr(self, stat) + increase > 84:
            print("Maximum height reached.")
            return False
        
        if stat != "height" and getattr(self, stat) + increase > 100:
            print("Maximum rating reached.")
            return False

        setattr(self, stat, getattr(self, stat) + increase)
        self.money -= price

        print(f"Upgrade successful! {stat} increased by {increase}.")
        print(f"Money left: ${self.money}")

        return True
  

    def earn_money(self, amount):
        self.money += amount
        print(f"You now have ${self.money}")
    
    def lose_money(self, amount):
        self.money = max(0, self.money - amount)
        print(f"Money left: ${self.money}")