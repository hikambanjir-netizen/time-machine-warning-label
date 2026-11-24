"""Funniest Time Machine Warning Label — make.fun bounty
u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.

Writes one warning label (120 characters at most) to /output/entry.txt.

The label plays the judge's brief straight: a genuine safety notice whose
punchline is the hazard itself — a time machine has no undo, so every
mistake you make in the past becomes the history everyone has to live with.
Pure standard library; no network, no files read, no randomness.
"""

import os

LABEL = (
    "WARNING: This machine has no undo button. "
    "Your mistakes are now historically accurate."
)

MAX_CHARS = 120


def validate(label: str) -> str:
    """Enforce the competition gate: 1-120 chars, one line, not blank."""
    text = label.strip()
    if not text:
        raise ValueError("label is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"label is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> None:
    label = validate(LABEL)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(label)
    print(label)


if __name__ == "__main__":
    main()
