from core.event_store.event_store import EventStore


class EventReplayEngine:
    def __init__(self):
        self.store = EventStore()

    def replay(self):
        return self.store.replay()

    def replay_by_type(self, event_type: str):
        return [e for e in self.store.replay() if e.type == event_type]

    def reconstruct_state(self):
        """
        Very simplified state reconstruction
        """
        state = {}

        for event in self.store.replay():
            state[event.type] = event.payload

        return state