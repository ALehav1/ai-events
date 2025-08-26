from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Gartner AI and technology events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # Gartner IT Symposium/Xpo 2026: October 19-23, 2026 - Orlando, FL
    ev1 = Event(
        id=stable_id(url, "2026-10-19"),
        name="Gartner IT Symposium/Xpo 2026",
        start_date="2026-10-19", 
        end_date="2026-10-23",
        city="Orlando", 
        state_province="FL", 
        country="USA", 
        venue="Walt Disney World Swan and Dolphin Resort",
        region="US", 
        format="live",
        site_url="https://www.gartner.com/en/conferences/na/symposium-us",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Gartner's premier IT conference with extensive AI, automation, and digital transformation coverage"
        ),
        tracks_themes=["AI Strategy", "Digital Transformation", "IT Leadership", "Automation", "Enterprise AI"],
        emerging_flagship=True,
        priority="go",
        why_priority="Gartner's flagship IT conference with major AI and automation focus",
        source_urls=[url]
    )
    events.append(ev1)
    
    # Gartner Data & Analytics Summit 2026: March 23-25, 2026 - Orlando, FL
    ev2 = Event(
        id=stable_id(url, "2026-03-23"),
        name="Gartner Data & Analytics Summit 2026",
        start_date="2026-03-23", 
        end_date="2026-03-25",
        city="Orlando", 
        state_province="FL", 
        country="USA", 
        venue="Gaylord Palms Resort",
        region="US", 
        format="live",
        site_url="https://www.gartner.com/en/conferences/na/data-analytics-us",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Gartner's premier data and analytics conference with AI, ML, and advanced analytics focus"
        ),
        tracks_themes=["Data Analytics", "Machine Learning", "Advanced Analytics", "Data Strategy", "Business Intelligence"],
        emerging_flagship=True,
        priority="go",
        why_priority="Gartner's flagship data and analytics summit with comprehensive AI coverage",
        source_urls=[url]
    )
    events.append(ev2)
    
    # Gartner AI & Data Science Summit 2026: June 8-10, 2026 - London, UK
    ev3 = Event(
        id=stable_id(url, "2026-06-08"),
        name="Gartner AI & Data Science Summit 2026",
        start_date="2026-06-08", 
        end_date="2026-06-10",
        city="London", 
        state_province="", 
        country="UK", 
        venue="ExCeL London",
        region="International", 
        format="live",
        site_url="https://www.gartner.com/en/conferences/emea/ai-data-science-uk",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Gartner's dedicated AI and data science summit for European market"
        ),
        tracks_themes=["Artificial Intelligence", "Data Science", "Machine Learning", "AI Ethics", "AI Governance"],
        emerging_flagship=True,
        priority="go",
        why_priority="Gartner's dedicated AI and data science summit with global reach",
        source_urls=[url]
    )
    events.append(ev3)
    
    # Gartner Digital Workplace Summit 2026: May 12-13, 2026 - London, UK
    ev4 = Event(
        id=stable_id(url, "2026-05-12"),
        name="Gartner Digital Workplace Summit 2026",
        start_date="2026-05-12", 
        end_date="2026-05-13",
        city="London", 
        state_province="", 
        country="UK", 
        venue="The Brewery",
        region="International", 
        format="live",
        site_url="https://www.gartner.com/en/conferences/emea/digital-workplace-uk",
        size_profile=SizeProfile(
            tier="major",
            evidence="Gartner summit on digital workplace transformation with AI-powered productivity focus"
        ),
        tracks_themes=["Digital Workplace", "AI Productivity", "Workplace Automation", "Employee Experience"],
        emerging_flagship=False,
        priority="go",
        why_priority="Gartner summit focusing on AI-powered workplace transformation",
        source_urls=[url]
    )
    events.append(ev4)
    
    # Gartner Security & Risk Management Summit 2026: September 8-10, 2026 - National Harbor, MD
    ev5 = Event(
        id=stable_id(url, "2026-09-08"),
        name="Gartner Security & Risk Management Summit 2026",
        start_date="2026-09-08", 
        end_date="2026-09-10",
        city="National Harbor", 
        state_province="MD", 
        country="USA", 
        venue="Gaylord National Resort",
        region="US", 
        format="live",
        site_url="https://www.gartner.com/en/conferences/na/security-risk-management-us",
        size_profile=SizeProfile(
            tier="major",
            evidence="Gartner's premier security conference with AI security and risk management focus"
        ),
        tracks_themes=["AI Security", "Risk Management", "Cybersecurity", "AI Governance", "Security Operations"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major Gartner security summit with significant AI security coverage",
        source_urls=[url]
    )
    events.append(ev5)
    
    return events
