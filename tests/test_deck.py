import unittest

from poker.card import Deck


class DeckTest(unittest.TestCase):
    def test_deck_unique(self) -> None:
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(len({str(c) for c in deck.cards}), 52)


if __name__ == '__main__':
    unittest.main()
