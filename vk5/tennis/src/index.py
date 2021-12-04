from tennis_game import TennisGame
from tennis_court import TennisCourt
from player import Player

def main():
    player1 = Player("player1")
    player2 = Player("player2")
    
    tennis_court = TennisCourt(player1, player2)
    
    tennis_court.set_point(player1)
    tennis_court.set_point(player1)
    tennis_court.set_point(player2)
    tennis_court.set_point(player1)
    tennis_court.set_point(player1)
    

if __name__ == "__main__":
    main()
