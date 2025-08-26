from .models import Event

def classify_region(country: str) -> str:
    """Classify country into US or International region"""
    us_variants = {"USA", "UNITED STATES", "UNITED STATES OF AMERICA", "US"}
    return "US" if country.upper() in us_variants else "International"
