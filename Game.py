"""resposable for game mechanics"""

import random

def play_game():
    player1 = create_player("Paladin")
    player2 = create_player("Necromancer")

    while True:
        player1_attack = player_attack(player1["speed"])
        player2_defense = player_defense(player2["defense"])
        player2["health"] -= max(0, player1_attack - player2_defense)

        if player2["health"] <= 0:
            return f"{player1['name']} wins!"

        player2_attack = player_attack(player2["speed"])
        player1_defense = player_defense(player1["defense"])
        player1["health"] -= max(0, player2_attack - player1_defense)

        if player1["health"] <= 0:
            return f"{player2['name']} wins!"

def create_player(role):
    player = {
        "name": role,
        "speed": random.randint(1, 6),
        "defense": random.randint(1, 6),
        "health": 20,
    }
    return player

def player_attack(speed):
    return speed + random.randint(1, 12)

def player_defense(defense):
    return defense + random.randint(1, 12)
