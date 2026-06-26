class TaskNode:
    def __init__(self, name, actions=None):
        self.name = name
        self.actions = actions or []
        self.dependencies = []


class TaskGraph:
    def __init__(self):
        self.nodes = {}

    def add_task(self, task: TaskNode):
        self.nodes[task.name] = task

    def add_dependency(self, task_name, depends_on):
        self.nodes[task_name].dependencies.append(depends_on)

    def resolve_order(self):
        """
        Very simple topological sort (linear fallback)
        """
        visited = set()
        order = []

        def visit(node):
            if node.name in visited:
                return
            visited.add(node.name)

            for dep in node.dependencies:
                visit(self.nodes[dep])

            order.append(node)

        for node in self.nodes.values():
            visit(node)

        return order