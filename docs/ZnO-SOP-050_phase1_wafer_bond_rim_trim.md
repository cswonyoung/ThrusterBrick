<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Phase-1 Bonding: Nanovoid Foil to Silicon-Wafer Backer, and Rim Trim
### Vacuum-compatible foil-to-wafer die-attach on the bench — polished wafer face preserved as the neighbour's void cap

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-050 | Revision | 4.2 |
| Effective date | ____________ | Supersedes | Rev 4.1 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-040 (strip / clean / dry) | Next step | ZnO-SOP-060 (Phase-2 vacuum stack close) |

---

## 1. Purpose and scope

This procedure performs **Phase 1** of the two-phase assembly: it bonds the freed Ni-P nanovoid foil (high-P face) to the **unpolished back side of a 150 mm silicon wafer**, cures the bond flat and near-isothermally on the bench, then **chemically de-rims** the sacrificial zinc handling rim and gives the voids their **single final deep-clean and capillary-safe dry** (deferred here from ZnO-SOP-040). The output is a **wafer-backed nanovoid cell** whose *working* (mid-P void) face is open and clean and whose *polished* wafer face is pristine — that polished face becomes, in ZnO-SOP-060, the vacuum-facing cap over the **next** cell's working voids.

**What changed at Rev 4.0 (architecture).** The backer is now a **silicon wafer**, not a conversion-coated aluminium plate; the finished stack runs under a **single common vacuum** (ZnO-SOP-060), not an N₂-filled, spacer-gapped, butyl-sealed cell array. Consequently **this SOP no longer creates or protects any butyl seal land.** The two-phase "separate silicone from butyl in time and by fixture" scaffolding of Rev ≤3.2 — the PTFE film mask, the land-cleanliness release gate, the masking carrier — is **withdrawn.** Phase 1 is now a single clean die-attach.

**Governing principles.**
- **Bond direction is the safety principle.** Silicone is metered onto the rigid wafer; the fragile 25 µm foil arrives last and is **laid on, never pressed.**
- **Two clean faces out, bond in the middle.** The bond is Ni **high-P face ↔ wafer rough (back) side.** The two faces that must stay pristine are the Ni **mid-P void face** (stays open) and the wafer **polished (front) face** (stays clean — it is a functional surface, not just a backer).
- **Low-outgassing governs the material choice.** Everything this bond is made of ends up *inside* the vacuum in Phase 2, where it outgasses into the common volume the getter must maintain. Low-outgassing is therefore the controlling silicone requirement (it was thermal conductivity in the aluminium era).
- **CTE discipline.** Ni/Si thermal-expansion mismatch is ≈ 10.8 ppm/°C (α_Ni ≈ 13.4, α_Si ≈ 2.6). Cure **at or near room temperature** and keep the bondline **thin and compliant** so the bonded pair does not bow the brittle wafer bimetallically. Wafer bow is now a measured release parameter.
- **Support transfer via the zinc rim.** The unetched 13 mm zinc rim (from ZnO-SOP-040) tensions the etched centre like a drumhead through transfer; it is removed (by chemical de-rim, §6.5) only after the wafer bond has cured and taken over support.

**Substrate at entry:** clean, dry, rim-framed Ni-P nanovoid foil (mid-P void working face, high-P bond face), held under N₂.

**Output:** a silicon-wafer-backed nanovoid cell — **de-rimmed to the ⌀130 active area, voids finally cleaned and capillary-safe dried**, working face open and clean, **polished wafer face pristine**, wafer bow within budget, held under N₂ — ready for the Phase-2 vacuum close, where it stacks **polished (shiny) Si face down** (the hypothesised thrust direction; ZnO-SOP-060 §6.2).

---

## 2. Definitions and interpretation

