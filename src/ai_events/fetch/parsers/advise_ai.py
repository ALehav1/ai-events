from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Advise AI by FinancialPlanning conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Advise AI 2025
    event = Event(
        id=stable_id(url, "2025-10-28"),
        name="Advise AI by FinancialPlanning",
        start_date="2025-10-28",
        end_date="2025-10-29",
        city="Las Vegas",
        state_province="NV",
        country="USA",
        region="US",
        format="live",
        site_url="https://conference.financial-planning.com/event/advise-ai/summary",
        tracks_themes=["AI in Wealth Management", "Robo-advisors", "Financial Advisory", "AI Advisory Tools", "Wealth Tech"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=425,
            evidence="~425 attendees, focused on AI in wealth management and advisory, 25 speakers from advisory firms"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized event for AI in wealth management and financial advisory services"
    )
    events.append(event)
    
    return events
