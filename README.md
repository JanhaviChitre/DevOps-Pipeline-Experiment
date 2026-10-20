# Notes API - DevOps Pipeline Mini Project

A tiny Flask REST API used to demonstrate an end-to-end DevOps pipeline:
Git -> GitHub -> GitHub Actions (build + test) -> Docker (containerize) -> deploy (run container).

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## Run tests

```bash
python -m pytest -v
```

## Run in Docker

```bash
docker build -t notes-api .
docker run -p 5000:5000 notes-api
```

Then open http://localhost:5000/health
