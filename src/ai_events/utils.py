import hashlib, re
from datetime import datetime
from urllib.parse import urlparse

def stable_id(url: str, start_date: str) -> str:
    """Generate a stable 12-character ID from URL and start date"""
    return hashlib.sha1(f"{url}|{start_date}".encode()).hexdigest()[:12]

def clean_text(s: str) -> str:
    """Clean and normalize text by removing extra whitespace"""
    return re.sub(r"\s+", " ", s or "").strip()

def iso_today() -> str:
    """Get current date/time in ISO format"""
    return datetime.utcnow().isoformat()
