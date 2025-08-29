"""
Static event loader for JSON-based event data
Loads events from static_events.json instead of individual parser files
"""

import json
from pathlib import Path
from typing import List
from ..models import Event, SizeProfile

def load_static_events() -> List[Event]:
    """
    Load all events from the static JSON file
    
    Returns:
        List of Event objects loaded from static_events.json
    """
    # Path to the JSON file
    json_path = Path(__file__).parent.parent / "static_events.json"
    
    if not json_path.exists():
        print(f"Warning: static_events.json not found at {json_path}")
        return []
    
    # Load the JSON data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Convert JSON data to Event objects
    events = []
    for event_data in data.get('events', []):
        # Handle the size_profile separately since it's nested
        if 'size_profile' in event_data:
            event_data['size_profile'] = SizeProfile(**event_data['size_profile'])
        
        # Create Event object
        try:
            event = Event(**event_data)
            events.append(event)
        except Exception as e:
            print(f"Error loading event {event_data.get('name', 'Unknown')}: {e}")
            continue
    
    return events

def get_events() -> List[Event]:
    """
    Main function to get all events (compatible with existing interface)
    
    Returns:
        List of Event objects
    """
    return load_static_events()
