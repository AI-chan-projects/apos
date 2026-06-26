from core.event_store.event_store import EventStore


class ReplayEngine:

    def __init__(self):
        self.store = EventStore()

    def replay(self):
        return self.store.replay()

    def replay_until(self, event_id):

        events = self.store.replay()
        buffer = []

        for e in events:
            buffer.append(e)
            if e.id == event_id:
                break

        return buffer