<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Caustic Strip (Zinc / ZnO Removal) and Cleaning-Drying of the Ni-P Nanovoid Foil
### Selective NaOH release of the template, leaving a clean, dry, free-standing nickel replica

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-040 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-030 (electroless Ni-P) | Next step | ZnO-SOP-050 (Phase-1 bond & rim trim) |

---

## 1. Purpose and scope

This procedure dissolves the zinc foil and the ZnO nanotip template out from under the electroless Ni-P coating using sodium hydroxide, freeing a self-supporting nickel foil that carries the former tips as open, tapered nanovoids. It then rinses and dries those nanovoids so the working surface is clean, residue-free, and ready for edge trimming and bonding to the aluminium plate.

**Selectivity is the whole idea:** NaOH dissolves Zn and ZnO (both amphoteric) and largely spares the high-P Ni-P.

**Substrate at entry:** a 25 µm Ni-P coating (from ZnO-SOP-030) still backed by its ZnO tips and Zn foil, held in a temporary caustic-proof carrier that supports the plated (outer) nickel face and exposes the bare Zn reverse face to the bath.

**Output:** a clean, dry, free-standing (carrier-supported) 25 µm Ni-P foil with open void relief on the working face, held under N₂, ready for trim and bonding.

---

## 2. Definitions and interpretation

- **Reactions.** Zn + 2 NaOH + 2 H₂O → Na₂[Zn(OH)₄] + **H₂↑**; ZnO + 2 NaOH + H₂O → Na₂[Zn(OH)₄]. The zinc reaction evolves hydrogen (see §3); the ZnO reaction does not.
- **Geometry.** The carrier holds the smooth outer nickel face. NaOH attacks from the exposed Zn reverse: it removes the foil, then reaches and dissolves the ZnO tips from behind, clearing them out of the nickel cavities. The face that was against the foil becomes the exposed working surface.
- **The slow step is not the foil.** A 70 µm zinc foil dissolves in minutes; **clearing ZnO out of the blind, narrowing nanovoids is diffusion-limited** and is what sets the strip time. Endpoint is complete ZnO removal, not a bare-looking part.
- **Residuals.** APTES leaves with the ZnO. Silver seeds are noble and are **not** dissolved by NaOH, so expect residual Ag on the interior cavity walls — acceptable unless later steps say otherwise. Any residual zincate or NaOH left inside a cavity is a contaminant that will be sealed into the N₂ cavity later, so rinsing must reach into the voids.
- **Aluminium is forbidden in this bath.** Aluminium is amphoteric and dissolves in NaOH (2 Al + 2 NaOH + 6 H₂O → 2 Na[Al(OH)₄] + 3 H₂). The aluminium plate is bonded only **after** this step; it never sees caustic.

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **Hydrogen evolution.** Dissolving the zinc foil liberates flammable H₂ (~0.2 L per coupon, more in a batch). Work with adequate ventilation, **no ignition sources**, and manage bubble accumulation. Do not strip in a sealed vessel.
- **Sodium hydroxide.** Severe caustic burns and eye hazard; heated solution is worse. Full splash protection: face shield/goggles, caustic-rated gloves and apron; add NaOH to water, never the reverse.
- **PPE:** caustic-resistant gloves, goggles + face shield, apron; fume hood or well-ventilated caustic bench.
- **Solvents (drying).** IPA/ethanol are flammable — keep away from any ignition and from the H₂ source.
- **Waste:** the spent bath is hot alkaline **zincate** (dissolved Zn in caustic) and off-gasses H₂ while active. Collect separately; **keep far from all acid streams** (violent neutralisation, Zn re-precipitation); neutralise carefully and dispose per local regulations.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents

- Sodium hydroxide (NaOH), technical/ACS.
- Deionised water, Type I/II.
- Isopropanol (IPA) or ethanol, for solvent-exchange drying.
- Optional: very dilute mild acid (e.g. ~1 % acetic) for a neutralising rinse, used with caution.
- Dry nitrogen for drying and inert hold.

