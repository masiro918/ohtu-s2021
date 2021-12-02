from tennis_game import TennisGame

class TennisCourt:
    self.game = None

    def __init__(self, game, player1, player2):
        self.game = TennisGame(player1.get_name, player2.get_name())
    
    def set_point(self, player):
        self.game.won_point(player.get_name())

    def is_finish(self):
        score = self.game.get_score()

        if "Win for" in score:
            return True
        else:
            return False