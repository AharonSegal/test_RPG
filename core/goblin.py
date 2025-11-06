import random
from core.assets import goblin_names
from core.monsters import Monster


class Goblin(Monster):
    def __init__(self):
        super().__init__()
        self.name = (random.choice(goblin_names))
        self.type = "goblin"
        self.power = random.randint(5,10)
        self.speed = random.randint(5,10)

    def speak(self):
        print(f"{self.name} type: {self.type}: whblgraa")

        
    def attack(self):
        attack = random.randint(20) + self.speed
        return attack

    # def run_away(self):
    #     """if goblin hp is below 50% there is a 30% chance to run away"""
    #     if self.hp < 10:
    #         # 30% chance to run away
    #         if random.random() < 0.3:
    #             return True        
    #     return False

x = Goblin()

print(x.weapon_name)
