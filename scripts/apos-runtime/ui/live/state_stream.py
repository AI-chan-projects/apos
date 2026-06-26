from core.execution.orchestrator import APOSOrchestrator


class StateStream:

    def __init__(self, ws_manager):
        self.ws = ws_manager
        self.orchestrator = APOSOrchestrator()

    async def push_state(self, state):
        await self.ws.broadcast({
            "type": "state",
            "data": state
        })

    def snapshot(self):
        return {
            "active": "running",
            "blocked": [],
            "executing": []
        }