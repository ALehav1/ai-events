#!/usr/bin/env python3
"""Cleanup script for AI Events Tracker static_events.json.

Removes events whose end_date is before a fixed cutoff date.

Usage:
    python3 cleanup_events.py

Notes:
- This script mutates src/ai_events/static_events.json in place.
- It preserves top-level metadata fields (version, description, etc.).
- It updates the last_updated field to the current date.
"""

import datetime
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Cutoff date: events that END strictly before this date will be removed.
CUTOFF_DATE_STR = "2025-12-07"
DATE_FMT = "%Y-%m-%d"

# Project-relative path to the JSON file
PROJECT_ROOT = Path(__file__).resolve().parent
EVENTS_PATH = PROJECT_ROOT / "src" / "ai_events" / "static_events.json"


def log(msg: str) -> None:
    """Lightweight logging helper.

    We keep this simple (no external deps) but very explicit so issues can be
    traced easily if something goes wrong during cleanup.
    """

    sys.stderr.write(f"[cleanup_events] {msg}\n")


def load_events(path: Path) -> Dict[str, Any]:
    """Load the static_events.json file.

    Returns the full document (including metadata) so we can preserve it.
    """

    log(f"Loading events from {path}")
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        log("ERROR: static_events.json not found. Aborting.")
        raise
    except json.JSONDecodeError as exc:
        log(f"ERROR: Failed to parse JSON: {exc}")
        raise

    if not isinstance(data, dict):
        log("ERROR: Top-level JSON is not an object; aborting.")
        raise SystemExit(1)

    if "events" not in data or not isinstance(data["events"], list):
        log("ERROR: JSON has no 'events' array; aborting.")
        raise SystemExit(1)

    return data


def parse_date(value: str, *, field: str, event_id: str) -> datetime.date:
    """Parse a YYYY-MM-DD date string with strong error logging.

    If parsing fails, we log an error and raise, because the data contract for
    this app assumes valid date strings in static_events.json.
    """

    try:
        return datetime.datetime.strptime(value, DATE_FMT).date()
    except Exception as exc:  # noqa: BLE001
        log(
            f"ERROR: Invalid {field}='{value}' for event id={event_id}: {exc}. "
            "Fix the data manually and re-run cleanup."
        )
        raise


def filter_events(events: List[Dict[str, Any]], cutoff: datetime.date) -> List[Dict[str, Any]]:
    """Return only events whose end_date is >= cutoff.

    Events missing start_date or end_date are treated as data errors and will
    be logged; for safety we keep them (so you can inspect/fix manually)
    rather than silently dropping them.
    """

    kept: List[Dict[str, Any]] = []

    for ev in events:
        eid = str(ev.get("id", "<missing-id>"))

        if "end_date" not in ev or "start_date" not in ev:
            log(
                f"WARN: Event id={eid} missing start_date or end_date; "
                "keeping it so it can be inspected manually."
            )
            kept.append(ev)
            continue

        end_date = parse_date(str(ev["end_date"]), field="end_date", event_id=eid)
        # Also parse start_date mainly to validate, even if we don't filter on it
        _ = parse_date(str(ev["start_date"]), field="start_date", event_id=eid)

        if end_date < cutoff:
            log(
                f"Removing event id={eid} with end_date={end_date} "
                f"(before cutoff {cutoff})"
            )
            continue

        kept.append(ev)

    return kept


def save_events(path: Path, data: Dict[str, Any]) -> None:
    """Persist the updated JSON back to disk with pretty formatting."""

    log(f"Writing updated events to {path}")
    tmp_path = path.with_suffix(".tmp")

    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=False)
        f.write("\n")

    # Atomic-ish rename on most platforms
    tmp_path.replace(path)


def main() -> int:
    cutoff_date = datetime.datetime.strptime(CUTOFF_DATE_STR, DATE_FMT).date()
    log(f"Cutoff date: {cutoff_date} (end_date strictly before this will be removed)")
    log(f"Target JSON file: {EVENTS_PATH}")

    data = load_events(EVENTS_PATH)
    events = data.get("events", [])

    original_count = len(events)
    log(f"Loaded {original_count} events from JSON")

    parsed_events: List[Dict[str, Any]] = events
    filtered_events = filter_events(parsed_events, cutoff_date)

    remaining_count = len(filtered_events)
    removed_count = original_count - remaining_count

    # Update metadata
    today_str = datetime.date.today().strftime(DATE_FMT)
    data["events"] = filtered_events
    data["last_updated"] = today_str

    save_events(EVENTS_PATH, data)

    # Summary on stdout for easy scripting/CI use
    print("Cleanup complete")
    print(f"  Cutoff date           : {cutoff_date}")
    print(f"  Original event count  : {original_count}")
    print(f"  Removed (past events) : {removed_count}")
    print(f"  Remaining events      : {remaining_count}")
    print(f"  last_updated          : {today_str}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
