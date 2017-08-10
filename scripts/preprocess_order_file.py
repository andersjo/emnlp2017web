import argparse
from pathlib import Path

import pandas as pd
import re

parser = argparse.ArgumentParser(description="Converts from custom 'order' format to YAML")
parser.add_argument("order_file", help="A conference order file", type=Path)
# parser.add_argument("--output-dir",
#                     help="Place output files here (default is tests/integration-tests/generated)",
#                     type=Path,
#                     default=CACHE_DIR)
# parser.add_argument("--input-dir",
#                     help="Read input files here (default is tests/integration_tests/definitions)",
#                     type=Path,
#                     default=DEFINITIONS_DIR)
# parser.add_argument('--wiri-url', help="URL for wiri (default: use deployed orchard version)",
#                     default=WIRI_URL)
# parser.add_argument('--verbose', '-v', help="Turns on more verbose logging", action='store_true')
# parser.add_argument('--no-generate-user-signal', '--no-wiri',
#                     help="When defined don't call to wiri",
#                     dest='generate_user_signal',
#                     action='store_false')
args = parser.parse_args()

days = []
session = []

for line in args.order_file.open():
    line = line.strip()
    if not line:
        continue

    if line.startswith("*"):
        print("New day", line)
        pass
        # New day
    elif line.startswith("+"):
        print("New single session", line)
        pass
        # Single session
    elif line.startswith("="):
        print("New parallel session", line)
        pass
        # Parallel session

    # print(line)
    else:
        m = re.match("(\d+)([^\s]+)? ((\d{2}:\d{2})--(\d{2}:\d{2}))?\s*#?\s*(.+)", line)

        paper_id, paper_subtype, time_slot, start_time, end_time, title = m.groups()

        # ('100', None, '16:45--17:15', '16:45', '17:15', 'Unsupervised Morphology Induction Using Word Embeddings')

        assert m, "didn't match {}".format(line)
        print()
        # if not m:
        #     print("No match", line)
        # else:
        #     print(m.groups())

        # parts = re.split("\s+", line, 3)
        # paper_id, time_slot, paper_type, title = parts

        # print("Normal", parts)

        # "14:50 - -15:15"

        # print("Normal line", line)
