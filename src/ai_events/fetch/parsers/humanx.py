from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id, clean_text

async def parse(url:str) -> list[Event]:
    """Parse HumanX conference data from their website"""
    doc = await fetch_html(url)
    
    # Static data from HumanX website (Apr 6–9, 2026 — San Francisco, CA)
    start, end = "2026-04-06", "2026-04-09"
    city, state, country, venue = "San Francisco", "CA", "USA", "Moscone Center"
    
    # Sample speakers from site content
    speakers = [
        "Bret Taylor — Sierra / OpenAI (Chair)",
        "Andrew Ng — DeepLearning.AI",
        "Ali Ghodsi — Databricks",
        "Katrin Lehmann — Mercedes-Benz CIO",
        "May Habib — Writer"
    ]
    
    ev = Event(
        id=stable_id(url, start),
        name="HumanX",
        start_date=start, 
        end_date=end,
        city=city, 
        state_province=state, 
        country=country, 
        venue=venue,
        region="US", 
        format="live",
        site_url=url,
        call_for_speakers_url=None,  # add when published
        speakers_sample=speakers,
        size_profile=SizeProfile(
            tier="flagship",
            evidence="Positioned as 'Davos of AI' with F500 focus per official site."
        ),
        tracks_themes=["Enterprise AI Strategy","Agentic Systems","Governance"],
        emerging_flagship=False,
        priority="go",
        why_priority="Elite enterprise audience; high-caliber speakers; partner density.",
        source_urls=[url]
    )
    return [ev]
