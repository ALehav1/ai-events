from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Lisbon AI events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # AIMLR2026: April 16-18, 2026 - Lisbon, Portugal
    ev1 = Event(
        id=stable_id(url, "2026-04-16"),
        name="AIMLR2026 - International Conference on Artificial Intelligence, Machine Learning, and Robotics",
        audience_tag="Mixed Audience",
        start_date="2026-04-16", 
        end_date="2026-04-18",
        city="Lisbon", 
        state_province="", 
        country="Portugal", 
        venue="Lisbon Marriott Hotel",
        region="International", 
        format="live",
        site_url="https://www.aimlr-conference.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Annual international conference focused on AI, machine learning, and robotics"
        ),
        tracks_themes=["Artificial Intelligence", "Machine Learning", "Robotics", "AI Research", "ML Applications"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major international conference covering AI, ML, and robotics with academic and industry focus",
        source_urls=[url]
    )
    events.append(ev1)
    
    # International Conference on Artificial Intelligence and Data Mining (ICAIDM): October 15-16, 2026 - Lisbon, Portugal
    ev2 = Event(
        id=stable_id(url, "2026-10-15"),
        name="International Conference on Artificial Intelligence and Data Mining (ICAIDM)",
        audience_tag="Mixed Audience",
        start_date="2026-10-15", 
        end_date="2026-10-16",
        city="Lisbon", 
        state_province="", 
        country="Portugal", 
        venue="Lisbon Congress Centre",
        region="International", 
        format="live",
        site_url="https://www.icaidm.org/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference focusing on AI and data mining research and applications"
        ),
        tracks_themes=["AI Research", "Data Mining", "Machine Learning", "Data Analytics", "AI Applications"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic conference with specialized focus on AI and data mining",
        source_urls=[url]
    )
    events.append(ev2)
    
    return events
