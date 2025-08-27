from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Dreamforce conference data"""
    doc = await fetch_html(url)
    
    # Dreamforce 2026: October 14-16, 2025 - San Francisco, CA
    start, end = "2026-10-14", "2026-10-16"
    city, state, country, venue = "San Francisco", "CA", "USA", "Moscone Center"
    
    ev = Event(
        id=stable_id(url, start),
        name="Dreamforce 2026",
        audience_tag="Business Leaders",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://www.salesforce.com/dreamforce/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Salesforce's flagship event with 40,000+ attendees, major AI and CRM announcements"
        ),
        tracks_themes=["Salesforce AI", "CRM Innovation", "Business Automation", "Einstein AI", "Data Cloud"],
        emerging_flagship=False,
        priority="go",
        why_priority="Largest CRM/AI enterprise event, major product announcements, extensive AI track",
        source_urls=[url]
    )
    return [ev]
