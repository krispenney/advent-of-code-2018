import re
from dateutil.parser import parse
from collections import defaultdict

import numpy as np

rexp = re.compile(r"\[(.*)\] (Guard #[0-9]+)?(falls asleep)?(wakes up)?")

def make_entry(line):
    match = rexp.match(line)
    date = parse(match.group(1))

    entry = { "date": date }
    entry["minute"] = date.minute
    entry["guard"] = match.group(2)
    entry["asleep"] = match.group(3) != None
    entry["awake"] = match.group(4) != None

    return entry

def parse_guard_id(guard):
    guard_id = int(guard.split(' ')[1][1:]) # Guard #[0-9]+
    return guard_id

if __name__ == '__main__':
    entries = []
    with open('input.txt', 'r') as f:
        for line in f:
            entry = make_entry(line)
            entries.append(entry)

        entries = sorted(entries, key=lambda e: e["date"])

        max_guard = 0
        max_sleep_time = 0

        current_id = -1
        track_time = defaultdict(lambda: np.zeros(60))
        last_entry = None
        for entry in entries:
            if entry["guard"] != None:
                current_id = parse_guard_id(entry["guard"])

            if entry["asleep"]:
                last_entry = entry

            if entry["awake"]:
                track_time[current_id][last_entry["minute"]:entry["minute"]] += 1
                total_time = track_time[current_id].sum()

                if max_sleep_time < total_time:
                    max_sleep_time = total_time
                    max_guard = current_id
        print("KEY:", max_guard * track_time[max_guard].argmax())
