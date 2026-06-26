from core.execution.dag_memory import DAGMemory
from core.event_store.event_store import EventStore


class CausalFeedbackEngine:

    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.memory = DAGMemory()
        self.store = EventStore()

    # ---------------------------------------
    # STEP 1: evaluate execution quality
    # ---------------------------------------
    def evaluate_run(self, executed, blocked):

        score = len(executed) - len(blocked) * 2

        return max(score, 0)

    # ---------------------------------------
    # STEP 2: store experience
    # ---------------------------------------
    def learn(self, dag_nodes, executed, blocked):

        score = self.evaluate_run(executed, blocked)

        self.memory.store(dag_nodes, score)

    # ---------------------------------------
    # STEP 3: update scheduler bias
    # ---------------------------------------
    def update_scheduler_bias(self):

        best = self.memory.get_best()

        if not best:
            return

        best_dag = best["dag"]

        # inject bias into scheduler
        self.scheduler.set_reference_dag(best_dag)