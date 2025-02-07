from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI(title="Stage0 Basic Info API ")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_info():
    current_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "email": "kingokingsleykaah@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/dmkvoltage/HNG12"
    }