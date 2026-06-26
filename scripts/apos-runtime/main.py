from datetime import datetime
import uuid
import time

from core.event_store.event_store import EventStore, Event


# -------------------------
# Minimal AIR Generator (stub)
# -------------------------
def generate_air(goal: str):
    """
    Minimal AIR:
    Goal → Tasks → Actions (very simplified)
    """

    return {
        "objective": goal,
        "tasks": [
            {
                "name": "initialize_system",
                "actions": [
                    {"type": "log", "payload": {"msg": "APOS initialized"}}
                ],
            }
        ],
    }


# -------------------------
# Policy Engine (minimal stub)
# -------------------------
def evaluate_policy(action):
    """
    Very minimal rule-based policy
    """

    if action["type"] == "log":
        return "ALLOW"

    return "APPROVE"


# -------------------------
# Kernel Executor (single worker)
# -------------------------
def execute_action(action):
    """
    Executes action and returns event
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
# APOS Heartbeat Loop
# -------------------------
def run():
    store = EventStore()

    # Step 1: Human Intent (hardcoded MVP)
    goal = "boot APOS system"

    print(f"[HUMAN] Goal received: {goal}")

    # Step 2: AIR generation
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

    print("[AIR] Generated")

    # Step 3: Flatten actions
    actions = []
    for task in air["tasks"]:
        actions.extend(task["actions"])

    # Step 4: Execution loop (heartbeat)
    while True:
        print("\n[HEARTBEAT] ticking...")

        for action in actions:
            decision = evaluate_policy(action)

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

                print(f"[KERNEL] executed: {action['type']}")

            else:
                print(f"[POLICY] blocked: {action['type']}")

        # single-pass heartbeat for MVP
        print("[HEARTBEAT] cycle complete")
        break

    # Step 5: Final state output
    print("\n[EVENT STORE SNAPSHOT]")
    for e in store.replay():
        print(e)


# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    run()