# Unit test all sub-programs with return statements.
import unittest
from src.BlackJack import BlackJack


class BlackJackTest(unittest.TestCase):
    bjack = BlackJack()

    def test_score_hand(self):
        self.assertEqual(14, self.bjack.score_hand(['H7', 'S7']))

    def test_deal_to_player(self):
        self.assertFalse(self.bjack.deal_to_player(['H5', 'SQ'], ['HK', 'SK', "CK"]))
        self.assertTrue(self.bjack.deal_to_player(['H5', 'SQ'], ['HA', 'C4']))

    def test_valid_deal_input(self):
        self.assertTrue(self.bjack.valid_deal_input() == 'D' or 'S')

    def test_find_winner(self):
        self.assertEqual([0, 1], self.bjack.find_winner([["S9", "CK"], ["CK", "S9"]]))

    def test_initialise_computer_risk(self):
        result = self.bjack.initialise_computer_risk(2)
        self.assertTrue(2 <= result[1] <= 9)