- **Wafer backer.** A 150 mm silicon wafer, **polished on one face only**. The **unpolished (back) face** receives the bond; the **polished (front) face** is preserved. Prime/test/reclaim grade is acceptable as long as the polished face meets the cleanliness/flatness gate — this is a mechanical/vacuum part, not a device wafer.
- **Bonding platen / wafer chuck.** A 150 mm vacuum chuck holds the wafer flat, **polished face down on a clean, compliant, particle-free chuck pad** (the pad protects the polished face), rough face up and accessible for bonding. The chuck holds the wafer flat through cure. *(The Rev ≤3.2 rectangular platen + PTFE butyl-land mask of ZnO-DR-006 is superseded for this step; a round wafer-chuck cut-set is part of the deferred DR revision.)*
- **One silicone → one vacuum-grade silicone.** A single **low-outgassing**, RT/addition-cure, dielectric silicone serves the Phase-1 bond. "Low-outgassing" means qualified to **ASTM E595: TML < 1.0 %, CVCM < 0.1 %.** A thermally-conductive low-outgassing grade is *preferred* (it shortens the thermal-drift path for the force test), but outgassing is the pass/fail requirement; thermal conductivity is a tiebreaker.
- **Which faces bond.** Ni **high-P (outer)** face → wafer **rough (back)** side. The Ni **mid-P void face** and the wafer **polished face** both stay open/clean.
- **No butyl lands (Rev 4.0).** There is no butyl anywhere in the Rev 4.0 architecture, so there is no seal land to mask or gate here. Any reference to "butyl lands," "land-cleanliness gate," or the PTFE film mask in earlier revisions does not apply.
- **Polished-face preservation is a release gate.** The wafer's polished front is the Casimir/vacuum cap for the adjacent cell (ZnO-SOP-060). Handle wafers by the edge; protect the polished face on the chuck; a contaminated or scratched polished face fails release.
- **Silver retained** in the void walls by design (ZnO-SOP-040).

---

## 3. Health, safety and environment

- **Silicone adhesive** — SDS; skin/eye irritant; ventilate during cure (addition-cure grades are low-byproduct).
- **Silicon wafer handling** — brittle; fractures to sharp shards. Handle by the edge with wafer tweezers/vacuum wand; eye protection; never point-load or flex a 150 mm wafer.
- **De-rim etch** — **dilute acetic acid** (HCl works but is avoided for vapour/toxicity, per ZnO-SOP-010): irritant. **Evolves H₂ (~2.3 L per cell as the zinc rim dissolves)** — ventilate, no ignition sources, do not seal the vessel. Spares Ni-P / Ag / Si / cured silicone (non-HF acid only). **Solvent dry** (IPA): flammable — no ignition sources.
- **Vacuum chuck** — pinch hazard at the port; keep hands clear.
- **PPE:** gloves, safety glasses, lab coat.
- **Waste:** trimmed rim is **zinc-bearing nickel** — segregate as heavy-metal metal scrap. Broken-wafer scrap → sharps/silicon scrap.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents / consumables

- **Low-outgassing, RT / addition-cure, dielectric silicone** adhesive (ASTM E595: TML < 1.0 %, CVCM < 0.1 %) — thermally-conductive grade preferred. The one Phase-1 silicone.
- **150 mm silicon wafers**, single-side polished, ~625–700 µm typical (SEMI standard 675 µm nominal), polished front / unpolished back; grade per §2.
- Isopropanol; dry nitrogen; particle-free chuck pad / protective film for the polished face.
- **De-rim etchant:** **dilute acetic acid, ~5–10 % v/v** (diluted from glacial acetic acid, ≥99 %; §5.1), zinc-selective; DI water for make-up and the final rinse. (Dilute HCl also dissolves zinc but acetic is preferred — lower toxicity, no vapour, per ZnO-SOP-010.)

### 4.2 Equipment

- **150 mm vacuum wafer chuck / bonding platen** with polished-face protection pad; venturi/pump, valve, gauge.
- Silicone metering/dispense (thin, uniform film).
- De-rim bath + cascade DI rinse station + solvent-exchange (IPA) dry; optional critical-point (CO₂) / freeze dryer for the final capillary-safe dry. (Laser trimmer with a ⌀130-concentric fixture is an acceptable dry alternative to the etch.)
- **Wafer-bow / flatness gauge** (dial indicator on a flat, optical flat, or profilometer) — bow is a QC output now.
- N₂ hold; PTFE-tipped / edge-grip wafer tweezers; SEM/EDS; adhesion coupons.

