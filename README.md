# AI Events Tracker

Automated AI events tracking system that fetches, analyzes, and reports on global AI conferences with intelligent prioritization, advanced filtering, and Windsurf IDE integration.

## Recent Updates

### December 2024 - Audience Tag Integration & Event Count Fix

- **Audience Tag System**: Successfully implemented comprehensive audience categorization
  - Added audience_tag field to Event model for target audience classification
  - Categories: Business Leaders, Tech Leaders, Mixed Audience, Practitioners
  - All 70+ event parsers updated with appropriate audience tags based on event focus
  - Tags displayed prominently on event cards with distinct styling
- **Advanced Tag Filtering**: Complete overhaul of tag filtering system
  - Fixed multi-word tag handling by switching from space to pipe delimiter
  - Tag filter dropdown now shows tier tags first (Flagship/Major/Focused), then audience tags
  - Proper separation between tag categories with visual dividers
  - All audience tags now appear in filter (previously only "Practitioners" was showing)
- **Tag Display Hierarchy**: Reordered tag presentation for better visual hierarchy
  - Event tier (Flagship/Major) appears first on event cards
  - Audience tag appears second
  - Format and theme tags follow
- **Filter UX Improvements**: Enhanced user experience with instructional placeholders
  - "Select (any)" placeholder text instead of confusing "0 items"
  - Multi-select functionality for both city and tag filters
  - Dynamic filter updates based on selections
- **Event Count Accuracy Fix**: Resolved discrepancy between desktop and mobile event counts
  - Fixed JavaScript counting logic that was incorrectly adding minor events to totals
  - Desktop and mobile now show consistent counts (76 US, 57 International)
  - Minor events are properly categorized but not double-counted in statistics
  - **Note**: Mobile/desktop consistency fully resolved by ensuring index.html is synced with dist/report.html for Vercel deployment
- **Event Statistics Display Refinement**: Improved clarity and visual consistency of event counts
  - Stats boxes now show only significant events (Flagship + Major) as the main count
  - Added breakdown showing "X Flagship + Y Major" with "(plus Z other)" below
  - Made stats boxes smaller and more compact for better visual balance
  - Removed "Significant Events" subtitle for cleaner appearance
  - Fixed text alignment issues by shortening "International Events" to "Intl Events"
  - Stats boxes now have consistent height and internal spacing

### November 2024

- **Comprehensive Event Addition**: Expanded from 44 to 63 total events with major flagship conferences
- **Date System Overhaul**: Fixed filtering to use current date, extended horizon through December 2026
- **CSS Layout Fixes**: Implemented perfect card alignment with grid and flexbox improvements
- **Documentation Updates**: Updated README to reflect current system capabilities and event counts

### October 2024

- **Initial System Creation**: Built complete AI events tracking system with web scraping and reporting
- **Windsurf Integration**: Added keyboard shortcuts, NPM scripts, and command palette integration
- **macOS Automation**: Implemented weekly launchd job with installation scripts
- **Database System**: SQLite persistence with change detection and event history

## Live Demo

