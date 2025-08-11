import unittest

from poker.player import Player
from poker.tournament import Tournament


class TournamentTest(unittest.TestCase):
    def test_leaderboard(self) -> None:
        players = [Player("A"), Player("B")]
        t = Tournament(players)
        t.play(1)
        lb = t.leaderboard()
        self.assertEqual(len(lb), 2)
        self.assertGreaterEqual(lb[0].chips, lb[1].chips)


if __name__ == '__main__':
    unittest.main()
