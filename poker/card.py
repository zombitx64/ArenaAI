from dataclasses import dataclass
import random
from typing import List

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return f"{self.rank}{self.suit[0]}"

class Deck:
    """Standard 52 card deck."""
    def __init__(self) -> None:
        self.cards: List[Card] = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        return [self.cards.pop() for _ in range(n)]
