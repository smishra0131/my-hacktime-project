class Shop:
    """Class representing the shop in the game."""
    def __init__(self):
        pass

    def display_shop(self):
        print("\n==== Shop ====")
        print("1: Physical Characteristics")
        print("2: Skills")
        print("3: Exit")

    def display_physical_characteristics(self, player):
        print("\n==== Physical Characteristics ====")
        print(f"1: Height: {player.height} inches (+1) - $50")
        print(f"2: Speed: {player.speed} rating (+5) - $75")
        print(f"3: Stamina: {player.stamina} rating (+5) - $75")
        print(f"4: Strength: {player.strength} rating (+5) - $75")

    def display_skills(self, player):
        print("\n==== Skills ====")
        print(f"1: Ball Handling: {player.ball_handling} rating (+5) - $75")
        print(f"2: Shooting: {player.shooting} rating (+5) - $100")
        print(f"3: Rebounding: {player.rebounding} rating (+5) - $75")
        print(f"4: Defending: {player.defending} rating (+5) - $75")

    def purchase_upgrade(self, choice, category):
        physical_upgrades = {
            1: ("height", 50, 1),
            2: ("speed", 75, 5),
            3: ("stamina", 75, 5),
            4: ("strength", 75, 5),
        }

        skill_upgrades = {
            1: ("ball_handling", 75, 5),
            2: ("shooting", 100, 5),
            3: ("rebounding", 75, 5),
            4: ("defending", 75, 5),
        }

        if category == "1":
            upgrade = physical_upgrades.get(int(choice))
        elif category == "2":
            upgrade = skill_upgrades.get(int(choice))
        else:
            upgrade = None

        if upgrade is None:
            print("Invalid upgrade choice. Enter a valid number from 1-4.")
            return None

        return upgrade

    def confirm_purchase(self, upgrade, player,):
        if upgrade is None:
            print("No upgrade selected.")
            return False
        
        stat, cost, increase = upgrade
        
        if player.money < cost:
            print("Not enough money to purchase this upgrade.")
            return False
        
        confirmation = input(f"Confirm purchase of stat {stat} for ${cost}? ((y)es/(n)o): ").lower()
        if confirmation == "y" or confirmation == "yes":
            success = player.purchase_upgrade(stat, cost, increase)
            return success
        else:
            print("Purchase denied.")
            return False




