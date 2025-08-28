from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI for Agencies Summit data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI for Agencies Summit 2026
    event = Event(
        id=stable_id(url, "2026-02-01"),
        name="AI for Agencies Summit",
        start_date="2026-02-01",
        end_date="2026-02-01",
        city="Virtual",
        country="Online",
        region="International",
        format="virtual",
        site_url="https://www.marketingaiinstitute.com/events/ai-for-agencies-summit",
        tracks_themes=["AI for Agencies", "Agency Growth", "AI Tools", "Talent Strategies", "Agency Transformation"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=300,
            evidence="Marketing AI Institute's virtual event for agency growth and AI transformation"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized virtual summit for marketing and sales agencies on AI adoption"
    )
    events.append(event)
    
    return events
