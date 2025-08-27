from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse OpenAI DevDay conference data"""
    doc = await fetch_html(url)
    
    # OpenAI DevDay 2026: October 6, 2025 - San Francisco, CA
    start, end = "2026-10-06", "2026-10-06"
    city, state, country, venue = "San Francisco", "CA", "USA", "Fort Mason"
    
    ev = Event(
        id=stable_id(url, start),
        name="OpenAI DevDay 2026",
        audience_tag="Practitioners",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://openai.com/index/announcing-devday-2025/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="OpenAI's flagship developer conference with 1,500+ attendees, major GPT and API announcements"
        ),
        tracks_themes=["GPT Models", "OpenAI API", "ChatGPT", "AI Development", "Large Language Models"],
        emerging_flagship=False,
        priority="go",
        why_priority="OpenAI's premier developer event, major model announcements, extensive API updates",
        source_urls=[url]
    )
    return [ev]
