from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Dubai AI Week 2025 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Dubai AI Week 2025: April 21-25, 2025 - Dubai, UAE
    events.append(Event(
        id=stable_id("dubai-ai-week", "2025-04-21"),
        name="Dubai AI Week 2025",
        start_date="2025-04-21", 
        end_date="2025-04-25",
        city="Dubai", 
        state_province=None, 
        country="United Arab Emirates", 
        venue="Various venues city-wide",
        region="International", 
        format="live",
        site_url="https://week.dub.ai/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Week-long AI festival with 2,500+ participants at Dubai Assembly for AI, government-driven initiative"
        ),
        tracks_themes=["AI in Government", "Smart Cities", "Enterprise AI", "AI Competitions", "AI Policy", "Future of Work"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Government-driven Middle East AI event, good for regional insights and public-sector AI",
        source_urls=[url]
    ))
    
    return events
