#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single one-line review of the entrant's own Monday
(1-200 characters, UTF-8) to /output/entry.txt.

The review: a deadpan one-star review. Monday is written up like a
bad coworker -- it crashed before the entrant had even logged in,
then booked a 9 a.m. meeting to discuss the crash. The joke lands on the
final words, names concrete Monday details (logging in, a meeting),
and reads as a review of a real Monday.
"""

import os
import sys

REVIEW = (
    "One star. Monday crashed before I'd even logged in, "
    "then booked a 9 a.m. meeting to discuss the crash."
)

MAX_CHARS = 200


def main() -> None:
    # Guards: the gate rejects anything over 200 characters,
    # whitespace-only, or more than one line.
    if not REVIEW.strip():
        print("error: review is empty", file=sys.stderr)
        raise SystemExit(1)
    if len(REVIEW) > MAX_CHARS:
        print(
            f"error: review is {len(REVIEW)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in REVIEW.strip():
        print("error: review must be a single line", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
