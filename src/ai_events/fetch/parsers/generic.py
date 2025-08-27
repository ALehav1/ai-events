from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url:str, name:str, region:str) -> list[Event]:
    """
    Minimal placeholder parser for quick YAML-driven stubs.
    Use when you only want to track a known date/location from rules.yml.
    Replace with real parser when implementing specific source.
    """
    return [Event(
        id=stable_id(url,"2099-01-01"),
        name=name,
        start_date="2099-01-01",
        end_date="2099-01-02",
        city="TBD", 
        country="TBD",
        region="US" if region=="US" else "International",
        format="live",
        site_url=url,
        size_profile=SizeProfile(tier="focused", evidence="Placeholder; update parser."),
        emerging_flagship=False,
        source_urls=[url]
    )]
