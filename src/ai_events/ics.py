from datetime import datetime
from pathlib import Path

ICS = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//AI Events Weekly//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{stamp}Z
SUMMARY:Review & send weekly AI events update
DESCRIPTION:Run the 7-month sweep; summarize new adds; prompt register/speaking decisions.
DTSTART;TZID=America/New_York:{dtstart}
RRULE:FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0;BYSECOND=0
END:VEVENT
END:VCALENDAR
"""

def write_ics(out: Path, next_monday_9_local: str):
    """Generate ICS calendar file for weekly AI events review"""
    uid = f"ai-events-weekly-{next_monday_9_local}"
    out.write_text(ICS.format(
        uid=uid,
        stamp=datetime.utcnow().strftime("%Y%m%dT%H%M%S"),
        dtstart=next_monday_9_local
    ), encoding="utf-8")
