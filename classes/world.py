class World:

    players = []
    monsters = []
    items = []

    @staticmethod
    def add_player(player):
        World.players.append(player)
    
    @staticmethod
    def return_player(player_id):
        for i in World.players: 
            if i.id == player_id: 
                return i
    
