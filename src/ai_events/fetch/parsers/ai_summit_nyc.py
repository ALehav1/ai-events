from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI Summit New York 2025 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI Summit New York 2025: December 10-11, 2025 - New York, NY
    events.append(Event(
        id=stable_id("ai-summit-nyc", "2025-12-10"),
        name="The AI Summit New York 2025",
        audience_tag="Business Leaders",
        start_date="2025-12-10", 
        end_date="2025-12-11",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="Jacob K. Javits Convention Center",
        region="US", 
        format="live",
        site_url="https://newyork.theaisummit.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Premier enterprise AI conference with 2,000+ attendees, part of global AI Summit series"
        ),
        tracks_themes=["Enterprise AI Deployment", "MLOps", "AI in Finance", "AI in Healthcare", "AI Strategy", "Generative AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier enterprise AI conference in NYC, strong industry focus, excellent networking",
        source_urls=[url]
    ))
    
    return events
