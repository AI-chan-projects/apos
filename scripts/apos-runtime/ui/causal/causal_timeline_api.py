from ui.causal_timeline.causal_bind_service import CausalBindService


class CausalTimelineAPI:

    def __init__(self):
        self.service = CausalBindService()

    def get_timeline(self):
        return self.service.get_bound_timeline()

    def get_causal_view(self):
        return self.service.linker.link(
            self.service.store.replay()
        )