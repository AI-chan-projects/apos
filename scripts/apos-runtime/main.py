from datetime import datetime
import uuid

from core.event_store.event_store import EventStore, Event


# -------------------------
# Minimal AIR Generator
# -------------------------
def generate_air(goal: str):
    """
    Minimal AIR model:
    Goal → Tasks → Actions
    """

    return {
        "objective": goal,
        "tasks": [
            {
                "name": "process_goal",
                "actions": [
                    {
                        "type": "log",
                        "payload": {"msg": f"processing goal: {goal}"},
                    }
                ],
            }
        ],
    }


# -------------------------
# Policy Engine (minimal rule-based)
# -------------------------
def evaluate_policy(action):
    """
    Returns:
        ALLOW / APPROVE
    """

    if action["type"] == "log":
        return "ALLOW"

    return "APPROVE"


# -------------------------
# Kernel Executor (deterministic single action execution)
# -------------------------
def execute_action(action):
    """
    Converts Action → Event
    """

    return Event(
        id=str(uuid.uuid4()),
        timestamp=datetime.utcnow().isoformat(),
        type=f"action_{action['type']}",
        payload=action.get("payload", {}),
        source="Kernel",
        status="success",
    )


# -------------------------
# APOS Execution Unit (NO LOOP HERE)
# -------------------------
def run_once(goal: str):
    store = EventStore()

    # 1. AIR 생성
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

    # 2. Action flatten
    actions = []
    for task in air["tasks"]:
        actions.extend(task["actions"])

    executed = []
    rejected = []

    # 3. Policy + Kernel execution (single pass)
    for action in actions:
        decision = evaluate_policy(action)

        store.append(
            Event(
                id=str(uuid.uuid4()),
                timestamp=datetime.utcnow().isoformat(),
                type="policy_evaluated",
                payload={
                    "action": action,
                    "decision": decision,
                },
                source="Policy",
                status="success",
            )
        )

        if decision == "ALLOW":
            event = execute_action(action)
            store.append(event)
            executed.append(action["type"])

        else:
            rejected.append(action["type"])

    # 4. Result summary event
    summary = {
        "goal": goal,
        "executed": executed,
        "rejected": rejected,
        "total_events": len(store.replay()),
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


# -------------------------
# Optional CLI entry (not main runtime anymore)
# -------------------------
if __name__ == "__main__":
    result = run_once("boot APOS system")

    print("\nAPOS EXECUTION RESULT")
    print("======================")
    for k, v in result.items():
        print(f"{k}: {v}")