class World:

    players = []
    monsters = []
    items = []

    @staticmethod
    def add_player(player):
        World.players.append(player)
    
