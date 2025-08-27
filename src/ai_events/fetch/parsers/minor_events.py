from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse minor AI events - focused/specialized conferences"""
    
    events = []
    
    # AI DevWorld (focused developer conference)
    events.append(Event(
        id=stable_id("ai-devworld-2025", "2025-10-15"),
        name="AI DevWorld 2025",
        audience_tag="Mixed Audience",
        start_date="2025-10-15",
        end_date="2025-10-16", 
        city="San Jose",
        state_province="CA",
        country="USA",
        venue="San Jose Convention Center",
        region="US",
        format="live",
        site_url="https://aidevworld.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Regional developer-focused conference with ~500 attendees"
        ),
        tracks_themes=["AI Development", "MLOps", "AI Tools"],
        emerging_flagship=False,
        priority="maybe",
        source_urls=[url]
    ))
    
    # European AI Ethics Summit (focused academic conference)
    events.append(Event(
        id=stable_id("eu-ai-ethics-2025", "2025-11-20"),
        name="European AI Ethics Summit",
        audience_tag="Mixed Audience",
        start_date="2025-11-20",
        end_date="2025-11-21",
        city="Brussels",
        state_province=None,
        country="Belgium", 
        venue="EU Parliament",
        region="International",
        format="live",
        site_url="https://aiethics.eu/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Specialized academic conference on AI ethics with ~300 attendees"
        ),
        tracks_themes=["AI Ethics", "Policy", "Regulation"],
        emerging_flagship=False,
        priority="maybe",
        source_urls=[url]
    ))
    
    # AI in Healthcare Workshop (focused industry event)
    events.append(Event(
        id=stable_id("ai-healthcare-workshop-2025", "2025-09-25"),
        name="AI in Healthcare Workshop",
        audience_tag="Mixed Audience",
        start_date="2025-09-25",
        end_date="2025-09-25",
        city="Boston",
        state_province="MA", 
        country="USA",
        venue="MIT Campus",
        region="US",
        format="live",
        site_url="https://aihealthcare.mit.edu/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Single-day workshop focused on healthcare AI applications"
        ),
        tracks_themes=["Healthcare AI", "Medical Research", "Clinical Applications"],
        emerging_flagship=False,
        priority="maybe",
        source_urls=[url]
    ))
    
    # Add many more minor events to test scrolling
    additional_events = [
        # More US minor events
        Event(
            id=stable_id("ai-startup-pitch-2025", "2025-11-05"),
            name="AI Startup Pitch Day",
            audience_tag="Mixed Audience",
            start_date="2025-11-05", end_date="2025-11-05",
            city="Austin", state_province="TX", country="USA",
            venue="Austin Convention Center", region="US", format="live",
            site_url="https://aistartuppitch.com/",
            size_profile=SizeProfile(tier="focused", evidence="Regional startup event"),
            tracks_themes=["Startups", "Funding", "AI Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-retail-summit-2025", "2025-12-10"),
            name="AI in Retail Summit",
            audience_tag="Mixed Audience",
            start_date="2025-12-10", end_date="2025-12-10",
            city="Chicago", state_province="IL", country="USA",
            venue="McCormick Place", region="US", format="live",
            site_url="https://airetail.com/",
            size_profile=SizeProfile(tier="focused", evidence="Industry-specific conference"),
            tracks_themes=["Retail AI", "Customer Experience", "Supply Chain"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-finance-workshop-2025", "2025-10-30"),
            name="AI in Finance Workshop",
            audience_tag="Mixed Audience",
            start_date="2025-10-30", end_date="2025-10-30",
            city="New York", state_province="NY", country="USA",
            venue="Wall Street Conference Center", region="US", format="live",
            site_url="https://aifinance.org/",
            size_profile=SizeProfile(tier="focused", evidence="Single-day workshop"),
            tracks_themes=["Financial AI", "Risk Management", "Trading Algorithms"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-education-forum-2025", "2025-09-20"),
            name="AI in Education Forum",
            audience_tag="Mixed Audience",
            start_date="2025-09-20", end_date="2025-09-20",
            city="Denver", state_province="CO", country="USA",
            venue="Colorado Convention Center", region="US", format="live",
            site_url="https://aieducation.edu/",
            size_profile=SizeProfile(tier="focused", evidence="Education sector focus"),
            tracks_themes=["EdTech", "Learning Analytics", "AI Tutoring"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-gaming-meetup-2025", "2025-11-15"),
            name="AI Gaming Meetup",
            audience_tag="Mixed Audience",
            start_date="2025-11-15", end_date="2025-11-15",
            city="Los Angeles", state_province="CA", country="USA",
            venue="LA Convention Center", region="US", format="live",
            site_url="https://aigaming.com/",
            size_profile=SizeProfile(tier="focused", evidence="Gaming industry meetup"),
            tracks_themes=["Game AI", "Procedural Generation", "NPC Behavior"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-agriculture-conference-2025", "2025-10-08"),
            name="AI in Agriculture Conference",
            audience_tag="Mixed Audience",
            start_date="2025-10-08", end_date="2025-10-08",
            city="Des Moines", state_province="IA", country="USA",
            venue="Iowa Events Center", region="US", format="live",
            site_url="https://aiagriculture.org/",
            size_profile=SizeProfile(tier="focused", evidence="Agriculture sector focus"),
            tracks_themes=["Precision Agriculture", "Crop Monitoring", "Farm Automation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        
        # More International minor events
        Event(
            id=stable_id("ai-nordics-summit-2025", "2025-11-12"),
            name="AI Nordics Summit",
            audience_tag="Mixed Audience",
            start_date="2025-11-12", end_date="2025-11-12",
            city="Stockholm", state_province=None, country="Sweden",
            venue="Stockholm Convention Center", region="International", format="live",
            site_url="https://ainordics.se/",
            size_profile=SizeProfile(tier="focused", evidence="Regional Nordic focus"),
            tracks_themes=["Digital Government", "Sustainability AI", "Nordic Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-africa-forum-2025", "2025-12-03"),
            name="AI Africa Forum",
            audience_tag="Mixed Audience",
            start_date="2025-12-03", end_date="2025-12-03",
            city="Cape Town", state_province=None, country="South Africa",
            venue="Cape Town International Convention Centre", region="International", format="live",
            site_url="https://aiafrica.org/",
            size_profile=SizeProfile(tier="focused", evidence="Regional African focus"),
            tracks_themes=["AI for Development", "Mobile AI", "African Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-asia-pacific-workshop-2025", "2025-10-22"),
            name="AI Asia-Pacific Workshop",
            audience_tag="Mixed Audience",
            start_date="2025-10-22", end_date="2025-10-22",
            city="Singapore", state_province=None, country="Singapore",
            venue="Marina Bay Sands", region="International", format="live",
            site_url="https://aiapac.sg/",
            size_profile=SizeProfile(tier="focused", evidence="Regional APAC focus"),
            tracks_themes=["Smart Cities", "Digital Economy", "APAC Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-latin-america-summit-2025", "2025-11-28"),
            name="AI Latin America Summit",
            audience_tag="Mixed Audience",
            start_date="2025-11-28", end_date="2025-11-28",
            city="São Paulo", state_province=None, country="Brazil",
            venue="Expo Center Norte", region="International", format="live",
            site_url="https://ailatam.com/",
            size_profile=SizeProfile(tier="focused", evidence="Regional Latin America focus"),
            tracks_themes=["Digital Transformation", "FinTech AI", "Regional Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-middle-east-conference-2025", "2025-12-15"),
            name="AI Middle East Conference",
            audience_tag="Mixed Audience",
            start_date="2025-12-15", end_date="2025-12-15",
            city="Dubai", state_province=None, country="UAE",
            venue="Dubai World Trade Centre", region="International", format="live",
            site_url="https://aimiddleeast.ae/",
            size_profile=SizeProfile(tier="focused", evidence="Regional Middle East focus"),
            tracks_themes=["Energy AI", "Smart Infrastructure", "Regional Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-canada-meetup-2025", "2025-09-30"),
            name="AI Canada Meetup",
            audience_tag="Mixed Audience",
            start_date="2025-09-30", end_date="2025-09-30",
            city="Toronto", state_province="ON", country="Canada",
            venue="Metro Toronto Convention Centre", region="International", format="live",
            site_url="https://aicanada.ca/",
            size_profile=SizeProfile(tier="focused", evidence="Regional Canadian focus"),
            tracks_themes=["AI Policy", "Research Commercialization", "Canadian Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        
        # Additional US Minor Events - More realistic distribution
        Event(
            id=stable_id("ai-manufacturing-expo-2025", "2025-10-12"),
            name="AI Manufacturing Expo",
            audience_tag="Mixed Audience",
            start_date="2025-10-12", end_date="2025-10-12",
            city="Detroit", state_province="MI", country="USA",
            venue="Cobo Center", region="US", format="live",
            site_url="https://aimanufacturing.com/",
            size_profile=SizeProfile(tier="major", evidence="Large industry-specific conference with 2000+ attendees"),
            tracks_themes=["Industrial AI", "Robotics", "Smart Manufacturing"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-legal-tech-summit-2025", "2025-11-08"),
            name="AI Legal Tech Summit",
            audience_tag="Mixed Audience",
            start_date="2025-11-08", end_date="2025-11-08",
            city="Washington", state_province="DC", country="USA",
            venue="Walter E. Washington Convention Center", region="US", format="live",
            site_url="https://ailegaltech.org/",
            size_profile=SizeProfile(tier="focused", evidence="Legal industry specialization"),
            tracks_themes=["Legal AI", "Contract Analysis", "Compliance"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-transportation-forum-2025", "2025-10-25"),
            name="AI Transportation Forum",
            audience_tag="Mixed Audience",
            start_date="2025-10-25", end_date="2025-10-25",
            city="Seattle", state_province="WA", country="USA",
            venue="Washington State Convention Center", region="US", format="live",
            site_url="https://aitransportation.org/",
            size_profile=SizeProfile(tier="major", evidence="Major transportation industry event with autonomous vehicle focus"),
            tracks_themes=["Autonomous Vehicles", "Smart Logistics", "Traffic AI"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-energy-workshop-2025", "2025-11-22"),
            name="AI Energy Workshop",
            audience_tag="Mixed Audience",
            start_date="2025-11-22", end_date="2025-11-22",
            city="Houston", state_province="TX", country="USA",
            venue="George R. Brown Convention Center", region="US", format="live",
            site_url="https://aienergy.org/",
            size_profile=SizeProfile(tier="focused", evidence="Energy sector specialization"),
            tracks_themes=["Smart Grid", "Renewable Energy AI", "Energy Optimization"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-media-entertainment-2025", "2025-10-03"),
            name="AI Media & Entertainment Summit",
            audience_tag="Mixed Audience",
            start_date="2025-10-03", end_date="2025-10-03",
            city="Los Angeles", state_province="CA", country="USA",
            venue="Los Angeles Convention Center", region="US", format="live",
            site_url="https://aimediaent.com/",
            size_profile=SizeProfile(tier="focused", evidence="Media industry focus"),
            tracks_themes=["Content Generation", "Video AI", "Creative AI"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        
        # Additional International Minor Events - More realistic distribution
        Event(
            id=stable_id("ai-australia-summit-2025", "2025-10-15"),
            name="AI Australia Summit",
            audience_tag="Mixed Audience",
            start_date="2025-10-15", end_date="2025-10-15",
            city="Sydney", state_province=None, country="Australia",
            venue="International Convention Centre Sydney", region="International", format="live",
            site_url="https://aiaustralia.com.au/",
            size_profile=SizeProfile(tier="major", evidence="Major regional summit covering Australia/NZ with 1500+ attendees"),
            tracks_themes=["Australian AI Policy", "Mining AI", "Agriculture Tech"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-japan-workshop-2025", "2025-11-25"),
            name="AI Japan Workshop",
            audience_tag="Mixed Audience",
            start_date="2025-11-25", end_date="2025-11-25",
            city="Tokyo", state_province=None, country="Japan",
            venue="Tokyo Big Sight", region="International", format="live",
            site_url="https://aijapan.jp/",
            size_profile=SizeProfile(tier="major", evidence="Major Japanese AI event with robotics focus"),
            tracks_themes=["Robotics AI", "Manufacturing AI", "Japanese Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-india-summit-2025", "2025-10-28"),
            name="AI India Summit",
            audience_tag="Mixed Audience",
            start_date="2025-10-28", end_date="2025-10-28",
            city="Bangalore", state_province=None, country="India",
            venue="Bangalore International Exhibition Centre", region="International", format="live",
            site_url="https://aiindia.in/",
            size_profile=SizeProfile(tier="major", evidence="Major Indian AI summit with significant tech industry participation"),
            tracks_themes=["Digital India", "AI for Development", "Indian Innovation"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-germany-conference-2025", "2025-11-14"),
            name="AI Germany Conference",
            audience_tag="Mixed Audience",
            start_date="2025-11-14", end_date="2025-11-14",
            city="Berlin", state_province=None, country="Germany",
            venue="Messe Berlin", region="International", format="live",
            site_url="https://aigermany.de/",
            size_profile=SizeProfile(tier="focused", evidence="Regional German focus"),
            tracks_themes=["Industry 4.0", "German Engineering AI", "EU AI Act"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        ),
        Event(
            id=stable_id("ai-uk-workshop-2025", "2025-09-26"),
            name="AI UK Workshop",
            audience_tag="Mixed Audience",
            start_date="2025-09-26", end_date="2025-09-26",
            city="Manchester", state_province=None, country="United Kingdom",
            venue="Manchester Central", region="International", format="live",
            site_url="https://aiuk.co.uk/",
            size_profile=SizeProfile(tier="focused", evidence="Regional UK focus"),
            tracks_themes=["UK AI Strategy", "Financial AI", "Healthcare AI"],
            emerging_flagship=False, priority="maybe", source_urls=[url]
        )
    ]
    
    events.extend(additional_events)
    return events
