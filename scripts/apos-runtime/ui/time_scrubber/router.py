from fastapi import APIRouter
from ui.time_scrubber.state_reconstructor import StateReconstructor

router = APIRouter()
reconstructor = StateReconstructor()


@router.get("/state")
def get_state(timestamp: str):

    return reconstructor.reconstruct(timestamp)