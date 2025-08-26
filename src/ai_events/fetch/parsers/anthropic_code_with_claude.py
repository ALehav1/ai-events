from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Anthropic Code with Claude conference data"""
    doc = await fetch_html(url)
    
    # Code with Claude 2026: May 22, 2025 - San Francisco, CA
    start, end = "2026-05-22", "2026-05-22"
    city, state, country, venue = "San Francisco", "CA", "USA", "TBD"
    
    ev = Event(
        id=stable_id(url, start),
        name="Code with Claude 2026",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url="https://www.anthropic.com/events/code-with-claude-2025",
        size_profile=SizeProfile(
            tier="major",
            evidence="Anthropic's first developer conference focused on Claude API and development tools"
        ),
        tracks_themes=["Claude API", "Model Context Protocol", "AI Agents", "Claude Code", "Developer Tools"],
        emerging_flagship=True,
        priority="go",
        why_priority="Anthropic's inaugural developer conference, Claude API focus, emerging AI company",
        source_urls=[url]
    )
    return [ev]
