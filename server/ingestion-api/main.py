from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from db import init_db, save_location

security = HTTPBasic()
def check_auth(credentials: HTTPBasicCredentials = Depends(security)):
    ok_user = secrets.compare_digest(credentials.username, "admin")
    ok_pass = secrets.compare_digest(credentials.password, "password")
    if not (ok_user and ok_pass):
        raise HTTPException(status_code=401, detail="Unauthorized")

app = FastAPI()
init_db()

class LocationIn(BaseModel):
    device_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    accuracy_m: Optional[float] = None
    battery_level: Optional[float] = None
    bs: Optional[int] = None
    bearing: Optional[float] = None
    altitude: Optional[float] = None
    speed: Optional[float] = None # in m/s

@app.post("/api/v1/locations")
def create_location(location: LocationIn, auth=Depends(check_auth)):
    row_id = save_location(location)
    return {"status": "stored", "id": row_id}