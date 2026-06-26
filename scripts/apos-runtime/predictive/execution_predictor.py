from core.event_store.event_store import EventStore


class ExecutionPredictor:

    def __init__(self):
        self.store = EventStore()

    # -----------------------------------------
    # STEP 1: feature extraction from DAG
    # -----------------------------------------
    def extract_features(self, nodes):

        return {
            "node_count": len(nodes),
            "high_priority_nodes": sum(1 for n in nodes if n.priority > 5),
            "blocked_risk": sum(1 for n in nodes if n.status == "BLOCKED"),
        }

    # -----------------------------------------
    # STEP 2: naive risk scoring model
    # -----------------------------------------
    def predict_risk(self, nodes):

        f = self.extract_features(nodes)

        score = 0

        # simple heuristics (v1 model)
        score += f["blocked_risk"] * 3
        score += f["high_priority_nodes"] * 1
        score += f["node_count"] * 0.1

        return min(score, 10)

    # -----------------------------------------
    # STEP 3: decision layer
    # -----------------------------------------
    def should_execute(self, nodes):

        risk = self.predict_risk(nodes)

        return {
            "risk_score": risk,
            "safe_to_execute": risk < 5
        }