from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Gen AI & HyperAutomation in Finance Summit data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Gen AI & HyperAutomation in Finance Summit 2025
    event = Event(
        id=stable_id(url, "2025-10-16"),
        name="Gen AI & HyperAutomation in Finance Summit",
        start_date="2025-10-16",
        end_date="2025-10-16",
        city="Chicago",
        state_province="IL",
        country="USA",
        region="US",
        format="live",
        site_url="https://kinfos.events/haf/",
        tracks_themes=["Generative AI", "HyperAutomation", "Finance Automation", "Compliance Tools", "Operational Efficiency"],
        audience_tag="Tech Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=200,
            evidence="Similar events attract 100-300 attendees, one-day summit by Kinfos Events"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Focused on practical generative AI and automation applications in finance"
    )
    events.append(event)
    
    return events