---

## 5. Specifications

| Parameter | Specification | Notes |
|---|---|---|
| Bonded face | high-P (outer) Ni face → wafer **rough/back** side | mid-P void face and wafer polished face stay open/clean |
| Method | silicone on wafer; foil laid on, not pressed | protects the 25 µm membrane |
| Silicone | low-outgassing (ASTM E595 TML<1.0 % / CVCM<0.1 %), dielectric, RT/addition-cure | thermally-conductive grade preferred; outgassing governs |
| Bondline | ~50–100 µm, uniform, void-free, thin | thin + compliant to limit CTE bow and outgassing volume |
| Cure | RT per silicone spec; **near-isothermal**; vacuum chuck held through cure | limits bimetallic bow of the wafer |
| Wafer bow (post-cure) | within the full-face-contact budget of ZnO-SOP-060 | measured every cell; excessive bow = reject/rework |
| Polished-face cleanliness | pristine, un-scratched, particle-free | **release gate** — it caps the neighbour's voids in Phase 2 |
| Rim removal | **chemical de-rim** — dilute zinc-selective acid, self-stopping at ⌀130 (laser alt.) | after cure; spares Ni-P/Si/silicone; no mechanical cutting on the brittle wafer |
| Final void clean | cascade rinse → ~10 h deep-void DI soak → capillary-safe dry | the deferred SOP-040 clean, done once here post-de-rim |
| Residual Zn (post-de-rim) | none detectable in the active part | EDS |
| Voids (final) | clean, dry, no capillary collapse | SEM; escalate dry to critical-point if needed |

### 5.1 De-rim etchant (dilute acetic acid)

Reaction: **Zn + 2 CH₃COOH → Zn(CH₃COO)₂ + H₂↑.** The dilute acid dissolves the zinc handling rim and spares the high-P Ni-P, the Ag seeds on the void walls, the silicon wafer, and the cured silicone bond.

| Parameter | Specification | Notes |
|---|---|---|
| Acid | dilute acetic acid, **~5–10 % v/v** (≈0.9–1.7 M) | from glacial acetic acid (≥99 %) + DI; start ~10 %, drop toward 5 % if a witness shows Ni-P attack |
| Temperature | RT (optionally 30–40 °C to speed) | warm shortens the dissolve; not required |
| Agitation | mild | feeds fresh acid, sweeps H₂ off the rim |
| Charge | ~0.5–1 L per cell, single | rim ≈ 6.3 g Zn (≈0.10 mol) needs ≈0.19 mol acid; 1 L at 10 % holds ≈1.7 mol → ample excess |
| H₂ | **~2.3 L per cell** | ventilate; no ignition; do not seal |
| Endpoint | rim fully gone; no Zn by EDS | self-stops at the ⌀130 Ni-P boundary; time qualifies on first run (~tens of min; warm/►10 % if slow) |
| Selectivity | spares Ni-P, Ag, Si, cured silicone | confirm Ni-P survival on a witness coupon |

**Make-up (representative):**

| Target v/v | Per 0.5 L | Per 1.0 L |
|---|---|---|
| 5 % acetic | 25 mL glacial + DI to 0.5 L | 50 mL glacial + DI to 1.0 L |
| 10 % acetic | 50 mL glacial + DI to 0.5 L | 100 mL glacial + DI to 1.0 L |

**Always add acid to water.** Scale linearly.

---

## 6. Procedure

### 6.1 Chuck set-up

1. Verify the chuck face and its protection pad are clean and particle-free. Load the wafer **polished face down** onto the pad, rough face up; pull vacuum; confirm seated and flat (gauge).
2. Confirm the wafer's polished face was protected and uncontaminated at load (it will not be accessible again until release).

