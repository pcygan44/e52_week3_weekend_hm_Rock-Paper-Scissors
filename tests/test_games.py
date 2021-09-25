import unittest
from unittest import result

from models.game import game
from models.player import Player

class TestGames(unittest.TestCase):

    def setUp(self, ):
        self.player1 = Player ("Jim", "paper" )
        self.player2 = Player ("Tom", "rock")
        self.player3 = Player ("Gil", "paper")

    def test_game_draw(self):
        resoult = game(self, self.player1, self.player3)
        self.assertEqual(None,resoult)


    def test_game_player1_win(self):
        result = game(self, self.player1, self.player2)
        self.assertEqual("Player1 wins with paper", result)

    def test_game_palyer2_win(self):
        result = game(self, self.player1, self.player2)