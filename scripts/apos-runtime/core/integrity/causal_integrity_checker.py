# core/integrity/causal_integrity_checker.py

from core.causal.causal_graph_builder import CausalGraphBuilder


class CausalIntegrityChecker:

    def __init__(self):
        self.builder = CausalGraphBuilder()

    def validate(self, events):

        graph = self.builder.build_from_events(events)

        issues = []

        # 1. orphan node check
        for node in graph.nodes:
            if not node.parents and not node.children:
                issues.append({
                    "type": "orphan_node",
                    "node": node.id
                })

        # 2. missing causality links
        for node in graph.nodes:
            if node.event_type == "failure" and not node.parents:
                issues.append({
                    "type": "unexplained_failure",
                    "node": node.id
                })

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }