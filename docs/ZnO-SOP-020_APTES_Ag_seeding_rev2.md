<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## APTES Functionalisation and Silver Seeding of ZnO Nanotips
### AgNO₃ activation with ascorbate reduction — catalytic seed layer for electroless Ni-P

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-020 | Revision | 2.0 |
| Effective date | ____________ | Supersedes | Rev 1.0 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-010 (nanotip growth) | Next step | ZnO-SOP-030 (electroless Ni-P) |

---

## 1. Purpose and scope

This procedure functionalises grown ZnO nanotips with an aminosilane (APTES) monolayer, then anchors and reduces silver to form a dispersed layer of metallic Ag⁰ nanoparticles. That silver layer is the catalytic seed that initiates a subsequent electroless nickel-phosphorus (Ni-P) deposition; it is **not** the final metallisation.

**Process chain:** hydroxylate → vapour-phase APTES (amine groups) → AgNO₃ loading (Ag⁺ capture) → ascorbate reduction (Ag⁰ seeds) → hold under N₂ → electroless Ni-P (ZnO-SOP-030).

**Substrate:** Zn foil, 70 µm × 100 mm × 125 mm, bearing ZnO nanotips on one face (reverse masked by the carrier), from ZnO-SOP-010.

**Design intent:** amine density sets seed density sets Ni-P nucleation density, so silane quality carries the "densely packed" goal into the metal layer.

---

## 2. Definitions and interpretation

- **Seeding / activation:** creating catalytic Ag⁰ nuclei on the surface. Ni-P will not initiate on bare ZnO/APTES; it needs the reduced metallic silver.
- **Vapour-phase silanisation:** APTES is delivered as vapour to a substrate in a sealed chamber, not by liquid immersion. Chosen here because it coats the high-aspect-ratio tip array evenly and avoids silane polymerising in the crevices between tips.
- **Near-neutral rule:** the substrate (ZnO tips on Zn foil) is amphoteric and Zn is very active. **Keep every wet step near-neutral pH.** No ammonia, no strongly alkaline reductants, no strong acid.
- **Reductant — sodium ascorbate (Rev 2.0).** Ascorbate reduces Ag⁺ → Ag⁰ at room temperature and is essentially benign, replacing dimethylamine borane (toxic; borane off-gassing in the box). Use the **sodium salt**, or free ascorbic acid neutralised to pH 6–7: free ascorbic acid at working strength sits near pH 3, which would violate the near-neutral rule. Ascorbate is a milder reducer than DMAB — expect **minutes rather than seconds** to the grey haze, and re-qualify seed size/dispersion on the first run.
- **Silver source:** AgNO₃ (soluble, gives free Ag⁺ that the amine can coordinate). AgCl was considered and rejected — it is essentially insoluble and the complexants needed to dissolve it either attack the substrate (ammonia) or out-compete the amine anchoring (thiosulfate).

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **APTES** — moisture-sensitive, corrosive/irritant, flammable liquid. Handle dry, in a glovebox or hood; gloves and goggles.
- **Silver nitrate (AgNO₃)** — oxidiser; corrosive, causes burns and black staining of skin; light-sensitive; toxic to aquatic life. See §3.1 for the substrate-specific galvanic hazard.
- **Sodium ascorbate / ascorbic acid** — low hazard (food-grade antioxidant); mild eye/respiratory irritant as dust. No flammable off-gassing — the special glovebox purge provisions required for the former borane reductant no longer apply.
- **Enclosed-atmosphere work** — silver stages need dim/amber light (silver photoreduces).
- **PPE:** nitrile gloves, safety goggles, lab coat.
- **Waste:** collect silver-bearing solutions and rinses separately for silver recovery; do not drain-dispose. Never mix silver solution with ammonia (explosive silver-nitride/fulminate risk).

### 3.1 Substrate-specific hazard — galvanic silver displacement

Any **bare zinc** contacting AgNO₃ will spontaneously cement silver and dissolve zinc (Zn + 2 Ag⁺ → Zn²⁺ + 2 Ag). This roughens and undercuts the substrate during silver loading, not just during later plating. Mitigate by keeping the reverse face masked, minding cut edges, keeping AgNO₃ concentration modest and immersion short, and ensuring continuous ZnO/APTES coverage so solution cannot reach foil through pinholes.

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

