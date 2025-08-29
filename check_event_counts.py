#!/usr/bin/env python3
"""Check event counts in the database."""

from datetime import datetime, timedelta
import sys
sys.path.append('src')
from ai_events.models import Event
from ai_events.db import get_all_events

def main():
    # Get all events from database
    all_events_raw = get_all_events()
    
    # Get current date and 6 months from now
    today = datetime.now().date()
    horizon = today + timedelta(days=180)
    
    # Filter events in the date range
    all_events = []
    for event in all_events_raw:
        if event.start_date:
            event_date = datetime.fromisoformat(event.start_date).date()
            if today <= event_date <= horizon:
                all_events.append(event)
    
    # Count by region
    us_events = [e for e in all_events if e.region == 'US']
    intl_events = [e for e in all_events if e.region == 'International']
    
    print(f"Total events in database: {len(all_events_raw)}")
    print(f"Events in next 6 months: {len(all_events)}")
    print(f"US events: {len(us_events)}")
    print(f"International events: {len(intl_events)}")
    
    # Count by tier
    us_flagship = len([e for e in us_events if e.size_profile and e.size_profile.get('tier') == 'flagship'])
    us_major = len([e for e in us_events if e.size_profile and e.size_profile.get('tier') == 'major'])
    us_focused = len([e for e in us_events if e.size_profile and e.size_profile.get('tier') == 'focused'])
    us_other = len([e for e in us_events if not e.size_profile or e.size_profile.get('tier') not in ['flagship', 'major', 'focused']])
    
    intl_flagship = len([e for e in intl_events if e.size_profile and e.size_profile.get('tier') == 'flagship'])
    intl_major = len([e for e in intl_events if e.size_profile and e.size_profile.get('tier') == 'major'])
    intl_focused = len([e for e in intl_events if e.size_profile and e.size_profile.get('tier') == 'focused'])
    intl_other = len([e for e in intl_events if not e.size_profile or e.size_profile.get('tier') not in ['flagship', 'major', 'focused']])
    
    print(f"\nUS breakdown: {us_flagship} flagship, {us_major} major, {us_focused} focused, {us_other} other")
    print(f"International breakdown: {intl_flagship} flagship, {intl_major} major, {intl_focused} focused, {intl_other} other")
    
    # Check for events that might be missing
    print("\n\nChecking for events that might be filtered out...")
    
    # Events with missing dates
    no_date_events = [e for e in all_events_raw if not e.start_date]
    print(f"Events with no start date: {len(no_date_events)}")
    
    # Events in the past
    past_events = []
    for event in all_events_raw:
        if event.start_date:
            event_date = datetime.fromisoformat(event.start_date).date()
            if event_date < today:
                past_events.append(event)
    print(f"Past events: {len(past_events)}")
    
    # Events beyond 6 months
    future_events = []
    for event in all_events_raw:
        if event.start_date:
            event_date = datetime.fromisoformat(event.start_date).date()
            if event_date > horizon:
                future_events.append(event)
    print(f"Events beyond 6 months: {len(future_events)}")
    
    # Show some recent events that might be missing
    print("\n\nSome events that should be included:")
    sorted_events = sorted(all_events, key=lambda e: e.start_date)
    for event in sorted_events[:10]:
        print(f"- {event.name} ({event.start_date}) - {event.region} - {event.audience_tag or 'No audience tag'}")

if __name__ == "__main__":
    main()
