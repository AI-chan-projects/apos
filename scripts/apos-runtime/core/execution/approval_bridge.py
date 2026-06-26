from core.execution.resume_engine import ResumeEngine
from core.approval.approval_store import ApprovalStore


class ApprovalExecutionBridge:
    def __init__(self):
        self.resume_engine = ResumeEngine()
        self.approvals = ApprovalStore()

    def on_approval(self, approval_id):
        return self.resume_engine.resume(approval_id)