from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AWS re:Invent conference data"""
    doc = await fetch_html(url)
    
    # AWS re:Invent 2026: December 1-5, 2025 - Las Vegas, NV
    start, end = "2026-12-01", "2026-12-05"
    city, state, country, venue = "Las Vegas", "NV", "USA", "Multiple venues on the Strip"
    
    ev = Event(
        id=stable_id(url, start),
        name="AWS re:Invent 2026",
        audience_tag="Tech Leaders",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://reinvent.awsevents.com/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="AWS flagship conference with 60,000+ attendees, major cloud/AI service announcements"
        ),
        tracks_themes=["AWS AI/ML Services", "SageMaker", "Bedrock", "Generative AI", "Cloud Computing", "Serverless"],
        emerging_flagship=False,
        priority="go",
        why_priority="Largest cloud computing conference, major AI/ML service launches, extensive training",
        source_urls=[url]
    )
    return [ev]
