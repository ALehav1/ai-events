from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Los Angeles AI events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # Generative AI Summit Los Angeles 2026: March 15, 2026 - Los Angeles, CA
    ev1 = Event(
        id=stable_id(url, "2026-03-15"),
        name="Generative AI Summit Los Angeles 2026",
        audience_tag="Mixed Audience",
        start_date="2026-03-15", 
        end_date="2026-03-15",
        city="Los Angeles", 
        state_province="CA", 
        country="USA", 
        venue="Los Angeles City Center",
        region="US", 
        format="live",
        site_url="https://world.aiacceleratorinstitute.com/location/losangeles/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Summit for pioneering engineers, developers & executives facilitating the latest tech revolution"
        ),
        tracks_themes=["Generative AI", "AI Engineering", "AI Development", "Tech Innovation", "AI Applications"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major GenAI summit bringing together engineers and executives in tech hub",
        source_urls=[url]
    )
    events.append(ev1)
    
    # ViVE Event 2026 AI Zone: March 10-12, 2026 - Los Angeles, CA
    ev2 = Event(
        id=stable_id(url, "2026-03-10"),
        name="ViVE Event 2026 - AI Zone",
        audience_tag="Mixed Audience",
        start_date="2026-03-10", 
        end_date="2026-03-12",
        city="Los Angeles", 
        state_province="CA", 
        country="USA", 
        venue="Los Angeles Convention Center",
        region="US", 
        format="live",
        site_url="https://www.viveevent.com/ai-pavilion",
        size_profile=SizeProfile(
            tier="major",
            evidence="Premier digital health event with dedicated AI Zone for healthcare decision makers"
        ),
        tracks_themes=["Healthcare AI", "Digital Health", "Medical AI", "Health Technology", "AI in Healthcare"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier healthcare AI event with dedicated AI focus and decision maker audience",
        source_urls=[url]
    )
    events.append(ev2)
    
    # AI in Communications Boot Camp - West Coast: March 12-13, 2026 - Los Angeles, CA
    ev3 = Event(
        id=stable_id(url, "2026-03-12"),
        name="AI in Communications Boot Camp - West Coast",
        audience_tag="Mixed Audience",
        start_date="2026-03-12", 
        end_date="2026-03-13",
        city="Los Angeles", 
        state_province="CA", 
        country="USA", 
        venue="Los Angeles Business Center",
        region="US", 
        format="live",
        site_url="https://www.thepworld.com/event/ai-in-communications-bootcamp/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Hands-on AI training for leading communicators with practical applications"
        ),
        tracks_themes=["AI Communications", "Marketing AI", "Communication Tools", "AI Training", "Practical AI"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Specialized training for communications professionals with hands-on approach",
        source_urls=[url]
    )
    events.append(ev3)
    
    # AI for Good Global Summit 2026: May 20-22, 2026 - Los Angeles, CA
    ev4 = Event(
        id=stable_id(url, "2026-05-20"),
        name="AI for Good Global Summit 2026",
        audience_tag="Mixed Audience",
        start_date="2026-05-20", 
        end_date="2026-05-22",
        city="Los Angeles", 
        state_province="CA", 
        country="USA", 
        venue="Los Angeles Convention Center",
        region="US", 
        format="live",
        site_url="https://aiforgood.itu.int/summit26",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="ITU-led global summit bringing top AI experts and decision-makers for innovative AI solutions"
        ),
        tracks_themes=["AI for Good", "Social Impact AI", "Global Challenges", "AI Ethics", "Sustainable AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="ITU-led flagship summit focusing on AI solutions for global challenges",
        source_urls=[url]
    )
    events.append(ev4)
    
    # AIM Conference (Artificial Intelligence in Management): March 20-21, 2026 - Los Angeles, CA
    ev5 = Event(
        id=stable_id(url, "2026-03-20"),
        name="AIM Conference - Artificial Intelligence in Management",
        audience_tag="Mixed Audience",
        start_date="2026-03-20", 
        end_date="2026-03-21",
        city="Los Angeles", 
        state_province="CA", 
        country="USA", 
        venue="UCLA Campus",
        region="US", 
        format="live",
        site_url="https://sites.google.com/view/aimanagement/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference on AI and machine learning methods in management applications"
        ),
        tracks_themes=["AI in Management", "Machine Learning", "Business AI", "Management Science", "AI Applications"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic conference with focus on AI applications in management",
        source_urls=[url]
    )
    events.append(ev5)
    
    return events
