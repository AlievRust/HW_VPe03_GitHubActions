from datetime import datetime, timezone

from fastapi import FastAPI


app = FastAPI(title="Server Time API", version="1.0.0")


@app.get("/")
def read_root() -> dict[str, str]:
    current_time = datetime.now(timezone.utc).astimezone().isoformat()
    return {
        "message": "FastAPI server is running",
        "server_time": current_time,
    }


@app.get("/time")
def read_time() -> dict[str, str]:
    current_time = datetime.now(timezone.utc).astimezone().isoformat()
    return {
        "server_time": current_time,
    }
