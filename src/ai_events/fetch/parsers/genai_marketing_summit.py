from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Generative AI for Marketing Summit data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Generative AI for Marketing Summit 2025
    event = Event(
        id=stable_id(url, "2025-11-24"),
        name="Generative AI for Marketing Summit",
        start_date="2025-11-24",
        end_date="2025-11-26",
        city="London",
        country="UK",
        region="International",
        format="live",
        site_url="https://www.aidataanalytics.network/events-generative-ai-for-marketing",
        tracks_themes=["Generative AI", "Marketing Disruption", "GenAI Adoption", "Value Maximization", "Marketing Innovation"],
        audience_tag="Mixed Audience",
        size_profile=SizeProfile(
            tier="focused",
            attendees_estimate=350,
            evidence="~200-500 practitioners and regulators, AI Data Analytics Network event"
        ),
        emerging_flagship=False,
        priority="maybe",
        why_priority="Focused on GenAI adoption and value maximization in marketing"
    )
    events.append(event)
    
    return events
