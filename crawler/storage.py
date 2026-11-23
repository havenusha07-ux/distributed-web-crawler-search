import sqlite3
from pathlib import Path

DB_PATH = Path("crawler.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS pages (url TEXT PRIMARY KEY, title TEXT, content TEXT)"
        )

def save_page(url: str, title: str, content: str):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO pages(url, title, content) VALUES (?, ?, ?)",
            (url, title, content),
        )

def search_pages(term: str):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT url, title FROM pages WHERE title LIKE ? OR content LIKE ? ORDER BY title",
            (f"%{term}%", f"%{term}%"),
        ).fetchall()
    return [{"url": url, "title": title} for url, title in rows]
