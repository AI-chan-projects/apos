from causal.event_correlation_matrix import EventCorrelationMatrix
from causal.causal_chain_builder import CausalChainBuilder
from causal.root_cause_ranker import RootCauseRanker
from causal.failure_explainer import FailureExplainer


class FailureAttributionEngine:

    def __init__(self):
        self.matrix = EventCorrelationMatrix()
        self.chain_builder = CausalChainBuilder()
        self.ranker = RootCauseRanker()
        self.explainer = FailureExplainer()

    def analyze(self, failure_event_type):

        # 1. correlation map
        correlation = self.matrix.build()

        # 2. causal chain
        chain = self.chain_builder.build_chain(failure_event_type)

        # 3. rank causes
        ranked = self.ranker.rank(chain)

        # 4. explanation
        explanation = self.explainer.explain(ranked)

        return {
            "correlation": correlation,
            "chain": chain,
            "ranked_causes": ranked,
            "explanation": explanation
        }