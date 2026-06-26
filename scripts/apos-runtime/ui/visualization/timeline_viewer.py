from core.event_store.event_store import EventStore


class TimelineViewer:

    def __init__(self):
        self.store = EventStore()

    def build_timeline(self):
        events = self.store.replay()

        timeline = []

        for e in events:
            timeline.append({
                "timestamp": e.timestamp,
                "type": e.type,
                "source": e.source,
                "summary": self._summary(e)
            })

        return sorted(timeline, key=lambda x: x["timestamp"])

    def _summary(self, event):

        if event.type == "air_generated":
            return "AIR created"

        if "dag" in event.type:
            return "DAG scheduled"

        if "node_executing" in event.type:
            return "Node executing"

        if "node_blocked" in event.type:
            return "Node blocked"

        if "execution_complete" in event.type:
            return "Execution completed"

        return event.type