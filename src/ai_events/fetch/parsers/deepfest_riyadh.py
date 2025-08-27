from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse DeepFest 2026 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # DeepFest 2026: April 13-16, 2026 - Riyadh, Saudi Arabia
    events.append(Event(
        id=stable_id("deepfest-riyadh", "2026-04-13"),
        name="DeepFest 2026",
        audience_tag="Mixed Audience",
        start_date="2026-04-13", 
        end_date="2026-04-16",
        city="Riyadh", 
        state_province=None, 
        country="Saudi Arabia", 
        venue="Riyadh Exhibition & Convention Center (Malham)",
        region="International", 
        format="live",
        site_url="https://deepfest.com",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Middle East's premier AI event co-located with LEAP (200k+ visitors), region's most influential AI conference"
        ),
        tracks_themes=["AI in Industry", "Energy AI", "Finance AI", "AI Startups", "AI Investment", "Autonomous Systems"],
        emerging_flagship=False,
        priority="go",
        why_priority="Middle East's premier AI event, massive scale with LEAP, unparalleled regional access and networking",
        source_urls=[url]
    ))
    
    return events
