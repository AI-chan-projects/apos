from core.event_store.event_store import EventStore


class EventStream:

    def __init__(self, ws_manager):
        self.store = EventStore()
        self.ws = ws_manager

    async def push_event(self, event):
        await self.ws.broadcast({
            "type": "event",
            "data": {
                "id": event.id,
                "type": event.type,
                "timestamp": event.timestamp,
                "payload": event.payload,
                "source": event.source
            }
        })