from core.execution.execution_engine import ExecutionEngine


class DAGSExecutor:
    """
    ADR-001 compliant execution layer
    - strictly sequential execution
    - single worker only
    """

    def __init__(self):
        self.engine = ExecutionEngine()

    # -----------------------------------------
    # deterministic execution
    # -----------------------------------------
    def execute(self, ordered_nodes):

        executed = []
        blocked = []

        for node in ordered_nodes:

            if node.status == "BLOCKED":
                blocked.append(node.name)
                continue

            self.engine.execute([node])
            executed.append(node.name)

        return {
            "executed": executed,
            "blocked": blocked
        }