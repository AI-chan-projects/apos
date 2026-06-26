from core.event_store.event_store import EventStore


class ExecutionTraceRenderer:

    def __init__(self):
        self.store = EventStore()

    def render_trace(self):
        """
        Groups events into execution phases
        """

        events = self.store.replay()

        phases = {
            "air": [],
            "planning": [],
            "execution": [],
            "approval": [],
            "completion": []
        }

        for e in events:

            if e.type == "air_generated":
                phases["air"].append(e)

            elif "dag" in e.type:
                phases["planning"].append(e)

            elif "execute" in e.type:
                phases["execution"].append(e)

            elif "approval" in e.type:
                phases["approval"].append(e)

            elif "complete" in e.type:
                phases["completion"].append(e)

        return phases