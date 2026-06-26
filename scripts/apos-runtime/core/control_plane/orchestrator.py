from core.air.task_graph_builder import TaskGraphBuilder
from runtime.scheduler.scheduler import Scheduler as CausalDAGScheduler
from core.execution.dag_executor import DAGSExecutor   # 🔥 SINGLE WORKER EXECUTOR
from core.event_store.event_store import EventStore, Event
from core.evolution.dag_evolver import DAGEvolver
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


# 🧠 Causal Feedback Engine
try:
    from core.evolution.causal_feedback_engine import CausalFeedbackEngine
except:
    CausalFeedbackEngine = None


# -------------------------------------------------
# 🧠 Execution Predictor (Light Risk Gate)
# -------------------------------------------------
class ExecutionPredictor:

    def __init__(self):
        self.store = EventStore()

    def extract_features(self, nodes):
        return {
            "node_count": len(nodes),
            "high_priority_nodes": sum(1 for n in nodes if n.priority > 5),
            "blocked_risk": sum(1 for n in nodes if n.status == "BLOCKED"),
        }

    def predict_risk(self, nodes):
        f = self.extract_features(nodes)

        score = 0
        score += f["blocked_risk"] * 3
        score += f["high_priority_nodes"] * 1
        score += f["node_count"] * 0.1

        return min(score, 10)

    def should_execute(self, nodes):
        risk = self.predict_risk(nodes)

        return {
            "risk_score": risk,
            "safe_to_execute": risk < 5
        }


# =================================================
# 🧠 APOS ORCHESTRATOR (SINGLE WORKER CORE)
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

        # 🔥 SINGLE WORKER EXECUTION CORE (ADR-001 ENFORCED)
        self.dag_executor = DAGSExecutor()

        self.evolver = DAGEvolver()

    # -------------------------------------------------
    # MAIN LOOP (DETERMINISTIC SINGLE PASS)
    # -------------------------------------------------
    def run_once(self, air: dict):

        self._emit("orchestrator_start", {"air": air})

        # 1. BUILD TASK GRAPH
        builder = TaskGraphBuilder().build_from_air(air)
        builder.attach_approval_flags(self._policy_engine)

        nodes = builder.get_nodes()

        self._emit("task_graph_built", {"nodes": len(nodes)})

        # -------------------------------------------------
        # 🧠 PREDICTIVE SAFETY GATE
        # -------------------------------------------------
        prediction = self.predictor.should_execute(nodes)

        self._emit("execution_prediction", prediction)

        if not prediction["safe_to_execute"]:
            self._emit("execution_blocked_by_predictor", prediction)

            return {
                "executed": [],
                "blocked": [n.name for n in nodes],
                "prediction": prediction
            }

        # -------------------------------------------------
        # 2. CAUSAL DAG SCHEDULING
        # -------------------------------------------------
        scheduler = CausalDAGScheduler(nodes)
        ordered_nodes = scheduler.resolve()

        self._emit("dag_scheduled", {"count": len(ordered_nodes)})

        # -------------------------------------------------
        # 3. SINGLE WORKER EXECUTION (CRITICAL)
        # -------------------------------------------------
        result = self.dag_executor.execute(ordered_nodes)

        executed = result.get("executed", [])
        blocked = result.get("blocked", [])

        self._emit("execution_complete", {
            "executed": executed,
            "blocked": blocked
        })

        # -------------------------------------------------
        # 4. POST-CYCLE SYSTEMS
        # -------------------------------------------------
        self._post_cycle_recovery()
        self._apply_feedback(nodes, executed, blocked)
        self._apply_evolution(nodes, executed, blocked)

        return {
            "executed": executed,
            "blocked": blocked,
            "prediction": prediction
        }

    # -------------------------------------------------
    # 🧠 POST-CYCLE RECOVERY
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
    # 🧠 FEEDBACK LOOP (CAUSAL LEARNING)
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
    # 🧠 DAG EVOLUTION LOOP
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
    # 🧠 POLICY ENGINE
    # -------------------------------------------------
    def _policy_engine(self, action):
        if action["type"] == "log":
            return "ALLOW"

        if action["type"] in ["write", "delete"]:
            return "APPROVE_REQUIRED"

        return "ALLOW"

    # -------------------------------------------------
    # 📡 EVENT EMITTER (SOURCE OF TRUTH)
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

        self._emit_live(event)

    # -------------------------------------------------
    # 🌐 LIVE STREAM LAYER (UI BINDING)
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