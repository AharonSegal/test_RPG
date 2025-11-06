import random
class Player:
    def __init__(self,profession):
        # self.name = input("Hello player! Enter your Champions Name: ")
        self.name = "test"
        self.profession = profession
        self.speed = random.randint(5,10)
        self.hp = 50 if profession != "healer" else 60
        current_armor = random.randint(5,10)
        self.armor_rating = current_armor if profession != "warrior" else current_armor + 10


    def speak(self):
        print(f"{self.name} I WILL DESTROY YOU")

    def attack(self):
        attack = random.randint(20) + self.speed
        return attack

    