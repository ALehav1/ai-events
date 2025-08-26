from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse ODSC West conference data"""
    doc = await fetch_html(url)
    
    # ODSC West 2026: October 28-30, 2025 - Burlingame, CA
    start, end = "2026-10-28", "2026-10-30"
    city, state, country, venue = "Burlingame", "CA", "USA", "Hyatt Regency San Francisco Airport"
    
    ev = Event(
        id=stable_id(url, start),
        name="ODSC West 2026",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://odsc.com/california/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Leading data science conference with 3,000+ attendees, extensive ML and AI training"
        ),
        tracks_themes=["Machine Learning", "Deep Learning", "MLOps", "Data Science", "AI Training", "Large Language Models"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier data science conference, hands-on ML training, extensive AI practitioner content",
        source_urls=[url]
    )
    return [ev]
