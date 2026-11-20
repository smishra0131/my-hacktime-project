import random

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


class Opponent:
    """Class representing the opponent in the game."""
    def __init__(self):
        self.name = "Ben Simmons"
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

    def run_shop(self, player):
        while True:
            print(f"\n You currently have ${player.money}")
            self.display_shop()
            category = input("Choose from the categories (1-2) or 3 to exit: ")

            if category == "1":
                self.display_physical_characteristics(player)
            elif category == "2":
                self.display_skills(player)
            elif category == "3":
                print("Exiting shop.")
                break
            else:
                print(f"Invalid choice. Please enter a number from 1-3.")
                continue

            choice = input("Choose and upgrade (1-4) or 5 to exit: ")
            if choice == "5":
                continue
            
            try:
                upgrade = self.purchase_upgrade(choice, category)
            except ValueError:
                print("Invalid choice. Please enter a number from 1-4.")
                continue
            
            self.confirm_purchase(upgrade, player)


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
        self.player_turnovers = 0
        self.opponent_turnovers = 0

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
        self.display_stats()
        

    def simulate_possession(self):
        self.possessions += 1
        if self.current_possession == "player":
            shooter = self.player
            defender = self.opponent
        else:
            shooter = self.opponent
            defender = self.player

        if self.determine_steal(shooter, defender):
            return

        if self.determine_turnover(shooter):
            return
        
        self.calculate_shot(shooter, defender)

    def calculate_shot_chance(self, shooter, defender):
        difference = shooter.shooting - defender.defending
        shot_chance = 0.55 + (difference * 0.008)
        shot_chance = max(0.20, min(0.85, shot_chance))
        return shot_chance
    
    def calculate_shot(self, shooter, defender):
        self.attempted_shots += 1
        if shooter == self.player:
            self.player_attempts += 1
        else:
            self.opponent_attempts += 1

        shot_chance = self.calculate_shot_chance(shooter, defender)
        shot_made = random.random() < shot_chance
        if shooter == self.player:
            self.stats.record_shot(shot_made)
        
        if shot_made:
            if shooter == self.player:
                self.player_shots += 1
                self.update_score(2, self.player)
                print(f"{self.player.name} makes the shot!")
                self.current_possession = "opponent"
            else:
                self.opponent_shots += 1
                self.update_score(2, self.opponent)
                print(f"{self.opponent.name} makes the shot!")
                self.current_possession = "player"
        else:
            self.determine_rebound(shooter, defender)

    def calculate_rebound_chance(self, player):
        height_rating = ((player.height - 60) / 24) * 100
        rating = (player.rebounding * 0.60 + height_rating * 0.25 + player.strength * 0.15)
        return rating

    def determine_rebound(self, shooter, defender):
        shooter_rating = self.calculate_rebound_chance(shooter)
        defender_rating = self.calculate_rebound_chance(defender)
        rebound_chance = 0.50 + ((defender_rating - shooter_rating) * 0.005)
        rebound_chance = max(0.15, min(0.85, rebound_chance))
        if random.random() < rebound_chance:
            rebounder = defender
        else:
            rebounder = shooter

        if rebounder == self.player:
            self.player_rebounds += 1
            self.stats.record_rebound()
            self.current_possession = "player"
            print(f"{self.player.name} gets the rebound!")
        else:
            self.opponent_rebounds += 1
            self.current_possession = "opponent"
            print(f"{self.opponent.name} gets the rebound!")
        
    def calculate_defensive_rating(self, defender):
        rating = (defender.defending * 0.60 + defender.speed * 0.40)
        return rating
    
    def determine_steal(self, shooter, defender):
        defensive_rating = self.calculate_defensive_rating(defender)
        steal_chance = 0.1 + (defensive_rating - shooter.ball_handling) * 0.003
        steal_chance = max(0.03, min(0.30, steal_chance))

        if random.random() < steal_chance:
            if defender == self.player:
                self.player_steals += 1
                self.stats.record_steal()
                self.current_possession = "player"
                print(f"{self.player.name} steals the ball!")
            else:
                self.opponent_steals += 1
                self.current_possession = "opponent"
                print(f"{self.opponent.name} steals the ball!")
            return True
        
        return False

    def calculate_turnover_chance(self, shooter):
        turnover_chance = 0.15 - (shooter.ball_handling * 0.0015)
        return turnover_chance

    def determine_turnover(self, shooter):
        turnover_chance = self.calculate_turnover_chance(shooter)

        if random.random() < turnover_chance:
            if shooter == self.player:
                self.player_turnovers += 1
                self.stats.record_turnover()
                self.current_possession = "opponent"
            else:
                self.opponent_turnovers += 1
                self.current_possession = "player"

            return True
        return False

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
        if self.player_score > self.opponent_score:
            print(f"{self.player.name} wins!")
            result = "win"
        elif self.player_score < self.opponent_score:
            print(f"{self.opponent.name} wins!")
            result = "loss"
        else:
            print("It's a tie!")
            result = "tie"
        self.stats.record_result(result, self.player_score, self.opponent_score)
    
    def display_final_score(self):
        print(f"\n ==== Final Score ====")
        print(f"{self.player.name} score: {self.player_score}")
        print(f"{self.opponent.name} score: {self.opponent_score}")

    def display_stats(self):
        print(f"\n ==== Player Stats ====")
        print(f"Player shots made: {self.player_shots}")
        print(f"Player shots attempted: {self.player_attempts}")
        print(f"Player rebounds: {self.player_rebounds}")
        print(f"Player steals: {self.player_steals}")
        print(f"Player turnovers: {self.player_turnovers}")


def main():
    user_player_name = input("Create and enter your player name: ")
    player = Player(user_player_name)
    stats = GameStats()
    shop = Shop()

    while True:
        print("\n ==== Smart Basketball ==== ")
        print("1. Start Game")
        print("2. View Player Stats")
        print("3. Visit Shop to Upgrade Player")
        print("4. Display Record")
        print("5. Leave Game")
        choice = input("Enter your choice 1-5: ")
        
        if choice == "1":
            opponent = Opponent()
            game = BasketballGame(player, opponent, stats)
            game.start_game()
            if game.player_score > game.opponent_score:
                player.earn_money(300)
            elif game.player_score < game.opponent_score:
                player.lose_money(100)
            else:
                print("It's a tie! No money earned or lost.")
        elif choice == "2":
            player.display_stats()
        elif choice == "3":
            shop.run_shop(player)
        elif choice == "4":
            stats.display_record()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 - 5.")


if __name__ == "__main__":
    main()
