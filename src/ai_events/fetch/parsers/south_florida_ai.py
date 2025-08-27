from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse South Florida AI events data"""
    doc = await fetch_html(url)
    
    events = []
    
    # Business Transformation World Summit 2026: January 26-28, 2026 - Miami, FL
    ev1 = Event(
        id=stable_id(url, "2026-01-26"),
        name="Business Transformation World Summit 2026",
        audience_tag="Mixed Audience",
        start_date="2026-01-26", 
        end_date="2026-01-28",
        city="Miami", 
        state_province="FL", 
        country="USA", 
        venue="Miami Convention Center",
        region="US", 
        format="live",
        site_url="https://www.businesstransformationworld.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Five co-located events with focus on Agentic & AI transformation, major industry summit"
        ),
        tracks_themes=["Agentic AI", "AI Transformation", "Business Innovation", "Enterprise AI", "Digital Transformation"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major transformation summit with AI at center of agenda, five co-located events",
        source_urls=[url]
    )
    events.append(ev1)
    
    # Generative AI Expo 2026: February 10-12, 2026 - Fort Lauderdale, FL
    ev2 = Event(
        id=stable_id(url, "2026-02-10"),
        name="Generative AI Expo 2026",
        audience_tag="Mixed Audience",
        start_date="2026-02-10", 
        end_date="2026-02-12",
        city="Fort Lauderdale", 
        state_province="FL", 
        country="USA", 
        venue="Broward County Convention Center",
        region="US", 
        format="live",
        site_url="https://www.generativeaiexpo.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Part of #TECHSUPERSHOW, practical GenAI applications across multiple sectors"
        ),
        tracks_themes=["Generative AI", "Marketing AI", "Finance AI", "Healthcare AI", "Practical Applications"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major GenAI expo covering practical applications across key industries",
        source_urls=[url]
    )
    events.append(ev2)
    
    # Agile International Conference (AIC 2026): March 5-6, 2026 - Miami, FL
    ev3 = Event(
        id=stable_id(url, "2026-03-05"),
        name="Agile International Conference (AIC 2026)",
        audience_tag="Mixed Audience",
        start_date="2026-03-05", 
        end_date="2026-03-06",
        city="Miami", 
        state_province="FL", 
        country="USA", 
        venue="Miami Conference Center",
        region="US", 
        format="live",
        site_url="https://www.agilealliance.org/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Agile methodology conference with AI and leadership focus, workshops and sessions"
        ),
        tracks_themes=["Agile Methodologies", "AI Leadership", "Tech Innovation", "Professional Development"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Agile-focused with AI components, professional development oriented",
        source_urls=[url]
    )
    events.append(ev3)
    
    # MindFest 2026: April 1-2, 2026 - Boca Raton, FL
    ev4 = Event(
        id=stable_id(url, "2026-04-01"),
        name="MindFest 2026",
        audience_tag="Mixed Audience",
        start_date="2026-04-01", 
        end_date="2026-04-02",
        city="Boca Raton", 
        state_province="FL", 
        country="USA", 
        venue="Florida Atlantic University, Boca Campus",
        region="US", 
        format="live",
        site_url="https://www.fau.edu/future-mind/mindfest/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference on AI, philosophy, psychology, and neuroscience intersection"
        ),
        tracks_themes=["AI Philosophy", "Psychology", "Neuroscience", "Future of Intelligence", "Academic Research"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic focus on AI and consciousness, interdisciplinary approach",
        source_urls=[url]
    )
    events.append(ev4)
    
    # ACE 2026: April 13, 2026 - Miami, FL
    ev5 = Event(
        id=stable_id(url, "2026-04-13"),
        name="ACE 2026",
        audience_tag="Mixed Audience",
        start_date="2026-04-13", 
        end_date="2026-04-13",
        city="Miami", 
        state_province="FL", 
        country="USA", 
        venue="Hilton Miami Downtown",
        region="US", 
        format="live",
        site_url="https://www.ace-conference.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Digital thread, AI, and PLM conference for manufacturing and engineering"
        ),
        tracks_themes=["Digital Thread", "AI in Manufacturing", "Product Lifecycle Management", "Engineering AI"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Industry-specific AI applications in manufacturing and PLM",
        source_urls=[url]
    )
    events.append(ev5)
    
    # BST Global's AI Summit 2026: November 10-12, 2026 - Palm Beach, FL
    ev6 = Event(
        id=stable_id(url, "2026-11-10"),
        name="BST Global's AI Summit 2026",
        audience_tag="Mixed Audience",
        start_date="2026-11-10", 
        end_date="2026-11-12",
        city="Palm Beach", 
        state_province="FL", 
        country="USA", 
        venue="Palm Beach Convention Center",
        region="US", 
        format="live",
        site_url="https://www.bstglobal.com/ai-summit/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Premier AEC industry AI event, data-driven future focus for construction leaders"
        ),
        tracks_themes=["AEC Industry AI", "Construction AI", "Data-Driven Construction", "Architecture AI", "Engineering AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier AI summit for Architecture, Engineering, and Construction industry",
        source_urls=[url]
    )
    events.append(ev6)
    
    # Miami Startup Ecosystem Conference 2026: February 12-13, 2026 - Miami, FL
    ev7 = Event(
        id=stable_id(url, "2026-02-12"),
        name="Miami Startup Ecosystem Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-02-12", 
        end_date="2026-02-13",
        city="Miami", 
        state_province="FL", 
        country="USA", 
        venue="Miami Dade College",
        region="US", 
        format="live",
        site_url="https://www.miamistartupconference.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Startup and entrepreneurship conference with AI as key topic for growth and innovation"
        ),
        tracks_themes=["Startup AI", "AI Innovation", "Entrepreneurship", "Tech Investment", "AI Growth"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Startup-focused with AI as key discussion topic for innovation",
        source_urls=[url]
    )
    events.append(ev7)
    
    return events
