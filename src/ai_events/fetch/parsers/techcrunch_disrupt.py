"""TechCrunch Disrupt parser - major tech conference with significant AI coverage"""

from ai_events.models import Event, SizeProfile

async def parse(url: str = None) -> list[Event]:
    """Parse TechCrunch Disrupt events"""
    
    events = [
        Event(
            id="techcrunch-disrupt-sf-2025",
            name="TechCrunch Disrupt San Francisco 2025",
            start_date="2025-10-28",
            end_date="2025-10-30",
            city="San Francisco",
            state_province="CA",
            country="USA",
            region="US",
            format="live",
            site_url="https://techcrunch.com/events/tc-disrupt-2025/",
            call_for_speakers_url="https://techcrunch.com/events/tc-disrupt-2025/",
            tracks_themes=["Startup Ecosystem", "AI Innovation", "Venture Capital", "Enterprise Tech", "Consumer Tech"],
        audience_tag="Mixed Audience",
            size_profile=SizeProfile(
                tier="flagship",
                attendees_estimate=10000,
                evidence="Major annual tech conference with 10,000+ attendees"
            ),
            emerging_flagship=False,
            priority="go",
            source_urls=["https://techcrunch.com/events/"]
        ),
        Event(
            id="techcrunch-disrupt-sf-2026",
            name="TechCrunch Disrupt San Francisco 2026",
            start_date="2026-10-27",
            end_date="2026-10-29",
            city="San Francisco",
            state_province="CA",
            country="USA",
            region="US",
            format="live",
            site_url="https://techcrunch.com/events/tc-disrupt-2025/",
            call_for_speakers_url="https://techcrunch.com/events/tc-disrupt-2025/",
            tracks_themes=["Startup Ecosystem", "AI Innovation", "Venture Capital", "Enterprise Tech", "Consumer Tech"],
        audience_tag="Mixed Audience",
            size_profile=SizeProfile(
                tier="flagship",
                attendees_estimate=10000,
                evidence="Major annual tech conference with 10,000+ attendees"
            ),
            emerging_flagship=False,
            priority="go",
            source_urls=["https://techcrunch.com/events/"]
        )
    ]
    
    return events
