from tennis_game import TennisGame

class TennisCourt:
    def __init__(self, player1, player2):
        self.game = TennisGame(player1.get_name(), player2.get_name())
    
    def is_finish(self):
        score = self.game.get_score()

        if "Win for" in score:
            return True
        else:
            return False
    
    def set_point(self, player):
        self.game.won_point(player.get_name())

        if (self.is_finish() == True):
            print(self.game.get_score())
        else:
            print(self.game.get_score())

    