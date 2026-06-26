import copy


class DAGEvolver:

    def __init__(self):
        self.history = []

    # -----------------------------------------
    # STEP 1: analyze execution outcome
    # -----------------------------------------
    def analyze(self, nodes, executed, blocked):

        return {
            "success_rate": len(executed) / max(len(nodes), 1),
            "block_rate": len(blocked) / max(len(nodes), 1),
        }

    # -----------------------------------------
    # STEP 2: evolve DAG structure
    # -----------------------------------------
    def evolve(self, nodes, executed, blocked):

        metrics = self.analyze(nodes, executed, blocked)

        new_nodes = copy.deepcopy(nodes)

        # CASE 1: too many blocked → reduce dependency pressure
        if metrics["block_rate"] > 0.3:
            for n in new_nodes:
                n.depends_on = []  # flatten DAG

        # CASE 2: low success → reduce priority sensitivity
        if metrics["success_rate"] < 0.5:
            for n in new_nodes:
                n.priority = max(0, n.priority - 1)

        # CASE 3: good performance → reinforce structure
        if metrics["success_rate"] > 0.8:
            for n in new_nodes:
                n.priority += 1

        return new_nodes