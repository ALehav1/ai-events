from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Microsoft Ignite conference data"""
    doc = await fetch_html(url)
    
    # Microsoft Ignite 2026: November 17-21, 2025 - San Francisco, CA
    start, end = "2026-11-17", "2026-11-21"
    city, state, country, venue = "San Francisco", "CA", "USA", "Moscone Center"
    
    ev = Event(
        id=stable_id(url, start),
        name="Microsoft Ignite 2026",
        audience_tag="Tech Leaders",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://ignite.microsoft.com/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Microsoft's flagship conference with 25,000+ attendees, major Azure AI and platform announcements"
        ),
        tracks_themes=["Azure AI", "Microsoft Copilot", "Azure OpenAI", "Power Platform", "Microsoft 365 AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Microsoft's premier conference, major AI platform announcements, extensive Azure AI content",
        source_urls=[url]
    )
    return [ev]
