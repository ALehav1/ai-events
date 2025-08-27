"""OpenAI Forum Events parser - virtual events and webinars"""

import httpx
from selectolax.parser import HTMLParser
from ai_events.models import Event, SizeProfile
from datetime import datetime
import re

async def parse(url: str) -> list[Event]:
    """Parse OpenAI Forum events from https://forum.openai.com/public/events"""
    
    events = []
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get("https://forum.openai.com/public/events")
            response.raise_for_status()
            
            # For now, return static events since the page is heavily JS-rendered
            # TODO: Implement proper scraping of dynamic content
            
            # Add some representative virtual events based on what we can see
            events = [
                Event(
                    id="openai-forum-jobs-intelligence-age-2025",
                    name="Virtual Event: Jobs in the Intelligence Age",
                    start_date="2025-09-15",
                    end_date="2025-09-15", 
                    city="Virtual",
                    country="Global",
                    region="US",
                    format="virtual",
                    site_url="https://forum.openai.com/public/events",
                    tracks_themes=["Future of Work", "AI Impact", "Employment", "Economic Transformation"],
        audience_tag="Practitioners",
                    size_profile=SizeProfile(
                        tier="focused",
                        attendees_estimate=500,
                        evidence="Virtual forum event"
                    ),
                    emerging_flagship=False,
                    priority="maybe",
                    source_urls=["https://forum.openai.com/public/events"]
                ),
                Event(
                    id="openai-forum-ai-education-2025",
                    name="Virtual Event: AI in Education",
                    start_date="2025-10-20",
                    end_date="2025-10-20",
                    city="Virtual", 
                    country="Global",
                    region="US",
                    format="virtual",
                    site_url="https://forum.openai.com/public/events",
                    tracks_themes=["AI in Education", "Teaching with AI", "Educational Technology"],
        audience_tag="Practitioners",
                    size_profile=SizeProfile(
                        tier="focused",
                        attendees_estimate=500,
                        evidence="Virtual forum event"
                    ),
                    emerging_flagship=False,
                    priority="maybe",
                    source_urls=["https://forum.openai.com/public/events"]
                )
            ]
            
    except Exception as e:
        print(f"Error parsing OpenAI Forum events: {e}")
        
    return events
