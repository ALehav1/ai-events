#!/bin/zsh
set -euo pipefail

PLIST="$HOME/Library/LaunchAgents/com.ai.events.weekly.plist"

# Create necessary directories
mkdir -p ~/Library/LaunchAgents ~/Library/Logs/ai-events

# Copy plist file to LaunchAgents
cp "$(dirname "$0")/../launchd/com.ai.events.weekly.plist" "$PLIST"

# Unload existing job if present
launchctl unload "$PLIST" 2>/dev/null || true

# Load the new job
launchctl load "$PLIST"

# Verify installation
if launchctl list | grep com.ai.events.weekly >/dev/null; then
    echo "✅ AI Events weekly job installed successfully"
    echo "📅 Will run every Monday at 9:00 AM ET"
    echo "📝 Logs: ~/Library/Logs/ai-events/"
else
    echo "❌ Installation failed"
    exit 1
fi
