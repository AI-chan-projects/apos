from collections import defaultdict


class WebSocketManager:

    def __init__(self):
        self.clients = set()

    def connect(self, client):
        self.clients.add(client)

    def disconnect(self, client):
        self.clients.discard(client)

    async def broadcast(self, message):
        for client in self.clients:
            await client.send_json(message)