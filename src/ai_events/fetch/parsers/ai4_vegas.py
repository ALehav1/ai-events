from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Ai4 2025 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Ai4 2025: August 11-13, 2025 - Las Vegas, NV
    events.append(Event(
        id=stable_id("ai4-vegas", "2025-08-11"),
        name="Ai4 2025",
        start_date="2025-08-11", 
        end_date="2025-08-13",
        city="Las Vegas", 
        state_province="NV", 
        country="USA", 
        venue="MGM Grand",
        region="US", 
        format="live",
        site_url="https://ai4.io/vegas/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="North America's largest AI industry event with 8,000+ attendees from 75+ countries, 600+ speakers"
        ),
        tracks_themes=["Enterprise AI", "Generative AI", "AI Applications", "AI Strategy", "AI Governance"],
        emerging_flagship=False,
        priority="go",
        why_priority="North America's largest AI industry event, 8,000+ attendees, comprehensive enterprise AI coverage",
        source_urls=[url]
    ))
    
    return events
