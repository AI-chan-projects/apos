from core.event_store.event_store import EventStore


class CausalTraceEngine:

    def __init__(self):
        self.store = EventStore()

    def trace_back(self, event_id):
        """
        Trace backward causal chain from event
        """

        events = self.store.replay()

        chain = []
        found = False

        for e in reversed(events):

            if e.id == event_id:
                found = True

            if found:
                chain.append(e)

        return list(reversed(chain))