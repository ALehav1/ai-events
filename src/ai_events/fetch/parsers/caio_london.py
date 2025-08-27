"""Parser for Chief AI Officer Summit London by RE•WORK"""

from datetime import datetime
from typing import List, Optional
from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> List[Event]:
    """Parse Chief AI Officer Summit London events"""
    events = []
    
    # Chief AI Officer Summit London 2025
    event = Event(
        id="",  # Will be set by stable_id
        name="Chief AI Officer Summit London",
        start_date="2026-02-25",
        end_date="2026-02-26",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://caio-london.re-work.co",
        tracks_themes=["Enterprise AI", "AI Strategy", "AI Governance", "AI Leadership"],
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=500,
            evidence="RE•WORK events typically attract 300-800 senior executives"
        )
    )
    event.id = stable_id(event.site_url, event.start_date)
    events.append(event)
    
    return events
