import random
from weapons import random_weapon

class Orc:
    def __init__(self, name, speed, power ,armor_rating, weapon):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.power = random.randint(10,15)
        self.weapon = random_weapon() # tup (name: str, power: int)
        self.speed = random.randint(0,5)
        self.armor_rating = random.randint(2,8)

    def speak():
        pass

    def attack():
        pass

