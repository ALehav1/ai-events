#!/usr/bin/env python3
"""
Script to migrate all events from parser files to static_events.json
This extracts events from all parser files and creates a consolidated JSON file
"""

import json
import asyncio
import importlib
import sys
from pathlib import Path
from typing import List, Dict, Any

# Add src to path so we can import ai_events modules
sys.path.insert(0, str(Path(__file__).parent))

from src.ai_events.models import Event

async def extract_events_from_parsers() -> List[Dict[str, Any]]:
    """Extract all events from parser files"""
    events = []
    parsers_dir = Path(__file__).parent / "src" / "ai_events" / "fetch" / "parsers"
    
    # List of parser modules to import (excluding __init__ and generic)
    parser_files = [
        f.stem for f in parsers_dir.glob("*.py") 
        if f.stem not in ["__init__", "generic"]
    ]
    
    print(f"Found {len(parser_files)} parser files to process")
    
    for parser_name in sorted(parser_files):
        try:
            # Import the parser module
            module = importlib.import_module(f"src.ai_events.fetch.parsers.{parser_name}")
            
            # Check if it has a parse function or get_events function
            if hasattr(module, 'get_events'):
                # Direct function that returns events
                parser_events = module.get_events()
                if parser_events:
                    print(f"  ✓ {parser_name}: {len(parser_events)} events")
                    for event in parser_events:
                        # Convert Event object to dict
                        if isinstance(event, Event):
                            event_dict = event.model_dump(exclude_none=True)
                            # Convert any HttpUrl objects to strings
                            if 'site_url' in event_dict:
                                event_dict['site_url'] = str(event_dict['site_url'])
                            if 'register_url' in event_dict:
                                event_dict['register_url'] = str(event_dict['register_url'])
                            if 'call_for_speakers_url' in event_dict:
                                event_dict['call_for_speakers_url'] = str(event_dict['call_for_speakers_url'])
                            events.append(event_dict)
            elif hasattr(module, 'parse'):
                # Async parser function
                url = getattr(module, 'URL', None) or f"https://example.com/{parser_name}"
                parser_events = await module.parse(url)
                if parser_events:
                    print(f"  ✓ {parser_name}: {len(parser_events)} events")
                    for event in parser_events:
                        if isinstance(event, Event):
                            event_dict = event.model_dump(exclude_none=True)
                            # Convert any HttpUrl objects to strings
                            if 'site_url' in event_dict:
                                event_dict['site_url'] = str(event_dict['site_url'])
                            if 'register_url' in event_dict:
                                event_dict['register_url'] = str(event_dict['register_url'])
                            if 'call_for_speakers_url' in event_dict:
                                event_dict['call_for_speakers_url'] = str(event_dict['call_for_speakers_url'])
                            events.append(event_dict)
            else:
                print(f"  ⚠ {parser_name}: No parse or get_events function found")
                
        except Exception as e:
            print(f"  ✗ {parser_name}: Error - {str(e)}")
            
    return events

async def main():
    """Main migration function"""
    print("Starting migration of events to JSON...")
    print("-" * 50)
    
    # Extract all events
    events = await extract_events_from_parsers()
    
    print("-" * 50)
    print(f"Total events extracted: {len(events)}")
    
    # Sort events by start date, then by name
    events.sort(key=lambda x: (x.get('start_date', ''), x.get('name', '')))
    
    # Create the JSON structure
    json_data = {
        "version": "1.0.0",
        "last_updated": "2024-12-29",
        "description": "Consolidated AI events data migrated from parser files",
        "events": events
    }
    
    # Write to static_events.json
    output_path = Path(__file__).parent / "src" / "ai_events" / "static_events.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Successfully wrote {len(events)} events to {output_path}")
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("-" * 30)
    
    # Count by region
    us_count = sum(1 for e in events if e.get('region') == 'US')
    intl_count = sum(1 for e in events if e.get('region') == 'International')
    print(f"US Events: {us_count}")
    print(f"International Events: {intl_count}")
    
    # Count by tier
    tiers = {}
    for event in events:
        if 'size_profile' in event and 'tier' in event.get('size_profile', {}):
            tier = event['size_profile']['tier']
            tiers[tier] = tiers.get(tier, 0) + 1
    
    for tier, count in sorted(tiers.items()):
        print(f"{tier.capitalize()} Events: {count}")
    
    # Count by format
    formats = {}
    for event in events:
        format_type = event.get('format', 'unknown')
        formats[format_type] = formats.get(format_type, 0) + 1
    
    print("\nBy Format:")
    for format_type, count in sorted(formats.items()):
        print(f"  {format_type}: {count}")

if __name__ == "__main__":
    asyncio.run(main())
