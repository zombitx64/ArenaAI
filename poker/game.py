from typing import List, Tuple

from .card import Deck
from .hand import evaluate
from .player import Player


class Game:
    def __init__(self, players: List[Player]) -> None:
        self.players = players

    def play_round(self, ante: int = 10) -> Tuple[List[str], List[Player], int]:
        deck = Deck()
        pot = 0
        active: List[Player] = []
        for player in self.players:
            if player.chips < ante:
                player.active = False
                continue
            player.chips -= ante
            pot += ante
            player.hand = deck.deal(2)
            if player.decide([]):
                active.append(player)
        community = deck.deal(5)
        if not active:
            return [str(c) for c in community], [], pot
        scores = [(evaluate(p.hand + community), p) for p in active]
        scores.sort(reverse=True)
        best = scores[0][0]
        winners = [p for score, p in scores if score == best]
        share = pot // len(winners)
        for w in winners:
            w.chips += share
        return [str(c) for c in community], winners, pot
