# AI Events Tracker

Automated tracking system for global AI conferences with intelligent prioritization and beautiful reports.

🌐 **Live Demo**: [https://ai-events-delta.vercel.app/](https://ai-events-delta.vercel.app/)

## What It Does

- **Tracks major AI conferences** through December 2026
- **Categorizes events** by Event tiers:
  - **Flagship**: 2000+ attendees
  - **Major**: 1000-2000 attendees
  - **Other**: <1000 attendees
- **Generates beautiful reports** with filtering and search
- **Updates weekly** via automation or manual trigger

## Quick Start

```bash
# Clone and setup
git clone https://github.com/ALehav1/ai-events.git
cd ai-events
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .

# Generate report
ai-events fetch    # Fetch event data
ai-events report   # Generate HTML report
open dist/report.html

# Deploy to Vercel
cp dist/report.html index.html
git add index.html && git commit -m "Update events" && git push
```

## Architecture

```text
ai-events/
├── src/ai_events/
│   ├── static_events.json     # All event data (48 current events)
│   ├── fetch/
│   │   ├── base.py           # HTTP fetch utilities (for future scrapers)
│   │   ├── static_loader.py  # JSON event loader
│   │   └── parsers/          # Legacy parsers (to be removed)
│   ├── models.py             # Event data model (Pydantic)
│   ├── db.py                 # SQLite persistence
│   ├── report.py             # HTML report generation
│   └── templates/            # Jinja2 templates
├── cleanup_events.py       # Maintenance script to remove past events
├── .windsurf/              # Windsurf IDE configuration
├── .vscode/                # VS Code tasks (Windsurf compatible)
├── scripts/                # Automation scripts
├── launchd/                # macOS weekly job configuration
└── dist/                   # Generated reports (created at runtime)
```

## Current State (December 2025)

- ✅ Major conferences tracked through December 2026
- ✅ All events migrated to single `static_events.json` file
- ✅ JSON-based loading system implemented
- ✅ Full system working and deployed
- ✅ Past events cleaned up (December 2025 - current data starts from Dec 10, 2025)

## Roadmap

### Phase 1: JSON Migration (✅ Completed)

- [x] Moved all static events to `static_events.json`
- [x] Created `static_loader.py` to load from JSON
- [x] Updated CLI to use JSON loader
- [x] Eliminated unnecessary HTTP fetches
- [x] Remove redundant parser files (cleanup complete)

### Phase 2: Optimization (Next)

- [ ] Add real scrapers for dynamic conferences
- [ ] Implement caching to reduce API calls
- [ ] Add event deduplication

### Phase 3: Enhancements (Future)

- [ ] Email/Slack notifications
- [ ] Calendar integration
- [ ] Trend analysis

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/ALehav1/ai-events.git
cd ai-events

# Create virtual environment (Python 3.11 required)
python3.11 -m venv .venv
source .venv/bin/activate

# Install package in development mode
pip install -e .
```

### Commands

```bash
# Fetch all events
ai-events fetch

# Generate HTML report
ai-events report

# Run both in sequence
ai-events fetch && ai-events report

# Open report
open dist/report.html

# Clean up past events (maintenance)
python3 cleanup_events.py
```

### Maintenance: Cleaning Up Past Events

The `cleanup_events.py` script removes events whose end date has passed:

```bash
# Remove events that ended before today
python3 cleanup_events.py
```

This script:

- Filters out events with `end_date < 2025-12-07` (or current cutoff)
- Updates the `last_updated` field in `static_events.json`
- Preserves all metadata and validates date formats
- Provides detailed logging and summary output

**When to run:**

- Periodically (monthly/quarterly) to keep the event list current
- Before generating reports for distribution
- After major conference seasons pass

### Testing

```bash
# Check parser functionality
python check_parsers.py

# Verify event counts
python check_event_counts.py

# Test JSON loader
python -c "from src.ai_events.fetch.static_loader import load_static_events; print(f'Loaded {len(load_static_events())} events')"
```

## Deployment

### Vercel (Current)

```bash
# Generate fresh report
ai-events fetch && ai-events report

# Copy to root for Vercel
cp dist/report.html index.html

# Commit and push
git add index.html
git commit -m "Update AI events report"
git push origin main
```

Vercel automatically deploys on push to main branch.

### Weekly Automation (macOS)

```bash
# Install launchd job
./scripts/install-launchd.sh

# Uninstall if needed
./scripts/uninstall-launchd.sh

# Check job status
launchctl list | grep ai.events
```

## Tech Stack

**Backend**: Python 3.11+, AsyncIO, SQLite

**Frontend**: JavaScript ES6+, Bootstrap 5.3

## Known Issues

### Tag Consistency
Several unresolved tag inconsistencies exist in parser files:
- **FinTech capitalization**: Some events use "FinTech" while others use "Fintech"
- **Generic AI tags**: Standalone "AI" tags appear alongside more specific tags
- **Infrastructure tags**: "Infrastructure" tags not consistently applied

These issues will be resolved during the JSON migration phase.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See LICENSE file for details

---

**Last updated: December 2024**
**JSON Migration: Completed**
