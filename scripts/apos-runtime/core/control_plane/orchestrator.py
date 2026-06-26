from core.air.task_graph_builder import TaskGraphBuilder
from runtime.scheduler.scheduler import Scheduler as CausalDAGScheduler
from core.execution.dag_executor import DAGSExecutor
from core.event_store.event_store import EventStore, Event
from core.evolution.dag_evolver import DAGEvolver
from core.approval.approval_store import approval_store
from core.debug.boot_trace_recorder import BootTraceRecorder
from datetime import datetime
import uuid
import asyncio


# =================================================
# 🔥 EVENT STREAM LAYER (SYNC + ASYNC SAFE WRAPPER)
# =================================================
class SafeEventStream:

    def __init__(self, stream):
        self.stream = stream

    def push(self, payload):
        """
        Safe dispatch layer:
        - async loop 있으면 create_task
        - 없으면 ignore safely
        """
        if not self.stream:
            return

        try:
            asyncio.get_running_loop()
            asyncio.create_task(self.stream.push_event(payload))
        except RuntimeError:
            # no running loop → silent fallback
            pass


# -------------------------------------------------
# 🔥 Live Stream Hook
# -------------------------------------------------
try:
    from ui.live.event_stream import EventStream
    from ui.live.websocket_manager import WebSocketManager

    ws_manager = WebSocketManager()
    _raw_stream = EventStream(ws_manager)
    global_event_stream = SafeEventStream(_raw_stream)

except:
    global_event_stream = None


# -------------------------------------------------
# 🧠 Runtime Health Monitor
# -------------------------------------------------
try:
    from runtime_monitor.health_monitor import RuntimeHealthMonitor
    health_monitor = RuntimeHealthMonitor()
except:
    health_monitor = None


# -------------------------------------------------
# 🧠 Failure Recovery Engine
# -------------------------------------------------
try:
    from recovery.recovery_orchestrator import FailureAutoRecoveryEngine
    recovery_engine = FailureAutoRecoveryEngine()
except:
    recovery_engine = None


# -------------------------------------------------
# 🧠 Causal Feedback Engine
# -------------------------------------------------
try:
    from core.evolution.causal_feedback_engine import CausalFeedbackEngine
except:
    CausalFeedbackEngine = None


# =================================================
# 🧠 EXECUTION PREDICTOR
# =================================================
class ExecutionPredictor:

    def extract_features(self, nodes):
        nodes = list(nodes.values()) if isinstance(nodes, dict) else nodes

        return {
            "node_count": len(nodes),
            "high_priority_nodes": sum(1 for n in nodes if getattr(n, "priority", 0) > 5),
            "blocked_risk": sum(1 for n in nodes if getattr(n, "status", None) == "BLOCKED"),
        }

    def predict_risk(self, nodes):
        f = self.extract_features(nodes)

        score = (
            f["blocked_risk"] * 3 +
            f["high_priority_nodes"] * 1 +
            f["node_count"] * 0.1
        )

        return min(score, 10)

    def should_execute(self, nodes):
        risk = self.predict_risk(nodes)
        return {
            "risk_score": risk,
            "safe_to_execute": risk < 5
        }


# =================================================
# 🧠 APOS ORCHESTRATOR CORE
# =================================================
class APOSOrchestrator:

    def __init__(self):

        self.store = EventStore()

        self.health_monitor = health_monitor
        self.recovery_engine = recovery_engine

        self.feedback_engine = (
            CausalFeedbackEngine(self) if CausalFeedbackEngine else None
        )

        self.predictor = ExecutionPredictor()
        self.dag_executor = DAGSExecutor()
        self.evolver = DAGEvolver()

        self.boot_recorder = BootTraceRecorder()

        self._reference_dag = None

    # -------------------------------------------------
    # COMPATIBILITY HOOK
    # -------------------------------------------------
    def set_reference_dag(self, dag):
        self._reference_dag = dag

    # -------------------------------------------------
    # MAIN EXECUTION LOOP
    # -------------------------------------------------
    def run_once(self, air: dict):

        self._emit("orchestrator_start", {"air": air})

        # 1. BUILD TASK GRAPH
        builder = TaskGraphBuilder().build_from_air(air)
        builder.attach_approval_flags(self._policy_engine)

        node_map = builder.get_nodes()
        nodes = list(node_map.values())

        self._emit("task_graph_built", {"nodes": len(nodes)})

        # 2. PREDICTION
        prediction = self.predictor.should_execute(nodes)
        self._emit("execution_prediction", prediction)

        if not prediction["safe_to_execute"]:
            self._emit("execution_blocked_by_predictor", prediction)
            return {
                "executed": [],
                "blocked": [n.name for n in nodes],
                "prediction": prediction
            }

        # 3. SCHEDULING
        scheduler = CausalDAGScheduler(nodes)
        ordered_nodes = scheduler.resolve()

        self._emit("dag_scheduled", {"count": len(ordered_nodes)})

        self.set_reference_dag(ordered_nodes)

        # 4. EXECUTION
        result = self.dag_executor.execute(ordered_nodes)

        executed = result.get("executed", [])
        blocked = result.get("blocked", [])

        self._emit("execution_complete", {
            "executed": executed,
            "blocked": blocked
        })

        # 5. POST SYSTEMS
        self._post_cycle_recovery()
        self._apply_feedback(nodes, executed, blocked)
        self._apply_evolution(nodes, executed, blocked)

        # 6. BOOT TRACE
        signature = self.boot_recorder.record(
            air=air,
            nodes=[self._normalize(n) for n in nodes],
            ordered_nodes=[self._normalize(n) for n in ordered_nodes],
            executed=executed,
            blocked=blocked
        )

        self._emit("boot_trace_recorded", {"signature": signature})

        return {
            "executed": executed,
            "blocked": blocked,
            "prediction": prediction
        }

    # -------------------------------------------------
    # NODE NORMALIZATION (UNIFIED CONTRACT)
    # -------------------------------------------------
    def _normalize(self, node):
        return {
            "id": getattr(node, "id", None),
            "name": getattr(node, "name", str(node)),
            "status": getattr(node, "status", None),
            "priority": getattr(node, "priority", 0),
        }

    # -------------------------------------------------
    # RECOVERY
    # -------------------------------------------------
    def _post_cycle_recovery(self):

        if not (self.health_monitor and self.recovery_engine):
            return

        try:
            health_state = {
                **self.health_monitor.probe.run_probe(),
                **self.health_monitor.metrics.snapshot(),
                "anomalies": []
            }

            self.recovery_engine.recover(health_state)

        except Exception as e:
            self._emit("recovery_failed", {"error": str(e)})

    # -------------------------------------------------
    # FEEDBACK
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
    # EVOLUTION
    # -------------------------------------------------
    def _apply_evolution(self, nodes, executed, blocked):

        try:
            new_nodes = self.evolver.evolve(nodes, executed, blocked)

            self._emit("dag_evolved", {
                "old_count": len(nodes),
                "new_count": len(new_nodes)
            })

        except Exception as e:
            self._emit("evolution_failed", {"error": str(e)})

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
    # EVENT EMITTER (FULL SAFE MODE)
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

        if self.health_monitor:
            self.health_monitor.record_event()

        if global_event_stream:
            global_event_stream.push({
                "id": event.id,
                "timestamp": event.timestamp,
                "type": event.type,
                "payload": event.payload,
                "source": event.source,
                "status": event.status
            })