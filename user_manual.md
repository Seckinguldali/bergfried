
on the server:
git clone https://github.com/Seckinguldali/bergfried.git
cd bergfried/server/ingestion-api
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pydantic
uvicorn main:app --host 0.0.0.0 --port 8000