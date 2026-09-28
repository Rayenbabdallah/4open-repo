# Full replication archive

The 4open.science mirror is self-contained. The complete replication core is stored as four parts so each file remains below GitHub's per-file size limit:

- `fse2027-replication-core.zip.part001`
- `fse2027-replication-core.zip.part002`
- `fse2027-replication-core.zip.part003`
- `fse2027-replication-core.zip.part004`

To reconstruct the full archive, run:

```sh
python reassemble-core.py
```

The script concatenates the parts into `fse2027-replication-core.zip` and checks the result against `fse2027-replication-core.zip.sha256`. `SHA256SUMS.txt` also records the checksum of each part and of the reconstructed archive.

For quick inspection, reviewers can use `fse2027-review-supplement.zip` without reconstructing the full archive.
