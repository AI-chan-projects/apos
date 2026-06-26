from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid


@dataclass
class TaskNode:
    id: str
    name: str
    actions: List[Dict[str, Any]] = field(default_factory=list)
    depends_on: List[str] = field(default_factory=list)
    priority: int = 0
    status: str = "PENDING"  # PENDING / BLOCKED / READY / DONE


class TaskGraphBuilder:
    """
    Converts AIR structure → executable Task Graph
    """

    def __init__(self):
        self.nodes: Dict[str, TaskNode] = {}

    def build_from_air(self, air: Dict[str, Any]):
        """
        AIR → Task Graph
        """

        tasks = air.get("tasks", [])

        previous_task_id = None

        for i, task in enumerate(tasks):
            task_id = str(uuid.uuid4())

            node = TaskNode(
                id=task_id,
                name=task["name"],
                actions=task.get("actions", []),
                priority=i,  # default ordering priority
            )

            # linear dependency by default (AIR baseline assumption)
            if previous_task_id:
                node.depends_on.append(previous_task_id)

            self.nodes[task_id] = node
            previous_task_id = task_id

        return self

    def get_nodes(self):
        return self.nodes