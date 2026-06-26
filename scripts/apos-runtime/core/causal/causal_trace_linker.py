from core.event_store.event_store import EventStore


class CausalTraceLinker:

    def __init__(self):
        self.store = EventStore()

    def link(self, events):
        """
        Converts raw execution events → causal graph nodes
        """

        graph = {}

        for e in events:

            node_id = e.payload.get("node") or e.id

            if node_id not in graph:
                graph[node_id] = {
                    "events": [],
                    "causes": [],
                    "effects": []
                }

            graph[node_id]["events"].append({
                "type": e.type,
                "timestamp": e.timestamp,
                "payload": e.payload
            })

            # causal tagging (failure propagation hint)
            if "failure" in e.type or "blocked" in e.type:
                graph[node_id]["causes"].append("failure_signal")

        return graph