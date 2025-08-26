from datetime import datetime, timedelta

# Rolling window for event relevance (12 months from now)
HORIZON_MONTHS = 12

# Default configuration values
DEFAULT_TIMEOUT = 20  # HTTP request timeout in seconds
DEFAULT_USER_AGENT = "ai-events/0.1"

# Priority scoring thresholds
PRIORITY_THRESHOLD = 50  # Score >= 50 = "go", else "maybe"

# Scoring weights
SCORE_FLAGSHIP = 40
SCORE_MAJOR = 25
SCORE_FOCUSED = 10
SCORE_LLM_TOPIC = 10
SCORE_EMERGING_FLAGSHIP = 20
SCORE_US_REGION = 5
