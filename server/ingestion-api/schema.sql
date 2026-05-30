CREATE TABLE IF NOT EXISTS location_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT NOT NULL,
    device_timestamp TEXT,
    received_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    accuracy_m REAL,
    battery_level REAL,
    bs INTEGER,
    bearing REAL,
    altitude REAL,
    speed REAL
);

CREATE INDEX IF NOT EXISTS idx_location_events_device_time
ON location_events (device_id, received_at);