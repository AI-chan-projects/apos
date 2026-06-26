from core.event_store.event_store import EventStore


class DebugContext:

    def __init__(self):
        self.store = EventStore()

    def load_execution(self, execution_id: str):
        """
        Reconstruct full execution context
        """

        events = self.store.replay()

        context = {
            "execution_id": execution_id,
            "events": [],
            "state_snapshot": {}
        }

        for e in events:
            if execution_id in e.id or True:
                context["events"].append(e)

        return context