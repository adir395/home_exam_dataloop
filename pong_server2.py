from fastapi import FastAPI
import requests
import time
import uvicorn

app = FastAPI()

ping_target = None
pong_time_ms = None
is_game_running = False

@app.get("/")
async def read_root():
    return {"message": "Server Start"}

@app.post("/ping")
async def ping():
    global is_game_running, pong_time_ms

    if not is_game_running:
        return {"message": "Game is not running."}

    time.sleep(pong_time_ms / 1000)
    requests.post(ping_target + "/ping")
    return {"message": "pong"}


@app.post("/start/{peer_url}/{ptms}")
async def start_game(peer_url: str, ptms: int):
    global ping_target, is_game_running, pong_time_ms

    ping_target = peer_url
    pong_time_ms = ptms
    is_game_running = True

    requests.post(ping_target + "/ping")
    return {"message": "Game started."}




@app.post("/stop")
async def stop_game():
    global is_game_running
    is_game_running = False
    return {"message": "Game stopped."}


@app.post("/pause")
async def pause_game():
    global is_game_running
    is_game_running = False
    return {"message": "Game paused."}


@app.post("/resume")
async def resume_game():
    global is_game_running
    is_game_running = True

    requests.post(ping_target + "/ping")
    return {"message": "Game resumed."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8001)
