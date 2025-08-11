import time
from typing import List, Optional

from .game import Game
from .player import Player


class Tournament:
    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self.game = Game(players)

    def leaderboard(self) -> List[Player]:
        return sorted(self.players, key=lambda p: p.chips, reverse=True)

    def play(self, rounds: int, broadcaster: Optional["Broadcaster"] = None) -> None:
        for rnd in range(1, rounds + 1):
            community, winners, pot = self.game.play_round()
            if broadcaster:
                data = {
                    "round": rnd,
                    "community": community,
                    "winners": [w.name for w in winners],
                    "pot": pot,
                    "leaderboard": [(p.name, p.chips) for p in self.leaderboard()],
                }
                broadcaster.publish(data)
            time.sleep(1)


class Broadcaster:
    def publish(self, data: dict) -> None:  # pragma: no cover - interface
        raise NotImplementedError