### 6.2 Silicone application

1. Meter a thin, uniform layer of the low-outgassing Phase-1 silicone onto the wafer's **rough** bond footprint, inboard of a small edge exclusion (keep the extreme wafer edge and the polished face clean).

### 6.3 Lay the foil (never press)

1. Bring the rim-framed foil to the wafer, **high-P face down**, tensioned by its own rim.
2. Lay from one edge across, letting bondline air escape at the advancing front. Do not press.
3. Settle lightly; verify no trapped bubbles in the active area.

### 6.4 Cure and release

1. Cure at room temperature per spec, **near-isothermal**, vacuum chuck held.
2. Release vacuum; lift the bonded cell by the wafer edge.
3. Inspect the **polished wafer face** — clean, un-scratched, particle-free (**release gate**). Measure **wafer bow**; confirm within the ZnO-SOP-060 contact budget.

### 6.5 Chemical de-rim + final void clean

1. **Dissolve the zinc rim.** With the foil now bonded and fully supported by the wafer, remove the ⌀156→⌀130 zinc handling rim in the **dilute acetic-acid etchant of §5.1** (~5–10 % v/v, RT, mild agitation), which dissolves the zinc and spares the high-P Ni-P, the Ag seeds, the cured silicone, and the silicon wafer. The etch self-stops at the ⌀130 Ni-P boundary; no mechanical cutting (the wafer is brittle). Manage H₂ (~2.3 L/cell) — ventilate, no ignition, do not seal. *(Laser trim with a ⌀130-concentric fixture is an acceptable dry alternative.)*
2. **Flush the voids.** The de-rim etchant also acidifies and dissolves any zincate/NaOH left deep in the blind voids from ZnO-SOP-040 — this is why that deep-void clean was deferred to here.
3. **Final rinse — the single deep-void soak.** Cascade-rinse to neutral, then hold a **~10 h static DI soak** to diffuse all residual zincate/salt out of the blind void apexes; refresh the DI at least once; verify effluent neutral and Zn-free.
4. **Final capillary-safe dry.** Solvent-exchange DI → IPA and evaporate under N₂; finish with a gentle warm N₂ dry. If SEM shows residue, trapped liquid, or deformed features, escalate this (single) final dry to critical-point (CO₂) or freeze-drying.
5. Keep etchant and debris off the polished wafer face throughout. Bare silicon at the wafer edge is unharmed by the dilute (non-HF) acid.

### 6.6 Inspect and hold

1. Verify: void-free bond; **no detectable Zn in the active part (EDS)** after de-rim; **voids clean and dry — no salt residue, no trapped liquid, no capillary-collapsed features (SEM)**; working face undamaged; polished wafer face pristine; wafer bow within budget.
2. Hold under N₂, both faces protected. Label with run ID. The cell is now Phase-2-ready.

---

## 7. Acceptance criteria and QC

