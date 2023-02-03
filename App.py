"""interactions with end-user"""

from Game import play_game



"""interacts with user"""
print("Welcome to the Combat Arena Game!")
print("You will be facing 3 enemies in turn-based combat.")

player_name = input("Enter your name: ")

def main():
    player_name = input("Enter your name: ")
    play_game(player_name)
    print("Thanks for playing!")
if __name__ == "__main__":
    main()
