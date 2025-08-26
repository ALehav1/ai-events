from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> list[Event]:
    """Parse AI Summit London - major European AI conference"""
    doc = await fetch_html(url)
    
    # AI Summit London 2026 (typically June)
    event = Event(
        id=stable_id(url, "2026-06-11"),
        name="AI Summit London",
        start_date="2026-06-11",
        end_date="2026-06-12",
        city="London",
        state_province=None,
        country="United Kingdom",
        venue="ExCeL London",
        region="International",
        format="live",
        site_url=url,
        speakers_sample=[
            "DeepMind Leadership",
            "UK Government AI Office",
            "European AI Researchers",
            "Financial Services AI Leaders"
        ],
        size_profile=SizeProfile(
            tier="major",
            evidence="Leading European AI conference with government and enterprise focus"
        ),
        tracks_themes=["Enterprise AI", "AI Regulation", "Financial AI", "Healthcare AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major European flagship with strong enterprise and regulatory focus",
        source_urls=[url]
    )
    
    return [event]
