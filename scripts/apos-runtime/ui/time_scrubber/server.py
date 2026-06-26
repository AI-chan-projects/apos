from fastapi import FastAPI
from ui.time_scrubber.router import router

app = FastAPI()

app.include_router(router, prefix="/time")

@app.get("/")
def root():
    return {"status": "APOS Time Scrubber Active"}