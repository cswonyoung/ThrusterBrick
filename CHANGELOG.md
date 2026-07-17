# Changelog — ZnO Nanovoid Process document set

All notable changes to this document set are recorded here. The set is dedicated
to the public domain under CC0 1.0 (see `LICENSE`). Versions follow the git tags;
the Zenodo **concept DOI** `10.5281/zenodo.21224278` always resolves to the
latest published version.

## [2.2] — 2026-07-17

Builds on the released **v2.1** (2026-07-15). The rotor-line ruggedization and the
integration SOPs (SOP-070/080) shipped in v2.1; this release reorganises the set
into two directories and adds the second, 300 mm line.

### Added — 300 mm flying-machine line (`docs-flight/`)
A complete second fabrication line at 300 mm wafers, for the flying-machine
application, re-derived from the 150 mm line on its own locked datum
(`300mm-datum-reference.md`: wafer ⌀300 × 0.775 mm, active ⌀280, zinc blank ⌀306,
carrier ⌀350). The **chemistry is identical**; geometry, bath volumes (~4×), masses
(~145 g/cell), and tooling scale with the larger wafer. Contents:
- **Fabrication SOPs** `ZnO-SOP-010-300 … 060-300` (growth → seed → plate → strip →
  wafer bond → vacuum stack close, including the Appendix A ruggedization at 300 mm).
- **Design references** `ZnO-DR-001-300 … 006-300` and the **shop packet** `ZnO-SP-001-300`.
- **DXF cut set** `ZnO_cut_*_300.dxf` (carrier ⌀350 / window ⌀280 / bolt circle ⌀330
  ×16 M4; ⌀300 wafer chuck) with matching **to-scale SVG plans**, both emitted by a
  shipped, reproducible generator **`gen_round_dxf_300.py`** and validated with ezdxf.
- The **flying-integration procedure** `ZnO-SOP-080-300` remains a 150 mm-based
  **seed**, pending a defined flyer (airframe, measured per-puck thrust, T/W).

Naming: the 150 mm step numbers with a `-300` suffix. The 300 mm choice is for
handling/throughput — thrust-to-weight is ~scale-invariant, not a better lift ratio.

### Changed — Two end-use lines, one set
The set was reorganised into two documentation directories under one publication:
- **`docs-rotor/`** — the 150 mm **rotor / generator** line (the former `docs/`,
  now including SOP-070); complete at 19 files.
- **`docs-flight/`** — the 300 mm **flying-machine** line (new; detailed above).
  Because the wafer size cascades through the whole fabrication chain, this line is
  built on its own locked datum.

One README/LICENSE/NOTICE/MANIFEST/CHANGELOG/CHECKSUMS covers both — a single
publication and a single Zenodo deposit, not two.

### Changed — Rotor line (`docs-rotor/`) refinements
- **SOP-070** thrust goal corrected to **50 lbf ≈ 222 N** (→ τ ≈ 102 N·m, ≈5.3 kW at
  500 rpm); the earlier "50 N" figure was an lbf→N slip.
- **SOP-080** (flying-vehicle integration) moved out of the rotor set into
  `docs-flight/` as the 300 mm-line seed (`ZnO-SOP-080-300`), since the flyer uses
  300 mm wafers.

### Changed — Housekeeping
- Directories: `docs/` → `docs-rotor/`; added `docs-flight/`.
- `MANIFEST.md`, `README.md`, `NOTICE.md`, and `TIMESTAMPING.md` updated to match.
- `CHECKSUMS.sha256` regenerated over both directories and verified (`sha256sum -c`
  passes on all entries).

## [2.1] — 2026-07-15

First application-specific mounting / integration work, in the single `docs/`
layout (before the two-line reorganisation of v2.2).

### Added — Ruggedization variant (SOP-060 Appendix A)
An application-agnostic option for units that will experience in-service inertial
loading at arbitrary orientation: a pre-cured, low-outgassing platinum-silicone
edge-cushion inside the vacuum envelope (protecting the brittle wafer edges) and an
outboard, filled, low-exotherm epoxy carrier pot (mounting datum + centre-of-gravity
budget). Sized to a design acceleration, with a spinning-rotor case (~128 × gravity)
as the bounding example. The baseline measurement brick omits both.

### Added — Application-integration procedures (SOP-070, SOP-080)
- **SOP-070** — a self-driven, thrust-vectored rotor test rig: integration,
  balancing, fail-safe braking/signal logic, and a commissioning sequence with
  built-in confound controls (null / drive / reversal / balanced-pair) and
  honest-null reporting.
- **SOP-080** — a staged flying-vehicle demonstrator: constrained thrust/lift
  measurement first, with free flight gated behind measured thrust-to-weight,
  demonstrated control, and a verified fail-safe.

Both are written to be safe and informative whether or not any net force exists,
and claim nothing.

## [2.0] — 2026-07-09

### Changed — Architecture migration (rectangular → round; Si-wafer / common vacuum)
The stack was rebuilt around a single-side-polished 150 mm silicon-wafer backer
and a zero-gap, common-vacuum design:
- Each electroless Ni-P foil is silicone-bonded (high-phosphorus face) to the
  unpolished back of a silicon wafer; cells stack with each foil's working (void)
  face in direct mechanical contact against the next cell's polished silicon
  face — no per-interface bond.
- One common vacuum for the whole stack, held by a getter inside a conformal
  metallized (vacuum-insulation-panel-grade) barrier envelope; atmospheric
  pressure supplies the preload.
- Retired: the aluminium backer plate, the nitrogen-filled spacer gap, and the
  per-cell butyl seals.
- SOP-010 through SOP-060 and the shop packet (SP-001) updated to the round
  156 mm blank / 130 mm active datum and 0.15 mm zinc; all six design-reference
  (DR) docs rewritten to Rev 2.0 and all five DXF cut files regenerated (the
  butyl clamp frame retired; the aluminium platen repurposed as a flat 150 mm
  wafer vacuum chuck).

## [1.x] — initial release

First public-domain release of the fabrication process (earlier rectangular,
nitrogen-filled architecture), archived on Zenodo under concept DOI
`10.5281/zenodo.21224278`.

---

**Scope.** These documents specify the fabrication of a stacked nickel "nanovoid"
article and rigs to test it. Whether a finished stack produces any net force is
an open, unmeasured hypothesis — to be settled by direct measurement with
controls, not asserted here.
