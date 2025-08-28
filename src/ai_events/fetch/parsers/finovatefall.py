from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse FinovateFall conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # FinovateFall 2025
    event = Event(
        id=stable_id(url, "2025-09-08"),
        name="FinovateFall",
        start_date="2025-09-08",
        end_date="2025-09-10",
        city="New York City",
        state_province="NY",
        country="USA",
        region="US",
        format="live",
        site_url="https://informaconnect.com/finovatefall/",
        tracks_themes=["Fintech", "AI-driven Innovations", "Banking", "Investments", "Customer Experience"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=2000,
            evidence="~2,000 attendees including C-suite from finance, 150+ speakers from firms like JPMorgan"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Long-standing major fintech event since 2007, attracts 2000+ executives from major financial institutions"
    )
    events.append(event)
    
    return events
