import random
from weapons import random_weapon

class Goblin:
    def __init__(self, name, speed, power ,armor_rating, weapon):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.power = random.randint(5.10)
        self.weapon = random_weapon() # tup (name: str, power: int)
        self.speed = random.randint(5.10)
        self.armor_rating = 1

    def speak(self):
        pass

    def attack(self):
        pass

    def run_away(self):
        """if goblin hp is below 50% there is a 30% chance to run away"""
        if self.hp < 10:
            # 30% chance to run away
            if random.random() < 0.3:
                return True        
        return False