import random

weapons = {"knife" : 1.5,
            "sword" : 1,
            "axe" : 1.5
}

def random_weapon():
    random_item = random.choice(list(weapons.items()))
    return random_item 




