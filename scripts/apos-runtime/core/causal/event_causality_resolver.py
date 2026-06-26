class EventCausalityResolver:

    def explain(self, event):
        """
        Human-readable causal explanation
        """

        if event.type == "node_blocked":
            return "Node was blocked due to policy constraint"

        if event.type == "approval_requested":
            return "Action exceeded risk threshold"

        if event.type == "node_executing":
            return "Node scheduled by DAG resolver"

        return "Causal relation unknown"