class DAGMemory:

    def __init__(self):
        self.history = []

    def store(self, dag, score):

        self.history.append({
            "dag": dag,
            "score": score
        })

    def get_best(self):

        if not self.history:
            return None

        return sorted(
            self.history,
            key=lambda x: x["score"],
            reverse=True
        )[0]