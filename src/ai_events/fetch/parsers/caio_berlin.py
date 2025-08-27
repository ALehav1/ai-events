"""Parser for Chief AI Officer Summit Berlin"""
from datetime import datetime
from typing import List
from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> List[Event]:
    """Parse Chief AI Officer Summit Berlin events"""
    events = []
    
    # Chief AI Officer Summit Berlin 2025
    event = Event(
        emerging_flagship=False,
        id="",  # Will be set by stable_id
        name="Chief AI Officer Summit Berlin",
        start_date="2025-09-11",
        end_date="2025-09-11",
        city="Berlin",
        country="Germany",
        region="International",
        format="live",
        site_url="https://world.aiacceleratorinstitute.com/location/caioberlin",
        tracks_themes=["AI Strategy", "Enterprise AI", "AI Scale", "AI Production", "AI Leadership"],
        audience_tag="Business Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=150,
            evidence="150+ executives expected, primarily VPs and C-level from tech and finance"
        )
    )
    event.id = stable_id(event.site_url, event.start_date)
    events.append(event)
    
    return events
