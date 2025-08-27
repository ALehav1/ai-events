from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI Summit London 2026 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI Summit London 2026: June 2026 - London, UK
    events.append(Event(
        id=stable_id("ai-summit-london", "2026-06-10"),
        name="The AI Summit London 2026",
        audience_tag="Business Leaders",
        start_date="2026-06-10", 
        end_date="2026-06-11",
        city="London", 
        state_province=None, 
        country="United Kingdom", 
        venue="ExCeL London",
        region="International", 
        format="live",
        site_url="https://london.theaisummit.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Europe's leading AI conference with 2,000-5,000 attendees, part of London Tech Week"
        ),
        tracks_themes=["AI in Industry", "Finance AI", "Retail AI", "Responsible AI", "AI Strategy", "Machine Learning"],
        emerging_flagship=False,
        priority="go",
        why_priority="Europe's leading AI conference, cornerstone of London Tech Week, excellent networking",
        source_urls=[url]
    ))
    
    return events
