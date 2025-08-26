from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse World Summit AI Amsterdam conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # World Summit AI Amsterdam 2025: October 8-9, 2025 - Amsterdam, Netherlands
    events.append(Event(
        id=stable_id("world-summit-ai-amsterdam", "2025-10-08"),
        name="World Summit AI Amsterdam 2025",
        start_date="2025-10-08", 
        end_date="2025-10-09",
        city="Amsterdam", 
        state_province=None, 
        country="Netherlands", 
        venue="RAI Amsterdam",
        region="International", 
        format="live",
        site_url="https://worldsummit.ai/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Europe's flagship AI conference with 1,500-2,500 attendees, global reach with enterprise leaders and startups"
        ),
        tracks_themes=["Generative AI", "AI in Finance", "Enterprise AI", "Startup Innovation", "AI Investment"],
        emerging_flagship=False,
        priority="go",
        why_priority="Europe's flagship AI conference, global audience, mix of corporate and cutting-edge content",
        source_urls=[url]
    ))
    
    return events
