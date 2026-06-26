import subprocess


class RecoveryHooks:

    def restart_runtime(self):

        subprocess.run([
            "python",
            "runtime/main.py"
        ])

    def soft_recover(self):
        print("[RECOVERY] soft recovery triggered")

    def handle(self, anomalies):

        if "CPU_FAILURE" in anomalies:
            print("[RECOVERY] restarting runtime")
            self.restart_runtime()

        if "NO_ACTIVITY" in anomalies:
            self.soft_recover()