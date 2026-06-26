from core.air.task_graph_builder import TaskGraphBuilder
from core.execution.dag_scheduler import DAGScheduler
from core.execution.execution_engine import ExecutionEngine
from core.event_store.event_store import EventStore, Event
from core.approval.approval_store import approval_store
from datetime import datetime
import uuid


# 🔥 Live Stream Hook (optional external injection)
try:
    from ui.live.event_stream import EventStream
    from ui.live.websocket_manager import WebSocketManager

    ws_manager = WebSocketManager()
    global_event_stream = EventStream(ws_manager)

except:
    global_event_stream = None


# 🧠 Runtime Health Monitor Hook (NEW)
try:
    from runtime_monitor.health_monitor import RuntimeHealthMonitor

    health_monitor = RuntimeHealthMonitor()

except:
    health_monitor = None


class APOSOrchestrator:

    def __init__(self):
        self.store = EventStore()
        self.execution_engine = ExecutionEngine()

        # 🧠 attach monitor to orchestrator lifecycle
        self.health_monitor = health_monitor

    # -------------------------------------------------
    # MAIN LOOP
    # -------------------------------------------------
    def run_once(self, air: dict):
        """
        Single deterministic execution cycle
        """

        self._emit("orchestrator_start", {"air": air})

        # 1. Build Task Graph
        builder = TaskGraphBuilder().build_from_air(air)
        builder.attach_approval_flags(self._policy_engine)

        nodes = builder.get_nodes()

        self._emit("task_graph_built", {"nodes": len(nodes)})

        # 2. DAG Scheduling
        scheduler = DAGScheduler(nodes)
        ordered_nodes = scheduler.resolve()

        self._emit("dag_scheduled", {"count": len(ordered_nodes)})

        # 3. Execution Loop
        executed = []
        blocked = []

        for node in ordered_nodes:

            if node.status == "BLOCKED":
                blocked.append(node.name)
                self._emit("node_blocked", {"node": node.name})
                continue

            self._emit("node_executing", {"node": node.name})

            self.execution_engine.execute([node])

            executed.append(node.name)

        # 4. Summary Event
        self._emit("execution_complete", {
            "executed": executed,
            "blocked": blocked
        })

        return {
            "executed": executed,
            "blocked": blocked
        }

    # -------------------------------------------------
    # POLICY ENGINE (injected hook)
    # -------------------------------------------------
    def _policy_engine(self, action):
        if action["type"] == "log":
            return "ALLOW"

        if action["type"] in ["write", "delete"]:
            return "APPROVE_REQUIRED"

        return "ALLOW"

    # -------------------------------------------------
    # EVENT EMITTER (CORE UPGRADE)
    # -------------------------------------------------
    def _emit(self, event_type, payload):

        event = Event(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            type=event_type,
            payload=payload,
            source="Orchestrator",
            status="success",
        )

        # 1. Persist to Event Store (source of truth)
        self.store.append(event)

        # 🧠 1.5 Runtime Health Monitor Hook (NEW)
        if self.health_monitor:
            self.health_monitor.record_event()

        # 2. Live Stream (real-time UI)
        self._emit_live(event)

    # -------------------------------------------------
    # LIVE STREAM HOOK
    # -------------------------------------------------
    async def _emit_live(self, event):

        if global_event_stream:
            await global_event_stream.push_event({
                "id": event.id,
                "timestamp": event.timestamp,
                "type": event.type,
                "payload": event.payload,
                "source": event.source,
                "status": event.status
            })