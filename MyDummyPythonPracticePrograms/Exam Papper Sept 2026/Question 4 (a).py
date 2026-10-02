#Given ISO timestamps, return the hour from 0 to 23 with the most logins.
#If hours tie, return the earliest. Use only built-in modules
"""
    Step by step method
    Step 1. Reject an empty list because no peak hour can be identified.
    Step 2. Convert each ISO timestamp with datetime.fromisoformat() and extract its .hour value.
    Step 3. Count how often each hour occurs by using collections.Counter.
    Step 4. Find the highest frequency.
    Step 5. Collect the hours having that frequency and return min(...), which enforces the earliest-hour tie rule.

"""
from collections import Counter
from datetime import datetime


def find_peak_usage(logs):
    if not logs:
        raise ValueError("The log list cannot be empty.")

    hours = [datetime.fromisoformat(item).hour for item in logs]
    counts = Counter(hours)
    highest_count = max(counts.values())

    tied_hours = [
        hour for hour, count in counts.items()
        if count == highest_count
    ]
    return min(tied_hours)


logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T09:05:00",
    "2026-08-04T13:44:10",
    "2026-08-04T09:50:23",
    "2026-08-04T18:12:45",
]

print("Peak hour:", find_peak_usage(logs))
