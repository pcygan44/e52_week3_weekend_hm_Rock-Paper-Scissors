import unittest

from models.player import Player




class TestPlayers(unittest.TestCase):

    def setUp(self):
        self.player1 = Player ("Jim", "paper" )
        self.player2 = Player ("Tom", "rock")


    def test_player_name(self):
        self.assertEqual("Jim", self.player1.name)

    def test_player_choice(self):
        self.assertEqual("rock", self.player2.choice)