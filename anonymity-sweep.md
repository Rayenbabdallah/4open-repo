# Anonymity sweep note

The packaging audit rejects known host paths and the local user-name marker before writing replication archives. The final sweep checks the manuscript, reviewer-facing notes, and archive manifests for known author-name indicators, Windows home-directory paths, and repository remotes.

Raw third-party captures may contain upstream contact strings or email-like identifiers from public packages. Those are not treated as author identifiers, and their presence means the sweep is a best-effort double-anonymous check rather than a guarantee that no email-like strings occur anywhere in raw evidence.

The package intentionally omits `.git`, build caches, editor metadata, and Python bytecode, since those can expose local paths or timestamps unrelated to replication.

Compiled binaries are never shipped. A compiled program can embed the absolute build path (the home directory and package cache) in a way a text scan cannot see, so the analyzers travel as source only; reviewers rebuild them with `cargo build --release` per the reproduction guide, and each result file pins the analyzer source hashes. The packager fails closed if any compiled binary is ever added to the payload.
