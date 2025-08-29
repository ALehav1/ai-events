# AI Events Tracker - Complete Implementation Plan

## Overview
Building a comprehensive AI events tracking system that automatically fetches, analyzes, and reports on AI conferences and events with weekly automation for MacBook Air (M2) + Windsurf IDE.

## Project Structure
```
ai-events/
├── pyproject.toml                    # Python project configuration
├── README.md                         # Project documentation
├── PROJECT_PLAN.md                   # This implementation plan
├── AGENT_TODO.md                     # Future agent tasks
├── package.json                      # NPM scripts for Windsurf integration
├── .vscode/
│   └── tasks.json                    # VS Code/Windsurf tasks
├── .windsurf/
│   └── commands.json                 # Windsurf-specific commands
├── scripts/
│   ├── install-launchd.sh           # macOS automation setup
│   └── uninstall-launchd.sh         # macOS automation removal
├── launchd/
│   └── com.ai.events.weekly.plist   # Weekly automation config
├── src/ai_events/
│   ├── __init__.py                   # Package initialization
│   ├── cli.py                        # Command-line interface (updated for JSON)
│   ├── config.py                     # Configuration settings
│   ├── db.py                         # SQLite database operations
│   ├── models.py                     # Pydantic data models
│   ├── utils.py                      # Utility functions
│   ├── classify.py                   # Event classification logic
│   ├── score.py                      # Event scoring and prioritization
│   ├── report.py                     # HTML report generation
│   ├── ics.py                        # Calendar file generation
│   ├── static_events.json            # Consolidated event data (76 events)
│   ├── fetch/
│   │   ├── __init__.py
│   │   ├── base.py                   # Base fetching functionality
│   │   ├── static_loader.py          # JSON event loader (NEW)
│   │   ├── rules.yml                 # Source configuration
│   │   └── parsers/
│   │       └── __init__.py           # Legacy directory (parsers removed)
│   └── templates/
│       └── report.html.j2            # HTML report template
└── dist/                             # Generated reports (created at runtime)
    ├── report.html
    └── AI_Events_Weekly_Update.ics
```

## Implementation Phases

### Phase 1: Core Infrastructure (High Priority)
1. **Data Models & Database**
   - Event model with all required fields (priority, region, format, etc.)
   - SizeProfile model for event classification
   - SQLite database operations (upsert, retrieve, metadata)
   - Utility functions for ID generation and text cleaning

2. **Configuration & Utilities**
   - Configuration constants (horizon months, etc.)
   - Text processing utilities
   - Date/time handling functions

### Phase 2: Data Fetching System (High Priority)
1. **Base Fetching Infrastructure**
   - HTTP client with proper headers and error handling
   - HTML parsing with selectolax
   - Async fetching capabilities

2. **Event Parsers**
   - HumanX parser (flagship enterprise AI event)
   - AI Conference SF parser (major technical conference)
   - NeurIPS parser (academic research conference with satellites)
   - Generic parser template for future sources

3. **Source Configuration**
   - YAML rules file for source definitions
   - Parser routing and management

### Phase 3: Analysis & Reporting (High Priority)
1. **Event Classification & Scoring**
   - Region classification (US vs International)
   - Priority scoring algorithm
   - Emerging flagship detection

2. **Report Generation**
   - HTML report with Jinja2 templates
   - Event categorization (US, International, Emerging Flagships)
   - New events detection and highlighting
   - Calendar file (.ics) generation

### Phase 4: CLI Interface (High Priority)
1. **Command Structure**
   - `ai-events fetch` - Crawl sources and update database
   - `ai-events report` - Generate HTML report and calendar
   - `ai-events list [--priority go|maybe]` - List events
   - `ai-events open --id <id> --action register|speak` - Open event URLs

2. **Output Management**
   - HTML report in dist/ directory
   - Automatic browser opening
   - Progress logging and error handling

### Phase 5: Windsurf Integration (Medium Priority)
1. **Windsurf Commands**
   - `.windsurf/commands.json` with "AI Events: Generate & Open Report"
   - Keyboard shortcut binding (Cmd+Shift+R)
   - Command palette integration

2. **NPM Integration**
   - `package.json` with report script for Windsurf Run panel
   - Shell command wrapping for venv activation

3. **Environment Setup**
   - Terminal auto-activation configuration
   - Workspace-specific settings

### Phase 6: Automation (Medium Priority)
1. **macOS Automation**
   - launchd plist for weekly execution (Mondays 9:00 AM ET)
   - Installation/uninstallation scripts
   - Logging configuration

2. **VS Code Tasks**
   - Task configuration for manual execution
   - Integration with Windsurf task system

### Phase 7: Testing & Documentation (Medium Priority)
1. **System Testing**
   - End-to-end workflow testing
   - Error handling verification
   - Report generation validation

2. **Documentation Updates**
   - Comprehensive README with setup instructions
   - Usage examples and troubleshooting
   - Architecture documentation

## Key Features

### Event Data Model
- **Comprehensive Metadata**: ID, name, dates, location, venue, region, format
- **URLs**: Site, registration, call for speakers
- **Content**: Speaker samples, tracks/themes
- **Classification**: Priority (go/maybe), emerging flagship status, size profile
- **Tracking**: Source URLs, last seen, change detection

### Intelligent Scoring
- **Tier-based Scoring**: Flagship (40pts), Major, Focused events
- **Topic Relevance**: LLM/AI focus detection (+10pts)
- **Emerging Detection**: New flagship events (+20pts)
- **Regional Preference**: US events slight boost (+5pts)
- **Priority Threshold**: 70+ points = "go", otherwise "maybe"

### Rich Reporting
- **HTML Dashboard**: Clean, professional layout with event cards
- **Categorization**: US events, International events, Emerging flagships
- **Change Detection**: "New since last week" highlighting
- **Interactive Elements**: Clickable links, registration buttons
- **Calendar Export**: ICS file for calendar integration

### Automation Features
- **Weekly Execution**: Automatic Monday morning reports
- **Browser Integration**: Auto-opens generated reports
- **Error Logging**: Comprehensive logging for troubleshooting
- **Incremental Updates**: Only processes changed events

## Dependencies
- **httpx**: Async HTTP client for web scraping
- **selectolax**: Fast HTML parsing
- **jinja2**: Template engine for HTML reports
- **pydantic**: Data validation and serialization
- **python-dateutil**: Date/time parsing and manipulation

## Windsurf-Specific Enhancements
- **Command Palette Integration**: One-click report generation
- **Status Bar Button**: Quick access to report generation
- **NPM Script Integration**: Visible in Windsurf Run panel
- **Terminal Auto-activation**: Automatic venv activation
- **Agent Integration**: AGENT_TODO.md for future enhancements

## Future Extensions
- **Additional Sources**: ODSC West, Dreamforce, AWS re:Invent, MS Ignite, KubeCon
- **Enhanced Parsing**: More sophisticated content extraction
- **Notification System**: Email/Slack integration for new flagship events
- **Analytics**: Trend analysis and event prediction
- **Mobile Support**: Responsive design for mobile viewing

## Success Criteria
1. **Functional CLI**: All commands work correctly
2. **Automated Fetching**: Successfully scrapes target sources
3. **Quality Reports**: Professional HTML output with all event data
4. **Weekly Automation**: Reliable Monday morning execution
5. **Windsurf Integration**: Seamless IDE workflow
6. **Error Resilience**: Graceful handling of network/parsing failures

This plan provides a comprehensive roadmap for building a production-ready AI events tracking system optimized for Windsurf IDE on macOS.
