from __future__ import annotations
from pathlib import Path
from fastapi import FastAPI, HTTPException

APP_NAME = "gitops-fastapi-version-service"
VERSION_FILE = Path(__file__).resolve().parent.parent / "VERSION"

app = FastAPI(title="GitOps FastAPI Version Service")


def read_version() -> str:
    try:
        version = VERSION_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail="VERSION file missing") from exc
    except OSError as exc:
        raise HTTPException(status_code=500, detail="Unable to read VERSION file") from exc

    if not version:
        raise HTTPException(status_code=500, detail="VERSION file is empty")

    return version


@app.get("/version")
async def get_version() -> dict[str, str]:
    return {"application": APP_NAME, "version": read_version()}


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Version service is running"}
