# Checks for THE DAY'S HERALD entry: size, dimensions, fresh words.
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1048576


def fail(msg):
    print("FAIL:", msg)
    return 1


def main():
    path = os.path.join(HERE, "entry.png")
    if not os.path.isfile(path):
        return fail("entry.png missing")
    data = open(path, "rb").read()
    if len(data) > MAX_BYTES:
        return fail("entry.png too large: %d bytes" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return fail("entry.png is not a PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        return fail("dimensions %dx%d, want 1024x1024" % (width, height))

    fresh_path = None
    for cand in (os.path.join(HERE, "ni23-fresh.txt"),
                 "/home/hatch/workspace/makefun/ni23-fresh.txt"):
        if os.path.isfile(cand):
            fresh_path = cand
            break
    if fresh_path is None:
        return fail("ni23-fresh.txt not found")
    words = [ln.strip().lower() for ln in open(fresh_path) if ln.strip()]

    hay = ""
    for name in ("compose.py", "test_entry.py"):
        p = os.path.join(HERE, name)
        if os.path.isfile(p):
            hay += open(p, encoding="utf-8").read().lower() + "\n"
    missing = [w for w in words if w not in hay]
    if missing:
        return fail("fresh words missing: %s" % ", ".join(missing))

    print("PASS: %d bytes, 1024x1024, %d fresh words present"
          % (len(data), len(words)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
