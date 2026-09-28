#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

HERE = Path(__file__).resolve().parent
OUT = HERE / "fse2027-replication-core.zip"
PARTS = sorted(HERE.glob("fse2027-replication-core.zip.part*"))
EXPECTED = (HERE / "fse2027-replication-core.zip.sha256").read_text(encoding="ascii").split()[0]
if not PARTS:
    raise SystemExit("no fse2027-replication-core.zip.part* files found")
with OUT.open("wb") as out:
    for part in PARTS:
        out.write(part.read_bytes())
actual = hashlib.sha256(OUT.read_bytes()).hexdigest()
if actual != EXPECTED:
    OUT.unlink(missing_ok=True)
    raise SystemExit(f"checksum mismatch: expected {EXPECTED}, got {actual}")
print(f"wrote {OUT.name} ({OUT.stat().st_size} bytes), sha256 {actual}")
