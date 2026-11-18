from player import Player
from opponent import Opponent
from game_stats import GameStats
from shop import Shop
from basketball_game import BasketballGame

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
