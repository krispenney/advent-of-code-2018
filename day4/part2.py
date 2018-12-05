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
        num_guards = 0
        for line in f:
            entry = make_entry(line)
            entries.append(entry)

            if entry["guard"] != None:
                guard_id = parse_guard_id(entry["guard"])
                if num_guards < guard_id:
                    num_guards = guard_id

        entries = sorted(entries, key=lambda e: e["date"])

        sleep_time = np.zeros((num_guards+1, 60))
        for entry in entries:
            if entry["guard"] != None:
                current_id = parse_guard_id(entry["guard"])

            if entry["asleep"]:
                last_entry = entry

            if entry["awake"]:
                sleep_time[current_id,last_entry["minute"]:entry["minute"]] += 1

        guard_id, time = np.unravel_index(np.argmax(sleep_time),sleep_time.shape)
        print(sleep_time)
        print(guard_id, time)
        print("KEY", guard_id * time)
