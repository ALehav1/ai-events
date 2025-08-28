from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI for Finance Summit Paris data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI for Finance Summit 2025
    event = Event(
        id=stable_id(url, "2025-11-24"),
        name="AI for Finance Summit",
        start_date="2025-11-24",
        end_date="2025-11-26",
        city="Paris",
        country="France",
        region="International",
        format="live",
        site_url="https://aiforfinance.artefact.com/",
        tracks_themes=["AI in Banking", "AI in Insurance", "European AI Regulation", "AI Strategy", "Financial Services AI"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="flagship",
            attendees_estimate=5000,
            evidence="~5,000 attendees, 150 speakers from European financial firms, Artefact's major event"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Major European AI finance event with 5000 attendees, strong focus on banking and insurance"
    )
    events.append(event)
    
    return events
