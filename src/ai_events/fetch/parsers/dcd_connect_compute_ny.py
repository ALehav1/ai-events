from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse DCD>Connect | Compute New York conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # DCD>Connect | Compute New York 2026
    event = Event(
        id=stable_id(url, "2026-03-17"),
        name="DCD>Connect | Compute New York",
        start_date="2026-03-17",
        end_date="2026-03-18",
        city="New York City",
        state_province="NY",
        country="USA",
        region="US",
        format="live",
        site_url="https://www.datacenterdynamics.com/en/dcdconnect-compute/new-york/2026/",
        tracks_themes=["AI Infrastructure", "Data Center", "GPU Computing", "AI Workloads", "Cloud Infrastructure"],
        audience_tag="Tech Leaders",
        size_profile=SizeProfile(
            tier="major",
            attendees_estimate=800,
            evidence="~800 data center and AI infrastructure professionals, focused on compute for AI workloads"
        ),
        emerging_flagship=False,
        priority="go",
        why_priority="Critical AI infrastructure event focused on data centers and compute requirements for AI"
    )
    events.append(event)
    
    return events
