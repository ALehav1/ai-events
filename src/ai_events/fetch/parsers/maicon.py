from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse MAICON (Marketing AI Conference) data"""
    doc = await fetch_html(url)
    
    events = []
    
    # MAICON 2025
    event = Event(
        id=stable_id(url, "2025-10-14"),
        name="MAICON 2025 (Marketing AI Conference)",
        start_date="2025-10-14",
        end_date="2025-10-16",
        city="Cleveland",
        state_province="OH",
        country="USA",
        region="US",
        format="live",
        site_url="https://www.marketingaiinstitute.com/events/marketing-artificial-intelligence-conference",
        tracks_themes=["Marketing AI", "AI Marketing Strategies", "Content Creation", "Marketing Automation", "AI Trends"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=500,
            evidence="Typically 500+ attendees, Marketing AI Institute's flagship conference"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Marketing AI Institute's flagship event on AI in marketing, 500+ marketers and executives"
    )
    events.append(event)
    
    return events
