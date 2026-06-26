from core.causal.causal_graph_builder import CausalGraphBuilder
from core.causal.causal_trace_engine import CausalTraceEngine


class CausalViewer:
    """
    UI-facing abstraction over causal core engine
    """

    def __init__(self):
        self.builder = CausalGraphBuilder()
        self.trace = CausalTraceEngine()

    def graph(self):
        """
        Returns causal graph for UI rendering
        """
        return self.builder.build()

    def trace_event(self, event_id: str):
        """
        Returns causal chain for selected event
        """
        return self.trace.trace_back(event_id)