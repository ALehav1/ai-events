from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI in Finance Summit London data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI in Finance Summit London 2025
    event = Event(
        id=stable_id(url, "2025-09-09"),
        name="AI in Finance Summit London",
        start_date="2025-09-09",
        end_date="2025-09-10",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://london-ai-finance.re-work.co/",
        tracks_themes=["AI in Finance", "Machine Learning", "Fraud Detection", "Personalized Banking", "Risk Management"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=150,
            evidence="~100-200 senior executives and innovators from banks like HSBC and fintech firms"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized AI finance event with senior executives from major banks"
    )
    events.append(event)
    
    return events
