import httpx
from bs4 import BeautifulSoup

async def fetch_page(url: str) -> tuple[str, str]:
    async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:
        response = await client.get(url)
        response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else url
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    content = soup.get_text(" ", strip=True)
    return title, content
