from .models import Event
from .config import (
    PRIORITY_THRESHOLD, SCORE_FLAGSHIP, SCORE_MAJOR, SCORE_FOCUSED,
    SCORE_LLM_TOPIC, SCORE_EMERGING_FLAGSHIP, SCORE_US_REGION
)

def score(ev: Event) -> int:
    """Calculate priority score for an event based on various factors"""
    s = 0
    
    # Tier-based scoring
    if ev.size_profile:
        if ev.size_profile.tier == "flagship": 
            s += SCORE_FLAGSHIP
        elif ev.size_profile.tier == "major": 
            s += SCORE_MAJOR
        elif ev.size_profile.tier == "focused": 
            s += SCORE_FOCUSED
    
    # Topic relevance - check for LLM/AI keywords in tracks/themes
    topics_text = " ".join(ev.tracks_themes).upper()
    if any(keyword in topics_text for keyword in ["LLM", "AI", "ARTIFICIAL INTELLIGENCE", "MACHINE LEARNING", "ML"]):
        s += SCORE_LLM_TOPIC
    
    # Emerging flagship bonus - treat as flagship tier
    if ev.emerging_flagship:
        s += SCORE_FLAGSHIP  # Treat emerging flagships as full flagships
    
    # Regional preference for US events
    if ev.region == "US":
        s += SCORE_US_REGION
    
    return min(s, 100)  # Cap at 100

def apply_priority(ev: Event):
    """Apply priority classification based on calculated score"""
    event_score = score(ev)
    ev.priority = "go" if event_score >= PRIORITY_THRESHOLD else "maybe"
