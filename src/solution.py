from typing import List, Dict

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


def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:

    # Convert events to minute intervals
    event_intervals = []
    for e in events:
        start = to_minutes(e["start"])
        end = to_minutes(e["end"])

        # Ignore events completely outside working hours
        if end <= WORK_START or start >= WORK_END:
            continue

        event_intervals.append((start, end))

    slots = []

    current = WORK_START
    last_start = WORK_END - meeting_duration

    while current <= last_start:
        meeting_end = current + meeting_duration

        # Skip lunch break starts
        if LUNCH_START <= current < LUNCH_END:
            current += SLOT_INCREMENT
            continue

        # Check overlap with events
        conflict = False
        for es, ee in event_intervals:
            if overlaps(current, meeting_end, es, ee):
                conflict = True
                break

        if not conflict:
            slots.append(to_time_str(current))

        current += SLOT_INCREMENT

    return slots
