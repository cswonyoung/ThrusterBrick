<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-020` Rev 2.1.** The seeding
> **chemistry, temperatures, per-litre concentrations, and target seed geometry are
> identical** to the 150 mm procedure — only the **substrate blank, vessels/chambers,
> fixtures, reagent volumes, and per-coupon masses** scale with the larger wafer. All
> dimensions come from `300mm-datum-reference.md`; this SOP does not restate them
> independently.

---

# Working Procedure & Specification

## APTES Functionalisation and Silver Seeding of ZnO Nanotips (300 mm)
### AgNO₃ activation with ascorbate reduction — catalytic seed layer for electroless Ni-P

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-020-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 2.1) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-010-300 (nanotip growth) | Next step | ZnO-SOP-030-300 (electroless Ni-P) |

---

## 1. Purpose and scope

This procedure functionalises grown ZnO nanotips with an aminosilane (APTES) monolayer, then anchors and reduces silver to form a dispersed layer of metallic Ag⁰ nanoparticles. That silver layer is the catalytic seed that initiates a subsequent electroless nickel-phosphorus (Ni-P) deposition; it is **not** the final metallisation.

**Process chain:** hydroxylate → vapour-phase APTES (amine groups) → AgNO₃ loading (Ag⁺ capture) → ascorbate reduction (Ag⁰ seeds) → hold under N₂ → electroless Ni-P (ZnO-SOP-030-300).

**Substrate:** Zn foil, **0.15 mm × ⌀306 round blank** (⌀280 active area inside a 13 mm rim, to back a 300 mm silicon wafer — see `300mm-datum-reference.md`), bearing ZnO nanotips on one face (reverse masked by the carrier), from ZnO-SOP-010-300.

**Design intent:** amine density sets seed density sets Ni-P nucleation density, so silane quality carries the "densely packed" goal into the metal layer. *(At 300 mm the same requirement now has to hold uniformly across the larger ⌀280 field — see §7.)*

---

## 2. Definitions and interpretation

- **Seeding / activation:** creating catalytic Ag⁰ nuclei on the surface. Ni-P will not initiate on bare ZnO/APTES; it needs the reduced metallic silver.
- **Vapour-phase silanisation:** APTES is delivered as vapour to a substrate in a sealed chamber, not by liquid immersion. Chosen here because it coats the high-aspect-ratio tip array evenly and avoids silane polymerising in the crevices between tips. *(Even delivery over the larger ⌀280 face is a new concern at 300 mm — see §6.2 and §7.)*
- **Near-neutral rule:** the substrate (ZnO tips on Zn foil) is amphoteric and Zn is very active. **Keep every wet step near-neutral pH.** No ammonia, no strongly alkaline reductants, no strong acid.
- **Reductant — sodium ascorbate (from 150 mm Rev 2.0).** Ascorbate reduces Ag⁺ → Ag⁰ at room temperature and is essentially benign, replacing dimethylamine borane (toxic; borane off-gassing in the box). Use the **sodium salt**, or free ascorbic acid neutralised to pH 6–7: free ascorbic acid at working strength sits near pH 3, which would violate the near-neutral rule. Ascorbate is a milder reducer than DMAB — expect **minutes rather than seconds** to the grey haze, and re-qualify seed size/dispersion on the first run.
- **Silver source:** AgNO₃ (soluble, gives free Ag⁺ that the amine can coordinate). AgCl was considered and rejected — it is essentially insoluble and the complexants needed to dissolve it either attack the substrate (ammonia) or out-compete the amine anchoring (thiosulfate).

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **APTES** — moisture-sensitive, corrosive/irritant, flammable liquid. Handle dry, in a glovebox or hood; gloves and goggles.
- **Silver nitrate (AgNO₃)** — oxidiser; corrosive, causes burns and black staining of skin; light-sensitive; toxic to aquatic life. See §3.1 for the substrate-specific galvanic hazard.
- **Sodium ascorbate / ascorbic acid** — low hazard (food-grade antioxidant); mild eye/respiratory irritant as dust. No flammable off-gassing — the special glovebox purge provisions required for the former borane reductant no longer apply.
- **Enclosed-atmosphere work** — silver stages need dim/amber light (silver photoreduces).
- **Larger reagent volumes** — the silver and reductant baths are now **~4× larger (~4× the 150 mm volume)** to submerge the ⌀306 coupon. More silver in solution per batch means a larger silver-recovery burden and a larger spill footprint; use stable, well-supported vessels and handle the fuller baths with safe lifting practice.
- **PPE:** nitrile gloves, safety goggles, lab coat.
- **Waste:** collect silver-bearing solutions and rinses separately for silver recovery; do not drain-dispose (volumes are now ~4× the 150 mm line — size the recovery stream accordingly). Never mix silver solution with ammonia (explosive silver-nitride/fulminate risk).

### 3.1 Substrate-specific hazard — galvanic silver displacement

Any **bare zinc** contacting AgNO₃ will spontaneously cement silver and dissolve zinc (Zn + 2 Ag⁺ → Zn²⁺ + 2 Ag). This roughens and undercuts the substrate during silver loading, not just during later plating. Mitigate by keeping the reverse face masked, minding cut edges, keeping AgNO₃ concentration modest and immersion short, and ensuring continuous ZnO/APTES coverage so solution cannot reach foil through pinholes. *(The ⌀306 coupon has a longer rim/edge perimeter to mask and inspect than the 150 mm blank — check the whole circumference.)*

---

## 4. Materials, reagents and equipment

### 4.1 Reagents

- (3-Aminopropyl)triethoxysilane (APTES), C₉H₂₃NO₃Si (M = 221.37 g/mol), anhydrous grade.
- Silver nitrate (AgNO₃), ACS grade (M = 169.87 g/mol).
- Sodium L-ascorbate, C₆H₇NaO₆ (M = 198.11 g/mol) — or L-ascorbic acid, C₆H₈O₆ (M = 176.12 g/mol), neutralised to pH 6–7 with dilute NaOH at make-up.
- Deionised water, Type I (≥ 18 MΩ·cm).
- Anhydrous ethanol (optional silver-bath co-solvent and rinsing).
- Dry nitrogen (glovebox atmosphere and drying).

### 4.2 Equipment

- UV-ozone cleaner or low-power O₂ plasma unit (outside the glovebox), **with a working area / chamber that clears the ⌀306 coupon** (⌀280 active field must be exposed evenly — a source too small for the face will hydroxylate non-uniformly; see §6.1 / §7).
- Wet-type N₂ glovebox with amber / low-light capability, large enough to work the ⌀306 coupon and the larger vessels comfortably.
- Sealed vapour chamber (glass desiccator or closed vessel) **sized to accept the ⌀306 coupon** for APTES vapour deposition; small inert reservoir dish for the APTES liquid.
- Hotplate capable of a stable ~110 °C cure (gentle ramp), platen large enough to support the full ⌀306 disc flat.
- Amber glassware, PTFE-tipped tweezers, analytical balance (0.1 mg), timer, drying stand, pH paper/meter (reductant make-up check).
- Substrate carrier (round, per ZnO-DR-003-300 / ZnO-DR-005-300) that masks the reverse face and holds the **⌀306** coupon flat; amber wet-seeding vessels sized to submerge the ⌀306 coupon with clearance (~⌀340–360 mm, ~4× the 150 mm bath volume). The larger coupon is floppier — support it fully across all transfers (see §6).

---

## 5. Process specification

| Stage | Parameter | Specification | Notes / tolerance |
|---|---|---|---|
| Hydroxylation | Method | UV-ozone 10–15 min *or* O₂ plasma 30–60 s (low power) | Maximises surface –OH; leaves trace surface water (needed for vapour APTES); ensure the source covers the whole ⌀280 field |
| Hydroxylation | Location | Outside the box | Transfer into the box promptly; do not over-dry |
| APTES vapour | Reservoir | ~800–1200 µL liquid APTES, not touching samples | Scaled ~4× with the larger chamber headspace/face; sealed chamber |
| APTES vapour | Condition | ~70 °C, 45–60 min (optional mild vacuum) | RT overnight is an alternative; larger chamber may need the longer end of the window / mild vacuum for even vapour reach |
| APTES cure | Condition | ~110 °C, 20–30 min, air or N₂ | Gentle ramp; far below 419.5 °C Zn m.p. |
| Ag loading | Solution | 10–20 mM AgNO₃ in DI (or 1:1 ethanol/water) | Ethanol/water wets the array better; **per-litre loading unchanged** |
| Ag loading | Condition | RT, 15–30 min, dim/amber light | Brief gentle DI rinse after |
| Reduction | Solution | 10–50 mM sodium ascorbate, aqueous, pH 6–7 | Fresh; make up immediately before use; discard if yellowed; **per-litre loading unchanged** |
| Reduction | Condition | RT, ~2–10 min to a faint grey haze | Milder than the former DMAB — allow minutes; rinse DI, blow dry N₂ |
| All wet stages | pH | Near-neutral | Substrate is amphoteric — see §2; verify reductant pH at make-up |
| Silver stages | Light | Dim / amber | AgNO₃ and Ag⁺ photoreduce |
| Post-reduction | Storage | Hold under N₂ until plating | Keeps fresh silver clean |

> **Concentrations, temperatures, and times are unchanged from the 150 mm line** — they
> are per-litre / per-area effects independent of coupon size. The ⌀306 coupon simply
> needs **~4× the litres** of the same solutions in larger vessels; only volume-driven
> fill and immersion handling scale. The APTES reservoir scales with the larger chamber
> headspace, not the bath concentration (APTES is vapour-delivered, so it has no bath
> concentration).

### 5.1 Solution make-up (representative volumes)

Per-litre loadings are unchanged from the 150 mm line; only the batch volume grows (~4×) to submerge the ⌀306 coupon in the larger amber vessels. Columns below add the ~4× working volumes alongside the original reference columns.

| Solution | Target | Per 100 mL | Per 250 mL | Per 1.0 L | Per 2.0 L |
|---|---|---|---|---|---|
| AgNO₃ loading | 15 mM | 0.255 g | 0.637 g | 2.548 g | 5.096 g |
| AgNO₃ (low) | 10 mM | 0.170 g | 0.425 g | 1.699 g | 3.397 g |
| AgNO₃ (high) | 20 mM | 0.340 g | 0.849 g | 3.397 g | 6.795 g |
| Sodium ascorbate reductant | 30 mM | 0.594 g | 1.486 g | 5.943 g | 11.887 g |
| — as free ascorbic acid* | 30 mM | 0.528 g | 1.321 g | 5.284 g | 10.567 g |

\* If made from free ascorbic acid, neutralise to pH 6–7 with dilute NaOH before use and verify with pH paper/meter. **Scale linearly** — mass = (per-litre loading) × volume in L. **Sizing:** use the smallest volume that fully submerges the ⌀306 coupon in its carrier with clearance — typically **~1.5–2 L** per wet stage in a ~⌀340–360 mm amber vessel (vs. a few hundred mL at 150 mm). APTES is delivered as vapour, so it has no bath concentration — only the reservoir volume in §5 (~800–1200 µL, scaled with the larger chamber).

---

## 6. Procedure

> **Glovebox flow (one in, one out).** Hydroxylation (§6.1) happens outside, as it needs the UV-ozone / plasma tool. Run §6.2 through §6.5 as a single campaign inside the wet box: enter once with hydroxylated foil, exit once with plating-ready seeded tips. Keep amber light for the silver stages. **Support the large ⌀306 coupon fully on every transfer** — it is floppier than the 150 mm blank and must stay flat so the APTES layer and seed field come out uniform.

### 6.1 Surface hydroxylation (before the box)

1. Handle the foil only with PTFE-tipped tweezers by an edge; never touch the growth face. Support the full ⌀306 disc so it does not fold.
2. UV-ozone the growth face 10–15 min (or low-power O₂ plasma 30–60 s) to maximise surface –OH. **Ensure the source illuminates/treats the whole ⌀280 active field evenly** — if the tool's active area is smaller than the coupon, index the coupon or use a larger source, and confirm uniform activation (see §7). Uneven hydroxylation seeds uneven APTES and uneven silver downstream.
3. Do **not** bake bone-dry afterward — the trace adsorbed water is needed for the vapour silane to hydrolyse and bond. Transfer into the glovebox promptly.

### 6.2 Vapour-phase APTES silanisation (in the box)

1. Place the substrate in the sealed chamber (sized for the ⌀306 coupon) with a small open reservoir of ~800–1200 µL APTES nearby (scaled to the larger chamber headspace). Liquid APTES must not contact the sample. Seat the coupon flat on a support so the whole face is exposed to the vapour.
2. Hold ~45–60 min at ~70 °C (optionally under mild vacuum to speed vapour transport), or leave at RT overnight. **Over the larger face, favour the longer end of the window and/or mild vacuum** so vapour reaches the centre and edges alike.
3. Remove and cure at ~110 °C for 20–30 min to condense the siloxane bonds (gentle ramp; the 0.15 mm foil thickness is unchanged, but the larger ⌀306 disc has more unsupported area — cure it on a full-face support to keep it flat; still far below the 419.5 °C Zn m.p.).
4. Verify monolayer quality once before committing a batch (water contact-angle drop, or XPS nitrogen signal) — **and at 300 mm, sample the centre and edge of the ⌀280 field, not just one spot**, to confirm the silane is uniform across the larger area (see §7).

### 6.3 Silver loading — AgNO₃ (in the box, dim/amber light)

1. Immerse in 10–20 mM AgNO₃ (DI, or 1:1 ethanol/water for better array wetting), RT, 15–30 min, dark. Use the ~1.5–2 L working volume that submerges the ⌀306 coupon with clearance; **per-litre AgNO₃ loading is unchanged**. Enter the bath so no air is trapped against the larger face — tilt on entry to sweep bubbles clear.
2. Withdraw and give a brief gentle DI rinse to remove unbound silver.
3. Inspect edges and any exposed foil for dark cemented silver — that is galvanic displacement (§3.1) and indicates a masking or coverage problem, not successful seeding. **Check the whole ⌀306 circumference** — the longer edge perimeter is more chances for a masking gap.

### 6.4 Reduction to Ag⁰ seeds (in the box)

1. Make up fresh 10–50 mM sodium ascorbate (aqueous; or ascorbic acid neutralised to pH 6–7) immediately before use, in the ~1.5–2 L working volume (**per-litre loading unchanged**). Verify pH 6–7. Discard and remake if the solution has yellowed — that is oxidised ascorbate and it reduces poorly.
2. Immerse the silver-loaded substrate at RT. A faint silver-grey haze should develop within ~2–10 minutes as Ag⁺ → Ag⁰. Ascorbate is milder than the former DMAB — allow up to ~15 min before treating a slow run as a fault. **Watch that the haze develops evenly across the whole ⌀280 field**, not just at the centre or one edge.
3. Rinse in DI and blow dry with N₂, holding the ⌀306 disc so water sheets off cleanly.

### 6.5 Hold / handoff

1. Store the seeded substrates under N₂ in the box (or a sealed inert container) until the electroless Ni-P step, so the fresh silver stays clean. Store the large coupon flat between clean flat supports.
2. Label with run ID, silane batch, and seeding date.

---

## 7. Acceptance criteria and QC

- **APTES:** measurable contact-angle change vs. bare ZnO (or XPS N signal); uniform, with no visible polymer haze or particulate film. **Sample centre and edge of the ⌀280 field** — over the larger active area, confirm the silane is uniform, not just present at one spot (a bigger face is more prone to centre-to-edge gradients from uneven hydroxylation or vapour reach).
- **Silver seeds (SEM):** fine, evenly distributed Ag nanoparticles decorating the tips; dispersion (not a continuous film) is the goal. Sample **multiple sites across the ⌀280 field** (centre + several radii/edges), not just the centre — uniform Ag dispersion across the larger field is a first-run gate at 300 mm. **First-run gate:** re-qualify seed size and dispersion with the ascorbate reductant (its milder kinetics can shift the particle-size distribution) **and confirm cross-field uniformity** before releasing the recipe to routine use.
- **Substrate integrity (SEM):** ZnO tips intact — no dissolution, rounding, or roughening from a pH excursion; no cemented silver on the foil or edges (check the full ⌀306 circumference).
- **Readiness:** surface visibly activated (faint grey, even across the face) and held under N₂ pending plating.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| No / patchy grey after reduction | Poor APTES monolayer, short Ag loading, or oxidised/stale ascorbate → re-hydroxylate and redo §6.2; extend loading; make fresh reductant and verify pH 6–7. |
| **Centre-to-edge non-uniformity of APTES or Ag seeds** (new at 300 mm) | Uneven hydroxylation or vapour reach over the larger ⌀280 face, or uneven immersion → cover the whole field in §6.1 (index or larger source); favour the longer vapour step / mild vacuum in §6.2; ensure even, bubble-free immersion depth in §6.3–6.4; sample multiple sites per §7. |
| Reduction very slow (> ~15 min) | Ascorbate weaker than expected → confirm fresh, un-yellowed solution; raise concentration within 10–50 mM; extend time. Do not substitute an alkaline reductant. |
| Dark silver on foil / edges; tips undercut | Galvanic displacement on bare Zn (§3.1) → improve masking; check ZnO/APTES pinhole coverage; shorten immersion; lower AgNO₃ concentration. Inspect the full ⌀306 edge — more perimeter to mask than at 150 mm. |
| Silane haze / particulate film | Too much moisture in the vapour step → drier box atmosphere, smaller reservoir, shorter time. |
| Tips dissolved / roughened | pH excursion → keep all wet steps near-neutral; verify the reductant was neutralised (free ascorbic acid is pH ~3 — always use the sodium salt or neutralise). |
| Uneven seed density | Vapour did not reach the whole array → use mild vacuum, extend the vapour step; confirm even hydroxylation. Over the ⌀280 field this is more likely — verify with centre + edge sampling. |
| Coupon folds / warps during handling | Larger ⌀306 coupon is floppier than the 150 mm blank → support the full disc on every transfer; seat it on a full-face support for the cure and dry; store flat between supports. |
| Seeds tarnish / discolour before plating | Air / contamination exposure → hold under N₂; shorten the gap to plating. |

---

## 9. Waste and storage

- Collect silver-bearing solutions and rinses separately for silver recovery; do not drain-dispose (volumes are ~4× the 150 mm line — size the recovery stream accordingly). Never combine with ammonia.
- Spent ascorbate solutions mixed with silver follow the silver-recovery stream; ascorbate itself carries no special disposal burden.
- Store APTES sealed and dry (moisture-sensitive); AgNO₃ in amber, away from light and organics; sodium ascorbate/ascorbic acid sealed, cool, and dry (oxidises slowly in air).
- Store seeded substrates under N₂, labelled, and flat between clean supports, until the electroless Ni-P step.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-020` Rev 2.1.** Substrate scaled to a **⌀306 round zinc blank** (⌀280 active + 13 mm rim, backing a 300 mm wafer per `300mm-datum-reference.md`); UV-ozone/plasma source, APTES vapour chamber, and wet-seeding vessels sized to clear the ⌀306 coupon; wet-bath working volumes ~4× (~1.5–2 L) with the §5.1 table extended to per-1 L/2 L columns; APTES reservoir scaled to ~800–1200 µL for the larger chamber; seeding carrier updated to ZnO-DR-003-300 / ZnO-DR-005-300 and cross-references updated to the -300 names; added centre-to-edge APTES/Ag uniformity checks (multi-site sampling across the ⌀280 field) and large-floppy-coupon handling/flatness notes. **Seeding chemistry, per-litre concentrations, temperatures, times, near-neutral rule, "no cemented Ag on edges," and glovebox/inert-atmosphere requirements are unchanged** — they are per-litre / per-area effects independent of coupon size. |
