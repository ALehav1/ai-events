from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse London AI events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # AI & Big Data Expo Global 2026: February 4-5, 2026 - London, UK
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
        tracks_themes=["Big Data", "Machine Learning", "NLP", "Business Applications", "Responsible AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major global expo with comprehensive AI and big data coverage",
        source_urls=[url]
    )
    events.append(ev1)
    
    # Data & AI Governance Conference Europe 2026: March 23-26, 2026 - London, UK
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
    
    # Chief AI Officer Summit UK 2026: February 25, 2026 - London, UK
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
    
    # Global AI Conference 2026: June 29-30, 2026 - London, UK
    ev4 = Event(
        id=stable_id(url, "2026-06-29"),
        name="Global AI Conference",
        start_date="2026-06-29", 
        end_date="2026-06-30",
        city="London", 
        state_province="", 
        country="UK", 
        venue="ExCeL London",
        region="International", 
        format="live",
        site_url="https://www.rcr-ai-conference.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Influential AI event for global tech, science, and industry ecosystem"
        ),
        tracks_themes=["AI Technology", "AI Science", "Industry AI", "Global AI", "AI Innovation"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major global AI conference for tech, science, and industry professionals",
        source_urls=[url]
    )
    events.append(ev4)
    
    return events
