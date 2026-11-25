#!/usr/bin/env python3
"""Fortune in a Pot entry.

Writes one fortune for a houseplant to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

from pathlib import Path

ENTRY = (
    "You will lean into this sill's sun, pretend it was your idea, "
    "and your keeper will turn your pot and call it love."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
