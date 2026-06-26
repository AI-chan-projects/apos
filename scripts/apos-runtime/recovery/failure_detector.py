class FailureDetector:

    def detect(self, health_state):

        failures = []

        if health_state.get("cpu") is False:
            failures.append("CPU_FAILURE")

        if health_state.get("memory") is False:
            failures.append("MEMORY_FAILURE")

        if "NO_ACTIVITY" in health_state.get("anomalies", []):
            failures.append("STALL_FAILURE")

        return failures