class AnomalyDetector:

    def detect(self, probe, metrics):

        anomalies = []

        if not probe["cpu"]:
            anomalies.append("CPU_FAILURE")

        if not probe["memory"]:
            anomalies.append("MEMORY_FAILURE")

        if metrics["events"] == 0:
            anomalies.append("NO_ACTIVITY")

        return anomalies