from core.air.task_graph_builder import TaskGraphBuilder
from core.execution.dag_scheduler import DAGScheduler
from core.execution.causal_dag_scheduler import CausalDAGScheduler
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


# 🧠 Failure Recovery Engine (NEW)
try:
    from recovery.recovery_orchestrator import FailureAutoRecoveryEngine
    recovery_engine = FailureAutoRecoveryEngine()

except:
    recovery_engine = None


class APOSOrchestrator:

    def __init__(self):
        self.store = EventStore()
        self.execution_engine = ExecutionEngine()

        # monitors
        self.health_monitor = health_monitor
        self.recovery_engine = recovery_engine

    # -------------------------------------------------
    # MAIN LOOP
    # -------------------------------------------------
    def run_once(self, air: dict):

        self._emit("orchestrator_start", {"air": air})

        # 1. Build Task Graph
        builder = TaskGraphBuilder().build_from_air(air)
        builder.attach_approval_flags(self._policy_engine)

        nodes = builder.get_nodes()

        self._emit("task_graph_built", {"nodes": len(nodes)})

        # 2. DAG Scheduling
        scheduler = CausalDAGScheduler(nodes)
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

        # 🧠 5. POST-CYCLE HEALTH + RECOVERY (NEW CORE INTEGRATION)
        self._post_cycle_recovery()

        return {
            "executed": executed,
            "blocked": blocked
        }

    # -------------------------------------------------
    # POST-CYCLE RECOVERY HOOK (NEW)
    # -------------------------------------------------
    def _post_cycle_recovery(self):

        if not self.health_monitor or not self.recovery_engine:
            return

        try:
            # 1. get health snapshot from monitor
            probe_state = self.health_monitor.probe.run_probe()
            metric_state = self.health_monitor.metrics.snapshot()

            health_state = {
                **probe_state,
                **metric_state,
                "anomalies": []
            }

            # 2. trigger recovery engine
            self.recovery_engine.recover(health_state)

        except Exception as e:
            self._emit("recovery_failed", {"error": str(e)})

    # -------------------------------------------------
    # POLICY ENGINE
    # -------------------------------------------------
    def _policy_engine(self, action):
        if action["type"] == "log":
            return "ALLOW"

        if action["type"] in ["write", "delete"]:
            return "APPROVE_REQUIRED"

        return "ALLOW"

    # -------------------------------------------------
    # EVENT EMITTER
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

        self.store.append(event)

        # 🧠 heartbeat to monitor
        if self.health_monitor:
            self.health_monitor.record_event()

        self._emit_live(event)

    # -------------------------------------------------
    # LIVE STREAM
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