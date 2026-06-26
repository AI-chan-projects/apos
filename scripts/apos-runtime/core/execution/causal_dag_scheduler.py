from core.event_store.event_store import EventStore


class CausalDAGScheduler:

    def __init__(self, nodes):
        self.nodes = nodes
        self.store = EventStore()

        # causal weights per node
        self.weights = {node.id: 0 for node in nodes}

    # ----------------------------
    # STEP 1: build causal signal
    # ----------------------------
    def build_causal_signal(self):

        events = self.store.replay()

        for e in events:

            # failure amplification signal
            if "failure" in e.type or "blocked" in e.type:
                node_name = e.payload.get("node")

                if node_name:
                    for node in self.nodes:
                        if node.name == node_name:
                            self.weights[node.id] += 3

            # execution success signal
            if "node_executing" in e.type:
                node_name = e.payload.get("node")

                if node_name:
                    for node in self.nodes:
                        if node.name == node_name:
                            self.weights[node.id] -= 1

    # ----------------------------
    # STEP 2: resolve causal order
    # ----------------------------
    def resolve(self):

        self.build_causal_signal()

        # sort by:
        # 1. dependency already handled outside
        # 2. causal weight (lower = more stable)
        ordered = sorted(
            self.nodes,
            key=lambda n: self.weights.get(n.id, 0)
        )

        return ordered