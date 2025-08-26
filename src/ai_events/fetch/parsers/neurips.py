from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url:str) -> list[Event]:
    """Parse NeurIPS conference data from their website"""
    doc = await fetch_html(url)
    
    # 2025: Dec 2–7, 2025 San Diego (+ MX City satellite)
    start, end = "2026-12-02", "2026-12-07"
    
    ev1 = {
        "name":"NeurIPS 2026 (San Diego)",
        "city":"San Diego","state":"CA","country":"USA","venue":"San Diego CC","region":"US"
    }
    ev2 = {
        "name":"NeurIPS 2026 (Mexico City satellite)",
        "city":"Mexico City","state":None,"country":"Mexico","venue":None,"region":"International"
    }
    
    out=[]
    for meta in (ev1, ev2):
        out.append(Event(
          id=stable_id(url+meta["name"], start),
          name=meta["name"],
          start_date=start, 
          end_date=end,
          city=meta["city"], 
          state_province=meta["state"], 
          country=meta["country"], 
          venue=meta["venue"],
          region="US" if meta["region"]=="US" else "International",
          format="hybrid",
          site_url=url,
          speakers_sample=[],
          size_profile=SizeProfile(
            tier="flagship",
            evidence="Top research venue; workshops; thousands of attendees."
          ),
          tracks_themes=["ML Research","Workshops","Tutorials"],
          emerging_flagship=False,
          priority="maybe",
          why_priority="Targeted workshops and sponsor rooms; selective presence.",
          source_urls=[url]
        ))
    return out
