from datetime import datetime
import uuid
import argparse

from core.control_plane.orchestrator import APOSOrchestrator


# =================================================
# 🧠 BOOTSTRAP
# =================================================

orchestrator = APOSOrchestrator()


# =================================================
# 🧠 CLI ENTRY
# =================================================

def build_air(goal: str):
    """
    Legacy AIR generator (for boot testing)
    """
    return {
        "objective": goal,
        "tasks": [
            {
                "name": "process_goal",
                "actions": [
                    {"type": "log", "payload": {"msg": f"processing {goal}"}},
                    {"type": "write", "payload": {"file": "output.txt"}},
                ],
            }
        ],
    }


# =================================================
# 🧠 MAIN EXECUTION PIPELINE
# =================================================

def run(goal: str):
    """
    APOS Unified Execution Entry
    """

    air = build_air(goal)

    print("\n🚀 [APOS BOOT] starting orchestrator...\n")

    result = orchestrator.run_once(air)

    print("\n==============================")
    print("🧠 APOS EXECUTION COMPLETE")
    print("==============================")
    print(result)

    return result


# =================================================
# 🧠 CLI INTERFACE
# =================================================

def main():
    parser = argparse.ArgumentParser(description="APOS Runtime Entry")

    parser.add_argument(
        "--goal",
        type=str,
        default="test_execution",
        help="Execution goal for APOS",
    )

    args = parser.parse_args()

    run(args.goal)


# =================================================
# 🧠 ENTRY POINT (SINGLE SOURCE OF TRUTH)
# =================================================

if __name__ == "__main__":
    main()