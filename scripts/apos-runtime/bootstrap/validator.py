import sys
import importlib


class EnvironmentValidator:

    REQUIRED_MODULES = [
        "fastapi",
        "uuid",
        "datetime"
    ]

    def check_python_version(self):
        return sys.version_info >= (3, 9)

    def check_modules(self):
        missing = []

        for module in self.REQUIRED_MODULES:
            try:
                importlib.import_module(module)
            except ImportError:
                missing.append(module)

        return missing

    def validate(self):
        result = {
            "python_ok": self.check_python_version(),
            "missing_modules": self.check_modules()
        }

        result["ok"] = (
            result["python_ok"] and len(result["missing_modules"]) == 0
        )

        return result