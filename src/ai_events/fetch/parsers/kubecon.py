from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url: str) -> list[Event]:
    """Parse KubeCon + CloudNativeCon conference data"""
    doc = await fetch_html(url)
    
    events = []
    
    # KubeCon + CloudNativeCon Europe 2026: April 1-4, 2025 - London, UK
    events.append(Event(
        id=stable_id("kubecon-europe", "2026-04-01"),
        name="KubeCon + CloudNativeCon Europe 2026",
        start_date="2026-04-01", 
        end_date="2026-04-04",
        city="London", 
        state_province=None, 
        country="United Kingdom", 
        venue="ExCeL London",
        region="International", 
        format="live",
        site_url="https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="CNCF flagship conference with 12,000+ attendees, major Kubernetes and cloud native announcements"
        ),
        tracks_themes=["Kubernetes", "Machine Learning on Kubernetes", "Cloud Native AI", "Container Orchestration", "DevOps"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier cloud native conference, extensive AI/ML infrastructure content, major platform announcements",
        source_urls=[url]
    ))
    
    # KubeCon + CloudNativeCon North America 2025: November 10-13, 2025 - Atlanta, GA
    events.append(Event(
        id=stable_id("kubecon-north-america", "2025-11-10"),
        name="KubeCon + CloudNativeCon North America 2025",
        start_date="2025-11-10", 
        end_date="2025-11-13",
        city="Atlanta", 
        state_province="GA", 
        country="USA", 
        venue="Georgia World Congress Center",
        region="US", 
        format="live",
        site_url="https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/",
        size_profile=SizeProfile(
            tier="flagship",
            evidence="CNCF flagship North American conference with 12,000+ attendees, major cloud native platform announcements"
        ),
        tracks_themes=["Kubernetes", "Machine Learning on Kubernetes", "Cloud Native AI", "Container Orchestration", "DevOps"],
        emerging_flagship=False,
        priority="go",
        why_priority="Premier North American cloud native conference, extensive AI infrastructure content",
        source_urls=[url]
    ))
    
    return events
