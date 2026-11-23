# Distributed Web Crawler & Search (Starter)

A Python project that crawls pages, extracts titles and text, stores results in SQLite, and exposes a simple search API.

## Tech stack
- Python 3.11+
- asyncio / httpx
- BeautifulSoup
- FastAPI
- SQLite

## Setup
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python -m crawler.cli https://example.com
uvicorn crawler.api:app --reload
```
Open http://127.0.0.1:8000/docs to explore the API.

## Current features
- Fetch a webpage
- Extract title and readable text
- Save crawled pages in SQLite
- Search stored pages via API

## Development status
This is a starter implementation. Add queueing, crawl limits, retry/backoff, robots.txt handling, and multi-worker coordination as future improvements.
