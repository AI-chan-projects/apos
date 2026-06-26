from fastapi import APIRouter
from core.causal.causal_viewer import CausalViewer

router = APIRouter()
viewer = CausalViewer()


@router.get("/graph")
def graph():
    return viewer.graph()


@router.get("/trace")
def trace(event_id: str):
    return viewer.trace_event(event_id)