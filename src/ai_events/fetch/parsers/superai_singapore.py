from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse SuperAI Singapore 2026 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # SuperAI Singapore 2026: June 10-11, 2026 - Singapore
    events.append(Event(
        id=stable_id("superai-singapore", "2026-06-10"),
        name="SuperAI Singapore 2026",
        audience_tag="Mixed Audience",
        start_date="2026-06-10", 
        end_date="2026-06-11",
        city="Singapore", 
        state_province=None, 
        country="Singapore", 
        venue="Marina Bay Sands",
        region="International", 
        format="live",
        site_url="https://www.superai.com/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Asia's largest AI conference with 7,000+ attendees in 2025, major industry partnerships with Microsoft, Google, AWS, OpenAI"
        ),
        tracks_themes=["AI Innovation", "Enterprise AI", "Cloud AI", "Robotics", "Autonomous Systems", "AI Startups"],
        emerging_flagship=False,
        priority="go",
        why_priority="Asia's largest AI conference, 7,000+ attendees, major tech partnerships, East meets West AI collaboration",
        source_urls=[url]
    ))
    
    return events