- UV-ozone cleaner or low-power O₂ plasma unit (outside the glovebox).
- Wet-type N₂ glovebox with amber / low-light capability.
- Sealed vapour chamber (glass desiccator or closed vessel) for APTES vapour deposition; small inert reservoir dish for the APTES liquid.
- Hotplate capable of a stable ~110 °C cure (gentle ramp).
- Amber glassware, PTFE-tipped tweezers, analytical balance (0.1 mg), timer, drying stand, pH paper/meter (reductant make-up check).
- Substrate carrier that masks the reverse face.

---

## 5. Process specification

| Stage | Parameter | Specification | Notes / tolerance |
|---|---|---|---|
| Hydroxylation | Method | UV-ozone 10–15 min *or* O₂ plasma 30–60 s (low power) | Maximises surface –OH; leaves trace surface water (needed for vapour APTES) |
| Hydroxylation | Location | Outside the box | Transfer into the box promptly; do not over-dry |
| APTES vapour | Reservoir | ~200–300 µL liquid APTES, not touching samples | Sealed chamber |
| APTES vapour | Condition | ~70 °C, 45–60 min (optional mild vacuum) | RT overnight is an alternative |
| APTES cure | Condition | ~110 °C, 20–30 min, air or N₂ | Gentle ramp; far below 419.5 °C Zn m.p. |
| Ag loading | Solution | 10–20 mM AgNO₃ in DI (or 1:1 ethanol/water) | Ethanol/water wets the array better |
| Ag loading | Condition | RT, 15–30 min, dim/amber light | Brief gentle DI rinse after |
| Reduction | Solution | 10–50 mM sodium ascorbate, aqueous, pH 6–7 | Fresh; make up immediately before use; discard if yellowed |
| Reduction | Condition | RT, ~2–10 min to a faint grey haze | Milder than the former DMAB — allow minutes; rinse DI, blow dry N₂ |
| All wet stages | pH | Near-neutral | Substrate is amphoteric — see §2; verify reductant pH at make-up |
| Silver stages | Light | Dim / amber | AgNO₃ and Ag⁺ photoreduce |
| Post-reduction | Storage | Hold under N₂ until plating | Keeps fresh silver clean |

### 5.1 Solution make-up (representative volumes)

| Solution | Target | Per 100 mL | Per 250 mL |
|---|---|---|---|
| AgNO₃ loading | 15 mM | 0.255 g | 0.637 g |
| AgNO₃ (low) | 10 mM | 0.170 g | 0.425 g |
| AgNO₃ (high) | 20 mM | 0.340 g | 0.849 g |
| Sodium ascorbate reductant | 30 mM | 0.594 g | 1.486 g |
| — as free ascorbic acid* | 30 mM | 0.528 g | 1.321 g |

\* If made from free ascorbic acid, neutralise to pH 6–7 with dilute NaOH before use and verify with pH paper/meter. Scale linearly. APTES is delivered as vapour, so it has no bath concentration — only the reservoir volume above.

---

## 6. Procedure

> **Glovebox flow (one in, one out).** Hydroxylation (§6.1) happens outside, as it needs the UV-ozone / plasma tool. Run §6.2 through §6.5 as a single campaign inside the wet box: enter once with hydroxylated foil, exit once with plating-ready seeded tips. Keep amber light for the silver stages.

### 6.1 Surface hydroxylation (before the box)

1. Handle the foil only with PTFE-tipped tweezers by an edge; never touch the growth face.
2. UV-ozone the growth face 10–15 min (or low-power O₂ plasma 30–60 s) to maximise surface –OH.
3. Do **not** bake bone-dry afterward — the trace adsorbed water is needed for the vapour silane to hydrolyse and bond. Transfer into the glovebox promptly.

### 6.2 Vapour-phase APTES silanisation (in the box)

1. Place the substrates in the sealed chamber with a small open reservoir of ~200–300 µL APTES nearby. Liquid APTES must not contact the samples.
2. Hold ~45–60 min at ~70 °C (optionally under mild vacuum to speed vapour transport), or leave at RT overnight.
3. Remove and cure at ~110 °C for 20–30 min to condense the siloxane bonds (gentle ramp for the thin foil).
4. Verify monolayer quality once before committing a batch (water contact-angle drop, or XPS nitrogen signal).

