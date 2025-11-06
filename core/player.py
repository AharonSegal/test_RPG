import random

class Player:
    def __init__(self, name, speed, profession):
        self.name = name
        self.profession = profession
        self.speed = random.randint(5,10)
        self.hp = 50 if profession != "healer" else 60
        current_armor = random.randint(5,10)
        self.armor_rating = current_armor if profession != "warrior" else current_armor + 10


    def speak():
        pass

    def attack():
        pass

    