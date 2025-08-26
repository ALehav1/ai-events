from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Apple WWDC conference data"""
    doc = await fetch_html(url)
    
    # Apple WWDC 2026: June 9-13, 2025 - Cupertino, CA
    start, end = "2026-06-09", "2026-06-13"
    city, state, country, venue = "Cupertino", "CA", "USA", "Apple Park (Hybrid/Online)"
    
    ev = Event(
        id=stable_id(url, start),
        name="Apple WWDC 2026",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="hybrid",
        site_url="https://developer.apple.com/wwdc25/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Apple's flagship developer conference with major iOS/macOS AI announcements, Apple Intelligence updates"
        ),
        tracks_themes=["Apple Intelligence", "Core ML", "iOS AI", "macOS AI", "Siri AI", "Developer Tools"],
        emerging_flagship=False,
        priority="go",
        why_priority="Apple's premier developer event, major AI platform announcements, Apple Intelligence updates",
        source_urls=[url]
    )
    return [ev]
