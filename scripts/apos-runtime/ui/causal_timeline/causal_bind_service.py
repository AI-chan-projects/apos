from core.causal.causal_trace_linker import CausalTraceLinker
from core.event_store.event_store import EventStore


class CausalBindService:

    def __init__(self):
        self.store = EventStore()
        self.linker = CausalTraceLinker()

    def get_bound_timeline(self):

        events = self.store.replay()

        causal_graph = self.linker.link(events)

        timeline = []

        for e in events:

            timeline.append({
                "timestamp": e.timestamp,
                "type": e.type,
                "node": e.payload.get("node"),
                "causal_context": causal_graph.get(
                    e.payload.get("node") or e.id, {}
                )
            })

        return timeline