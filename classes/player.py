from classes.inventory import *
from classes.weapon import * 

class Player:

    def __init__(self, player_id, name, _class):

        self.id = player_id
        self.name = name
        self._class = _class
        self.helf = 10
        self.power = 3
        self.weapon = Weapon('fist', 0, 'nothing')
        self.backpack = Inventory()


class Mag:

    def __init__(self, player):

        self.id = player.id
        self.name = player.name
        self._class = 'Маг'
        self.helf = 10
        self.power = 5
        self.weapon = Weapon('magick stick', 2, 'fire')

class Hero:

    def __init__(self, player):

        self.id = player.id
        self.name = player.name
        self._class = 'Герой'
        self.helf = 12
        self.power = 6
        self.weapon = Weapon('wood sword', 3, 'nothing')
        
    

    


