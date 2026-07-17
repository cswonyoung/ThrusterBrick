<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

# Master Datum — 300 mm flying-machine line

**The single source of truth for every dimension in the `docs-flight/` line.** All
300 mm SOPs, design references, and DXF cut files must cite these numbers, not
restate their own. Derived from the 150 mm line (`../docs-rotor/`) by scaling the
wafer ⌀150 → ⌀300; the **chemistry is identical**, only geometry, tooling, and
mass change.

**Status:** proposed defaults, ready to build against. Items still needing maker
sign-off are marked **[confirm]**; the rest are locked.

## 1. Core stack datum

| Parameter | 150 mm (reference) | **300 mm (this line)** | Note |
|---|---|---|---|
| Wafer diameter | ⌀150.0 | **⌀300.0** | — |
| Wafer thickness | 0.675 mm | **0.775 mm** | SEMI standard for 300 mm — **locked** |
| Wafer finish | 1-side polished | **1-side polished** | polished face is the working cap |
| Active (etched) region | ⌀130 | **⌀280** | 10 mm wafer margin (same absolute as 150 mm) |
| Zinc foil thickness | 0.15 mm | **0.15 mm** | template thickness is wafer-independent |
| Zinc handling rim | 13 mm | **13 mm** | per side |
| Zinc blank | ⌀156 | **⌀306** | = active ⌀280 + 2 × 13 mm rim |
| Ni-P thickness | 25 µm | **25 µm** | diameter-independent |
| Per-cell pitch | ≈0.78 mm | **≈0.875 mm** | wafer 0.775 + Ni-P 0.025 + bond ~0.075 |

## 2. Mass (flyer-critical)

| Item | Value | Basis |
|---|---|---|
| Silicon wafer | ≈128 g | ⌀300 × 0.775 mm, ρ 2.33 g/cm³ |
| Ni-P layer | ≈12 g | ⌀280 active × 25 µm, ρ ~7.9 g/cm³ |
| Silicone bond | ≈5 g | ⌀280 × ~75 µm, ρ ~1.1 g/cm³ |
| **Per cell** | **≈145 g** | — |
| Stack (N cells) | **≈0.145 N kg** active | + platens + envelope/getter |

> **Scaling caveat (record in the flyer spec):** active area (~4.6×) and cell mass
> (~4.4×) scale together vs 150 mm, so **thrust-to-weight is ~scale-invariant.**
> The reason for choosing 300 mm is **handling / throughput** — fewer, larger parts
> to process, bond, and stack for a given total active area — **not** a better lift
> ratio. State this plainly wherever lift is discussed.

## 3. Carrier / cut-set datum (bounded by the 500 × 600 mm bed)

The shared carrier plate is the largest cut part and sets the bed size. Scaled
from the 150 mm carrier (window ⌀130 · O-ring ⌀143 · pocket ⌀156.3 · bolt circle
⌀174 ×12 M4 · outer ⌀190), keeping the seal/land widths roughly constant:

| Feature | **300 mm value** | Note |
|---|---|---|
| Window (active aperture) | ⌀280 | exposes the ⌀280 active region |
| O-ring groove | ⌀296 | seals around the active area, inside the coupon |
| Coupon pocket | ⌀306.3 × 0.15 mm deep | locates the ⌀306 zinc blank |
| Bolt circle | ⌀330, **×16 M4** | more bolts than the 150 mm ×12 for seal/flatness — **locked** |
| Carrier outer | **⌀350** | fits the 500 × 600 bed with clamp margin |

- **Bed:** standard **500 × 600 mm** router. ⌀350 part + ~50 mm workholding each
  side ≈ ⌀450 blank → fits (use the 600 mm axis for clamp length). ~1 carrier per
  sheet, as on the 150 mm line.
- **Companion plastic parts** (strip backer, clamp frame, immersion/seeding
  carrier) scale to the ⌀306 coupon; all cut on the same 500 × 600 router.
- **Aluminium wafer chuck** (⌀300+): heavier cut; **no waterjet** (cost) → rigid
  mill, slow router pass, outsource, or an alternative flat material. Decide when
  the chuck is designed (plan §5.1).

## 4. What scales with area (not diameter)

For sizing baths, getters, and process times, the driver is **area (~4×)**, not
thickness:
- Bath / reagent volumes ~4× (SOP-010/020/030/040): larger vessels, longer fill.
- Strip H₂/zincate load ~4× (SOP-040); the ~10–12 h void-clearing is
  void-geometry-limited (unchanged).
- Getter capacity ~4× the permeation/outgassing area (SOP-060).
- Vacuum envelope + chamber-sealer clearance sized for ⌀300+.

## 5. Naming and rationale (decided 2026-07-15)

- **File naming:** reuse the 150 mm step numbers with a **`-300` suffix** —
  `ZnO-SOP-010-300`, `ZnO-DR-001-300`, `ZnO_cut_<part>_300.dxf`, `ZnO-SP-001-300`.
  The flying-integration SOP is `ZnO-SOP-080-300`.
- **300 mm rationale:** **handling / throughput** (fewer, larger parts per unit
  active area). T/W is ~scale-invariant — the win is process/assembly efficiency,
  not lift ratio.

**All datum items locked (confirmed 2026-07-15):** wafer thickness **0.775 mm** and
carrier bolt pattern **⌀330 ×16 M4** are final, along with everything above. Ready
to build against.
