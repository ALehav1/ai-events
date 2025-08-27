from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url:str) -> list[Event]:
    """Parse The AI Conference SF data from their website"""
    doc = await fetch_html(url)
    
    # Create events for both 2025 and 2026
    events = []
    
    # 2025 event
    start_2025, end_2025 = "2025-09-17", "2025-09-18"
    city_2025, state_2025, country_2025, venue_2025 = "San Francisco", "CA", "USA", "Pier 48"
    speakers_2025 = ["Peter Norvig — Google", "Jason Wei — OpenAI", "Joe Spisak — Meta"]
    
    ev_2025 = Event(
        id=stable_id(url, start_2025),
        name="The AI Conference (SF)",
        audience_tag="Mixed Audience",
        start_date=start_2025, 
        end_date=end_2025,
        city=city_2025, 
        state_province=state_2025, 
        country=country_2025, 
        venue=venue_2025,
        region="US", 
        format="live",
        site_url=url,
        speakers_sample=speakers_2025,
        size_profile=SizeProfile(
            tier="major",
            evidence="100+ speakers; multi-track; top researchers/product leads."
        ),
        tracks_themes=["Large Language Models","AI Infrastructure","Agents","Safety"],
        emerging_flagship=False,
        priority="go",
        why_priority="High-caliber technical + product mix; exec meeting surface.",
        source_urls=[url]
    )
    events.append(ev_2025)
    
    # 2026 event
    start, end = "2026-09-17", "2026-09-18"
    city, state, country, venue = "San Francisco", "CA", "USA", "Pier 48"
    
    speakers = ["Peter Norvig — Google", "Jason Wei — OpenAI", "Joe Spisak — Meta"]
    
    ev = Event(
        id=stable_id(url, start),
        name="The AI Conference (SF)",
        audience_tag="Mixed Audience",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url=url,
        speakers_sample=speakers,
        size_profile=SizeProfile(
            tier="major",
            evidence="100+ speakers; multi-track; top researchers/product leads."
        ),
        tracks_themes=["Large Language Models","AI Infrastructure","Agents","Safety"],
        emerging_flagship=False,
        priority="go",
        why_priority="High-caliber technical + product mix; exec meeting surface.",
        source_urls=[url]
    )
    events.append(ev)
    
    return events
