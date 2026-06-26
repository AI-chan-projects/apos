class FailureExplainer:

    def explain(self, ranked_causes):

        if not ranked_causes:
            return "No causal signal detected"

        top = ranked_causes[0]

        return {
            "primary_cause": top[0],
            "confidence": top[1],
            "explanation": f"{top[0]} occurred most frequently before failure"
        }