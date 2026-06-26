from fastapi import FastAPI, WebSocket
from ui.live.websocket_manager import WebSocketManager
from ui.live.event_stream import EventStream
from ui.live.state_stream import StateStream

app = FastAPI()

ws_manager = WebSocketManager()
event_stream = EventStream(ws_manager)
state_stream = StateStream(ws_manager)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    ws_manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except:
        ws_manager.disconnect(websocket)