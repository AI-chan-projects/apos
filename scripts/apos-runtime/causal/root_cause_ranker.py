class RootCauseRanker:

    def rank(self, chain):

        scores = {}

        for node in chain:

            event_type = node["event"]

            scores[event_type] = scores.get(event_type, 0) + 1

        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )