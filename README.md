# ZnO Nanovoid Process — document set

**Author:** Croft Swonyoung
**License:** CC0 1.0 Universal (public domain dedication) — see `LICENSE`
**Contents:** two application lines in one set — `docs-rotor/` (150 mm rotor/generator, 19 files, complete) and `docs-flight/` (300 mm flying machine, under construction). See `MANIFEST.md`.

To the extent possible under law, Croft Swonyoung has waived all copyright and
related or neighbouring rights to every file in this set and dedicated them to
the public domain worldwide. You may copy, modify, build on, and redistribute
them, including commercially, without permission. **No warranty** — see `LICENSE`.

## Cite / DOI
Archived on Zenodo: **10.5281/zenodo.21224278** —
<https://doi.org/10.5281/zenodo.21224278>

## What's here
- `docs-rotor/` — the 150 mm **rotor / generator** line (19 documents, complete).
- `docs-flight/` — the 300 mm **flying-machine** line (under construction; a
  re-derivation plan + a seed integration SOP so far). Every document in both
  directories carries the CC0 dedication and the author's name inline (a banner in
  the HTML/Markdown files; a comment header in the DXF cut files).
- `LICENSE` — full CC0 1.0 legal code.
- `NOTICE.md` — short human-readable dedication + a note on patents/prior art.
- `MANIFEST.md` — the file list with descriptions.
- `CHANGELOG.md` — version history (what changed in each release).
- `CHECKSUMS.sha256` — SHA-256 of every file (integrity + the timestamping anchor).
- `TIMESTAMPING.md` — how the dated proof works and the one command to create it.
- `UPLOAD-CHECKLIST.md` — step-by-step durable-publication guide.

## Verify integrity
```
sha256sum -c CHECKSUMS.sha256
```

## Reproduce / publish
See `UPLOAD-CHECKLIST.md`. Short version: fill the date in `NOTICE.md`, run
`ots stamp CHECKSUMS.sha256`, then push copies to several independent archives
(Zenodo for a DOI, GitHub + a mirror → Software Heritage, Internet Archive,
Arweave/IPFS).

## Scope note
These documents describe the *fabrication* of a stacked nickel "nanovoid"
structure (grow ZnO nanotips → seed → electroless Ni-P → strip the template →
bond each foil to a silicon wafer → stack and seal the wafer cells under a common
vacuum). They specify how to build the article; they
do not, by themselves, establish what net energy or other output the finished
article produces. Anyone reproducing the work should measure inputs and outputs
directly, with controls. Open publication under CC0 is what makes that
independent verification possible.

This set covers **two end-use lines** built from the same fabrication chemistry:
- **`docs-rotor/` — 150 mm rotor / generator line** (complete). Includes an
  application-integration procedure, `ZnO-SOP-070` (a self-driven rotor test rig).
- **`docs-flight/` — 300 mm flying-machine line** (under construction). The wafer
  size cascades through the whole fabrication chain, so this line is re-derived on
  its own datum — see `docs-flight/300mm-re-derivation-plan.md`.

The integration procedures describe **test rigs for measuring the hypothesised
force**, written to be safe and informative whether or not any net force exists,
and claiming nothing.

## Background & attribution
The tapered-nanocavity geometry in this process is motivated by:

> M. E. McCulloch, "Can Nano-Materials Push Off the Vacuum?",
> *Progress in Physics*, **16** (2), 92–93 (2020).

which argues — from the theory of *quantised inertia* (QI) — that arrays of
asymmetric sub-~129 nm cavities could experience a net force from the quantum
vacuum. Quantised inertia is a non-mainstream theory and the predicted effect is
unverified; this set documents only the *fabrication* of such a structure.
Whether a finished stack produces any net force is an open question to be settled
by direct measurement (see the scope note above). Credit for the underlying idea
is McCulloch's; responsibility for reducing it to a build process — and for any
errors in doing so — is the author's.

Documentation for this release was prepared with assistance from Claude
(Anthropic), reflected in the git commit history.
