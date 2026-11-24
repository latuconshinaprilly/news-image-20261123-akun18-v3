# THE DAY'S HERALD - entry carrier.
# The artwork already exists as entry.png beside this file.
# All this does is carry that page into the output folder.
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("carried entry.png to", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
