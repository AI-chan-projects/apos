from core.event_store.event_store import EventStore


class EventReplayEngine:

    def __init__(self):
        self.store = EventStore()

    def replay_all(self):
        return self.store.replay()

    def replay_by_type(self, event_type: str):
        return [
            e for e in self.store.replay()
            if e.type == event_type
        ]

    def replay_by_source(self, source: str):
        return [
            e for e in self.store.replay()
            if e.source == source
        ]

    def reconstruct_state(self):
        """
        Rebuild system state from event history
        """
        state = {
            "air": None,
            "tasks": [],
            "executed": [],
            "blocked": [],
            "approvals": [],
        }

        for event in self.store.replay():

            if event.type == "air_generated":
                state["air"] = event.payload

            elif "task" in event.type:
                state["tasks"].append(event.payload)

            elif event.type == "execution_complete":
                state["executed"] = event.payload.get("executed", [])
                state["blocked"] = event.payload.get("blocked", [])

            elif "approval" in event.type:
                state["approvals"].append(event.payload)

        return state