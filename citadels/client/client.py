import asyncio
import websockets
import json

class GameClient:
    def __init__(self, player_name):
        self.player_name = player_name
        self.message_handlers = {
            "welcome": self.handle_welcome,
            "choose-character-action": self.handle_choose_character_action,
        }

    async def connect(self):
        async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send(self.player_name)
            async for message in websocket:
                data = json.loads(message)
                self.handle_message(data)

    def handle_message(self, data):
        message_type = data.get("type")
        handler = self.message_handlers.get(message_type)
        if handler:
            handler(data.get("data"))

    def handle_welcome(self, data):
        print(f"Server: {data}")

    def handle_choose_character_action(self, data):
        characters = data.get("characters", [])
        print(f"Choose a character from: {characters}")
        character_choice = input("Choose a character: ")
        asyncio.create_task(self.send_choice(character_choice))

    async def send_choice(self, choice):
        async with websockets.connect("ws://localhost:8765") as websocket:
            await websocket.send(json.dumps({"type": "character-choice", "choice": choice}))

if __name__ == "__main__":
    player_name = input("Enter your player name: ")
    client = GameClient(player_name)
    asyncio.run(client.connect())