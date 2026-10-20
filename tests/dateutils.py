from datetime import datetime, timedelta, timezone

NOW = datetime.now(timezone.utc)
TOMORROW = NOW + timedelta(days=1)
YESTERDAY = NOW - timedelta(days=1)
