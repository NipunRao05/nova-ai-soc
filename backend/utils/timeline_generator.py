import re

TIMESTAMP_PATTERN = r'\b\d{2}:\d{2}:\d{2}\b'

def generate_timeline(log_content):

    timeline = []

    lines = log_content.split("\n")

    for line in lines:

        timestamp_match = re.search(TIMESTAMP_PATTERN, line)

        if timestamp_match:
            timeline.append({
                "time": timestamp_match.group(),
                "event": line.strip()
            })

    return timeline