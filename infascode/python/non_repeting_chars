#!/usr/bin/env python3

import argparse
import sys
import re

parser = argparse.ArgumentParser(
    prog="cleanup",
    description="Replace repeating special characters with a single character in a file and print it to stdout.",
    epilog="This is the epilog",
)

parser.add_argument("file", help="The file to read from.")
args = parser.parse_args()

try:
    with open(args.file, encoding="utf-8") as f:
        file_lines = f.readlines()
except:
    print(f"{parser.prog}: error: {args.file} could not be found.", file=sys.stderr)
    sys.exit(3)

repeating_regex = r"[:]{2,}|[,]{2,}|[.]{2,}|[;]{2,}|[ ]{2,}"
repeating = re.compile(repeating_regex)


def repl(match):
    complete_match = match.group(0)
    used_char = complete_match[0]
    return used_char


for line in enumerate(file_lines):
    file_lines[line[0]] = repeating.sub(repl, line[1])

output = "".join(file_lines)
print(output)
sys.exit(0)
