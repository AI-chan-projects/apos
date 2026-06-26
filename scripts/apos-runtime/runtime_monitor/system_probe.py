import os
import sys


class SystemProbe:

    def check_cpu_alive(self):
        return True  # placeholder (OS-level hook later)

    def check_memory_state(self):
        return True

    def check_runtime_process(self):
        return os.getpid() is not None

    def run_probe(self):

        return {
            "cpu": self.check_cpu_alive(),
            "memory": self.check_memory_state(),
            "process": self.check_runtime_process()
        }