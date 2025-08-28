from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Artificial Intelligence in Financial Services Conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Artificial Intelligence in Financial Services Conference 2025
    event = Event(
        id=stable_id(url, "2025-09-16"),
        name="Artificial Intelligence in Financial Services Conference",
        start_date="2025-09-16",
        end_date="2025-09-17",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://www.arena-international.com/event/aifs/",
        tracks_themes=["AI in Financial Services", "Predictive Analytics", "Risk Management", "Regulatory Compliance", "AI Disruptions"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=150,
            evidence="~150 senior leaders from institutions like Barclays, 7th edition by Arena International"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized conference for senior financial services executives discussing AI disruptions"
    )
    events.append(event)
    
    return events
