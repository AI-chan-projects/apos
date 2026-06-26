from core.event_store.event_store import EventStore, Event
from datetime import datetime
import uuid


class ExecutionEngine:
    def __init__(self):
        self.store = EventStore()

    def execute(self, nodes):
        """
        Executes DAG in resolved order
        """

        results = []

        for node in nodes:

            if node.status == "BLOCKED":
                continue

            for action in node.actions:

                event = Event(
                    id=str(uuid.uuid4()),
                    timestamp=datetime.utcnow().isoformat(),
                    type=f"execute_{action['type']}",
                    payload=action,
                    source="ExecutionEngine",
                    status="success",
                )

                self.store.append(event)

            node.status = "DONE"
            results.append(node.name)

        return results