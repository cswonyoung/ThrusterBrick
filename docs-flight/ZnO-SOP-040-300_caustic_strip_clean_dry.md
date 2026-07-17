<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-040` Rev 1.3.** The strip
> **chemistry, NaOH concentration, temperatures, per-litre loadings, and the
> two-stage division of labour are identical** to the 150 mm procedure — only the
> **coupon, vessel, bath charge, reagent/waste volumes, fixtures, and H₂/zincate
> load** scale with the larger wafer. All dimensions come from
> `300mm-datum-reference.md`; this SOP does not restate them independently.

---

# Working Procedure & Specification

## Caustic Strip (Zinc / ZnO Removal) and Cleaning-Drying of the Ni-P Nanovoid Foil (300 mm)
### Selective NaOH release of the template, leaving a clean, dry, free-standing nickel replica

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-040-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 1.3) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-030-300 (electroless Ni-P) | Next step | ZnO-SOP-050-300 (Phase-1 wafer bond & rim trim) |

---

## 1. Purpose and scope

This procedure dissolves the zinc foil and the ZnO nanotip template out from under the electroless Ni-P coating using sodium hydroxide, freeing a self-supporting nickel foil that carries the former tips as open, tapered nanovoids. It then rinses and dries those nanovoids so the working surface is clean, residue-free, and ready for edge trimming and bonding to the silicon wafer backer.

**Selectivity is the whole idea:** NaOH dissolves Zn and ZnO (both amphoteric) and largely spares the high-P Ni-P.

**Substrate at entry:** a 25 µm Ni-P coating (from ZnO-SOP-030-300) still backed by its ZnO tips and **0.15 mm Zn foil**, cut as a **⌀306 round blank** with a **⌀280 active area** inside a **13 mm handling rim** (see `300mm-datum-reference.md`), held in a temporary caustic-proof carrier that supports the plated (outer) nickel face and exposes the bare Zn reverse face to the bath.

**Output:** a free-standing (carrier-supported) 25 µm Ni-P foil, **bulk-caustic-free and bond-face-clean, gently dried** for handoff to bonding. The **final deep-void clean and capillary-safe dry are deferred to ZnO-SOP-050-300**, after its chemical de-rim re-wets the voids — so the extreme rinse-soak and any critical-point drying happen once, at the end, not twice. The strip endpoint (ZnO fully cleared from the voids) is still met and verified here.

---

## 2. Definitions and interpretation

- **Reactions.** Zn + 2 NaOH + 2 H₂O → Na₂[Zn(OH)₄] + **H₂↑**; ZnO + 2 NaOH + H₂O → Na₂[Zn(OH)₄]. The zinc reaction evolves hydrogen (see §3); the ZnO reaction does not. **At 300 mm the ⌀280 active area is ~4.6× the 150 mm ⌀130 area, so the total H₂ and zincate liberated per coupon scale ~4.6× — see the safety call-out in §3.**
- **Geometry.** The carrier holds the smooth outer nickel face. NaOH attacks from the exposed Zn reverse: it removes the foil, then reaches and dissolves the ZnO tips from behind, clearing them out of the nickel cavities. The face that was against the foil becomes the exposed working surface.
- **The slow step is not the foil.** Even in this deliberately dilute bath the **0.15 mm zinc foil** dissolves in roughly an hour; **clearing ZnO out of the blind, narrowing nanovoids is diffusion-limited** and is what sets the strip time. The zinc thickness is **unchanged from the 150 mm line (0.15 mm)**, so the foil phase is still ~1 hr; the rate-limiting void-clearing is fixed by the void geometry (ZnO-SOP-010-300), **not** by the coupon diameter or the backing thickness. Endpoint is complete ZnO removal, not a bare-looking part.
- **Two-stage clean (from Rev 1.3).** This SOP does the *strip* (full ZnO void clearing — unavoidable, verified here) plus a *bulk* clean sufficient to bond: a cascade rinse to neutral that removes all **active caustic** (so no NaOH rides into the bond to attack the silicon wafer), and a gentle baseline dry. The *deep-void* contaminant soak and any capillary-safe / critical-point drying are **deferred to ZnO-SOP-050-300** — the chemical de-rim there re-wets the voids and even redissolves leftover zincate/NaOH, so doing the extreme clean/dry here too would be wasted effort and extra capillary risk.
- **Residuals.** APTES leaves with the ZnO. Silver seeds are noble and are **not** dissolved by NaOH, so expect residual Ag on the interior cavity walls — acceptable unless later steps say otherwise. Any residual zincate or NaOH left inside a void is a contaminant that will be sealed into the evacuated stack later (and would outgas into the common vacuum), so rinsing must reach into the voids.
- **No aluminium or silicon in this bath.** Aluminium is amphoteric and dissolves in NaOH (2 Al + 2 NaOH + 6 H₂O → 2 Na[Al(OH)₄] + 3 H₂); silicon is likewise etched by hot NaOH. The **silicon wafer backer** (ZnO-SOP-050-300) is bonded only **after** this step, so it never sees caustic — the same rule that kept the old aluminium plate out.

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **Hydrogen evolution (scaled up at 300 mm).** Dissolving the zinc foil liberates flammable H₂ — now **~3.7 L per coupon** (≈4.6× the 150 mm coupon's ~0.8 L: the same 0.15 mm zinc over the larger ⌀280 active area), and proportionally more in a batch. The larger strip vents **~4.6× the hydrogen over a larger open bath**, so treat ventilation and ignition control as a first-order safety item at this scale: work with generous ventilation (size extraction for the larger evolution, not the old coupon), **no ignition sources anywhere near the bench**, and actively manage bubble accumulation across the wider face. **Never strip in a sealed vessel** — a covered-but-vented vessel only; the larger gas volume makes an unvented head-space genuinely dangerous.
- **Sodium hydroxide.** Severe caustic burns and eye hazard; heated solution is worse, and the **~4× larger, heavier charge** raises the splash/lift hazard — use a stable, well-supported vessel and safe lifting practice. Full splash protection: face shield/goggles, caustic-rated gloves and apron; add NaOH to water, never the reverse.
- **PPE:** caustic-resistant gloves, goggles + face shield, apron; fume hood or well-ventilated caustic bench sized for the larger bath.
- **Solvents (drying).** IPA/ethanol are flammable — keep away from any ignition and from the (now larger) H₂ source.
- **Waste:** the spent bath is hot alkaline **zincate** (dissolved Zn in caustic) and off-gasses H₂ while active; at 300 mm it is **~4× the volume and carries ~4.6× the dissolved zinc**. Collect separately; **keep far from all acid streams** (violent neutralisation, Zn re-precipitation); neutralise carefully and dispose per local regulations. Size waste collection for the larger volume.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents

- Sodium hydroxide (NaOH), technical/ACS.
- Deionised water, Type I/II.
- Isopropanol (IPA) or ethanol, for solvent-exchange drying.
- Optional: very dilute mild acid (e.g. ~1 % acetic) for a neutralising rinse, used with caution.
- Dry nitrogen for drying and inert hold.

### 4.2 Equipment

- **Caustic-proof temporary carrier** sized for the **⌀306 coupon**, holding the plated face and exposing the Zn reverse. Acceptable materials: polypropylene, PTFE/fluoropolymer, or passivated stainless. **Not aluminium, not glass** (hot NaOH slowly etches silica). Mechanical perimeter clamp preferred (releasable, caustic-tolerant). The larger, floppier coupon needs full-perimeter support to stay flat (see §6.1).
- **Wide** heated caustic-rated strip vessel (PP/PTFE or SS) able to submerge the ⌀306 carried coupon with clearance — a **~4–6 L charge in a ~⌀340–360 mm vessel**, matching the growth-bath footprint — with mild-to-moderate agitation (mechanical or recirculation) and a loose cover; ventilated bench/hood sized for the larger H₂ evolution.
- Cascade DI rinse station able to flow over the ⌀306 part; optional low-power ultrasonic bath large enough for the coupon.
- Drying capability: N₂ blow-off and gentle warm dry as baseline, with **fixtures/stands sized for the ⌀306 disc**; **critical-point (CO₂) dryer or freeze-dryer available** for fragile/residue-prone cases (its chamber must accept the larger coupon — a constraint that lands mainly at the ZnO-SOP-050-300 final dry, where the capillary-safe escalation actually runs).
- N₂ hold/storage sized for the larger part; PTFE-tipped tweezers; SEM/EDS access for QC.

---

## 5. Specifications

### 5.1 Strip bath

| Parameter | Specification | Notes / tolerance |
|---|---|---|
| NaOH concentration | 0.2–0.4 M (~8–16 g/L) | start at 0.2 M — deliberately dilute; ~10× slower strip than a 2 M bath (roughly first-order in OH⁻) but gentler on the Ni-P. **Per-litre loading unchanged from the 150 mm line** |
| Temperature | 40–55 °C | start ~45 °C; warm aids ZnO clearing from voids. Held constant so the slow-down comes from concentration alone |
| Agitation | continuous, mild–moderate | feeds fresh solution into voids; sweeps H₂ bubbles (more bubbles to sweep across the wider face) |
| Carrier | caustic-proof, perimeter clamp | holds outer Ni face; exposes Zn reverse; full support for the ⌀306 coupon |
| Bath charge / refresh | size for the ~4.6× zinc load; refresh before OH⁻ depletes | the ⌀280 active area × 0.15 mm zinc is **~4.6× the 150 mm coupon's zinc mass** → ~4.6× zincate + OH⁻ consumption; a too-small dilute charge saturates and stalls the void-clearing tail. Use the larger ~4–6 L vessel |
| Endpoint | complete ZnO removal (voids clear) | qualify by SEM/EDS — **not** just foil gone |
| Time | qualify on first runs (SEM endpoint) | foil still **~1 hr** (0.15 mm Zn, thickness unchanged); void clearing is the long pole (**~10–12 hr+** at 0.2 M), set by the void geometry (ZnO-SOP-010-300), **not** by coupon diameter or foil thickness — **do not scale this time with the larger coupon** |

> **Void-clearing time is diameter-invariant.** The ~10–12 h deep-void clearing is set by diffusion through the *nanovoid* geometry, which is identical to the 150 mm line. It does **not** get longer because the coupon is larger — the wider coupon just has more voids clearing in parallel, all on the same per-void clock. Size the *bath charge* up (~4.6× zinc), but keep the *time* the same.

> **Qualify Ni-P resistance.** Confirm on witness coupons that the high-P Ni-P survives the chosen concentration/temperature/time without thinning or pinholing. Use the mildest conditions that still fully clear the voids; do not over-etch.

### 5.2 Rinse

| Parameter | Specification | Notes |
|---|---|---|
| Method | copious flowing DI, cascade/multiple exchanges | flush zincate + NaOH out of the blind voids; scale the rinse volume/flow to the larger part |
| Agitation | mild; optional brief low-power ultrasonic | ultrasonic with caution — can dislodge the foil/features |
| Extended soak | **deferred to ZnO-SOP-050-300** (post-de-rim final clean) | the ~10 h deep-void diffusion soak is done once, after the de-rim re-wets the voids — not here |
| Endpoint (here) | bulk effluent neutral (pH ~7); no active caustic | removes bulk caustic to protect the Si wafer at bond; deep-void Zn is cleared at the SOP-050-300 final clean |

### 5.3 Dry

| Parameter | Specification | Notes |
|---|---|---|
| Baseline (here) | brief solvent exchange DI → IPA, then evaporate under N₂ | just enough to hand off dry to bonding; IPA lowers capillary stress. Use dry fixtures sized for the ⌀306 disc |
| Critical-point / freeze | **deferred to ZnO-SOP-050-300** final dry | the capillary-safe escalation is applied once, after the de-rim, if SEM then shows it (confirm the dryer chamber accepts the larger coupon) |
| Finish | gentle warm dry under N₂ | avoid oxidation of the fresh nickel void surface; support the larger disc flat while drying |
| Note | some deep-void residual may remain | acceptable here — redissolved and cleared at the SOP-050-300 de-rim + final clean |

---

## 6. Procedure

### 6.1 Carrier mounting (before strip)

1. Mount the plated **⌀306 coupon** in the caustic-proof carrier so the outer (smooth) nickel face is held/protected and the bare Zn reverse face is exposed to the bath. Support the full disc — the larger coupon is floppier and must be kept flat so it seats evenly and the clamp seals all round.
2. Clamp the perimeter. Note that the clamped border seals out the etchant, so zinc will remain trapped there — treat that border (the 13 mm handling rim) as **sacrificial trim area** outside the ⌀280 active zone.
3. Confirm no aluminium is present anywhere on the fixture.

### 6.2 Caustic strip

1. Bring the NaOH bath to temperature (start ~45 °C, 0.2 M) and confirm. Allow extra heat-up time for the larger ~4–6 L charge.
2. Immerse the carried coupon, Zn face to the solution. Expect immediate, vigorous H₂ evolution as the 0.15 mm foil dissolves over ~1 hr — now **~4.6× the H₂ of the 150 mm coupon (~3.7 L total)**, so keep bubbles swept off the wider face and the bench strongly vented, with no ignition source nearby.
3. Hold with continuous mild-to-moderate agitation. Once the foil is gone, continue to drive complete ZnO removal from the voids — the rate-limiting phase, still ~10–12 h and **unchanged by the larger coupon**. **Refresh or exchange the dilute bath as the ~4.6× larger zinc load builds zincate**, so OH⁻ depletion does not stall the void-clearing tail.
4. Pull a witness coupon (or inspect) to confirm the voids are fully cleared of ZnO before stopping. Record time and conditions.
5. Withdraw promptly at endpoint; minimise over-etch of the Ni-P.

### 6.3 Rinse / neutralisation

1. Transfer immediately to flowing DI; run several cascade exchanges with agitation to flush the **bulk** zincate and NaOH off the part and out of the open voids. Scale rinse volume to the larger part.
2. Verify the (bulk) rinse effluent is neutral (pH ~7) — **all active caustic must be gone** before bonding, so no NaOH rides into the bond to attack the silicon wafer.
3. **Do not run the ~10 h deep-void soak here** — it is deferred to the ZnO-SOP-050-300 final clean (after the de-rim re-wets the voids). Some residual zincate deep in the blind apexes may remain; that is expected and cleared later.

### 6.4 Dry

1. Solvent-exchange the rinse water for IPA (DI → IPA soak/exchange) and evaporate under N₂; finish with a gentle warm N₂ dry — just enough to hand off dry. Support the ⌀306 disc flat on a sized fixture throughout.
2. **Do not escalate to critical-point / freeze-dry here.** The capillary-safe final dry is applied once, at the ZnO-SOP-050-300 final clean after the de-rim.

### 6.5 Recovery and hold

1. Keep the foil on its carrier for support; handle only by the carrier/edge — the larger disc is more warp-prone unsupported.
2. Move the clean, dry part to N₂ hold to protect the fresh nickel void surface from oxidation until edge trim and wafer bonding.
3. Label with run ID, strip conditions, and drying method.

---

## 7. Process control and endpoint

- **Endpoint is void clearance, not foil loss.** Drive and verify complete ZnO removal from the tapered voids (SEM/EDS for residual Zn/O), sampling **multiple sites across the ⌀280 field**, since the narrow apexes clear last and a larger face is more prone to position-to-position variation.
- **Minimise over-etch.** Use the mildest concentration/temperature that clears the voids in a reasonable time to protect the Ni-P.
- **Agitation / solution exchange** are the levers for the diffusion-limited void clearing; increase them before increasing concentration or temperature — and across the wider face, ensure the exchange is even centre-to-edge.
- **Manage H₂:** keep ventilation adequate for the ~4.6× evolution and bubbles swept; trapped bubbles both shield the surface and mechanically stress the thinning membrane (a bigger membrane is easier to stress).

---

## 8. Acceptance criteria and QC

- **Template fully removed:** SEM shows clean hollow void cavities; EDS shows no residual Zn/O beyond expected residual Ag on cavity walls. Check across the ⌀280 field, not just centre.
- **Ni-P intact:** no thinning, pitting, or perforation; 25 µm preserved; foil coherent and not curled or warped.
- **Bulk chemistry cleared (here):** bulk rinse effluent neutral; no active caustic that could reach the wafer at bond. (Final deep-void Zn/salt clearance is a ZnO-SOP-050-300 gate, post-de-rim.)
- **Bond face:** high-P (bond) face clean and dry, ready for silicone die-attach.
- **Voids:** ZnO fully cleared (SEM/EDS) — the strip endpoint; final void cleanliness/dryness verified after the SOP-050-300 de-rim.
- **Handling state:** flat, carrier-supported, gently dried, held under N₂.

---

## 9. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Residual ZnO in void apexes | Diffusion-limited clearing incomplete → more agitation/solution exchange, longer time, slightly warmer; verify by SEM. (Do **not** assume the larger coupon needs a longer clock — the void clock is geometry-set; look to exchange/refresh first.) |
| Centre-to-edge non-uniform strip (new at 300 mm) | Uneven solution exchange over the wider face → improve agitation/recirculation for even centre-to-edge feed; ensure level, even immersion. |
| Ni-P thinned / pitted / perforated | Over-etch or too-aggressive bath → lower concentration/temperature, shorten to true endpoint; qualify Ni-P resistance. |
| Foil curls or warps after release | High deposit stress and/or larger unsupported area → address stress upstream (confirm high-P in ZnO-SOP-030-300); keep the ⌀306 disc fully supported and flat. |
| Salt residue in voids after drying | Rinse incomplete before drying → extend cascade rinse; verify neutral, Zn-free effluent first. |
| Collapsed / deformed void features | Capillary damage on evaporative drying → solvent-exchange; escalate to critical-point/freeze-dry (at SOP-050-300). |
| Carrier attacked / dissolving | Wrong carrier material → use PP/PTFE/passivated SS; never aluminium or glass. |
| Excess / hazardous H₂ accumulation (amplified at 300 mm) | ~4.6× evolution outpacing ventilation → increase extraction, keep the vessel vented (never sealed), sweep bubbles, remove ignition sources; do not batch more coupons than the ventilation can handle. |
| Foil torn / dislodged | Over-vigorous agitation/ultrasonic, or trapped H₂ → gentler handling; sweep bubbles. |

---

## 10. Waste and storage

- Collect the spent alkaline zincate bath and its rinses separately as caustic heavy-metal (Zn) waste; **keep away from all acid streams**; neutralise carefully (exothermic, Zn re-precipitation) and dispose per local regulations. Volumes and dissolved-Zn load are **~4× / ~4.6× the 150 mm line** — size collection accordingly.
- Vent H₂ safely while the bath remains active; do not seal active waste — the larger charge off-gasses proportionally more.
- Segregate flammable solvent (IPA) waste from the strip and its H₂ source.
- Store finished foils on-carrier, clean, dry, under N₂, labelled with run ID and strip/dry conditions; keep the larger disc flat between supports.

---

## 11. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-040` Rev 1.3.** Coupon scaled to a **⌀306 round blank** (⌀280 active + 13 mm rim, backing a 300 mm wafer per `300mm-datum-reference.md`); strip vessel and NaOH bath charge to the larger **~4–6 L / ~⌀340–360 mm** footprint; carrier, rinse, and dry fixtures sized to the ⌀306 coupon; **H₂ and zincate load ~4.6× (now ~3.7 L H₂/coupon)** with the larger active area — venting/ignition-control raised to a first-order safety item, waste sized ~4×. Cross-references retargeted to the `-300` set (ZnO-SOP-030-300, ZnO-SOP-050-300, ZnO-SOP-010-300). **Strip chemistry, 0.2–0.4 M NaOH, 40–55 °C, per-litre loadings, the ~1 hr foil phase (0.15 mm zinc unchanged), and the two-stage strip/bulk-clean → deferred-final-clean division of labour are unchanged.** The **~10–12 h deep void-clearing time is explicitly held constant** — it is nanovoid-geometry-limited, not diameter-driven, and must **not** be scaled with the larger coupon. |
