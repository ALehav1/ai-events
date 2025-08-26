"""
AI Events Parser Template
========================

Use this template to create parsers for new AI events. Copy this file and modify it for each event source.

Instructions:
1. Replace 'template_name' with your parser name (e.g., 'london_ai', 'dubai_ai', 'nyc_ai')
2. Fill in the event data for each event you find
3. Set appropriate tier levels: 'flagship', 'major', or 'focused'
4. Set priority: 'go' for must-attend events, 'maybe' for optional
5. Add relevant tracks/themes
6. Save as: src/ai_events/fetch/parsers/YOUR_PARSER_NAME.py

Event Research Guidelines:
- Look for official conference websites
- Check event dates, venues, and descriptions
- Identify target audience and scale
- Note any special themes or tracks
- Verify if events are recurring annually

Tier Guidelines:
- Flagship: 2000+ attendees, major industry announcements, global reach
- Major: 500-2000 attendees, significant regional/industry impact
- Focused: <500 attendees, specialized audience, niche topics

Priority Guidelines:
- 'go': Essential events with high industry impact, major announcements, networking value
- 'maybe': Valuable but optional events, specialized focus, regional importance
"""

from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse AI events data - replace with your parser description"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # TEMPLATE EVENT - Replace with actual event data
    # Copy this block for each event you want to add
    ev_template = Event(
        id=stable_id(url, "2026-MM-DD"),  # Use event start date
        name="Event Name Here",
        start_date="2026-MM-DD",  # Format: YYYY-MM-DD
        end_date="2026-MM-DD",    # Format: YYYY-MM-DD (same as start if single day)
        city="City Name", 
        state_province="State/Province (leave empty for international)", 
        country="Country Name", 
        venue="Venue Name",
        region="US",  # Use "US" for United States, "International" for all others
        format="live",  # Always use "live" for in-person events
        site_url="https://event-website.com/",
        size_profile=SizeProfile(
            tier="major",  # Choose: "flagship", "major", or "focused"
            evidence="Brief description of why this tier was chosen"
        ),
        tracks_themes=["Theme 1", "Theme 2", "Theme 3", "AI Applications", "Industry Focus"],
        emerging_flagship=False,  # Set to True only for rapidly growing events
        priority="go",  # Choose: "go" or "maybe"
        why_priority="Brief explanation of why this priority was assigned",
        source_urls=[url]
    )
    events.append(ev_template)
    
    # ADD MORE EVENTS HERE - Copy the block above for each event
    
    return events

# EXAMPLE: London AI Events Parser
# Replace this with your actual events

async def parse_london_example(url: str) -> list[Event]:
    """Example parser for London AI events"""
    events = []
    
    # AI & Big Data Expo Global 2026
    ev1 = Event(
        id=stable_id(url, "2026-02-04"),
        name="AI & Big Data Expo Global",
        start_date="2026-02-04", 
        end_date="2026-02-05",
        city="London", 
        state_province="", 
        country="UK", 
        venue="Olympia London",
        region="International", 
        format="live",
        site_url="https://www.ai-expo.net/global/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Global expo focusing on AI, big data, ML, and NLP with business applications"
        ),
        tracks_themes=["AI", "Big Data", "Machine Learning", "NLP", "Business Applications", "Responsible AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major global expo with comprehensive AI and big data coverage",
        source_urls=[url]
    )
    events.append(ev1)
    
    # Data & AI Governance Conference Europe 2026
    ev2 = Event(
        id=stable_id(url, "2026-03-23"),
        name="Data & AI Governance Conference Europe",
        start_date="2026-03-23", 
        end_date="2026-03-26",
        city="London", 
        state_province="", 
        country="UK", 
        venue="London Conference Centre",
        region="International", 
        format="live",
        site_url="https://www.irmuk.co.uk/data-ai-governance/",
        size_profile=SizeProfile(
            tier="major",
            evidence="European conference on responsible data and AI governance with MDM focus"
        ),
        tracks_themes=["AI Governance", "Data Governance", "Master Data Management", "Responsible AI", "Ethics"],
        emerging_flagship=False,
        priority="go",
        why_priority="Critical focus on AI governance and responsible AI implementation",
        source_urls=[url]
    )
    events.append(ev2)
    
    # Chief AI Officer Summit UK 2026
    ev3 = Event(
        id=stable_id(url, "2026-02-25"),
        name="Chief AI Officer Summit UK",
        start_date="2026-02-25", 
        end_date="2026-02-25",
        city="London", 
        state_province="", 
        country="UK", 
        venue="London Business Centre",
        region="International", 
        format="live",
        site_url="https://www.caiosummit.com/uk/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Executive-level summit for Chief AI Officers and AI practitioners in Europe"
        ),
        tracks_themes=["AI Leadership", "AI Strategy", "Executive AI", "AI Implementation", "Enterprise AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Executive-level summit for AI leadership in Europe",
        source_urls=[url]
    )
    events.append(ev3)
    
    return events

"""
RESEARCH CHECKLIST:
□ Event name and official website
□ Exact dates (start and end)
□ Venue name and full address
□ City, state/province, country
□ Event description and focus areas
□ Target audience and estimated size
□ Recurring event or one-time
□ Registration/ticket information
□ Speaker lineup (if available)
□ Tracks, themes, or focus areas
□ Organizer information

SUBMISSION FORMAT:
When you find events, provide this information for each:

Event Name: [Full official name]
Dates: [Start date - End date, Year]
Location: [Venue, City, State/Province, Country]
Website: [Official URL]
Description: [Brief description of focus and audience]
Estimated Size: [Small <500, Medium 500-2000, Large 2000+]
Tier Suggestion: [flagship/major/focused]
Priority Suggestion: [go/maybe]
Themes: [List of 3-5 relevant themes/tracks]
Notes: [Any additional relevant information]

EXAMPLE SUBMISSION:
Event Name: AI & Big Data Expo Global
Dates: February 4-5, 2026
Location: Olympia London, London, UK
Website: https://www.ai-expo.net/global/
Description: Global expo on AI, big data, ML, and NLP with focus on business applications and responsible AI
Estimated Size: Large (2000+)
Tier Suggestion: major
Priority Suggestion: go
Themes: AI, Big Data, Machine Learning, NLP, Business Applications, Responsible AI
Notes: Part of larger tech expo series, strong business focus
"""
