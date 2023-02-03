"""resposable for game mechanics"""
import Role1
import Role2
def play_game(player_name):
    speed = 10
    defense = 20
    magic = 15

    role = input("Enter '1' to play as Paladin or '2' to play as Necromancer: ")
    if role == '1':
        player = Role1.create_paladin(player_name, speed, defense)
        opponent = Role2.create_necromancer("AI", magic, defense)
    else:
        player = Role2.create_necromancer(player_name, magic, defense)
        opponent = Role1.create_paladin("AI", speed, defense)

    player_health = 20
    opponent_health = 20

    while True:
        print("Your turn to attack")
        attack_choice = input("Enter 'a' to attack, 'q' to quit: ")
        if attack_choice == 'q':
            return

        opponent_defense = Role2.defend(opponent, player['speed']) if role == '1' else Role1.defend(opponent, player['magic'])
        opponent_health = max(0, opponent_health - (Role1.attack(player) if role == '1' else Role2.cast_spell(player) - opponent_defense))

        if opponent_health <= 0:
            print(f"{player['name']} wins!")
            return

        print("Opponent's turn to attack")
        opponent_attack = Role2.cast_spell(opponent) if role == '1' else Role1.attack(opponent)
        player_defense = Role1.defend(player, opponent['magic']) if role == '1' else Role2.defend(player, opponent['speed'])
        player_health = max(0, player_health - (opponent_attack - player_defense))

        if player_health <= 0:
            print(f"{opponent['name']} wins!")
            return
