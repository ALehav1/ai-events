"""Parser for Responsible AI Summit 2025"""
from datetime import datetime
from typing import List
from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> List[Event]:
    """Parse Responsible AI Summit 2025 events"""
    events = []
    
    # Responsible AI Summit 2025
    event = Event(
        id="",  # Will be set by stable_id
        name="Responsible AI Summit 2025",
        start_date="2025-09-22",
        end_date="2025-09-24",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://www.aidataanalytics.network/events-responsible-ai-summit/",
        tracks_themes=["AI Ethics", "AI Governance", "Responsible AI", "AI Bias", "AI Regulation"],
        audience_tag="Mixed Audience",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=500,
            evidence="Enterprise leaders, regulators, and practitioners focused on AI ethics"
        )
    )
    event.id = stable_id(event.site_url, event.start_date)
    events.append(event)
    
    return events
