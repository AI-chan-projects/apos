from core.event_store.event_store import EventStore


class EventCorrelationMatrix:

    def __init__(self):
        self.store = EventStore()

    def build(self):

        events = self.store.replay()

        matrix = {}

        for i, e1 in enumerate(events):
            for j, e2 in enumerate(events):

                if i == j:
                    continue

                key = (e1.type, e2.type)

                matrix[key] = matrix.get(key, 0) + 1

        return matrix