import asyncio
import sys
from .fetch import fetch_page
from .storage import save_page

async def main(url: str):
    title, content = await fetch_page(url)
    save_page(url, title, content)
    print(f"Saved: {title} ({len(content)} characters)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m crawler.cli <URL>")
    asyncio.run(main(sys.argv[1]))
