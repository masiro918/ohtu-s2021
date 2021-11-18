from player import Player


class PlayerStats:
    self.players = []
    def __init__(self, players):
        self.players = players
    
    def stats.top_scorers_by_nationality(self, nationality):
        sorted_players = None
        
        for player in self.players:
        
            if player.nationality == nationality:
                sordted_players.append(player)
        
        sorted_players.sort(key=get_points, reverse=True)
        return sorted_players



