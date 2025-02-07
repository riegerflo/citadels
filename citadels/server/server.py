import asyncio
import websockets
import json

class GameServer:
    def __init__(self):
        self.clients = {}

    async def register(self, websocket, player_name):
        self.clients[player_name] = websocket
        await self.notify_player(player_name, "Welcome to the game!")

    async def unregister(self, player_name):
        del self.clients[player_name]

    async def notify_player(self, player_name, message_type, data=None):
        if player_name in self.clients:
            message = {"type": message_type, "data": data}
            await self.clients[player_name].send(json.dumps(message))

    async def handle_client(self, websocket):
        player_name = await websocket.recv()
        await self.register(websocket, player_name)
        try:
            async for message in websocket:
                data = json.loads(message)
                # Handle incoming messages from clients
                print(f"Received message from {player_name}: {data}")
        finally:
            await self.unregister(player_name)

    async def start(self):
        async with websockets.serve(self.handle_client, "localhost", 8765):
            await asyncio.Future()  # Run forever

if __name__ == "__main__":
    server = GameServer()
    asyncio.run(server.start())