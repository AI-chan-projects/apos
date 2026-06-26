from core.event_store.event_replay_engine import EventReplayEngine


class TimeEngine:

    def __init__(self):
        self.replay = EventReplayEngine()

    def get_state_at(self, timestamp: str):
        """
        Reconstruct system state at a given time
        """

        events = self.replay.replay_all()

        state = {
            "air": None,
            "tasks": {},
            "executed": [],
            "blocked": [],
            "current_time": timestamp
        }

        for e in events:

            if e.timestamp > timestamp:
                break

            if e.type == "air_generated":
                state["air"] = e.payload

            elif "node_executing" in e.type:
                state["executed"].append(e.payload)

            elif "node_blocked" in e.type:
                state["blocked"].append(e.payload)

        return state