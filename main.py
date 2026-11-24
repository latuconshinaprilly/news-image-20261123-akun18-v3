#!/usr/bin/env python3
"""THE UNIVERSAL LEDGER — entry program for news-image-20261123 (akun18).

The artwork is a one-page newspaper front, "THE UNIVERSAL LEDGER",
summing up Monday 23 November 2026 in 40 stories across 7 regions,
led by Tata Steel's Rs 28,000 crore pipe-business sale to APL Apollo.

This program is deliberately boring: it copies the bundled entry.png
to the output directory and refuses to run if the file does not match
the exact byte count and SHA-256 recorded below. Standard library
only (hashlib / os / sys); no imaging code runs here.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 273287
EXPECTED_SHA256 = "667d940bb52c9e866799c01b4b1f9707ffbe7cb3d1dace12144f6c246f036dd3"
PNG_HEADER = b"\x89PNG\r\n\x1a\n"
HARD_CAP = 1048576  # competition ceiling: 1 MiB


def load_entry():
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "entry.png")
    with open(path, "rb") as fh:
        return fh.read()


def check_payload(blob):
    if not blob:
        raise SystemExit("entry.png is empty")
    if blob[:8] != PNG_HEADER:
        raise SystemExit("entry.png lacks the PNG magic header")
    if len(blob) > HARD_CAP:
        raise SystemExit("entry.png exceeds the 1 MiB cap: %d" % len(blob))
    if len(blob) != EXPECTED_BYTES:
        raise SystemExit(
            "entry.png size drifted: %d bytes, expected %d"
            % (len(blob), EXPECTED_BYTES)
        )
    digest = hashlib.sha256(blob).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit("entry.png sha256 mismatch: %s" % digest)
    return digest


def verify_written(target, blob):
    """Re-read the copied file and confirm it is byte-identical."""
    with open(target, "rb") as fh:
        back = fh.read()
    if back != blob:
        raise SystemExit("written copy differs from the bundled entry.png")
    if hashlib.sha256(back).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("written copy fails the sha256 check")


def main():
    blob = load_entry()
    digest = check_payload(blob)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(target, "wb") as fh:
        fh.write(blob)
    verify_written(target, blob)
    sys.stderr.write(
        "THE UNIVERSAL LEDGER entry.png written: %d bytes sha256=%s\n"
        % (len(blob), digest)
    )


if __name__ == "__main__":
    main()
