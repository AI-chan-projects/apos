from core.event_store.event_store import EventStore


class DAGVisualizer:

    def __init__(self):
        self.store = EventStore()

    def build_graph(self):
        """
        Converts TaskGraph + Events → visual graph structure
        """

        events = self.store.replay()

        nodes = {}
        edges = []

        for e in events:

            if "task" in e.type:
                nodes[e.id] = {
                    "id": e.id,
                    "type": e.type,
                    "payload": e.payload,
                    "status": e.status
                }

            if "dependency" in e.type:
                edges.append({
                    "from": e.payload.get("from"),
                    "to": e.payload.get("to")
                })

        return {
            "nodes": list(nodes.values()),
            "edges": edges
        }