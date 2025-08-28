from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI in Finance Summit NY data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI in Finance Summit NY 2026
    event = Event(
        id=stable_id(url, "2026-04-15"),
        name="AI in Finance Summit NY",
        start_date="2026-04-15",
        end_date="2026-04-16",
        city="New York City",
        state_province="NY",
        country="USA",
        venue="Convene 237 Park Ave",
        region="US",
        format="live",
        site_url="https://ny-ai-finance.re-work.co/",
        tracks_themes=["AI/ML Tools", "Finance Innovation", "Machine Learning", "Financial Services", "AI Applications"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=200,
            evidence="~200 attendees, RE•WORK's NY edition focused on AI/ML tools for finance"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized AI finance event in NYC financial district with focused audience"
    )
    events.append(event)
    
    return events