🌐 **View the live AI Events Tracker**: [https://ai-events-delta.vercel.app/](https://ai-events-delta.vercel.app/)

## Features

- **🔍 Intelligent Event Discovery**: Automatically scrapes 40+ major AI conference websites globally
- **📊 Smart Categorization**: Events classified as Flagship, Major, or Other tier with intelligent scoring
- **📱 Beautiful Reports**: Professional HTML reports with perfect card alignment and responsive design
- **🔧 Advanced Filtering**: Multi-select city and tag filters for precise event discovery (shows "All" when no filters selected)
- **📅 Calendar Integration**: Generates ICS files for seamless calendar import
- **⚡ Windsurf Integration**: One-click commands, NPM scripts, and keyboard shortcuts
- **🤖 Weekly Automation**: macOS launchd job for hands-free operation
- **🌍 Global Coverage**: Events across North America, Europe, Asia, Middle East, and Africa
- **📍 Location Details**: Complete city, state/country information for all events
- **🎯 Through December 2026**: Fixed horizon for comprehensive AI event planning
- **📈 Dynamic Statistics**: US/International significant event counts with breakdowns update in real-time

## Architecture & Lessons Learned

### Understanding the Codebase

This section captures key insights about the codebase architecture that may not be immediately obvious:

#### 1. **Data Flow Architecture**

- **Parsers** → **Event Model** → **Database** → **Report Template** → **HTML Output**
- Each parser creates Event objects that must strictly conform to the Pydantic model
- The report template uses Jinja2 with embedded JavaScript for filtering

#### 2. **Critical Integration Points**

- **Event Model (`models.py`)**: The single source of truth for all event data structure
- **Report Template (`report.html.j2`)**: Complex Jinja2 template with embedded JavaScript
- **Tag System**: Tags are used for both visual display AND filtering logic
  - Tags must be properly formatted in `data-tags` attribute (pipe-delimited)
  - JavaScript splits and categorizes tags for filter dropdowns

#### 3. **Common Pitfalls & Solutions**

- **Multi-word Tags**: Initially broke filtering when space-delimited
  - Solution: Changed to pipe delimiter (`|`) in data-tags attribute
- **Audience Tag Filtering**: Only showed "Practitioners" due to hardcoded filter logic
  - Solution: Dynamic tag categorization in JavaScript
- **Tag Ordering**: Business requirement for tier tags to appear first
  - Solution: Explicit ordering in both template and JavaScript
- **Event Count Discrepancy**: Mobile showed 84/59 events while desktop showed 76/57 ✅ RESOLVED
  - Root cause: JavaScript was double-counting minor events in totals
  - Solution: Modified updateEventCounts() to exclude minor events from total count
  - **Final fix**: Syncing index.html with dist/report.html ensures consistency across all views
- **Stats Display Clarity**: Main event count was confusing (showed less than sum of categories)
  - Root cause: Total included only Flagship + Major, but wasn't clear to users
  - Solution: Changed display to show significant events only with clear breakdown

#### 4. **Template Complexity**

The report template (`report.html.j2`) is deceptively complex:
- Event cards have both visible tags and data attributes for filtering
- JavaScript functions handle dynamic filtering without page reload
- Tag categorization happens in multiple places (must stay synchronized)

#### 5. **Parser Patterns**

All parsers follow a consistent pattern but with important requirements:
- Must return a list of Event objects (even if just one event)
- Must set all required fields including the new `audience_tag`
- Must use `stable_id()` for consistent event identification
- Dates must be future dates in ISO format

## Project Structure

```
ai-events/
├── src/ai_events/           # Core Python package
│   ├── models.py            # Pydantic data models (Event, SizeProfile)
│   ├── db.py               # SQLite database operations
│   ├── cli.py              # Command-line interface & parser imports
│   ├── score.py            # Event scoring and prioritization
│   ├── report.py           # HTML report generation with Jinja2
│   ├── fetch/              # Web scraping system
│   │   ├── base.py         # HTTP client and HTML parsing utilities
│   │   ├── rules.yml       # Source configuration (currently unused)
│   │   └── parsers/        # Site-specific parsers (70+ files)
│   └── templates/          # Jinja2 HTML templates
│       └── report.html.j2  # Main report template with JS filtering
├── .windsurf/              # Windsurf IDE configuration
├── .vscode/                # VS Code tasks (Windsurf compatible)
├── scripts/                # Automation scripts
├── launchd/                # macOS weekly job configuration
└── dist/                   # Generated reports (created at runtime)
```

## Quick Setup (Windsurf on macOS)

1. **Clone/Open Project**:
   ```bash
   # Open in Windsurf: File > Open Folder... > ~/Desktop/ai-events
   ```

2. **Setup Environment**:
   ```bash
   python3.11 -m venv .venv && source .venv/bin/activate
   pip install -e .
   ```

3. **Generate First Report**:
   ```bash
   ai-events fetch && ai-events report && open dist/report.html
   ```

## Windsurf Integration

### Command Palette Commands

- **"AI Events: Generate & Open Report"** (Cmd+Shift+R) - Full workflow
- **"AI Events: Fetch Data Only"** - Update database only
- **"AI Events: List Priority Events"** - Show high-priority events

### NPM Scripts (Windsurf Run Panel)

- `npm run report` - Generate complete report
- `npm run fetch` - Fetch events only
- `npm run list` - List all events
- `npm run list-priority` - List priority events

### VS Code Tasks (Windsurf Compatible)

- **AI Events: Report** - Complete workflow with browser opening
- **AI Events: Fetch Only** - Data collection only
- **AI Events: List Priority** - Show "go" priority events

## CLI Commands

```bash
# Fetch events from all configured sources
ai-events fetch

# Generate HTML report and calendar file
ai-events report

# List events (optional priority filter)
ai-events list [--priority go|maybe]

# Open event URLs in browser
ai-events open --id <event-id> --action register|speak
```

## Deployment (Vercel)

The project is deployed to Vercel at <https://ai-events-delta.vercel.app/>

### Important: Deployment Process

**Vercel serves `index.html` from the root directory, NOT `dist/report.html`**

After generating a new report, you must copy it to deploy:

```bash
# Generate the report
ai-events fetch && ai-events report

# Copy to root for Vercel deployment
cp dist/report.html index.html

# Commit and push to deploy
git add index.html
git commit -m "Update event report"
git push origin main
```

Vercel will automatically deploy within ~1 minute of pushing to GitHub.

### Deployment Configuration

- **vercel.json**: Configured to serve static files from root directory
- **index.html**: The file Vercel actually serves (must be kept in sync with dist/report.html)
- **dist/report.html**: Generated by `ai-events report` command using the template

## Event Coverage

### Comprehensive Global AI Conference Tracking

The system currently tracks **70+ events** from major AI conferences, summits, and specialized gatherings through December 2026:

- **16 Flagship Events**: Premier global conferences including Ai4 Vegas, Data+AI Summit, SuperAI Singapore, DeepFest Riyadh, Dreamforce, NVIDIA GTC, AWS re:Invent, Microsoft Ignite, Google I/O, Apple WWDC, OpenAI DevDay, Meta Connect, KubeCon, and more
- **15 Major Events**: Significant regional and specialized conferences including AI Summit NYC, AI Summit London, World Summit AI Amsterdam, AI Expo Africa, ODSC West, Ray Summit, and others  
- **40+ Other Events**: Focused industry-specific, regional, and emerging conferences across all sectors and geographies

### Major Event Sources Include

**Global AI Flagship Events**:

- Ai4 2025 (Las Vegas) - North America's largest AI event, 8,000+ attendees
- SuperAI Singapore 2026 - Asia's largest AI conference, 7,000+ attendees
- DeepFest 2026 (Riyadh) - Middle East's premier AI event, co-located with LEAP
- Data + AI Summit 2025 (San Francisco) - Databricks flagship conference

**Enterprise & Platform Events**: Dreamforce, AWS re:Invent, Microsoft Ignite, Google I/O, Apple WWDC

**AI Developer Conferences**: OpenAI DevDay, Meta Connect, Code with Claude, NVIDIA GTC series

**Infrastructure & Cloud**: KubeCon + CloudNativeCon, Ray Summit, AI Compute NYC

**Academic & Research**: NeurIPS, World AI Summit series, dotAI Paris

**Regional Enterprise AI**: AI Summit NYC, AI Summit London, AI Expo Africa (Johannesburg), World Summit AI Amsterdam

**Specialized Conferences**: Austin AI events, South Florida summits, Singapore tech conferences, Dubai AI Week

**Global Coverage**: Events across North America, Europe, Asia-Pacific, Middle East, and Africa with comprehensive city and venue information

## Event Classification System

Events are automatically categorized into three tiers based on scale, significance, and industry impact:

### Tier Definitions

- **Flagship**: Premier global conferences with 2000+ attendees, major industry announcements
- **Major**: Significant regional or specialized conferences with 1000+ attendees
- **Other**: Focused, regional, or emerging conferences under 1000 attendees

## Weekly Automation

### Install macOS Automation
```bash
# Install weekly automation (runs Mondays 9:00 AM ET)
cd /Users/arilehavi/Desktop/ai-events
./scripts/install-launchd.sh
```

**Features**:

- Runs every Monday at 9:00 AM ET
- Automatically opens report in browser
- Logs to `~/Library/Logs/ai-events/`

### Uninstall Automation
```bash
./scripts/uninstall-launchd.sh
```

### Manual Triggers
```bash
# Generate fresh report anytime
ai-events fetch && ai-events report && open dist/report.html

# Or use Windsurf shortcuts:
# Cmd+Shift+R - Generate report
# Cmd+Shift+F - Fetch data only
```

### NPM Scripts (Windsurf Run Panel)

- `npm run report` - Full report generation
- `npm run fetch` - Data fetching only  
- `npm run list` - List priority events

## Configuration

### Event Horizon
- **Fixed Horizon**: Through December 2026 for comprehensive AI event planning
- **Configurable**: Edit horizon dates in `src/ai_events/cli.py`

### Adding New Event Sources

#### Step-by-Step Instructions

1. **Add source configuration** to `src/ai_events/fetch/rules.yml`:

   ```yaml
   - name: event_name
     parser: event_name
     url: "https://event-website.com"
     priority: "major"  # or "flagship" or "focused"
     region: "US"  # or "International"
   ```

2. **Create parser file** in `src/ai_events/fetch/parsers/event_name.py`:

   ```python
   from datetime import datetime
   from typing import List
   from ..base import fetch_html
   from ...models import Event, SizeProfile
   from ...utils import stable_id

   async def parse(url: str) -> List[Event]:
       events = []
       
       event = Event(
           id="",  # Will be set by stable_id
           name="Event Name",
           start_date="2026-MM-DD",  # ISO format, MUST be future date
           end_date="2026-MM-DD",
           city="City",
           state_province="State",  # Optional for US events
           country="Country",
           region="US" or "International",
           format="live",  # or "virtual" or "hybrid"
           site_url="https://event-website.com",
           tracks_themes=["AI Theme 1", "AI Theme 2"],
           audience_tag="Business Leaders",  # REQUIRED: Choose from below
           size_profile=SizeProfile(
               tier="major",  # "flagship", "major", or "focused"
               attendees_estimate=1000,
               evidence="Source or reasoning for size estimate"
           )
       )
       event.id = stable_id(event.site_url, event.start_date)
       events.append(event)
       
       return events
   ```

3. **Update CLI imports** in `src/ai_events/cli.py`:
   - Add to imports: `from ai_events.fetch.parsers import (..., event_name)`
   - Add to fetch_all() list: `(event_name, "https://event-website.com"),`

#### Required Fields Reference

- **Date Issues**: Always use future dates in ISO format "YYYY-MM-DD"
- **Field Names**: Use exact field names from Event model (e.g., `city` not `location`)
- **Region Values**: Must be exactly "US" or "International"
- **Format Values**: Must be exactly "live", "virtual", or "hybrid"
- **Tier Values**: Must be exactly "flagship", "major", or "focused"
- **Audience Tag Values**: Must be exactly one of:
  - "Business Leaders" - C-suite, executives, strategic decision makers
  - "Tech Leaders" - CTOs, engineering managers, technical decision makers
  - "Mixed Audience" - Events targeting both business and technical audiences
  - "Practitioners" - Developers, data scientists, hands-on technical professionals
- **ID Generation**: Always use `stable_id(url, start_date)` with string parameters

#### Testing Your Addition

```bash
# Test the fetch and report generation
ai-events fetch && ai-events report

# Check if your event appears
grep "Event Name" dist/report.html
```

### Scoring Weights
Adjust scoring in `src/ai_events/config.py`:
- `SCORE_FLAGSHIP` - Flagship tier events
- `SCORE_LLM_TOPIC` - AI/ML topic bonus
- `SCORE_EMERGING_FLAGSHIP` - New flagship events
- `PRIORITY_THRESHOLD` - Go/maybe cutoff

## Output Files

### HTML Report (`dist/report.html`)
- **Statistics Dashboard**: Event counts showing significant events (Flagship + Major) with breakdown
- **Advanced Filtering**: Multi-select city and tag filters with dynamic tag updates
- **Regional Sections**: US and International events with flagship, major, and other categories
- **Perfect Card Alignment**: Consistent event card heights with proper title wrapping
- **Location Information**: Complete city, state/country details for all events
- **Clean Design**: Professional styling with gradient backgrounds and responsive layout
- **Interactive Elements**: Clickable links, registration buttons, and filter controls

### Calendar File (`dist/AI_Events_Weekly_Update.ics`)
- Weekly reminder for Monday 9:00 AM ET
- Imports into macOS Calendar, Outlook, Google Calendar
- Prompts for review and registration decisions

## Data Storage

- **Database**: SQLite at `~/.ai-events/events.sqlite`
- **Tables**: Events (JSON payload) and metadata
- **Change Detection**: Hash-based tracking for "new" events
- **Persistence**: Events remain across runs for trend analysis

## Error Handling

- **Network Failures**: Graceful degradation, partial results
- **Parsing Errors**: Individual source failures don't crash system
- **Logging**: Comprehensive error tracking with timestamps
- **Recovery**: Automatic retry logic for transient failures

## Development

### Adding New Parsers
```python
# src/ai_events/fetch/parsers/myconf.py
from ..base import fetch_html
from ...models import Event, SizeProfile
from ...utils import stable_id

async def parse(url: str) -> list[Event]:
    doc = await fetch_html(url)
    # Extract event data from HTML
    return [Event(...)]
```

### Testing
```bash
# Test individual commands
ai-events fetch
ai-events list --priority go
ai-events report

# Test automation (dry run)
launchctl start com.ai.events.weekly

# Verify specific event was added
python -c "from ai_events.db import get_all_events; events = get_all_events(); found = [e for e in events if 'Your Event Name' in e.name]; print(f'Found {len(found)} matching events')"
```

## Troubleshooting

### Virtual Environment Issues
```bash
# Recreate environment
rm -rf .venv
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Permission Errors (launchd)
```bash
# Fix permissions
chmod +x scripts/*.sh
sudo chown $(whoami) ~/Library/LaunchAgents/
```

### Network/Parsing Failures

- Check logs: `~/Library/Logs/ai-events/`
- Verify internet connectivity
- Test individual parsers: `ai-events fetch`

### Windsurf Command Issues

- Ensure `.windsurf/commands.json` exists
- Restart Windsurf after configuration changes
- Check Command Palette for "AI Events" commands

## Recent Updates

### UI/UX Improvements

- Removed "Newly Announced Events" section for better reliability
- Eliminated keynote speakers display to focus on event essentials
- Added scroll indicators to "Other" events tiles for better discoverability
- Implemented consistent section alignment across all event cards
- Enhanced statistics cards with modern gradient design and equal sizing

### Event Coverage Expansion

- Extended horizon from 7 to 12 months for better planning
- Massive expansion from 44 to 63 total events tracked
- Added major flagship conferences: Dreamforce, NVIDIA GTC, AWS re:Invent, Microsoft Ignite, Google I/O, Apple WWDC, OpenAI DevDay, Meta Connect, KubeCon, and more
- Added comprehensive location details (city, state/country) to all events
- Enhanced international coverage across Europe, Asia-Pacific, and other regions

### Data Quality Improvements

- Adjusted event tier assignments for more realistic distributions
- Fixed flagship event styling (removed pink "emerging" backgrounds)
- Removed priority badges from event tiles for cleaner appearance
- Improved event categorization accuracy
- Fixed date filtering issues to properly display all 2025+ events

## Known Issues & Future Fixes

### Recently Resolved
- ✅ **FinTech Capitalization**: Fixed to consistent "FinTech AI" format across all parsers
- ✅ **Standalone AI Tags**: Replaced with descriptive compound tags like "Applied AI"
- ✅ **Infrastructure Tags**: Fixed to "AI Infrastructure" for consistency
- ✅ **Minor Events UI**: Fixed faded font colors and improved readability
- ✅ **Mobile Responsive Filters**: Fixed filter alignment on mobile devices

### Future Enhancements

See `AGENT_TODO.md` for detailed implementation tasks:
- Additional conference sources and automated discovery
- Email/Slack notifications for new events
- Trend analysis and attendance predictions
- Mobile-responsive design improvements
- Export options (PDF, CSV, JSON)

## Dependencies

- **httpx**: Async HTTP client for web scraping
- **selectolax**: Fast HTML parsing
- **jinja2**: Template engine for reports
- **pydantic**: Data validation and serialization
- **python-dateutil**: Date/time handling

## License

Private project for AI events tracking and analysis.
