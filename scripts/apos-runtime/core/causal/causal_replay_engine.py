from core.event_store.event_replay_engine import EventReplayEngine
from core.causal.causal_trace_linker import CausalTraceLinker


class CausalReplayEngine:

    def __init__(self):
        self.replay_engine = EventReplayEngine()
        self.linker = CausalTraceLinker()

    # -----------------------------------------
    # STEP 1: replay raw execution timeline
    # -----------------------------------------
    def replay(self):

        events = self.replay_engine.replay()

        return events

    # -----------------------------------------
    # STEP 2: causal reconstruction
    # -----------------------------------------
    def reconstruct(self):

        events = self.replay()

        causal_graph = self.linker.link(events)

        return causal_graph

    # -----------------------------------------
    # STEP 3: WHY ANALYSIS
    # -----------------------------------------
    def explain_failure(self, target_event_id=None):

        graph = self.reconstruct()

        explanation = {
            "root_causes": [],
            "propagation_chain": [],
            "event": target_event_id
        }

        for node, data in graph.items():

            for e in data["events"]:

                if "failure" in e["type"] or "blocked" in e["type"]:
                    explanation["root_causes"].append(node)

        return explanation