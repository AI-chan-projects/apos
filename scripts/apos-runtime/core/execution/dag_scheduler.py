from typing import Dict, List
from core.air.task_graph_builder import TaskNode


class DAGScheduler:
    """
    Resolves execution order using:
    - dependency graph
    - priority
    """

    def __init__(self, nodes: Dict[str, TaskNode]):
        self.nodes = nodes

    def _is_ready(self, node: TaskNode):
        return len(node.depends_on) == 0

    def resolve(self) -> List[TaskNode]:
        """
        Hybrid:
        1. dependency resolution
        2. priority ordering within ready set
        """

        unresolved = dict(self.nodes)
        resolved = []
        completed = set()

        while unresolved:

            ready = [
                n for n in unresolved.values()
                if all(dep in completed for dep in n.depends_on)
            ]

            if not ready:
                break  # circular dependency safeguard

            # priority sort
            ready.sort(key=lambda x: x.priority)

            for node in ready:
                resolved.append(node)
                completed.add(node.id)
                unresolved.pop(node.id)

        return resolved