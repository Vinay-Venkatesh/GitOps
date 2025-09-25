# GitOps FastAPI Version Service

This project exposes an endpoint that reports the currently deployed application version.

## Getting Started

```bash
pipenv install --skip-lock
pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/version` to see the version payload, or `/` for a basic status response.

Update the `VERSION` file whenever you deploy a new revision so the API always returns the latest value.
