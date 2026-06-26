from core.execution.causal_dag_scheduler import CausalDAGScheduler

class Scheduler:

    def __init__(self, nodes):
        self.causal = CausalDAGScheduler(nodes)

    def resolve(self):
        return self.causal.resolve()