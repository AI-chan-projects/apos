from dataclasses import dataclass, asdict
from datetime import datetime
import json
import os
from typing import Any, Dict, List, Optional


@dataclass
class Event:
    id: str
    timestamp: str
    type: str
    payload: Dict[str, Any]
    source: str  # AIR / Kernel / Human / Policy
    status: str  # success / failed / pending

    def to_dict(self):
        return asdict(self)


class EventStore:
    def __init__(self, path: str = "data/events/event_log.jsonl"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    # -------------------------
    # Append API (core reality write)
    # -------------------------
    def append(self, event: Event):
        record = json.dumps(event.to_dict(), ensure_ascii=False)

        with open(self.path, "a", encoding="utf-8") as f:
            f.write(record + "\n")

    # -------------------------
    # Replay Engine
    # -------------------------
    def replay(self) -> List[Event]:
        if not os.path.exists(self.path):
            return []

        events: List[Event] = []

        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue

                data = json.loads(line.strip())

                event = Event(
                    id=data["id"],
                    timestamp=data["timestamp"],
                    type=data["type"],
                    payload=data["payload"],
                    source=data["source"],
                    status=data["status"],
                )

                events.append(event)

        return events

    # -------------------------
    # Query helpers
    # -------------------------
    def get_by_type(self, event_type: str) -> List[Event]:
        return [e for e in self.replay() if e.type == event_type]

    def last_event(self) -> Optional[Event]:
        events = self.replay()
        return events[-1] if events else None


if __name__ == "__main__":
    store = EventStore()

    event = Event(
        id="e1",
        timestamp=datetime.utcnow().isoformat(),
        type="goal_created",
        payload={"goal": "build APOS"},
        source="Human",
        status="success",
    )

    store.append(event)

    print(store.replay())