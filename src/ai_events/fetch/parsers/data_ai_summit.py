from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Data + AI Summit 2025 conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Data + AI Summit 2025: June 9-12, 2025 - San Francisco, CA
    events.append(Event(
        id=stable_id("data-ai-summit", "2025-06-09"),
        name="Data + AI Summit 2025",
        start_date="2025-06-09", 
        end_date="2025-06-12",
        city="San Francisco", 
        state_province="CA", 
        country="USA", 
        venue="San Francisco Convention Center",
        region="US", 
        format="hybrid",
        site_url="https://www.databricks.com/dataaisummit",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Databricks flagship conference with several thousand in-person attendees plus virtual audience, major product announcements"
        ),
        tracks_themes=["Big Data Analytics", "Machine Learning", "AI in Data Platforms", "Data Governance", "Enterprise AI Integration"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier data/AI conference, deep technical content, major platform announcements from Databricks",
        source_urls=[url]
    ))
    
    return events
