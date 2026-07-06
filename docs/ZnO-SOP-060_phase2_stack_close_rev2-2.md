<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Phase-2 Stack Close: Plate-by-Plate Butyl-Compression Assembly under N₂
### Building the sealed, nitrogen-filled nanovoid stack — low-weight variant

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-060 | Revision | 2.2 |
| Effective date | ____________ | Supersedes | Rev 2.1 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-050 (Phase-1 cell plates) | Next step | Final QC / packaging |
| Variant | Low weight · bonded stack · 30 cells | — | — |

---

## 1. Purpose and scope

This procedure performs **Phase 2** of the two-phase assembly: the entire stack is closed **plate by plate inside the dry-N₂ glovebox**, with every inner interface made by a **butyl bead compressed on both faces at once** as each plate lands. No silicone is applied to any inner face at any time; the structural silicone skin is applied **from outside, after closure**. Each cavity's getter, N₂ fill, and seal are established at the single moment its top plate lands — the only moment it is ever open.

**The three governing rules:**
1. All silicone bonds were completed and cured in Phase 1, with the butyl lands masked.
2. Every inner interface is **butyl-by-compression only** — sealed on both faces simultaneously when the plate lands. Butyl does not cure; closing the cavity and finishing its seal are the same act.
3. All structure lives **outboard** (structural silicone skin, plus optional perimeter clamp) and must hold the inner butyl in permanent compression for the service life.

**Substrate at entry:** Phase-1 cell plates (Al-backed nanovoid foils, rims trimmed, butyl lands verified silicone-free), bare aluminium spacer frames, getters — all staged in the glovebox.

**Output:** a sealed, N₂-filled, getter-maintained 30-cell bonded stack (~1.36 kg target at 25 µm Ni).

---

## 2. Definitions and interpretation

- **Edge stack per cell:** plate → butyl bead → bare Al spacer → butyl bead → next plate. The spacer is **not** silicone-bedded; both its joints are butyl.
- **Butyl-by-compression.** The primary seal is uncured PIB/butyl squeezed to contact — the standard insulated-glass primary-seal mode, good for decades **provided the squeeze is maintained**. The outboard structure is therefore not cosmetic: it is what keeps every inner joint compressed for life.
- **Compression stop.** The spacer thickness (0.025″) is the hard stop; the beads compress against it to the design gap. Hot-applied PIB beads (~0.4–0.6 mm as laid) compress to the thin, wide barrier geometry.
- **Open voids, sealed cavity.** The nanovoids breathe into the cell cavity; the seal is at the edge. The working face is the mid-P void liner; the seal border (~13 mm) lands on clean conversion-coated aluminium.
- **Conversion coating — Cr(VI)-free.** All conversion-coated aluminium in the stack (spacer lands as well as the Phase-1 plates) uses the Cr(VI)-free coating specified in ZnO-SOP-050 §5 (trivalent-Cr MIL-DTL-5541 Type II class, or Zr/Ti-based); hexavalent-chromium coatings are not permitted anywhere in the build.
- **Getter spares nitrogen.** O₂-and-moisture scavenger only; a general NEG would pump the N₂ and accelerate pressure decay.
- **Fault tolerance.** Cells are independently sealed (parallel): one breached cell loses its own area; the 0.025″ partition survives a neighbour's full 0.22 atm single-fault differential.
- **No reheat.** The PIB is thermoplastic; nothing after bead application may heat the edge. The outboard skin is RT-cure.

---

## 3. Health, safety and environment

- **Hot-applied PIB (~130–160 °C)** — burn hazard; applicator per manual. Applied at the staging bench or in a glovebox antechamber with adequate handling — not over finished working faces.
- **Dry-N₂ glovebox** — asphyxiation risk; O₂ monitoring and purge discipline.
- **Structural silicone (RT-cure)** — SDS; ventilate during cure.
- **PPE:** gloves, safety glasses.
- **Waste:** PIB and cured-silicone scrap per local rules.

---

## 4. Materials, reagents and equipment

### 4.1 Components (per 30-cell stack)

- 30 × Phase-1 cell plates (29 interior 0.025″ 5052 + 1 bottom end plate 0.125″ 6061); 1 × top end plate (0.125″ 6061, ribbed outer).
- 30 × bare aluminium spacer frames, 0.025″ × ⅜″, one-piece, conversion-coated lands (**Cr(VI)-free per ZnO-SOP-050 §5** — state on purchase orders/travellers).
- 30 × getters — O₂ + moisture, N₂-sparing, thin (fits gap − 0.3 mm bow budget), oversized for life.
- IGU-grade PIB/butyl for hot application (or compressed uncured butyl tape against the spacer stop, leak-qualified).
- Two-part **RT-cure structural silicone** (plain grade) for the outboard skin.
- Optional: perimeter clamp/tie-frame hardware if specified for compression assurance.

### 4.2 Equipment

- Dry-N₂ glovebox with O₂/H₂O monitoring; staging antechamber.
- Hot-melt PIB applicator; alignment/registration fixture with spacer compression stop.
- He leak test (fine/gross); RGA for witness cells; SEM.

---

## 5. Specifications

| Element | Specification | Notes |
|---|---|---|
| Stack | 30 cells, closed plate-by-plate under N₂ | one cavity sealed per plate landing |
| Inner interfaces | butyl-by-compression, both faces at once | no cure; no silicone inboard |
| Bead (as laid) | ~0.4–0.6 mm hot PIB, 6–10 mm land | compresses to gap against spacer stop |
| Spacer | bare Al 0.025″ × ⅜″, one-piece | = compression stop = cavity gap; lands Cr(VI)-free conversion-coated |
| Seal border | ~13 mm, on clean Al | former clamp/rim footprint |
| Fill | dry N₂, ~1 atm (glovebox ambient) | trapped at plate landing |
| Getter | N₂-sparing O₂/H₂O scavenger, per cavity | placed just before its plate lands |
| Outboard skin | RT-cure structural silicone, 4–6 mm deep | applied from outside after close |
| Compression assurance | skin (± clamp) holds inner butyl squeezed for life | design requirement, not option |
| Target mass | ~1.36 kg (≈45 g/cell) | at 25 µm Ni |

---

## 6. Procedure

### 6.1 Staging

1. Stage in the glovebox: Phase-1 cell plates (lands verified silicone-free), spacers, getters, fixture. Confirm box O₂/H₂O within spec.
2. Verify no silicone product is present or applied inside the box during Phase-2 close.

### 6.2 Bead application

1. Apply the hot PIB bead to **both faces of each spacer frame** (continuous loop, no corner splice) at the staging bench/antechamber; let cool. Alternatively bead the plate land + spacer top.
2. Inspect each bead: continuous, uniform, centred on the land.

### 6.3 Plate-by-plate close (repeat × 30)

1. Register the current top plate in the fixture, working face up.
2. Glue the getter to the underside of the **next** plate (cavity-facing), clear of lands.
3. Land the beaded spacer on the current plate's seal land; press to the spacer stop — the lower bead seals.
4. Land the next plate onto the spacer's upper bead; press to the stop — **the cavity below is now sealed with its N₂, getter, and working face inside**. Both faces of each bead are squeezed at the moment of landing.
5. Verify registration and even squeeze-out; proceed upward. Never reopen a closed cavity.

### 6.4 Cap and outboard structure

1. Land the ribbed top end plate on the final beaded spacer.
2. Remove the stack from the box (all cavities are sealed).
3. Apply the **outboard structural silicone skin** into the perimeter channel from outside, full height; tool and cure at RT. If specified, install the perimeter clamp/tie-frame and preload before or instead of relying on the skin alone.
4. Confirm the compression path: the skin/clamp must hold every inner butyl joint squeezed permanently.

### 6.5 Recovery

1. Label with stack ID, cell count, fill date, getter lot. Proceed to leak test.

---

## 7. Acceptance criteria and QC

- **Per-cell seal:** He fine/gross leak within spec; qualify the process by accelerated aging + gas-loss testing (EN 1279 / ASTM E2190 frameworks).
- **Fill:** dry N₂ confirmed (RGA on witness cells); O₂/H₂O below limit.
- **Compression:** outboard skin continuous full-height (and clamp preloaded, if fitted); no inner joint relying on adhesion alone.
- **Structure:** stack aligned, flat, self-supporting; spacers carry the column load; butyl in compression, never peel.
- **Working surfaces:** void faces clean, un-oxidised, open to their cavities.
- **Fault tolerance:** verify (analysis or test) a single breached cell does not cascade.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Cell fails leak test | Bead discontinuity or corner defect → continuous one-piece beads; check compression stop and squeeze-out. |
| Butyl adhesion poor | Land contamination (silicone) → Phase-1 land gate failed; re-verify gate; segregate silicone. If a coating-chemistry change (trivalent-Cr ↔ Zr/Ti) coincided, re-qualify butyl adhesion on coupons. |
| Internal O₂/H₂O high | Box atmosphere out of spec or getter wrong/undersized → dry the box; N₂-sparing getter with margin. |
| Seal relaxes over time | Compression path inadequate → strengthen outboard skin; add perimeter clamp; verify no zinc under any land. |
| Plates bow into getter | Gap vs getter+bow budget, or N₂ loss → thinner getter; verify seal retention. |
| Stack misaligned | Fixture registration → improve stops; land plates square. |

---

## 9. Waste and storage

- PIB and cured-silicone scrap per local regulations.
- Store finished stacks flat, protected, labelled; retain leak-test records per stack.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | ____ | ____ | Initial release. |
| 1.1 | ____ | ____ | Working face = mid-P; seal border on clean Al. |
| 2.0 | ____ | ____ | Recast as Phase 2 of two-phase assembly: plate-by-plate glovebox close; every inner interface butyl-by-compression sealed on both faces as the plate lands; spacer bare Al (no silicone bedding); outboard structural skin applied from outside after closure and made responsible for permanent butyl compression. |
| 2.1 | ____ | ____ | Clarified bottom end plate as 0.125″ 6061 (per ZnO-SOP-050 §4.1 and SP-001 purchasing), distinct from the 29 × 0.025″ 5052 interior plates. |
| 2.2 | ____ | ____ | Flowed the Cr(VI)-free conversion-coating requirement (ZnO-SOP-050 §5) to the spacer-frame lands; butyl-adhesion re-qualification note on coating-chemistry change. |
