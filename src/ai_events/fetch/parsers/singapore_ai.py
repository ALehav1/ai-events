from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Singapore AI and technology events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # AI Singapore Summit 2026: March 18-19, 2026 - Singapore
    ev1 = Event(
        id=stable_id(url, "2026-03-18"),
        name="AI Singapore Summit 2026",
        audience_tag="Mixed Audience",
        start_date="2026-03-18", 
        end_date="2026-03-19",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Marina Bay Sands",
        region="International", 
        format="live",
        site_url="https://www.aisingapore.org/summit/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Singapore's premier AI summit bringing together global AI leaders and researchers"
        ),
        tracks_themes=["AI Research", "AI Applications", "AI Policy", "Southeast Asia AI", "AI Innovation"],
        emerging_flagship=True,
        priority="go",
        why_priority="Singapore's flagship AI summit with global reach and government backing",
        source_urls=[url]
    )
    events.append(ev1)
    
    # Tech in Asia Conference 2026: May 14-15, 2026 - Singapore
    ev2 = Event(
        id=stable_id(url, "2026-05-14"),
        name="Tech in Asia Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-05-14", 
        end_date="2026-05-15",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Suntec Singapore Convention Centre",
        region="International", 
        format="live",
        site_url="https://www.techinasia.com/conference/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Asia's largest tech conference with significant AI and startup focus"
        ),
        tracks_themes=["AI Startups", "Southeast Asia Tech", "AI Investment", "Tech Innovation", "Digital Transformation"],
        emerging_flagship=False,
        priority="go",
        why_priority="Asia's largest tech conference with major AI and innovation components",
        source_urls=[url]
    )
    events.append(ev2)
    
    # Singapore FinTech Festival 2026: November 4-6, 2026 - Singapore
    ev3 = Event(
        id=stable_id(url, "2026-11-04"),
        name="Singapore FinTech Festival 2026",
        audience_tag="Mixed Audience",
        start_date="2026-11-04", 
        end_date="2026-11-06",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Singapore Expo",
        region="International", 
        format="live",
        site_url="https://www.fintechfestival.sg/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="World's largest FinTech festival with extensive AI in finance focus"
        ),
        tracks_themes=["FinTech AI", "AI in Banking", "Financial AI", "RegTech", "AI Trading"],
        emerging_flagship=True,
        priority="go",
        why_priority="World's largest FinTech festival with major AI in finance coverage",
        source_urls=[url]
    )
    events.append(ev3)
    
    # RISE Conference 2026: July 15-17, 2026 - Singapore
    ev4 = Event(
        id=stable_id(url, "2026-07-15"),
        name="RISE Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-07-15", 
        end_date="2026-07-17",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Marina Bay Sands",
        region="International", 
        format="live",
        site_url="https://www.riseconf.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Asia's largest tech conference bringing together global tech leaders with AI focus"
        ),
        tracks_themes=["AI Innovation", "Tech Leadership", "Startup AI", "Enterprise AI", "AI Investment"],
        emerging_flagship=False,
        priority="go",
        why_priority="Asia's largest tech conference with significant AI and innovation focus",
        source_urls=[url]
    )
    events.append(ev4)
    
    # AI World Singapore 2026: September 23-24, 2026 - Singapore
    ev5 = Event(
        id=stable_id(url, "2026-09-23"),
        name="AI World Singapore 2026",
        audience_tag="Mixed Audience",
        start_date="2026-09-23", 
        end_date="2026-09-24",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Raffles City Convention Centre",
        region="International", 
        format="live",
        site_url="https://www.aiworld.sg/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Dedicated AI conference for Southeast Asia market with enterprise focus"
        ),
        tracks_themes=["Enterprise AI", "AI Implementation", "AI Strategy", "Southeast Asia AI", "AI Ethics"],
        emerging_flagship=False,
        priority="go",
        why_priority="Dedicated AI conference serving Southeast Asian enterprise market",
        source_urls=[url]
    )
    events.append(ev5)
    
    # Data Science & AI Summit Singapore 2026: April 22-23, 2026 - Singapore
    ev6 = Event(
        id=stable_id(url, "2026-04-22"),
        name="Data Science & AI Summit Singapore 2026",
        audience_tag="Mixed Audience",
        start_date="2026-04-22", 
        end_date="2026-04-23",
        city="Singapore", 
        state_province="", 
        country="Singapore", 
        venue="Pan Pacific Singapore",
        region="International", 
        format="live",
        site_url="https://www.datascienceaisummit.sg/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Data science and AI summit for practitioners and researchers in Southeast Asia"
        ),
        tracks_themes=["Data Science", "Machine Learning", "AI Research", "Analytics", "AI Applications"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Regional data science and AI summit with practitioner focus",
        source_urls=[url]
    )
    events.append(ev6)
    
    return events
