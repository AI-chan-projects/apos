from core.event_store.event_store import EventStore


class CausalDAGScheduler:

    def __init__(self, nodes):
        self.nodes = nodes
        self.store = EventStore()

        # causal weights per node
        self.weights = {node.id: 0 for node in nodes}

        # 🧠 reference DAG memory (NEW)
        self.reference = None

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
    # 🧠 NEW: reference DAG injection
    # ----------------------------
    def set_reference_dag(self, dag_nodes):
        self.reference = dag_nodes

    # ----------------------------
    # STEP 2: resolve causal order
    # ----------------------------
    def resolve(self):

        self.build_causal_signal()

        # if we have learned DAG preference, use it
        base = self.reference if self.reference is not None else self.nodes

        ordered = sorted(
            base,
            key=lambda n: self.weights.get(n.id, 0)
        )

        return ordered