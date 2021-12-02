import requests
from player import Player
from playerreader import PlayerReader
from playerstat import PlayerStats



def main():
    print("Players from FIN 2021-01-04 19:19:40.026464\n")
    url = None
    response = None
    stats = None
    
    player_reader = PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players")
    response = player_reader.get_players()
    stats = PlayerStats(response)
    players = stats.top_scorers_by_nationality("FIN")
    
    for player in players:
        print(player)

if __name__ == "__main__":
    main()
