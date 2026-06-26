from core.event_store.event_store import EventStore


class ReplayViewer:

    def __init__(self):
        self.store = EventStore()
        self.index = 0
        self.events = self.store.replay()

    def reset(self):
        self.index = 0

    def step_forward(self):
        if self.index < len(self.events):
            event = self.events[self.index]
            self.index += 1
            return self._render(event)
        return None

    def step_backward(self):
        if self.index > 0:
            self.index -= 1
            event = self.events[self.index]
            return self._render(event)
        return None

    def _render(self, event):
        return {
            "id": event.id,
            "type": event.type,
            "timestamp": event.timestamp,
            "payload": event.payload,
            "source": event.source
        }