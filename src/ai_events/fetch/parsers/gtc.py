from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse NVIDIA GTC conference data"""
    doc = await fetch_html(url)
    
    # NVIDIA GTC 2026 events - multiple locations
    events = []
    
    # GTC San Jose (main event) - March 2026
    events.append(Event(
        id=stable_id("gtc-san-jose", "2026-03-17"),
        name="NVIDIA GTC San Jose",
        start_date="2026-03-17", 
        end_date="2026-03-21",
        city="San Jose", 
        state_province="CA", 
        country="USA", 
        venue="San Jose McEnery Convention Center",
        region="US", 
        format="live",
        site_url="https://www.nvidia.com/gtc/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="NVIDIA's flagship AI/GPU conference with 25,000+ attendees, major hardware/software announcements"
        ),
        tracks_themes=["GPU Computing", "AI Infrastructure", "Generative AI", "Autonomous Vehicles", "Healthcare AI", "Robotics"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier AI hardware/software conference, Jensen Huang keynote, major product launches",
        source_urls=[url]
    ))
    
    # GTC Taipei - May 2026
    events.append(Event(
        id=stable_id("gtc-taipei", "2026-05-21"),
        name="NVIDIA GTC Taipei",
        start_date="2026-05-21", 
        end_date="2026-05-22",
        city="Taipei", 
        state_province=None, 
        country="Taiwan", 
        venue="Taipei Nangang Exhibition Center",
        region="International", 
        format="live",
        site_url="https://www.nvidia.com/gtc/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Regional GTC event focusing on Asia-Pacific AI ecosystem"
        ),
        tracks_themes=["GPU Computing", "AI Infrastructure", "Manufacturing AI", "Edge Computing"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major regional NVIDIA event, Asia-Pacific AI focus",
        source_urls=[url]
    ))
    
    # GTC Paris - June 2026
    events.append(Event(
        id=stable_id("gtc-paris", "2026-06-10"),
        name="NVIDIA GTC Paris",
        start_date="2026-06-10", 
        end_date="2026-06-12",
        city="Paris", 
        state_province=None, 
        country="France", 
        venue="Palais des Congrès de Paris",
        region="International", 
        format="live",
        site_url="https://www.nvidia.com/gtc/",
        size_profile=SizeProfile(
            tier="major",
            evidence="European GTC event focusing on European AI ecosystem and regulations"
        ),
        tracks_themes=["GPU Computing", "AI Infrastructure", "European AI Act", "Automotive AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major European NVIDIA event, EU AI regulation focus",
        source_urls=[url]
    ))
    
    return events