### 4.2 Equipment

- **Caustic-proof temporary carrier** holding the plated face and exposing the Zn reverse. Acceptable materials: polypropylene, PTFE/fluoropolymer, or passivated stainless. **Not aluminium, not glass** (hot NaOH slowly etches silica). Mechanical perimeter clamp preferred (releasable, caustic-tolerant).
- Heated caustic-rated strip vessel (PP/PTFE or SS), with mild-to-moderate agitation (mechanical or recirculation) and a loose cover; ventilated bench/hood.
- Cascade DI rinse station; optional low-power ultrasonic bath.
- Drying capability: N₂ blow-off and gentle warm dry as baseline; **critical-point (CO₂) dryer or freeze-dryer available** for fragile/residue-prone cases.
- N₂ hold/storage for finished parts; PTFE-tipped tweezers; SEM/EDS access for QC.

---

## 5. Specifications

### 5.1 Strip bath

| Parameter | Specification | Notes / tolerance |
|---|---|---|
| NaOH concentration | 2–4 M (~80–160 g/L) | start at 2 M; higher = faster but harder on Ni-P |
| Temperature | 40–55 °C | start ~45 °C; warm aids ZnO clearing from voids |
| Agitation | continuous, mild–moderate | feeds fresh solution into voids; sweeps H₂ bubbles |
| Carrier | caustic-proof, perimeter clamp | holds outer Ni face; exposes Zn reverse |
| Endpoint | complete ZnO removal (voids clear) | qualify by SEM/EDS — **not** just foil gone |
| Time | qualify on first runs | foil in minutes; void clearing is the long pole (tens of min → ~1 hr+) |

> **Qualify Ni-P resistance.** Confirm on witness coupons that the high-P Ni-P survives the chosen concentration/temperature/time without thinning or pinholing. Use the mildest conditions that still fully clear the voids; do not over-etch.

### 5.2 Rinse

| Parameter | Specification | Notes |
|---|---|---|
| Method | copious flowing DI, cascade/multiple exchanges | flush zincate + NaOH out of the blind voids |
| Agitation | mild; optional brief low-power ultrasonic | ultrasonic with caution — can dislodge the foil/features |
| Endpoint | effluent neutral (pH ~7), Zn-free | verify before drying |
| Optional | very dilute mild-acid neutralising rinse | brief; then DI again; use with caution on Ni-P |

### 5.3 Dry

| Parameter | Specification | Notes |
|---|---|---|
| Baseline | solvent exchange DI → IPA, then evaporate under N₂ | IPA lowers surface tension → less capillary stress in voids |
| Escalation | critical-point (CO₂) or freeze-dry | if SEM shows residue, trapped liquid, or feature damage |
| Finish | gentle warm dry under N₂ | avoid oxidation of the fresh nickel void surface |
| Prerequisite | rinse must be clean **first** | evaporating a dirty rinse leaves salt residue in the voids |

---

## 6. Procedure

### 6.1 Carrier mounting (before strip)

1. Mount the plated coupon in the caustic-proof carrier so the outer (smooth) nickel face is held/protected and the bare Zn reverse face is exposed to the bath.
2. Clamp the perimeter. Note that the clamped border seals out the etchant, so zinc will remain trapped there — treat that border as **sacrificial trim area** outside the active zone.
3. Confirm no aluminium is present anywhere on the fixture.

### 6.2 Caustic strip

1. Bring the NaOH bath to temperature (start ~45 °C, 2 M) and confirm.
2. Immerse the carried coupon, Zn face to the solution. Expect immediate H₂ evolution as the foil dissolves.
3. Hold with continuous mild-to-moderate agitation. Once the foil is gone, continue to drive complete ZnO removal from the voids — this is the rate-limiting phase; exchange or refresh solution as needed.
4. Pull a witness coupon (or inspect) to confirm the voids are fully cleared of ZnO before stopping. Record time and conditions.
5. Withdraw promptly at endpoint; minimise over-etch of the Ni-P.

