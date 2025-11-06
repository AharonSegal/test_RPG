import random
from core.assets import goblin_names
from core.monsters import Monster


class Goblin(Monster):
    def __init__(self,hp, weapon_name,weapon_power,armor_rating):
        super().__init__(hp, weapon_name,weapon_power,armor_rating)
        self.name = goblin_names.pop(random.choice(goblin_names))
        self.type = "goblin"
        self.power = random.randint(5.10)
        self.speed = random.randint(5.10)

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
