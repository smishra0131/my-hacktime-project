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
        print(f"Height in inches of {self.name}: {self.height} inches")
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

    def purchase_upgrade(self, choice):
        upgrades = {
            1: ("height", 50, 1),
            2: ("speed", 75, 5),
            3: ("stamina", 75, 5),
            4: ("strength", 75, 5),
            5: ("ball_handling", 75, 5),
            6: ("shooting", 100, 5),
            7: ("rebounding", 75, 5),
            8: ("defending", 75, 5)
        }

        if choice not in upgrades:
            print("Invalid choice")
            return

        stat, price, increase = upgrades[choice]
        if self.can_afford(price):
            
            if stat == "height" and getattr(self, stat) + increase > 84:
                print("Maximum height reached")
                return
            
            if stat != "height" and getattr(self, stat) + increase > 100:
                print("Maximum rating reached")
                return
            
            setattr(self, stat, getattr(self, stat) + increase)
            self.money -= price
            print(f"Upgraded {stat}")
            print(f"Money left: ${self.money}")
        else:
            print("Not enough money")
            print(f"You currently have ${self.money}. You need ${price - self.money} more")

    def earn_money(self, amount):
        self.money += amount
        print(f"You now have ${self.money}")
    
    def lose_money(self, amount):
        self.money = max(0, self.money - amount)
        print(f"Money left: ${self.money}")