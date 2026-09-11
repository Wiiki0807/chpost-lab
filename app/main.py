from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.routers import sla, volume

DASHBOARD = Path(__file__).resolve().parent.parent / "dashboard.html"

app = FastAPI(title="chpost-lab", version="0.1.0")
app.include_router(volume.router, prefix="/api/v1")
app.include_router(sla.router, prefix="/api/v1")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def dashboard() -> FileResponse:
    return FileResponse(DASHBOARD)
