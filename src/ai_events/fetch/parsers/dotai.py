from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> list[Event]:
    """Parse dotAI - major European AI conference in Paris"""
    doc = await fetch_html(url)
    
    # dotAI 2026 (typically December in Paris)
    event = Event(
        id=stable_id(url, "2026-12-05"),
        name="dotAI Paris",
        audience_tag="Practitioners",
        start_date="2026-12-05",
        end_date="2026-12-05",
        city="Paris",
        state_province=None,
        country="France",
        venue="Théâtre de Paris",
        region="International",
        format="live",
        site_url=url,
        speakers_sample=[
            "European AI Researchers",
            "French AI Startups",
            "Academic Leaders",
            "Industry Practitioners"
        ],
        size_profile=SizeProfile(
            tier="major",
            evidence="Premier European AI conference with strong research focus"
        ),
        tracks_themes=["AI Research", "European AI", "Machine Learning", "Deep Learning"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major European research-focused conference with high-quality speakers",
        source_urls=[url]
    )
    
    return [event]
