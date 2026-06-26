import json
import hashlib
from datetime import datetime
from core.event_store.event_store import Event, EventStore
import uuid


class BootTraceRecorder:

    def __init__(self):
        self.store = EventStore()

    def record(self, air, nodes, ordered_nodes, executed, blocked):

        trace = {
            "timestamp": datetime.utcnow().isoformat(),
            "air": air,
            "nodes": [self._node(n) for n in nodes],
            "ordered": [self._node_name(n) for n in ordered_nodes],
            "executed": executed,
            "blocked": blocked,
        }

        signature = self._hash(trace)

        event = Event(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            type="boot_trace_recorded",
            payload={
                "signature": signature,
                "trace": trace
            },
            source="BootTraceRecorder",
            status="success",
        )

        self.store.append(event)

        return signature

    # -------------------------------------------------
    # 🧠 NODE NORMALIZATION (DICT-FIRST SAFE)
    # -------------------------------------------------
    def _node(self, n):

        if isinstance(n, dict):
            return {
                "id": n.get("id"),
                "name": n.get("name"),
                "status": n.get("status"),
                "priority": n.get("priority", 0),
            }

        return {
            "id": getattr(n, "id", None),
            "name": getattr(n, "name", None),
            "status": getattr(n, "status", None),
            "priority": getattr(n, "priority", 0),
        }

    # -------------------------------------------------
    # 🧠 NODE NAME SAFE EXTRACTION
    # -------------------------------------------------
    def _node_name(self, n):
        if isinstance(n, dict):
            return n.get("name")
        return getattr(n, "name", None)

    # -------------------------------------------------
    # 🧠 STABLE HASH
    # -------------------------------------------------
    def _hash(self, obj):
        raw = json.dumps(obj, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()