from datetime import datetime
import uuid

from core.event_store.event_store import EventStore, Event
from core.policy.evaluator import evaluate_policy
from core.approval.approval_store import ApprovalStore


approval_store = ApprovalStore()


def generate_air(goal: str):
    return {
        "objective": goal,
        "tasks": [
            {
                "name": "process_goal",
                "actions": [
                    {"type": "log", "payload": {"msg": f"processing {goal}"}},
                    {"type": "write", "payload": {"file": "output.txt"}},
                ],
            }
        ],
    }


def execute_action(action):
    return Event(
        id=str(uuid.uuid4()),
        timestamp=datetime.utcnow().isoformat(),
        type=f"action_{action['type']}",
        payload=action.get("payload", {}),
        source="Kernel",
        status="success",
    )


def run_once(goal: str):
    store = EventStore()

    air = generate_air(goal)

    store.append(
        Event(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            type="air_generated",
            payload=air,
            source="AIR",
            status="success",
        )
    )

    actions = []
    for task in air["tasks"]:
        actions.extend(task["actions"])

    executed = []
    pending = []

    for action in actions:
        decision = evaluate_policy(action)

        if decision == "APPROVE_REQUIRED":
            approval_id = approval_store.create_request(
                action=action,
                context={"goal": goal},
            )

            store.append(
                Event(
                    id=str(uuid.uuid4()),
                    timestamp=datetime.utcnow().isoformat(),
                    type="approval_requested",
                    payload={
                        "approval_id": approval_id,
                        "action": action,
                    },
                    source="Policy",
                    status="pending",
                )
            )

            pending.append(approval_id)
            continue

        store.append(
            Event(
                id=str(uuid.uuid4()),
                timestamp=datetime.utcnow().isoformat(),
                type="policy_evaluated",
                payload={"action": action, "decision": decision},
                source="Policy",
                status="success",
            )
        )

        if decision == "ALLOW":
            event = execute_action(action)
            store.append(event)
            executed.append(action["type"])

    summary = {
        "goal": goal,
        "executed": executed,
        "pending_approvals": pending,
    }

    store.append(
        Event(
            id=str(uuid.uuid4()),
            timestamp=datetime.utcnow().isoformat(),
            type="execution_summary",
            payload=summary,
            source="Kernel",
            status="success",
        )
    )

    return summary