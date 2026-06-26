from core.event_store.event_store import EventStore


class OrchestratorTimeline:

    def __init__(self):
        self.store = EventStore()

    def build_timeline(self):
        """
        Converts event stream → ordered timeline view
        """

        events = self.store.replay()

        timeline = []

        for e in events:
            timeline.append({
                "time": e.timestamp,
                "type": e.type,
                "source": e.source,
                "summary": self._summarize(e)
            })

        return timeline

    def _summarize(self, event):
        """
        Human-readable compact view
        """

        if event.type == "air_generated":
            return "AIR generated"

        if "dag" in event.type:
            return "DAG scheduled"

        if "node_blocked" in event.type:
            return "Execution blocked"

        if "node_executing" in event.type:
            return "Node executing"

        if "execution_complete" in event.type:
            return "Execution finished"

        return event.type