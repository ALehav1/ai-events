import httpx, asyncio
from selectolax.parser import HTMLParser
from ..config import DEFAULT_TIMEOUT, DEFAULT_USER_AGENT

async def fetch_html(url: str, timeout=DEFAULT_TIMEOUT) -> HTMLParser:
    """Fetch HTML content from URL and return parsed document"""
    async with httpx.AsyncClient(follow_redirects=True, timeout=timeout) as client:
        r = await client.get(url, headers={"User-Agent": DEFAULT_USER_AGENT})
        r.raise_for_status()
        return HTMLParser(r.text)
