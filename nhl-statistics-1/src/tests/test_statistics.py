import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    def test_search(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.__str__(), "Semenko EDM 4 + 12 = 16")
        
    def test_search_none(self):
        player = self.statistics.search("Laine")
        self.assertEqual(player, None)
        
    def test_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(players[0].__str__(), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(len(players), 3)
        
    def test_top_scorers(self):
    	players = self.statistics.top_scorers(2)
    	self.assertEqual(len(players), 3)
    	self.assertEqual(players[0].__str__(), "Gretzky EDM 35 + 89 = 124")
    	
        
