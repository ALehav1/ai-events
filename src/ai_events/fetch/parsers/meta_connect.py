from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Meta Connect conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Meta Connect 2026: September 17-18, 2025 - Menlo Park, CA
    events.append(Event(
        id=stable_id("meta-connect", "2026-09-17"),
        name="Meta Connect 2026",
        start_date="2026-09-17", 
        end_date="2026-09-18",
        city="Menlo Park", 
        state_province="CA", 
        country="USA", 
        venue="Meta Headquarters",
        region="US", 
        format="live",
        site_url="https://www.meta.com/connect/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Meta's flagship developer conference with major AR/VR/AI announcements, Reality Labs updates"
        ),
        tracks_themes=["Meta AI", "Reality Labs", "AR/VR", "Llama Models", "Mixed Reality", "AI Platforms"],
        emerging_flagship=False,
        priority="go",
        why_priority="Meta's premier developer event, major AI model announcements, AR/VR platform updates",
        source_urls=[url]
    ))
    
    # LlamaCon 2026 (Meta's AI-focused event) - Date TBD
    events.append(Event(
        id=stable_id("llamacon", "2026-07-15"),
        name="LlamaCon 2026",
        start_date="2026-07-15", 
        end_date="2026-07-15",
        city="Menlo Park", 
        state_province="CA", 
        country="USA", 
        venue="Meta Headquarters",
        region="US", 
        format="live",
        site_url="https://www.meta.com/blog/connect-2025-llamacon-save-the-date/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Meta's inaugural AI-focused conference dedicated to Llama models and AI development"
        ),
        tracks_themes=["Llama Models", "Open Source AI", "AI Development", "Meta AI", "Large Language Models"],
        emerging_flagship=True,
        priority="go",
        why_priority="Meta's new AI-focused conference, major Llama model announcements, open source AI focus",
        source_urls=[url]
    ))
    
    return events
