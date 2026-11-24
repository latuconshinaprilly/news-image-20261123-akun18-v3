#!/usr/bin/env python3
"""Deliver THE UNIVERSAL LEDGER front page (akun18, NI23 G3).

The picture next to this file is a complete newspaper front page for
Monday 23 November 2026: forty stories, seven regions, one dotted
world map, and Tata Steel's Rs 28,000 crore pipe sale in the lead
slot. This script's only job is to hand that picture to the grader
untouched. It pins the picture down with a byte count and a SHA-256
digest, copies it into MAKEFUN_OUTPUT_DIR (or /output), and reads
the copy back to prove nothing changed on the way.

Standard library only: hashlib, os, sys. No image processing.
"""

import hashlib
import os
import sys

WANT_BYTES = 273287
WANT_SHA256 = "667d940bb52c9e866799c01b4b1f9707ffbe7cb3d1dace12144f6c246f036dd3"
MAGIC = b"\x89PNG\r\n\x1a\n"
LIMIT = 1048576


def read_source():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as fh:
        return fh.read()


def insist_valid(blob):
    problems = []
    if len(blob) == 0:
        problems.append("file is empty")
    if blob[:8] != MAGIC:
        problems.append("PNG magic header missing")
    if len(blob) > LIMIT:
        problems.append("file over the 1 MiB limit")
    if len(blob) != WANT_BYTES:
        problems.append("size %d != pinned %d" % (len(blob), WANT_BYTES))
    if hashlib.sha256(blob).hexdigest() != WANT_SHA256:
        problems.append("sha256 differs from the pinned digest")
    if problems:
        raise SystemExit("entry.png rejected: " + "; ".join(problems))


def confirm_copy(out_path, blob):
    """Second, independent check: the file on disk must equal the source."""
    with open(out_path, "rb") as fh:
        landed = fh.read()
    if landed != blob:
        raise SystemExit("copy verification failed: bytes differ after write")
    if hashlib.sha256(landed).hexdigest() != WANT_SHA256:
        raise SystemExit("copy verification failed: digest differs after write")


def run():
    blob = read_source()
    insist_valid(blob)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(blob)
    confirm_copy(out_path, blob)
    sys.stderr.write(
        "copied entry.png (%d bytes, sha256 %s)\n"
        % (len(blob), WANT_SHA256)
    )


if __name__ == "__main__":
    run()
