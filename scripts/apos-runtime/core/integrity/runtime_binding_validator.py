# core/integrity/runtime_binding_validator.py

class RuntimeBindingValidator:

    """
    Ensures execution trace ↔ causal trace alignment
    """

    def validate(self, execution_log, causal_graph):

        mismatches = []

        executed_nodes = {e["node"] for e in execution_log}

        causal_nodes = {n.id for n in causal_graph.nodes}

        # execution without causal explanation
        for node in executed_nodes - causal_nodes:
            mismatches.append({
                "type": "untracked_execution",
                "node": node
            })

        # causal node never executed
        for node in causal_nodes - executed_nodes:
            mismatches.append({
                "type": "unexecuted_causal_node",
                "node": node
            })

        return {
            "valid": len(mismatches) == 0,
            "mismatches": mismatches
        }