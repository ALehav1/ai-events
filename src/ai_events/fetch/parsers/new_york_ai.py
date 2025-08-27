from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse New York AI events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # Gen AI Conference 2026: March 23, 2026 - New York, NY
    ev1 = Event(
        id=stable_id(url, "2026-03-23"),
        name="Gen AI Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-03-23", 
        end_date="2026-03-23",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="New York Convention Center",
        region="US", 
        format="live",
        site_url="https://www.genaiconference.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Platform for business leaders in AI, ML, data, innovation, and technology with enterprise focus"
        ),
        tracks_themes=["Generative AI", "AI Governance", "Generative Agents", "Enterprise AI", "AI Innovation"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major business-focused GenAI conference with enterprise AI governance focus",
        source_urls=[url]
    )
    events.append(ev1)
    
    # AI Summit NYC 2026: May 19, 2026 - New York, NY
    ev2 = Event(
        id=stable_id(url, "2026-05-19"),
        name="AI Summit NYC 2026",
        audience_tag="Mixed Audience",
        start_date="2026-05-19", 
        end_date="2026-05-19",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="Jacob K. Javits Convention Center",
        region="US", 
        format="live",
        site_url="https://www.aisummitnyc.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Business-focused AI summit on applications in finance, banking, and insurance"
        ),
        tracks_themes=["AI in Finance", "Banking AI", "Insurance AI", "Data Science", "Machine Learning"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major AI summit focused on financial services applications",
        source_urls=[url]
    )
    events.append(ev2)
    
    # AI Sports 2026: May 19, 2026 - New York, NY
    ev3 = Event(
        id=stable_id(url, "2026-05-19-sports"),
        name="AI Sports 2026",
        audience_tag="Mixed Audience",
        start_date="2026-05-19", 
        end_date="2026-05-19",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="Madison Square Garden Training Center",
        region="US", 
        format="live",
        site_url="https://www.aisports.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Conference for sports professionals and tech innovators on AI in high-performance sports"
        ),
        tracks_themes=["Sports AI", "Data Analytics", "Athlete Performance", "Team Building", "Fan Engagement"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized conference for AI applications in sports and athletics",
        source_urls=[url]
    )
    events.append(ev3)
    
    # AWS Summit New York 2026: June 17, 2026 - New York, NY
    ev4 = Event(
        id=stable_id(url, "2026-06-17"),
        name="AWS Summit New York 2026",
        audience_tag="Mixed Audience",
        start_date="2026-06-17", 
        end_date="2026-06-17",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="Jacob K. Javits Convention Center",
        region="US", 
        format="live",
        site_url="https://aws.amazon.com/events/summits/new-york/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Large-scale AWS tech conference with heavy emphasis on AI and generative AI tools"
        ),
        tracks_themes=["Cloud AI", "Generative AI", "AWS AI Services", "Machine Learning", "AI Infrastructure"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major AWS summit with significant AI and generative AI focus",
        source_urls=[url]
    )
    events.append(ev4)
    
    # AI, Data Science & Biotechnology Conference 2026: April 11-12, 2026 - New York, NY
    ev5 = Event(
        id=stable_id(url, "2026-04-11"),
        name="AI, Data Science & Biotechnology Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-04-11", 
        end_date="2026-04-12",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="NYU Linhart Center",
        region="US", 
        format="live",
        site_url="https://publichealth.nyu.edu/department/biostatistics/seminars-events",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference on AI, ML, data science, biotechnology, and robotics advancements"
        ),
        tracks_themes=["AI in Biotech", "Data Science", "Machine Learning", "Biotechnology", "Robotics"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic conference with focus on AI applications in biotechnology",
        source_urls=[url]
    )
    events.append(ev5)
    
    # PROMPT NYC AI Conference 2026: March 14-15, 2026 - New York, NY
    ev6 = Event(
        id=stable_id(url, "2026-03-14"),
        name="PROMPT NYC AI Conference 2026",
        audience_tag="Mixed Audience",
        start_date="2026-03-14", 
        end_date="2026-03-15",
        city="New York", 
        state_province="NY", 
        country="USA", 
        venue="New York Marriott Marquis",
        region="US", 
        format="live",
        site_url="https://prompt.nyc/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Conference bringing together AI experts, researchers, and enthusiasts for latest AI trends"
        ),
        tracks_themes=["AI Trends", "AI Research", "AI Applications", "Machine Learning", "AI Innovation"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Community-focused conference for AI experts and researchers",
        source_urls=[url]
    )
    events.append(ev6)
    
    return events
