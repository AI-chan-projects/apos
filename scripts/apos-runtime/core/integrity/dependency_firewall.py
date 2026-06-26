# core/integrity/dependency_firewall.py

import ast
import os


class DependencyFirewall:

    """
    Enforces APOS architectural boundaries at import level
    """

    RULES = {
        "ui": ["core"],        # UI can read core
        "core": [],            # core cannot depend on ui
        "execution": ["core"],
        "causal": [],          # causal must be pure
    }

    def check_file(self, filepath: str):

        with open(filepath, "r") as f:
            tree = ast.parse(f.read())

        violations = []

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""

                for layer, allowed in self.RULES.items():
                    if layer in filepath:
                        for forbidden in self._detect_forbidden(module, allowed):
                            violations.append({
                                "file": filepath,
                                "import": module,
                                "violation": forbidden
                            })

        return violations

    def _detect_forbidden(self, module, allowed):
        for rule in allowed:
            if rule not in module:
                return [f"illegal dependency: {module}"]
        return []