- **Bond:** continuous, void-free; passes adhesion check; no edge delamination.
- **Silicone grade:** cert confirms ASTM E595 low-outgassing class (TML<1.0 % / CVCM<0.1 %). If the grade changes, re-run one adhesion + one outgassing-relevant coupon before release.
- **Polished wafer face:** pristine, un-scratched, particle-free — **release gate** for Phase 2.
- **Wafer bow:** within the full-face-contact budget of ZnO-SOP-060 (measured).
- **De-rim complete:** zinc rim fully removed; **no detectable Zn in the active part (EDS)**.
- **Working face / voids (final):** open mid-P voids clean, dry, undamaged; no salt residue, trapped liquid, or capillary collapse (SEM).
- **Dimensional:** de-rimmed to the ⌀130 active area; bondline ~50–100 µm uniform.
- **Handling:** wafer-supported, both faces protected, under N₂.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Bondline voids / bubbles | Laid too fast or silicone uneven → lay slower from one edge; meter evenly. |
| Membrane torn during lay-down | Rim tension lost or foil pressed → confirm rim intact; lay, never press; front-side support fallback. |
| Wafer bowed beyond budget | Cure too warm or bondline too thick/stiff (CTE mismatch) → cure nearer RT; thinner, more compliant bondline; verify near-isothermal cure. |
| Wafer cracked | Point load, flex, or debris under the chuck → handle by edge; flat clean chuck/pad; no flexing. |
| Polished face scratched/contaminated | Poor handling or unprotected chuck → protect the polished face on load; re-clean if recoverable, else scrap the wafer (gate). |
| Residual Zn in active part | De-rim etch incomplete → extend the etch to the ⌀130 boundary; re-verify EDS. |
| Voids damaged / capillary-collapsed after final dry | Evaporative stress on delicate voids → escalate the single final dry to critical-point (CO₂) / freeze-dry; verify by SEM. |
| Etchant wicked into / marked the working face | Uncontrolled de-rim exposure → mask the ⌀130 active area or run a rim-only edge etch; rinse promptly (the acid is rinse-able, unlike glue). |
| Wafer edge attacked | Wrong etchant (HF) → use only dilute non-HF acid (acetic/HCl); silicon and cured silicone are spared. |

---

## 9. Waste and storage

- Spent de-rim etchant is **zinc-acetate solution** → collect as aqueous heavy-metal (Zn) waste; do not drain-dispose; neutralise/dispose per local rules. Broken silicon → silicon/sharps scrap. Cured silicone per local rules.
- Store finished cells flat, **both faces protected**, under N₂, labelled.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | ____ | ____ | Initial release (bond-in-carrier concept). |
| 2.0 | ____ | ____ | Out-of-carrier lay-down bond; zinc-rim handling frame. |
| 3.0 | ____ | ____ | Recast as Phase 1 of two-phase assembly: single Phase-1 silicone; butyl-land mask ring in the bonding carrier; land-cleanliness release gate; spacer bedding removed (spacer butyl-bonded in Phase 2). |
| 3.1 | ____ | ____ | Mask ring replaced by 0.005″ PTFE film mask + clamp frame per ZnO-DR-006 (closes O7). |
| 3.2 | ____ | ____ | Cr(VI)-free aluminium conversion coating specified; hex-chrome prohibited. |
| 4.0 | ____ | ____ | **Architecture change: silicon-wafer backer + common-vacuum stack.** Backer changed from conversion-coated aluminium plate to a 150 mm single-side-polished silicon wafer; bond made to the wafer's unpolished back, polished face preserved as the neighbour's void cap. Butyl seal lands, PTFE film mask, and the two-phase silicone/butyl separation **retired** (no butyl in Rev 4.0). Silicone requirement changed from thermally-conductive to **low-outgassing (ASTM E595)** for vacuum service. Added CTE-bow discipline (near-isothermal RT cure, thin compliant bondline) and wafer-bow as a release gate; added brittle-wafer handling. Aluminium conversion-coating content removed. Downstream cut-set/manifest/mirror propagation deferred (see draft note). |
| 4.1 | ____ | Croft Swonyoung | Rim removal changed from mechanical trim to **chemical de-rim** (dilute zinc-selective acid, self-stopping at ⌀130; spares Ni-P/Si/silicone; laser trim as alternative) — no mechanical cutting on the brittle wafer. The **single deep-void soak + capillary-safe dry** (previously in ZnO-SOP-040) now lives here, after the de-rim re-wets the voids; void-cleanliness/dryness/capillary gates moved here from SOP-040. |
| 4.2 | ____ | Croft Swonyoung | Added the **de-rim etchant formulation (§5.1)**: dilute acetic acid ~5–10 % v/v from glacial, RT (opt. 30–40 °C), mild agitation, ~0.5–1 L/cell single charge, with a make-up table and no-Zn-by-EDS endpoint. Noted H₂ (~2.3 L/cell), selectivity (spares Ni-P/Ag/Si/cured silicone), and the zinc-acetate waste stream. Acetic preferred over HCl (lower toxicity, per SOP-010). |
