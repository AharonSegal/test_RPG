import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc
from core.assets import ascii_art


class Game:
    def __init__(self):
        self.player = None
        self.current_monster = None

    def start(self):
        print(ascii_art["start_message"])
        print("LETS BEGIN!")
        self.create_player()
        self.current_monster = game.choose_random_monster()

        print(self.current_monster.hp)

        #simple version
        player_start = True 
        # self.player.speak()
        # self.current_monster.speak()

        #first turn
        player_roll = Game.roll_dice(6) + self.player.speed
        print(f"you rolled {player_roll}")
        monster_roll = Game.roll_dice(6) + self.current_monster.speed
        print(f"monster rolled {monster_roll}")

        if player_roll < monster_roll:
            player_start = False
        
        self.battle(self,player_start)
        

    def show_menu(self):
        pass

    def create_player(self):
        #implement random profession
        self.player = Player("healer")
        print(self.player.name) 
        print(ascii_art["obtained"])


    def choose_random_monster(self):
        monster_list = [Orc,Goblin]
        current = random.choice(monster_list)
        print(current.name)
        return current

    def strike(self,attacker,defender):
        attack = attacker.attack()
        defend = self.defender.armor_rating
        if attack > defend:
            print(ascii_art["strike"])
            defender.hp -= attack
        else:
            print(ascii_art["evade"])

    def battle(self):
        first_turn = True
        player_turn = first_turn
        while self.current_monster.hp > 0 or self.player.hp > 0:
            if player_turn:
                Game.strike(self.player,self.current_monster)
                player_turn = False
            else:
                Game.strike(self.current_monster,self.player)

        if self.player.hp > 0:
            print(ascii_art["win"])
            print("YOU WIN")

        else:
            print("YOU LOOSE")

    @staticmethod
    def roll_dice(sides): 
        return random.randint(1,sides)

