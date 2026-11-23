from fastapi import FastAPI, Query
from .storage import search_pages

app = FastAPI(title="Crawler Search API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/search")
def search(q: str = Query(min_length=1, description="Search crawled pages")):
    return {"query": q, "results": search_pages(q)}
