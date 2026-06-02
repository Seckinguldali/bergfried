
# Bergfried — User Manual (Simple)

## What this does

This runs the Bergfried fleet tracking server. Devices send location data to it, and the server stores the data.

## Where the app lives

- App code: `/home/bergfried/bergfried/server/ingestion-api`
- Database: `/home/bergfried/bergfried/data/bergfried.db`

## Option A: Quick test (development only)

Use this to test the app. It stops when you close SSH.

```bash
cd /home/bergfried/bergfried/server/ingestion-api
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn pydantic
uvicorn main:app --host 0.0.0.0 --port 8000
```

Press Ctrl+C to stop.

## Option B: Keep it running (recommended — systemd)

The systemd service keeps the app running, restarts it if it crashes, and starts it again after reboot.

### Setup (one time)

1. Create a service user and move the repo:

```bash
useradd -m -s /bin/bash bergfried || true
mkdir -p /home/bergfried
mv /root/bergfried /home/bergfried/bergfried
chown -R bergfried:bergfried /home/bergfried/bergfried
```

2. Create virtualenv and install packages:

```bash
sudo -u bergfried bash -lc '
cd /home/bergfried/bergfried/server/ingestion-api
python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install fastapi uvicorn pydantic
'
```

3. Create the systemd service:

```bash
sudo tee /etc/systemd/system/bergfried.service > /dev/null <<'EOF'
[Unit]
Description=Bergfried ingestion API
After=network.target

[Service]
User=bergfried
Group=bergfried
WorkingDirectory=/home/bergfried/bergfried/server/ingestion-api
Environment=PATH=/home/bergfried/bergfried/server/ingestion-api/venv/bin
ExecStart=/home/bergfried/bergfried/server/ingestion-api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
Restart=always
RestartSec=5
KillMode=process

[Install]
WantedBy=multi-user.target
EOF
```

4. Start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now bergfried.service
```

### Check if it's running

```bash
sudo systemctl status bergfried.service
sudo journalctl -u bergfried.service -f
```

### Common commands

Restart the service:
```bash
sudo systemctl restart bergfried.service
```

Stop the service:
```bash
sudo systemctl stop bergfried.service
```

Check the logs:
```bash
sudo journalctl -u bergfried.service -f
```

## Database checks

### See newest records (by insert order)

```bash
sqlite3 /home/bergfried/bergfried/data/bergfried.db "SELECT * FROM location_events ORDER BY id DESC LIMIT 20;"
```

### See newest records (by server receive time)

```bash
sqlite3 /home/bergfried/bergfried/data/bergfried.db "SELECT * FROM location_events ORDER BY received_at DESC LIMIT 20;"
```

### Enable WAL mode (improves reliability)

```bash
sqlite3 /home/bergfried/bergfried/data/bergfried.db "PRAGMA journal_mode=WAL;"
chown bergfried:bergfried /home/bergfried/bergfried/data/bergfried.db
```

## Simple explanations (non-tech)

- **Virtualenv**: a private folder that holds Python packages for this app only — prevents conflicts.
- **Systemd**: the helper program that starts and watches your app; you don't need to keep SSH open.
- **Journalctl**: shows what the app is doing; use it to see errors or confirm it's receiving data.
- **Database**: stores all the location data from devices.

## Troubleshooting

### Service won't start?

Check the logs:
```bash
sudo journalctl -u bergfried.service -f
```

The error will show what's wrong (usually missing packages or path issues).

### Permission errors?

Make sure the files are owned by user `bergfried`:
```bash
sudo chown -R bergfried:bergfried /home/bergfried/bergfried
```

### No data coming in?

Check that:
1. Devices are sending data to `POST /api/v1/locations`
2. The server is accessible from the device (firewall, IP, port 8000)
3. Logs show `200 OK` for incoming requests:
```bash
sudo journalctl -u bergfried.service -f | grep "POST /api/v1/locations"
```

## Questions?

Check the logs first — they usually show the problem. If stuck, ask.