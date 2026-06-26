import uuid
from datetime import datetime


class ApprovalStore:
    def __init__(self):
        self.pending = {}
        self.history = {}

    def create_request(self, action, context):
        approval_id = str(uuid.uuid4())

        self.pending[approval_id] = {
            "id": approval_id,
            "action": action,
            "context": context,
            "status": "PENDING",
            "created_at": datetime.utcnow().isoformat(),
        }

        return approval_id

    def approve(self, approval_id):
        return self._resolve(approval_id, "APPROVED")

    def reject(self, approval_id):
        return self._resolve(approval_id, "REJECTED")

    def _resolve(self, approval_id, status):
        if approval_id not in self.pending:
            return None

        item = self.pending.pop(approval_id)
        item["status"] = status
        item["resolved_at"] = datetime.utcnow().isoformat()

        self.history[approval_id] = item

        return item

    def get(self, approval_id):
        return self.history.get(approval_id)
    

approval_store = ApprovalStore()