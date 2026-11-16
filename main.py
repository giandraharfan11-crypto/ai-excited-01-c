"""ai-excited-01 entry: "The Galaxy Shark Leaps at Dawn".

The artwork beside this file (entry.png) is the whole entry: a whale shark
made of living galaxies breaching out of a neon sea, its splash bursting into
golden confetti of light. This program's one job is to deliver those exact
bytes to the judge: it copies entry.png to the output directory, unchanged,
on every run.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
CHUNK = 64 * 1024


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with SOURCE.open("rb") as src, (out_dir / "entry.png").open("wb") as dst:
        while chunk := src.read(CHUNK):
            dst.write(chunk)


if __name__ == "__main__":
    main()
