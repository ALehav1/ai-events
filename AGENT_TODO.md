# AI Events Agent Tasks

## Role
Senior Python developer specializing in web scraping, data analysis, and automation systems.

## Goal
Complete the ai-events tool to production-ready status with full Windsurf IDE integration.

## Required Changes

### 1. Core Implementation
- **Models & Database**: Implement complete Pydantic models with Event, SizeProfile classes and SQLite operations
- **Utilities**: Create stable ID generation, text cleaning, and date handling functions
- **Configuration**: Set up horizon months and other constants

### 2. HTML Report Renderer
- **Template Engine**: Implement Jinja2 renderer using `src/ai_events/templates/report.html.j2`
- **Report Sections**: US events, International events, Emerging flagships, New items
- **Styling**: Professional layout with event cards, clickable links, registration buttons
- **Calendar Export**: Generate `.ics` files for calendar integration

### 3. Event Fetchers Implementation
Implement parsers for these sources with official page preference:

#### Primary Sources (Complete Implementation)
- **HumanX** (https://www.humanx.co/) - Enterprise AI flagship event
  - Parse: Apr 6-9, 2026, San Francisco, Moscone Center
  - Speakers: Bret Taylor, Andrew Ng, Ali Ghodsi, etc.
  - Classification: Flagship tier, emerging flagship, priority "go"

- **The AI Conference SF** (https://aiconference.com/) - Technical conference
  - Parse: Sep 17-18, 2025, San Francisco, Pier 48
  - Speakers: Peter Norvig, Jason Wei, Joe Spisak
  - Classification: Major tier, priority "go"

- **NeurIPS** (https://neurips.cc/) - Academic research conference
  - Parse: Dec 2-7, 2025, San Diego + Mexico City satellite
  - Classification: Flagship tier, hybrid format, priority "maybe"

#### Additional Sources (Scaffold with TODOs)
Create parser stubs for future implementation:
- **ODSC West** - Data science conference
- **Dreamforce** - Salesforce AI track
- **AWS re:Invent** - AI/ML sessions
- **Microsoft Ignite** - AI platform updates
- **KubeCon North America** - AI infrastructure

### 4. CLI Commands
Complete implementation of all CLI commands:

```bash
# Crawl sources and update SQLite database
ai-events fetch

# Generate HTML report and calendar file
ai-events report

# List events with optional priority filter
ai-events list --priority go

# Open event URLs in browser
ai-events open --id <12-char-id> --action register|speak
```

**Output Requirements**:
- `dist/report.html` - Professional HTML dashboard
- `dist/AI_Events_Weekly_Update.ics` - Calendar import file
- Automatic browser opening of report
- Progress logging and error handling

### 5. macOS Automation Scripts
Create complete launchd integration:

- **`launchd/com.ai.events.weekly.plist`** - Weekly Monday 9:00 AM ET execution
- **`scripts/install-launchd.sh`** - Setup automation with proper paths
- **`scripts/uninstall-launchd.sh`** - Clean removal of automation
- **Logging**: Configure stdout/stderr to `~/Library/Logs/ai-events/`

### 6. Content Quality Requirements
- **No Long Prose in Tables**: Keep event descriptions concise
- **Clickable Links**: All URLs must be properly linked
- **Professional Layout**: Clean, scannable design
- **Mobile Responsive**: Works on different screen sizes
- **Error Resilience**: Graceful handling of network/parsing failures

### 7. Data Management
- **7-Month Horizon**: Rolling window for event relevance
- **Change Detection**: Track "New since last week" events using hash comparison
- **Priority Algorithm**: 
  - Flagship tier: +40 points
  - LLM/AI topics: +10 points  
  - Emerging flagship: +20 points
  - US region: +5 points
  - Threshold: 70+ = "go", else "maybe"

## Acceptance Criteria

### Functional Requirements
1. **Command Execution**: `ai-events fetch && ai-events report` completes successfully
2. **Output Generation**: Produces `dist/report.html` and `dist/AI_Events_Weekly_Update.ics`
3. **Browser Integration**: Report opens automatically in default browser
4. **Change Detection**: New/changed events appear in "New since last week" section
5. **Data Persistence**: Events stored in SQLite with proper upsert logic

### Quality Requirements
1. **Error Handling**: Network failures don't crash the system
2. **Logging**: Comprehensive logs for debugging issues
3. **Performance**: Fetching completes within reasonable time (< 2 minutes)
4. **Data Accuracy**: Event details correctly parsed and displayed
5. **Professional Output**: Report looks polished and business-ready

### Integration Requirements
1. **Windsurf Compatibility**: Works seamlessly in Windsurf IDE
2. **macOS Automation**: Weekly launchd job executes reliably
3. **Calendar Integration**: ICS files import correctly
4. **CLI Usability**: All commands work as documented

## Implementation Notes
- Use async/await for concurrent fetching
- Implement proper User-Agent headers for web scraping
- Handle rate limiting and respectful crawling
- Use selectolax for fast HTML parsing
- Implement proper error logging with timestamps
- Ensure all file paths work on macOS
- Test with actual network requests to verify parsing

## Testing Checklist
- [ ] All CLI commands execute without errors
- [ ] HTML report renders correctly with sample data
- [ ] Event fetching works for all three primary sources
- [ ] Calendar file imports into macOS Calendar
- [ ] Weekly automation installs and runs correctly
- [ ] Error conditions handled gracefully
- [ ] Report opens automatically in browser
- [ ] New event detection works across runs

## Next Steps After Completion
1. Add remaining conference sources (ODSC, Dreamforce, etc.)
2. Implement email/Slack notifications for high-priority events
3. Add trend analysis and event prediction features
4. Create mobile-responsive improvements
5. Add export options (PDF, CSV, etc.)

---

**Usage**: Open this file in Windsurf and use "Run with Agent" or copy the requirements into a new agent conversation for implementation.
