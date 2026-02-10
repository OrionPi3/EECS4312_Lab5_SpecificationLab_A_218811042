## Student Name:
## Student ID: 

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict

<<<<<<< Updated upstream
=======
import sys
import os

WORK_START = 9 * 60      # 09:00
WORK_END = 17 * 60       # 17:00
LUNCH_START = 12 * 60    # 12:00
LUNCH_END = 13 * 60      # 13:00
SLOT_INCREMENT = 15      # minutes


def to_minutes(time_str: str) -> int:
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def to_time_str(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def overlaps(start1, end1, start2, end2) -> bool:
    return start1 < end2 and start2 < end1


>>>>>>> Stashed changes
def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
    # TODO: Implement this function
    raise NotImplementedError("suggest_slots function has not been implemented yet")