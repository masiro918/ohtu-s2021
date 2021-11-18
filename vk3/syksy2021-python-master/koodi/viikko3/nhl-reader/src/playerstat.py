from player import Player

def get_points(player):
    return player.points

class PlayerStats:
    def __init__(self, players):
        self.players = players
    
    def top_scorers_by_nationality(self, nationality):
        sorted_players = []
        for player in self.players:
            if player.nationality == nationality:
                sorted_players.append(player)
        
        sorted_players.sort(key=get_points, reverse=True)
        return sorted_players



