"""Parser for CDAO Defense & Security 2025"""
from datetime import datetime
from typing import List
from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> List[Event]:
    """Parse CDAO Defense & Security 2025 events"""
    events = []
    
    # CDAO Defense & Security 2025
    event = Event(
        id="",  # Will be set by stable_id
        name="CDAO Defense & Security 2025",
        start_date="2025-09-16",
        end_date="2025-09-17",
        city="Washington",
        state_province="DC",
        country="USA",
        region="US",
        format="live",
        site_url="https://cdao-def.coriniumintelligence.com/",
        tracks_themes=["Defense AI", "Security AI", "Government AI", "Data Analytics", "AI Governance"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=200,
            evidence="200+ senior leaders from defense agencies, intelligence communities"
        )
    )
    event.id = stable_id(event.site_url, event.start_date)
    events.append(event)
    
    return events
