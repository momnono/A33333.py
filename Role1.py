"""logic for paladin role"""
import random

def create_paladin(name, speed, defense):
    return {
        'name': name,
        'speed': speed,
        'defense': defense
    }

def attack(paladin):
    return paladin['speed'] + random.randint(1, 12)

def defend(paladin, attack_strength):
    return paladin['defense'] + random.randint(1, 12)