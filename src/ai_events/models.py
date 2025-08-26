from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Literal
from datetime import datetime

Priority = Literal["go", "maybe"]
Region = Literal["US", "International"]
Format = Literal["live", "virtual", "hybrid"]

class SizeProfile(BaseModel):
    attendees_estimate: Optional[int] = None
    tier: Literal["flagship","major","focused"] = "focused"
    evidence: Optional[str] = None

class Event(BaseModel):
    id: str
    name: str
    start_date: str
    end_date: str
    city: str
    state_province: Optional[str] = None
    country: str
    venue: Optional[str] = None
    region: Region
    format: Format
    site_url: HttpUrl
    register_url: Optional[HttpUrl] = None
    call_for_speakers_url: Optional[HttpUrl] = None
    tracks_themes: List[str] = []
    emerging_flagship: bool = False
    priority: Priority = "maybe"
    why_priority: Optional[str] = None
    source_urls: List[str] = []
    last_seen: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    last_changed_hash: Optional[str] = None
    first_discovered: Optional[str] = None
    size_profile: Optional[SizeProfile] = None
