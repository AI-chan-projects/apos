from bootstrap.validator import EnvironmentValidator
from bootstrap.installer import Installer
import subprocess


class BootstrapRunner:

    def __init__(self):
        self.validator = EnvironmentValidator()
        self.installer = Installer()

    def run(self):

        print("[BOOT] validating environment...")

        result = self.validator.validate()

        if not result["ok"]:
            print("[BOOT] fixing environment...")

            if result["missing_modules"]:
                self.installer.install_missing(result["missing_modules"])

        print("[BOOT] launching APOS runtime...")

        subprocess.run([
            "python",
            "runtime/main.py"
        ])