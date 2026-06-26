from core.approval.approval_store import approval_store
from core.event_store.event_store import EventStore, Event
from datetime import datetime
import uuid


class ResumeEngine:
    def __init__(self):
        self.store = EventStore()
        self.approvals = approval_store  # ⭐ singleton 공유

    def resume(self, approval_id):
        approval = self.approvals.get(approval_id)

        if not approval:
            return {"status": "not_found"}

        if approval["status"] != "APPROVED":
            return {"status": "not_approved"}

        action = approval["action"]

        event = Event(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            type=f"resumed_action_{action['type']}",
            payload=action,
            source="Kernel",
            status="success",
        )

        self.store.append(event)

        return {
            "status": "resumed",
            "action": action["type"],
        }