from typing import List

from .card import Card


class Player:
    def __init__(self, name: str, chips: int = 100) -> None:
        self.name = name
        self.chips = chips
        self.hand: List[Card] = []
        self.active = True

    def reset(self) -> None:
        self.hand = []
        self.active = True

    def decide(self, community: List[Card]) -> bool:
        """Return True to stay in hand, False to fold."""
        if not community:
            high = {'A', 'K', 'Q', 'J', 'T'}
            return any(card.rank in high for card in self.hand)
        return True
