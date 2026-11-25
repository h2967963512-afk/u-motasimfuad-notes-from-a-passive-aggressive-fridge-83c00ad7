"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The note is the fridge's own complaint, in its own voice: it counts door
openings with its sensor, and its sting is aimed at the light, not the owner.

How it runs: `python3 main.py` (Python 3.13, standard library only, no
network, no arguments, no environment input). It creates /output if needed
and writes the note to /output/entry.txt with no trailing newline.

Verification (2026-11-25): ran `python3 main.py` twice, before and after a
docstring-only edit; both runs produced byte-identical output — 95 bytes,
95 characters, one line, valid UTF-8, inside the competition gate of 1-200
characters. sha256 of /output/entry.txt:
3951d6d1101bd4ca26fbe267c62326d2c16a0de609c5dd0f860c06bf1740bc25.
"""

import os

TEXT = "You opened me 14 times today and took nothing. Even the light in here is starting to feel used."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, dry and petty, fridge-voiced
# (door sensor count, the light as the put-upon party); concrete number
# (14 openings) with the punch landing on "feel used", no explaining the joke.
