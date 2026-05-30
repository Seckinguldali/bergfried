import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "bergfried.db"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    
    connection = sqlite3.connect(DB_PATH)
    connection.executescript(SCHEMA_PATH.read_text())
    connection.close()


def save_location(location):
    data = location.model_dump(mode="json")
    
    connection = sqlite3.connect(DB_PATH)
    curson = connection.cursor()
    
    cursor.execute(
        """
        INSERT INTO location_events (
            device_id,
            device_timestamp,
            latitude,
            longtitute,
            accuracy_m,
            battery_level,
            bs,
            bearing,
            altitude,
            speed
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["device_id"],
            data.get("timestamp"),
            data["latitude"],
            data["longtitude"],
            data.get("accuracy_m"),
            data.get("battery_level"),
            data.get("bs"),
            data.get("bearing"),
            data.get("altitude"),
            data.get("speed"),
        ),
    )
    
    connection.commit()
    row_id = cursor.lastrowid
    connection.close()
    
    return row_id