### 6.3 Silver loading — AgNO₃ (in the box, dim/amber light)

1. Immerse in 10–20 mM AgNO₃ (DI, or 1:1 ethanol/water for better array wetting), RT, 15–30 min, dark.
2. Withdraw and give a brief gentle DI rinse to remove unbound silver.
3. Inspect edges and any exposed foil for dark cemented silver — that is galvanic displacement (§3.1) and indicates a masking or coverage problem, not successful seeding.

### 6.4 Reduction to Ag⁰ seeds (in the box)

1. Make up fresh 10–50 mM sodium ascorbate (aqueous; or ascorbic acid neutralised to pH 6–7) immediately before use. Verify pH 6–7. Discard and remake if the solution has yellowed — that is oxidised ascorbate and it reduces poorly.
2. Immerse the silver-loaded substrate at RT. A faint silver-grey haze should develop within ~2–10 minutes as Ag⁺ → Ag⁰. Ascorbate is milder than the former DMAB — allow up to ~15 min before treating a slow run as a fault.
3. Rinse in DI and blow dry with N₂.

### 6.5 Hold / handoff

1. Store the seeded substrates under N₂ in the box (or a sealed inert container) until the electroless Ni-P step, so the fresh silver stays clean.
2. Label with run ID, silane batch, and seeding date.

---

## 7. Acceptance criteria and QC

- **APTES:** measurable contact-angle change vs. bare ZnO (or XPS N signal); uniform, with no visible polymer haze or particulate film.
- **Silver seeds (SEM):** fine, evenly distributed Ag nanoparticles decorating the tips; dispersion (not a continuous film) is the goal. **Rev 2.0 first-run gate:** re-qualify seed size and dispersion with the ascorbate reductant (its milder kinetics can shift the particle-size distribution vs. DMAB) before releasing the recipe to routine use.
- **Substrate integrity (SEM):** ZnO tips intact — no dissolution, rounding, or roughening from a pH excursion; no cemented silver on the foil or edges.
- **Readiness:** surface visibly activated (faint grey) and held under N₂ pending plating.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| No / patchy grey after reduction | Poor APTES monolayer, short Ag loading, or oxidised/stale ascorbate → re-hydroxylate and redo §6.2; extend loading; make fresh reductant and verify pH 6–7. |
| Reduction very slow (> ~15 min) | Ascorbate weaker than expected → confirm fresh, un-yellowed solution; raise concentration within 10–50 mM; extend time. Do not substitute an alkaline reductant. |
| Dark silver on foil / edges; tips undercut | Galvanic displacement on bare Zn (§3.1) → improve masking; check ZnO/APTES pinhole coverage; shorten immersion; lower AgNO₃ concentration. |
| Silane haze / particulate film | Too much moisture in the vapour step → drier box atmosphere, smaller reservoir, shorter time. |
| Tips dissolved / roughened | pH excursion → keep all wet steps near-neutral; verify the reductant was neutralised (free ascorbic acid is pH ~3 — always use the sodium salt or neutralise). |
| Uneven seed density | Vapour did not reach the whole array → use mild vacuum, extend the vapour step; confirm even hydroxylation. |
| Seeds tarnish / discolour before plating | Air / contamination exposure → hold under N₂; shorten the gap to plating. |

---

## 9. Waste and storage

- Collect silver-bearing solutions and rinses separately for silver recovery; do not drain-dispose. Never combine with ammonia.
- Spent ascorbate solutions mixed with silver follow the silver-recovery stream; ascorbate itself carries no special disposal burden.
- Store APTES sealed and dry (moisture-sensitive); AgNO₃ in amber, away from light and organics; sodium ascorbate/ascorbic acid sealed, cool, and dry (oxidises slowly in air).
- Store seeded substrates under N₂, labelled, until the electroless Ni-P step.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | ____________ | Initial release — vapour-phase APTES, AgNO₃ loading, DMAB reduction; AgCl rejected on solubility/compatibility grounds. |
| 2.0 | __________ | ____________ | Lower-toxicity substitution: DMAB replaced by sodium ascorbate (10–50 mM, pH 6–7) — eliminates borane toxicity/off-gassing and the associated glovebox purge burden. Reduction time extended to minutes; free-acid neutralisation requirement and seed-morphology re-qualification gate added. |