### 6.3 Rinse / neutralisation

1. Transfer immediately to flowing DI; run several cascade exchanges with agitation to flush zincate and NaOH out of the voids.
2. (Optional) brief very-dilute mild-acid rinse to neutralise residual caustic, then DI again — use cautiously.
3. Verify the rinse effluent is neutral (pH ~7) and Zn-free before proceeding. Do not let the part dry with rinse liquid still in the voids.

### 6.4 Dry

1. Solvent-exchange the rinse water for IPA (DI → IPA soak/exchange).
2. Evaporate under N₂; finish with a gentle warm N₂ dry.
3. If SEM later shows residue, trapped liquid, or deformed features, switch this batch to critical-point (CO₂) or freeze-drying.

### 6.5 Recovery and hold

1. Keep the foil on its carrier for support; handle only by the carrier/edge.
2. Move the clean, dry part to N₂ hold to protect the fresh nickel void surface from oxidation until edge trim and Al bonding.
3. Label with run ID, strip conditions, and drying method.

---

## 7. Process control and endpoint

- **Endpoint is void clearance, not foil loss.** Drive and verify complete ZnO removal from the tapered voids (SEM/EDS for residual Zn/O), since the narrow apexes clear last.
- **Minimise over-etch.** Use the mildest concentration/temperature that clears the voids in a reasonable time to protect the Ni-P.
- **Agitation / solution exchange** are the levers for the diffusion-limited void clearing; increase them before increasing concentration or temperature.
- **Manage H₂:** keep ventilation adequate and bubbles swept; trapped bubbles both shield the surface and mechanically stress the thinning membrane.

---

## 8. Acceptance criteria and QC

- **Template fully removed:** SEM shows clean hollow void cavities; EDS shows no residual Zn/O beyond expected residual Ag on cavity walls.
- **Ni-P intact:** no thinning, pitting, or perforation; 25 µm preserved; foil coherent and not curled.
- **Voids clean and dry:** no salt residue, no trapped liquid, no capillary-collapsed features (SEM).
- **Chemistry cleared:** rinse effluent neutral and Zn-free; no caustic residue.
- **Handling state:** flat, carrier-supported, held under N₂.

---

## 9. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Residual ZnO in void apexes | Diffusion-limited clearing incomplete → more agitation/solution exchange, longer time, slightly warmer; verify by SEM. |
| Ni-P thinned / pitted / perforated | Over-etch or too-aggressive bath → lower concentration/temperature, shorten to true endpoint; qualify Ni-P resistance. |
| Foil curls after release | High deposit stress → address upstream (confirm high-P in ZnO-SOP-030). |
| Salt residue in voids after drying | Rinse incomplete before drying → extend cascade rinse; verify neutral, Zn-free effluent first. |
| Collapsed / deformed void features | Capillary damage on evaporative drying → solvent-exchange; escalate to critical-point/freeze-dry. |
| Carrier attacked / dissolving | Wrong carrier material → use PP/PTFE/passivated SS; never aluminium or glass. |
| Foil torn / dislodged | Over-vigorous agitation/ultrasonic, or trapped H₂ → gentler handling; sweep bubbles. |

---

## 10. Waste and storage

- Collect the spent alkaline zincate bath and its rinses separately as caustic heavy-metal (Zn) waste; **keep away from all acid streams**; neutralise carefully (exothermic, Zn re-precipitation) and dispose per local regulations.
- Vent H₂ safely while the bath remains active; do not seal active waste.
- Segregate flammable solvent (IPA) waste from the strip and its H₂ source.
- Store finished foils on-carrier, clean, dry, under N₂, labelled with run ID and strip/dry conditions.

---

## 11. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | ____________ | Initial release — selective NaOH strip of Zn/ZnO, carrier-supported, with void-safe clean/dry. |
|  |  |  |  |
