import uuid
from datetime import datetime


class ApprovalStore:
    """
    Human Director approval queue (minimal persistent in-memory version)
    """

    def __init__(self):
        self.pending = {}

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
        if approval_id in self.pending:
            self.pending[approval_id]["status"] = "APPROVED"
            return self.pending[approval_id]

        return None

    def reject(self, approval_id):
        if approval_id in self.pending:
            self.pending[approval_id]["status"] = "REJECTED"
            return self.pending[approval_id]

        return None

    def get(self, approval_id):
        return self.pending.get(approval_id)