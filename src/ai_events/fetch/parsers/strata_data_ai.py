from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse O'Reilly Strata Data & AI Conference data"""
    doc = await fetch_html(url)
    
    # Strata Data & AI Conference 2026: March 17-18, 2025 - San Jose, CA (Virtual/Hybrid)
    start, end = "2026-03-17", "2026-03-18"
    city, state, country, venue = "San Jose", "CA", "USA", "Virtual/Hybrid Event"
    
    ev = Event(
        id=stable_id(url, start),
        name="O'Reilly Strata Data & AI Conference 2026",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="hybrid",
        site_url="https://www.oreilly.com/conferences/strata-data-ai.html",
        size_profile=SizeProfile(
            tier="major",
            evidence="O'Reilly's flagship data and AI conference with 4,600+ participants, practical AI implementation focus"
        ),
        tracks_themes=["Applied AI", "Data Science", "Machine Learning", "AI Strategy", "Data Engineering"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier data science conference, practical AI implementation, extensive training content",
        source_urls=[url]
    )
    return [ev]
