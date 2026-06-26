import time


class MetricsCollector:

    def __init__(self):
        self.start_time = time.time()
        self.event_count = 0

    def increment_events(self):
        self.event_count += 1

    def uptime(self):
        return time.time() - self.start_time

    def snapshot(self):

        return {
            "uptime": self.uptime(),
            "events": self.event_count
        }