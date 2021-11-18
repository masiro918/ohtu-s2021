import requests
from player import Player
from playerreader import PlayerReader

def get_points(player):
    return player.points

def main():
    #url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    #response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)
    
    url = None
    player_reader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    response = None
    stats = None
    
    try:
        response = player_reader.get_players()
        print("1")
        for player in response:
            print(player)
        stats = PlayerStats(response)
        print("2")
        players = stats.top_scorers_by_nationality("FIN")
        
    except:
        print ("virhe haettaessa tietoja")
        return

    for player in players:
        print(player)
    
    return
    
    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games'],
        )
        
        if player.nationality == "FIN":
            players.append(player)

    #print("Oliot:")
    
    players.sort(key=get_points, reverse=True)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
