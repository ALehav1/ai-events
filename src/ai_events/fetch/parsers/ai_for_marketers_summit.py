from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI for Marketers Summit data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI for Marketers Summit 2025
    event = Event(
        id=stable_id(url, "2025-11-13"),
        name="AI for Marketers Summit",
        start_date="2025-11-13",
        end_date="2025-11-14",
        city="Virtual",
        country="Online",
        region="International",
        format="virtual",
        site_url="https://artificialintelligencesummit.com/",
        tracks_themes=["AI Marketing Case Studies", "Brand AI Strategies", "Marketing Automation", "AI Tools", "Digital Marketing"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=300,
            evidence="Digital format suggests broad reach, focused on real-world AI case studies for brands"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Virtual summit focused on practical AI marketing case studies and brand strategies"
    )
    events.append(event)
    
    return events
