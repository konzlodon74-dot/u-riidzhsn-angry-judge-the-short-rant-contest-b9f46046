#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry writer.

Writes one short funny rant about a broken printer to /output/entry.txt.
Standard library only, no network.
"""

import os

RANT = (
    "My printer has one job. ONE. It just sits there blinking like it's "
    "thinking, then announces 'paper jam' when there is NO paper in it. "
    "I wanted one page. ONE page. Now I'm on my knees, flashlight in my "
    "teeth, performing surgery on a machine that drinks more money in ink "
    "than I spend on rent — and it still won't print."
)


def main():
    text = RANT.strip()
    if not 1 <= len(text) <= 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
