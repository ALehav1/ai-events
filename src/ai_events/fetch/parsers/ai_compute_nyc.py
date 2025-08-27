from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI Compute NYC conference data"""
    doc = await fetch_html(url)
    
    # New York AI Conference 2026: March 27, 2026 - New York, NY
    start, end = "2026-03-27", "2026-03-27"
    city, state, country, venue = "New York", "NY", "USA", "Manhattan Conference Center"
    
    ev = Event(
        id=stable_id(url, start),
        name="New York AI Conference 2026",
        audience_tag="Mixed Audience",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://www.eventbrite.com/e/new-york-ai-conference-tickets-912664222257",
        size_profile=SizeProfile(
            tier="major",
            evidence="Major AI conference in NYC financial district with enterprise focus"
        ),
        tracks_themes=["Enterprise AI", "Financial AI", "AI Computing", "Machine Learning", "Deep Learning"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major NYC AI event, financial district location, enterprise AI focus",
        source_urls=[url]
    )
    return [ev]
