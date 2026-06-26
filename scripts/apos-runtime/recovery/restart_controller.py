import subprocess


class RestartController:

    def hard_restart(self):

        subprocess.run([
            "python",
            "runtime/main.py"
        ])

    def soft_restart(self):
        print("[RECOVERY] soft restart triggered")