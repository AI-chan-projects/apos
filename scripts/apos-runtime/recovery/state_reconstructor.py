class StateReconstructor:

    def rebuild(self, events):

        state = {
            "executed_nodes": [],
            "blocked_nodes": [],
            "last_event": None
        }

        for e in events:

            if "node_executing" in e.type:
                state["executed_nodes"].append(e.payload.get("node"))

            if "node_blocked" in e.type:
                state["blocked_nodes"].append(e.payload.get("node"))

            state["last_event"] = e

        return state