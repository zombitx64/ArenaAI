import asyncio
import json
from typing import Set

import websockets

from .tournament import Broadcaster


class WebsocketBroadcaster(Broadcaster):
    def __init__(self, host: str = "0.0.0.0", port: int = 8765) -> None:
        self.host = host
        self.port = port
        self.clients: Set[websockets.WebSocketServerProtocol] = set()
        self.queue: "asyncio.Queue[dict]" = asyncio.Queue()

    async def _client_handler(self, websocket: websockets.WebSocketServerProtocol) -> None:
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    async def _broadcaster(self) -> None:
        while True:
            data = await self.queue.get()
            if self.clients:
                message = json.dumps(data)
                await asyncio.gather(*(client.send(message) for client in self.clients))

    def publish(self, data: dict) -> None:
        self.queue.put_nowait(data)

    async def run(self) -> None:
        async with websockets.serve(self._client_handler, self.host, self.port):
            await self._broadcaster()
