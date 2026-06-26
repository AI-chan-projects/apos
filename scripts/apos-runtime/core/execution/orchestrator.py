from core.air.task_graph_builder import TaskGraphBuilder
from core.execution.dag_scheduler import DAGScheduler
from core.execution.execution_engine import ExecutionEngine
from core.event_store.event_store import EventStore, Event
from core.approval.approval_store import approval_store
from datetime import datetime
import uuid


class APOSOrchestrator:

    def __init__(self):
        self.store = EventStore()
        self.execution_engine = ExecutionEngine()

    def run_once(self, air: dict):
        """
        Single deterministic execution cycle
        """

        self._log("orchestrator_start", {"air": air})

        # 1. Build Task Graph
        builder = TaskGraphBuilder().build_from_air(air)

        builder.attach_approval_flags(self._policy_engine)
        nodes = builder.get_nodes()

        self._log("task_graph_built", {"nodes": len(nodes)})

        # 2. DAG Scheduling
        scheduler = DAGScheduler(nodes)
        ordered_nodes = scheduler.resolve()

        self._log("dag_scheduled", {"count": len(ordered_nodes)})

        # 3. Execution Loop
        executed = []
        blocked = []

        for node in ordered_nodes:

            if node.status == "BLOCKED":
                blocked.append(node.name)
                self._log("node_blocked", {"node": node.name})
                continue

            self._log("node_executing", {"node": node.name})

            self.execution_engine.execute([node])

            executed.append(node.name)

        # 4. Summary Event
        self._log("execution_complete", {
            "executed": executed,
            "blocked": blocked
        })

        return {
            "executed": executed,
            "blocked": blocked
        }

    # -----------------------------
    # Policy Engine (injected hook)
    # -----------------------------
    def _policy_engine(self, action):
        if action["type"] == "log":
            return "ALLOW"

        if action["type"] in ["write", "delete"]:
            return "APPROVE_REQUIRED"

        return "ALLOW"

    # -----------------------------
    # Event Logger
    # -----------------------------
    def _log(self, event_type, payload):
        self.store.append(
            Event(
                id=str(uuid.uuid4()),
                timestamp=datetime.utcnow().isoformat(),
                type=event_type,
                payload=payload,
                source="Orchestrator",
                status="success",
            )
        )