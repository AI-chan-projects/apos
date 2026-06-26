from recovery.failure_detector import FailureDetector
from recovery.replay_engine import ReplayEngine
from recovery.state_reconstructor import StateReconstructor
from recovery.restart_controller import RestartController


class FailureAutoRecoveryEngine:

    def __init__(self):
        self.detector = FailureDetector()
        self.replay = ReplayEngine()
        self.reconstructor = StateReconstructor()
        self.controller = RestartController()

    def recover(self, health_state):

        failures = self.detector.detect(health_state)

        if not failures:
            return {"status": "ok"}

        print("[RECOVERY] failures detected:", failures)

        # 1. replay event history
        events = self.replay.replay()

        # 2. reconstruct state
        state = self.reconstructor.rebuild(events)

        print("[RECOVERY] reconstructed state:", state)

        # 3. decision logic
        if "CPU_FAILURE" in failures:
            print("[RECOVERY] hard restart triggered")
            self.controller.hard_restart()

        else:
            self.controller.soft_restart()

        return {
            "status": "recovered",
            "failures": failures,
            "state": state
        }