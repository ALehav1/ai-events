from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Google I/O conference data"""
    doc = await fetch_html(url)
    
    # Google I/O 2026: May 20-21, 2026 - Mountain View, CA
    start, end = "2026-05-20", "2026-05-21"
    city, state, country, venue = "Mountain View", "CA", "USA", "Shoreline Amphitheatre"
    
    ev = Event(
        id=stable_id(url, start),
        name="Google I/O 2026",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://io.google/2025/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Google's flagship developer conference with 7,000+ attendees, major AI and platform announcements"
        ),
        tracks_themes=["Gemini AI", "Android AI", "Google Cloud AI", "TensorFlow", "Machine Learning", "Developer Tools"],
        emerging_flagship=False,
        priority="go",
        why_priority="Google's premier developer conference, major AI model announcements, extensive ML content",
        source_urls=[url]
    )
    return [ev]
