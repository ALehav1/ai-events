from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Fintech Americas Miami conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Fintech Americas Miami 2025
    event = Event(
        id=stable_id(url, "2025-11-18"),
        name="Fintech Americas Miami",
        start_date="2025-11-18",
        end_date="2025-11-19",
        city="Miami",
        state_province="FL",
        country="USA",
        region="US",
        format="live",
        site_url="https://www.fintechamericas.co/en/conferencia-miami-agenda",
        tracks_themes=["Fintech", "AI in Banking", "Digital Payments", "Latin America Finance", "Financial Innovation"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=1500,
            evidence="~1,500 attendees, largest fintech event focused on Latin America and Caribbean markets"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Major fintech conference connecting Latin American and US markets, strong AI focus"
    )
    events.append(event)
    
    return events
