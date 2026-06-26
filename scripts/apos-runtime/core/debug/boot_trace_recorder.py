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
            "ordered": [n.name for n in ordered_nodes],
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

    def _node(self, n):
        return {
            "id": getattr(n, "id", None),
            "name": n.name,
            "status": n.status,
            "priority": getattr(n, "priority", 0),
        }

    def _hash(self, obj):
        raw = json.dumps(obj, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()