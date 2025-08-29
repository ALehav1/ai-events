import argparse, asyncio, webbrowser
from pathlib import Path
from .db import upsert_event, get_all_events
from .report import render_html
from .ics import write_ics
from .score import apply_priority
from .models import Event
from .fetch.static_loader import load_static_events

OUT_DIR = Path.cwd() / "dist"

async def fetch_all():
    """Fetch events from all configured sources"""
    # Load events from static JSON file
    events = load_static_events()
    
    print(f"Loaded {len(events)} events from static_events.json")
    
    # Apply priority and save to database
    for ev in events:
        apply_priority(ev)
        upsert_event(ev)
    
    return events

def build_sections():
    """Build report sections from stored events"""
    from datetime import datetime
    
    # Filter to show events through December 2026
    from datetime import date
    today = datetime.now().date()
    horizon_end = date(2026, 12, 31)  # Fixed horizon through December 2026
    all_events = get_all_events()
    evs = [e for e in all_events if today <= datetime.fromisoformat(e.start_date).date() <= horizon_end]
    evs = sorted(evs, key=lambda e: (e.start_date, e.name))
    
    us = [e for e in evs if e.region == "US"]
    intl = [e for e in evs if e.region == "International"]
    
    # Get last report timestamp to identify truly new events
    from .db import load_meta, save_meta
    from datetime import datetime, timedelta
    
    last_report = load_meta("last_report_timestamp")
    new_items = []
    
    if last_report:
        # Show events that were first discovered since last report
        last_report_dt = datetime.fromisoformat(last_report)
        new_items = [e for e in evs if e.first_discovered and 
                    datetime.fromisoformat(e.first_discovered) > last_report_dt]
    else:
        # First run - show events discovered in the last 7 days as "new"
        week_ago = datetime.now() - timedelta(days=7)
        new_items = [e for e in evs if e.first_discovered and 
                    datetime.fromisoformat(e.first_discovered) > week_ago]
    
    # Save current timestamp for next run
    save_meta("last_report_timestamp", datetime.now().isoformat())
    
    # Categorize events by tier for breakdown stats
    def get_tier_breakdown(events):
        flagship = [e for e in events if (e.size_profile and e.size_profile.tier == "flagship") or e.emerging_flagship]
        major = [e for e in events if e.size_profile and e.size_profile.tier == "major" and not e.emerging_flagship]
        other = [e for e in events if e.size_profile and e.size_profile.tier == "focused"]
        return flagship, major, other
    
    us_flagship, us_major, us_other = get_tier_breakdown(us)
    intl_flagship, intl_major, intl_other = get_tier_breakdown(intl)
    new_flagship, new_major, new_other = get_tier_breakdown(new_items)
    
    return {
        "horizon_label": "Through December 2026",
        "new_items": new_items,
        "new_flagship": new_flagship,
        "new_major": new_major,
        "new_other": new_other,
        "us_events": us,
        "us_flagship": us_flagship,
        "us_major": us_major,
        "us_other": us_other,
        "intl_events": intl,
        "intl_flagship": intl_flagship,
        "intl_major": intl_major,
        "intl_other": intl_other
    }

def cmd_fetch(_):
    """Command: Fetch events from all sources"""
    asyncio.run(fetch_all())
    print("Fetched & upserted events.")

def cmd_report(_):
    """Command: Generate HTML report and calendar file"""
    sections = build_sections()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    render_html(sections, OUT_DIR / "report.html")
    
    # Generate calendar file (simplified: next Monday 9:00 AM)
    write_ics(OUT_DIR / "AI_Events_Weekly_Update.ics", "20250901T090000")
    print(f"Wrote {OUT_DIR/'report.html'} and .ics")

def cmd_open(args):
    """Command: Open event URLs in browser"""
    ev = next((e for e in get_all_events() if e.id.startswith(args.id)), None)
    if not ev:
        print("Event not found")
        return
    
    url = ev.register_url if args.action == "register" else ev.call_for_speakers_url or ev.site_url
    webbrowser.open(str(url))
    print("Opened:", url)

def cmd_list(args):
    """Command: List events with optional priority filter"""
    evs = get_all_events()
    for e in evs:
        if not args.priority or e.priority == args.priority:
            print(f"{e.start_date} {e.name} [{e.priority}] – {e.city}, {e.country} – {e.site_url}")

def main():
    """Main CLI entry point"""
    ap = argparse.ArgumentParser("ai-events")
    sp = ap.add_subparsers(required=True)

    # Fetch command
    p_fetch = sp.add_parser("fetch")
    p_fetch.set_defaults(func=cmd_fetch)
    
    # Report command
    p_report = sp.add_parser("report")
    p_report.set_defaults(func=cmd_report)
    
    # Open command
    p_open = sp.add_parser("open")
    p_open.add_argument("--id", required=True, help="prefix of event id (12 chars)")
    p_open.add_argument("--action", choices=["register", "speak"], default="register")
    p_open.set_defaults(func=cmd_open)

    # List command
    p_list = sp.add_parser("list")
    p_list.add_argument("--priority", choices=["go", "maybe"])
    p_list.set_defaults(func=cmd_list)

    args = ap.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
