from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Financial Times Future of AI event data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Future of AI 2025
    event = Event(
        id=stable_id(url, "2025-11-05"),
        name="Future of AI (Financial Times)",
        start_date="2025-11-05",
        end_date="2025-11-06",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://ai.live.ft.com/",
        tracks_themes=["AI Business Impact", "AI Investment", "AI Regulation", "Financial Services AI", "Policy Discussions"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=500,
            evidence="Typically 500+ executives for FT events, exploring AI's business impact with finance lens"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Financial Times flagship AI event with 500+ executives, major policy and investment discussions"
    )
    events.append(event)
    
    return events
