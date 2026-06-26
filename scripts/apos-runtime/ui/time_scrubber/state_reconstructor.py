from ui.time_scrubber.time_engine import TimeEngine


class StateReconstructor:

    def __init__(self):
        self.engine = TimeEngine()

    def reconstruct(self, timestamp: str):
        """
        Full system snapshot at time T
        """

        return self.engine.get_state_at(timestamp)