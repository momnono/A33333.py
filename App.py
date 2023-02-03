"""interacts with user"""

from Game import play_game

def main():
    print("Welcome to the Combat Arena RPG Game!")
    print("You will be facing 3 AI-controlled enemies in turn-based combat.")

    # Get player name
    player_name = input("Enter your name: ")

    # Start the game
    play_game(player_name)

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
