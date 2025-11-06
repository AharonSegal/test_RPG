from core.weapons import random_weapon

class Monster:

    def __init__(self):
        self.hp = 20
        weapon = random_weapon() # tup (name: str, power: int)
        self.weapon_name = weapon[0]
        self.weapon_power = weapon[1]
        self.armor_rating = 1


