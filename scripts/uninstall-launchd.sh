#!/bin/zsh
set -euo pipefail

PLIST="$HOME/Library/LaunchAgents/com.ai.events.weekly.plist"

# Unload the job if it exists
launchctl unload "$PLIST" 2>/dev/null || true

# Remove the plist file
rm -f "$PLIST"

echo "🗑️  AI Events weekly job uninstalled successfully"
