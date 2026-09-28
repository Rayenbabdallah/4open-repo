# Reviewer evidence guide

This guide uses descriptive names for the paper's evidence so reviewers do not need to decode historical experiment labels.

| Paper claim | Evidence in the full replication archive | Main command |
|---|---|---|
| Build directives from one package can affect another compilation unit | Cross-unit propagation witness and propagation-map results | `python analysis/make_revision_tables.py` |
| Native-library shadowing is executable and changes the linked binary | Native-shadow attack witness and runtime marker result | `python analysis/make_revision_tables.py` |
| A published victim crate can be shadowed without modifying the victim | Published-victim witness result | `python analysis/make_revision_tables.py` |
| A published application source can exercise the pattern end to end | Published-application witness result | `python analysis/make_revision_tables.py` |
| A real unchanged-source carrier can capture a default-features `curl` victim through `crypt32` | Limited-trust `winapi` to `curl` witness, including the recorded result and the Windows GNU/Cargo-cache rerun prerequisites in `REPRODUCE.md` | `python analysis/make_revision_tables.py`; optional rerun documented in `REPRODUCE.md` |
| Syscall sandboxing alone does not remove the link-line authority problem | Sandbox-comparison and syscall-confinement results | `python analysis/make_revision_tables.py` |
| The provenance-scoped defense blocks cross-unit shadowing | Provenance-scoped model and Cargo-wrapper result | `python analysis/make_revision_tables.py` |
| Real native-linking crates mostly remain compatible under the wrapper | Real-crate compatibility corpus | `python analysis/make_revision_tables.py` |
| The graph-level co-occurrence rate is measured on frozen resolved dependency graphs | Resolved-graph co-occurrence result | `python analysis/make_revision_tables.py` |
| All generated numbers are bound to evidence hashes | Artifact manifest, result hashes, and submission audit | `python analysis/verify_artifact.py`; `python analysis/submission_audit.py --skip-log` |

The archive keeps the exact executable file names used when the evidence was generated, because the validators compare current bytes against recorded SHA-256 digests. The reviewer-facing names above are the semantic labels used by the manuscript and this guide.
