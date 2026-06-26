from core.air.task_graph_builder import TaskGraphBuilder
from core.execution.causal_dag_scheduler import CausalDAGScheduler
from core.execution.execution_engine import ExecutionEngine
from core.event_store.event_store import EventStore, Event
from core.approval.approval_store import approval_store
from datetime import datetime
import uuid


# 🔥 Live Stream Hook
try:
    from ui.live.event_stream import EventStream
    from ui.live.websocket_manager import WebSocketManager

    ws_manager = WebSocketManager()
    global_event_stream = EventStream(ws_manager)

except:
    global_event_stream = None


# 🧠 Runtime Health Monitor
try:
    from runtime_monitor.health_monitor import RuntimeHealthMonitor
    health_monitor = RuntimeHealthMonitor()

except:
    health_monitor = None


# 🧠 Failure Recovery Engine
try:
    from recovery.recovery_orchestrator import FailureAutoRecoveryEngine
    recovery_engine = FailureAutoRecoveryEngine()

except:
    recovery_engine = None


# 🧠 Causal Feedback Engine (NEW)
try:
    from core.execution.causal_feedback_engine import CausalFeedbackEngine
except:
    CausalFeedbackEngine = None


class APOSOrchestrator:

    def __init__(self):
        self.store = EventStore()
        self.execution_engine = ExecutionEngine()

        # monitors
        self.health_monitor = health_monitor
        self.recovery_engine = recovery_engine

        # 🧠 feedback engine init (NEW)
        self.feedback_engine = CausalFeedbackEngine(self.execution_engine) if CausalFeedbackEngine else None

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

        # 2. DAG Scheduling (CAUSAL)
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

        # 🧠 5. POST-CYCLE HEALTH + RECOVERY
        self._post_cycle_recovery()

        # 🧠 6. CAUSAL FEEDBACK LOOP (NEW CORE)
        self._apply_feedback(nodes, executed, blocked)

        return {
            "executed": executed,
            "blocked": blocked
        }

    # -------------------------------------------------
    # POST-CYCLE RECOVERY
    # -------------------------------------------------
    def _post_cycle_recovery(self):

        if not self.health_monitor or not self.recovery_engine:
            return

        try:
            probe_state = self.health_monitor.probe.run_probe()
            metric_state = self.health_monitor.metrics.snapshot()

            health_state = {
                **probe_state,
                **metric_state,
                "anomalies": []
            }

            self.recovery_engine.recover(health_state)

        except Exception as e:
            self._emit("recovery_failed", {"error": str(e)})

    # -------------------------------------------------
    # 🧠 FEEDBACK LOOP (NEW CORE)
    # -------------------------------------------------
    def _apply_feedback(self, nodes, executed, blocked):

        if not self.feedback_engine:
            return

        try:
            self.feedback_engine.learn(nodes, executed, blocked)
            self.feedback_engine.update_scheduler_bias()

        except Exception as e:
            self._emit("feedback_failed", {"error": str(e)})

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

        # 🧠 heartbeat
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