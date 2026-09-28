# Anonymous review mirror

This repository is the 4open.science anonymous mirror for the FSE 2027 submission. It contains the anonymized paper, reviewer-facing documentation, the quick review supplement, and the complete replication core split into GitHub-safe parts.

## What to inspect first

1. `paper.pdf`: anonymized manuscript.
2. `reviewer-evidence-guide.md`: maps the paper's main claims to evidence and commands.
3. `fse2027-review-supplement.zip`: smaller inspection bundle for quick validation.
4. `fse2027-replication-core.zip.part001` through `part004`: complete replication archive split into parts below GitHub's per-file limit.
5. `SHA256SUMS.txt`: checksums for the PDF, supplement, each part, and the reconstructed core archive.

## Fast validation

Extract `fse2027-review-supplement.zip` and run:

```sh
python analysis/verify_artifact.py
```

## Full replication

Reassemble the complete core archive from the parts:

```sh
python reassemble-core.py
```

The script writes `fse2027-replication-core.zip` and checks it against `fse2027-replication-core.zip.sha256`. Then extract it and run:

```sh
python analysis/verify_artifact.py
python analysis/make_revision_tables.py
python -m unittest discover -s analysis/tests -v
python analysis/submission_audit.py --skip-log
```

`FULL-ARTIFACT.md` gives the same steps with the file list.
