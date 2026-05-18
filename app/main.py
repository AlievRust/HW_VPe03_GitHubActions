from datetime import datetime, timezone

from fastapi import FastAPI


app = FastAPI(title="Server Time API", version="1.0.0")


def get_server_datetime() -> datetime:
    return datetime.now(timezone.utc).astimezone()


@app.get("/")
def read_root() -> dict[str, str]:
    current_time = get_server_datetime().isoformat()
    return {
        "message": "FastAPI server is running",
        "server_time": current_time,
    }


@app.get("/time")
def read_time() -> dict[str, str]:
    current_time = get_server_datetime().isoformat()
    return {
        "server_time": current_time,
    }


@app.get("/date")
def read_date() -> dict[str, str]:
    current_date = get_server_datetime().date().isoformat()
    return {
        "server_date": current_date,
    }
