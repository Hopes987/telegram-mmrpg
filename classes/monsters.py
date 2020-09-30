from classes.weapon import *
from classes.world import *
import random

class Monster:
    def __init__(self,_class, id_monster):
        self._class = _class
        self.live = 7
        self.damage = 3
        self.id_monster = 0
        self.weapon_m = Weapon("fist",0, "nothing")
        self.skill = "nothing"

    # def damage(self,live):
    #     self.live=-live
    
    def add_weapons_in_word(self):
        self.weapon_m = World.items.append(random.shuffle(finish_weapons))

    def delete_monster(self,_class, id_monster):
        World.items.pop(id_monster)

class Zombie:
    def __init__(self,_class, weapon_m):
        self._class = "zombie"
        self.live = 5
        self.damage = 4
        self.weapon_m = random.shuffle(finish_weapons)
        self.skill = "so slow"
        self.id_monster =+1

class Little_boy:
    def __init__(self,_class, weapon_m):
        self._class = "Littel_boy"
        self.live = 6
        self.damage = 2
        self.weapon_m = random.shuffle(finish_weapons)
        self.skill = "faster"
        self.id_monster =+1

    
