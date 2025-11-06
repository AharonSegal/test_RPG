import random
from core.assets import orc_names
from core.monsters import Monster

class Orc(Monster):
    def __init__(self):
        super().__init__()
        self.hp += 30
        self.name = random.choice(orc_names)
        self.type = "orc"
        self.power = random.randint(10,15)
        self.speed = random.randint(0,5)
        self.armor_rating = random.randint(2,8)

    def speak(self):
        print(f"{self.name} type: {self.type}: BRWAAAAAAAAA!!!")


    def attack(self):
        attack = random.randint(20) + self.speed
        return attack


