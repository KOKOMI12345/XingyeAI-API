import websockets
import json
from ..utils import logger

class XingyeWebsocket:
    """
    用于连接Xingye的WebSocket
    """
    def __init__(self, url):
        self.url = url
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(self.url) # type: ignore
        logger.info(f"WebSocket connected to {self.url}")

    async def send(self, message: str | dict, json_encode: bool = False):
        if self.websocket is not None:
            if json_encode:
               message = json.dumps(message)
               await self.websocket.send(message)
            else:
                await self.websocket.send(message)
        else:
            raise Exception("WebSocket is not connected.")

    async def receive(self):
        if self.websocket is not None:
            return await self.websocket.recv()
        else:
            raise Exception("WebSocket is not connected.")

    async def close(self):
        if self.websocket is not None:
            await self.websocket.close()