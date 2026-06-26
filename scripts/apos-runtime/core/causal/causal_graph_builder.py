from core.event_store.event_store import EventStore


class CausalGraphBuilder:

    def __init__(self):
        self.store = EventStore()

    def build(self):
        """
        Converts event stream → causal graph
        """

        events = self.store.replay()

        nodes = {}
        edges = []

        prev_event = None

        for e in events:

            nodes[e.id] = {
                "id": e.id,
                "type": e.type,
                "timestamp": e.timestamp,
                "payload": e.payload
            }

            if prev_event:
                edges.append({
                    "from": prev_event.id,
                    "to": e.id,
                    "relation": self._infer_causality(prev_event, e)
                })

            prev_event = e

        return {
            "nodes": list(nodes.values()),
            "edges": edges
        }

    def _infer_causality(self, a, b):

        if a.type == "air_generated" and "dag" in b.type:
            return "AIR_TO_PLAN"

        if "node_executing" in b.type:
            return "PLAN_TO_EXECUTION"

        if "node_blocked" in b.type:
            return "EXECUTION_TO_BLOCK"

        if "approval" in b.type:
            return "BLOCK_TO_APPROVAL"

        return "TEMPORAL_FOLLOW"