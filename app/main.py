from fastapi import FastAPI
from app.api.tickets import router as tickets_router

app = FastAPI(title="Helpdesk API", version="0.1.0")

app.include_router(tickets_router)

@app.get("/health")
def health():
    return {"ok": True}