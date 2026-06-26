from core.event_store.event_store import EventStore


class CausalChainBuilder:

    def __init__(self):
        self.store = EventStore()

    def build_chain(self, failure_event_type):

        events = self.store.replay()

        chain = []

        for e in events:

            chain.append({
                "event": e.type,
                "payload": e.payload
            })

            if e.type == failure_event_type:
                break

        return chain