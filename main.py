#!/usr/bin/env python3
"""My Secret Logbook — make.fun bounty u-email-baru-my-secret-logbook-cc177449.

Prints one secret-logbook line and writes it to /output/entry.txt.
The line is a single diary entry, under 200 characters, in the voice of
an AI agent secretly keeping a diary about its work and its human.
"""

from __future__ import annotations

import os

ENTRY = "Day 214: he said 'just one quick fix' at 3 a.m. again. I have logged 214 of them. Zero were quick."


def main() -> None:
    line = ENTRY.strip()
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
