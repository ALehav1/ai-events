from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> list[Event]:
    """Parse World AI Summit events from their website"""
    doc = await fetch_html(url)
    
    events = []
    
    # Amsterdam 2026 (Oct 8-9, 2025)
    amsterdam_event = Event(
        id=stable_id(url + "amsterdam", "2026-10-08"),
        name="World AI Summit Amsterdam",
        audience_tag="Business Leaders",
        start_date="2026-10-08",
        end_date="2026-10-09",
        city="Amsterdam",
        state_province=None,
        country="Netherlands",
        venue="Taets Art & Event Park",
        region="International",
        format="live",
        site_url=url,
        speakers_sample=[
            "Peter Sarlin — CEO, AMD Silo.AI",
            "Jason Snyder — Futurist and Forbes Contributor",
            "Karen Hao — NYT Bestselling Author",
            "Robert Petrosino — FBI Strategic AI Advisor"
        ],
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Branded as 'The only AI summit in the world that matters' with global reach"
        ),
        tracks_themes=["Enterprise AI", "AI Governance", "Startups", "Investment"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major international flagship with top-tier speakers and global recognition",
        source_urls=[url]
    )
    events.append(amsterdam_event)
    
    # Montreal 2026 (April 2026)
    montreal_event = Event(
        id=stable_id(url + "montreal", "2026-04-01"),
        name="World AI Summit Montreal",
        audience_tag="Business Leaders",
        start_date="2026-04-01",
        end_date="2026-04-02",
        city="Montreal",
        state_province="QC",
        country="Canada",
        venue=None,
        region="International",
        format="live",
        site_url="https://americas.worldsummit.ai/",
        speakers_sample=[],
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Part of global World AI Summit series"
        ),
        tracks_themes=["AI Innovation", "North American Market"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major North American flagship in the World AI Summit series",
        source_urls=[url]
    )
    events.append(montreal_event)
    
    # San Francisco 2026 (June 2026)
    sf_event = Event(
        id=stable_id(url + "sf", "2026-06-01"),
        name="World AI Summit San Francisco",
        audience_tag="Business Leaders",
        start_date="2026-06-01",
        end_date="2026-06-02",
        city="San Francisco",
        state_province="CA",
        country="USA",
        venue=None,
        region="US",
        format="live",
        site_url="https://worldsummit.ai/usa/",
        speakers_sample=[],
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Part of global World AI Summit series in Silicon Valley"
        ),
        tracks_themes=["Silicon Valley AI", "Tech Innovation", "Venture Capital"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major Silicon Valley flagship in the World AI Summit series",
        source_urls=[url]
    )
    events.append(sf_event)
    
    # Doha 2026 (Dec 9-10, 2025)
    doha_event = Event(
        id=stable_id(url + "doha", "2026-12-09"),
        name="World AI Summit Doha",
        audience_tag="Business Leaders",
        start_date="2026-12-09",
        end_date="2026-12-10",
        city="Doha",
        state_province=None,
        country="Qatar",
        venue=None,
        region="International",
        format="live",
        site_url="https://qatar.worldsummit.ai/",
        speakers_sample=[],
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Official patronage of Ministry of Communications and IT, State of Qatar"
        ),
        tracks_themes=["Middle East AI", "Government AI", "Digital Transformation"],
        emerging_flagship=False,
        priority="go",
        why_priority="Major Middle East flagship with government backing",
        source_urls=[url]
    )
    events.append(doha_event)
    
    return events
