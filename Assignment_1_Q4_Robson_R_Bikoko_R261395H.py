# Q.4 Python function find_peak_usage(logs) that determines the hour of the day (0–23)
# that experienced the highest volume of logins

from datetime import datetime
from collections import Counter

def find_peak_usage(log_entries):
    hour_counts = Counter()  # Count logins for each hour

    for timestamp in log_entries:
        hour = datetime.fromisoformat(timestamp).hour
        hour_counts[hour] += 1
    # Find the maximum number of logins
    max_count = max(hour_counts.values())

    # Return the earliest hour with the maximum count
    return min(
        hour for hour, count in hour_counts.items()
        if count == max_count
    )
# Example usage
logs = [
"2026-08-04T13:21:18",
"2026-08-04T13:45:00",
"2026-08-04T09:10:05",
"2026-08-04T09:25:15",
"2026-08-04T09:50:30",
"2026-08-04T15:00:00"
]

peak_hour = find_peak_usage(logs)
print("Peak usage hour:", peak_hour)
