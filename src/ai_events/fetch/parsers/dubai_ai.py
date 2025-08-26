from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse Dubai AI events data"""
    # Static data - no web scraping needed for these events
    
    events = []
    
    # GITEX GLOBAL 2026: December 7-11, 2026 - Dubai, UAE
    ev1 = Event(
        id=stable_id(url, "2026-12-07"),
        name="GITEX GLOBAL 2026",
        start_date="2026-12-07", 
        end_date="2026-12-11",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Dubai Exhibition Centre, Expo City",
        region="International", 
        format="live",
        site_url="https://www.gitex.com/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="World's largest tech event with 5000+ exhibitors covering AI breakthroughs, quantum computing, and Metaverse"
        ),
        tracks_themes=["AI Breakthroughs", "Quantum Computing", "Metaverse", "Tech Innovation", "Startups"],
        emerging_flagship=True,
        priority="go",
        why_priority="World's largest tech event with major AI focus and global reach",
        source_urls=[url]
    )
    events.append(ev1)
    
    # AIBC Eurasia 2026: February 10-12, 2026 - Dubai, UAE
    ev2 = Event(
        id=stable_id(url, "2026-02-10"),
        name="AIBC Eurasia 2026",
        start_date="2026-02-10", 
        end_date="2026-02-12",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Festival Arena, Festival City",
        region="International", 
        format="live",
        site_url="https://www.aibcworld.com/eurasia/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Conference on AI and blockchain convergence with policymakers, developers, and investors"
        ),
        tracks_themes=["AI", "Blockchain", "Healthcare AI", "Education AI", "Smart Cities", "Policy"],
        emerging_flagship=False,
        priority="go",
        why_priority="Unique focus on AI-blockchain convergence with high-level attendees",
        source_urls=[url]
    )
    events.append(ev2)
    
    # AI Revolution in Healthcare Summit 2026: March 27, 2026 - Dubai, UAE
    ev3 = Event(
        id=stable_id(url, "2026-03-27"),
        name="AI Revolution in Healthcare Summit 2026",
        start_date="2026-03-27", 
        end_date="2026-03-27",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="JW Marriott Hotel Marina",
        region="International", 
        format="live",
        site_url="https://www.healthcareaisummit.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Specialized summit on clinical, operational, and regulatory AI advancements in healthcare"
        ),
        tracks_themes=["Healthcare AI", "Clinical AI", "Medical AI", "Regulatory AI", "Operational AI"],
        emerging_flagship=False,
        priority="go",
        why_priority="Specialized healthcare AI summit with clinical and regulatory focus",
        source_urls=[url]
    )
    events.append(ev3)
    
    # IPTC Summit on AI for the Energy Industry 2026: January 13-14, 2026 - Dubai, UAE
    ev4 = Event(
        id=stable_id(url, "2026-01-13"),
        name="IPTC Summit on AI for the Energy Industry 2026",
        start_date="2026-01-13", 
        end_date="2026-01-14",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Conrad Hotel Dubai",
        region="International", 
        format="live",
        site_url="https://www.iptcnet.org/ai-summit/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Industry-specific summit on AI for energy sector efficiency and decarbonization"
        ),
        tracks_themes=["Energy AI", "Decarbonization", "Energy Efficiency", "Sustainable AI", "Oil & Gas AI"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Industry-specific focus on energy sector AI applications",
        source_urls=[url]
    )
    events.append(ev4)
    
    # 2nd International Conference on Artificial Intelligence & Data Science 2026: February 12-13, 2026 - Dubai, UAE
    ev5 = Event(
        id=stable_id(url, "2026-02-12"),
        name="2nd International Conference on Artificial Intelligence & Data Science 2026",
        start_date="2026-02-12", 
        end_date="2026-02-13",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Dubai International Convention Centre",
        region="International", 
        format="live",
        site_url="https://www.aidata-conference.com/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference for data scientists, analysts, and tech professionals"
        ),
        tracks_themes=["AI Research", "Data Science", "Analytics", "Machine Learning", "Tech Innovation"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic-focused conference for data science professionals",
        source_urls=[url]
    )
    events.append(ev5)
    
    # Information System Design & Intelligent Applications (ISDIA) 2026: February 7, 2026 - Dubai, UAE
    ev6 = Event(
        id=stable_id(url, "2026-02-07"),
        name="Information System Design & Intelligent Applications (ISDIA) 2026",
        start_date="2026-02-07", 
        end_date="2026-02-07",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="University of Wollongong Dubai",
        region="International", 
        format="live",
        site_url="https://www.uowdubai.ac.ae/isdia/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Academic conference on Agentic AI & Sustainability by University of Wollongong"
        ),
        tracks_themes=["Agentic AI", "Sustainability", "Information Systems", "Intelligent Applications", "Academic Research"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Academic conference with unique focus on AI and sustainability",
        source_urls=[url]
    )
    events.append(ev6)
    
    # FiNext Awards & Conference Dubai 2026: February 10-11, 2026 - Dubai, UAE
    ev7 = Event(
        id=stable_id(url, "2026-02-10-finext"),
        name="FiNext Awards & Conference Dubai 2026",
        start_date="2026-02-10", 
        end_date="2026-02-11",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Dubai World Trade Centre",
        region="International", 
        format="live",
        site_url="https://www.finext.ae/",
        size_profile=SizeProfile(
            tier="focused",
            evidence="Financial sector conference on AI in finance, fintech, blockchain, and banking security"
        ),
        tracks_themes=["AI in Finance", "FinTech AI", "Blockchain", "Banking Security", "Financial AI"],
        emerging_flagship=False,
        priority="maybe",
        why_priority="Finance-focused conference with AI applications in banking and fintech",
        source_urls=[url]
    )
    events.append(ev7)
    
    # Dubai AI Festival 2026: April 14, 2026 - Dubai, UAE
    ev8 = Event(
        id=stable_id(url, "2026-04-14"),
        name="Dubai AI Festival 2026",
        start_date="2026-04-14", 
        end_date="2026-04-14",
        city="Dubai", 
        state_province="", 
        country="UAE", 
        venue="Madinat Jumeirah",
        region="International", 
        format="live",
        site_url="https://www.dubaiaifestival.com/",
        size_profile=SizeProfile(
            tier="major",
            evidence="Festival dedicated to AI innovations, investment opportunities, and ethical AI governance"
        ),
        tracks_themes=["AI Innovation", "AI Investment", "Ethical AI", "AI Governance", "AI Development"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major AI festival with focus on innovation, investment, and governance",
        source_urls=[url]
    )
    events.append(ev8)
    
    return events
