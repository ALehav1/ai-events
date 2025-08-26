from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI Expo Africa 2025 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # AI Expo Africa 2025: October 29-31, 2025 - Johannesburg, South Africa
    events.append(Event(
        id=stable_id("ai-expo-africa", "2025-10-29"),
        name="AI Expo Africa 2025",
        start_date="2025-10-29", 
        end_date="2025-10-31",
        city="Johannesburg", 
        state_province="Gauteng", 
        country="South Africa", 
        venue="Sandton Convention Centre",
        region="International", 
        format="live",
        site_url="https://aiexpoafrica.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Africa's largest enterprise AI event with 2,500+ attendees, 8th edition, hosting UN AI for Good Impact Africa Summit"
        ),
        tracks_themes=["AI Business Applications", "Enterprise AI", "AI for Development", "Data Science", "Innovation Ecosystems"],
        emerging_flagship=False,
        priority="go",
        why_priority="Africa's largest AI event, excellent networking for emerging markets, unique regional perspective",
        source_urls=[url]
    ))
    
    return events
