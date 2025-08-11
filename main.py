import asyncio
import contextlib

from poker.broadcast import WebsocketBroadcaster
from poker.player import Player
from poker.tournament import Tournament


def run_tournament(rounds: int = 20) -> None:
    players = [Player(f"AI{i}") for i in range(1, 5)]
    broadcaster = WebsocketBroadcaster()
    tournament = Tournament(players)

    async def runner() -> None:
        server_task = asyncio.create_task(broadcaster.run())
        try:
            await asyncio.to_thread(tournament.play, rounds, broadcaster)
        finally:
            server_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await server_task

    asyncio.run(runner())


if __name__ == "__main__":
    run_tournament()
