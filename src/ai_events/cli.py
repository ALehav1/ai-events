import argparse, asyncio, webbrowser
from pathlib import Path
from .db import upsert_event, get_all_events
from .report import render_html
from .ics import write_ics
from .score import apply_priority
from .models import Event
from ai_events.fetch.parsers import (
    humanx, neurips, aiconf_sf, world_ai_summit, ray_summit, ai_summit_london, dotai,
    dreamforce, gtc, aws_reinvent, microsoft_ignite, google_io, apple_wwdc, kubecon,
    meta_connect, anthropic_code_with_claude, openai_devday, gartner, minor_events,
    ai4_vegas, data_ai_summit, ai_summit_nyc, world_summit_ai, superai_singapore, 
    deepfest_riyadh, ai_expo_africa, techcrunch_disrupt, ai_compute_nyc, odsc_west,
    strata_data_ai, south_florida_ai, austin_ai, singapore_ai, london_ai, dubai_ai, 
    los_angeles_ai, new_york_ai, lisbon_ai, openai_forum_events)

OUT_DIR = Path.cwd() / "dist"

async def fetch_all():
    """Fetch events from all configured sources"""
    events = []
    for parser, url in [
        (humanx, "https://www.humanx.co/"),
        (aiconf_sf, "https://aiconference.com/"),
        (neurips, "https://neurips.cc/"),
        (world_ai_summit, "https://worldsummit.ai/"),
        (ray_summit, "https://raysummit.anyscale.com/"),
        (ai_summit_london, "https://london.theaisummit.com/"),
        (dotai, "https://www.dotai.io/"),
        (minor_events, "https://example.com/minor-events"),
        (dreamforce, "https://www.salesforce.com/dreamforce/"),
        (gtc, "https://www.nvidia.com/gtc/"),
        (aws_reinvent, "https://reinvent.awsevents.com/"),
        (ai_compute_nyc, "https://www.eventbrite.com/e/new-york-ai-conference-tickets-912664222257"),
        (microsoft_ignite, "https://ignite.microsoft.com/"),
        (google_io, "https://io.google/2025/"),
        (apple_wwdc, "https://developer.apple.com/wwdc25/"),
        (kubecon, "https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/"),
        (odsc_west, "https://odsc.com/california/"),
        (meta_connect, "https://www.meta.com/connect/"),
        (anthropic_code_with_claude, "https://www.anthropic.com/events/code-with-claude-2025"),
        (openai_devday, "https://openai.com/index/announcing-devday-2025/"),
        (strata_data_ai, "https://www.oreilly.com/conferences/strata-data-ai.html"),
        (south_florida_ai, "https://www.southfloridaai.com/events"),
        (austin_ai, "https://www.austinai.com/events"),
        (gartner, "https://www.gartner.com/en/conferences"),
        (singapore_ai, "https://www.singaporeai.com/events"),
        (london_ai, "https://www.londonai.com/events"),
        (dubai_ai, "https://www.dubaiaiweek.com/events"),
        (los_angeles_ai, "https://www.laaiconference.com/events"),
        (new_york_ai, "https://www.nyaiconference.com/events"),
        (lisbon_ai, "https://www.lisbonai.com/events"),
        (ai4_vegas, "https://ai4.io/vegas/"),
        (data_ai_summit, "https://www.databricks.com/dataaisummit"),
        (ai_summit_nyc, "https://newyork.theaisummit.com/"),
        (world_summit_ai, "https://worldsummit.ai/"),
        (superai_singapore, "https://www.superai.com/"),
        (deepfest_riyadh, "https://deepfest.com"),
        (ai_expo_africa, "https://aiexpoafrica.com/"),
        (techcrunch_disrupt, "https://techcrunch.com/events/"),
        (openai_forum_events, "https://forum.openai.com/public/events")
    ]:
        try:
            events.extend(await parser.parse(url))
        except Exception as e:
            print(f"Error fetching from {url}: {e}")
    
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
