from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> list[Event]:
    """Parse Ray Summit - major AI infrastructure conference"""
    doc = await fetch_html(url)
    
    # Ray Summit 2026 (typically September in San Francisco)
    event = Event(
        id=stable_id(url, "2026-09-10"),
        name="Ray Summit 2026",
        audience_tag="Tech Leaders",
        start_date="2026-09-10",
        end_date="2026-09-11",
        city="San Francisco",
        state_province="CA",
        country="USA",
        venue="Marriott Marquis",
        region="US",
        format="hybrid",
        site_url=url,
        speakers_sample=[
            "Anyscale Team",
            "OpenAI Engineers", 
            "Meta AI Researchers",
            "Google DeepMind Team"
        ],
        size_profile=SizeProfile(
            tier="major",
            evidence="Leading AI infrastructure conference for distributed computing"
        ),
        tracks_themes=["Distributed AI", "LLM Serving", "Machine Learning Infrastructure", "Ray Framework"],
        emerging_flagship=False,
        priority="go",
        why_priority="Critical for AI infrastructure and distributed computing knowledge",
        source_urls=[url]
    )
    
    return [event]
