"""logic for necromancer role"""
import random

def create_necromancer(name, magic, defense):
    return {
        'name': name,
        'magic': magic,
        'defense': defense
    }

def cast_spell(necromancer):
    return necromancer['magic'] + random.randint(1, 12)

def defend(necromancer, attack_strength):
    return necromancer['defense'] + random.randint(1, 12)