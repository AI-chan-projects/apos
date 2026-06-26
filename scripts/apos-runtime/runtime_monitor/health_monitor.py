from runtime_monitor.system_probe import SystemProbe
from runtime_monitor.metrics_collector import MetricsCollector
from runtime_monitor.anomaly_detector import AnomalyDetector
from runtime_monitor.recovery_hooks import RecoveryHooks


class RuntimeHealthMonitor:

    def __init__(self):
        self.probe = SystemProbe()
        self.metrics = MetricsCollector()
        self.detector = AnomalyDetector()
        self.recovery = RecoveryHooks()

    def tick(self):

        probe_state = self.probe.run_probe()
        metric_state = self.metrics.snapshot()

        anomalies = self.detector.detect(probe_state, metric_state)

        if anomalies:
            print("[HEALTH] anomalies detected:", anomalies)
            self.recovery.handle(anomalies)

        return {
            "probe": probe_state,
            "metrics": metric_state,
            "anomalies": anomalies
        }

    def record_event(self):
        self.metrics.increment_events()