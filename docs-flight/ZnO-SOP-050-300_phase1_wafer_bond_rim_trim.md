<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-050` Rev 4.2.** The bond
> **chemistry, silicone grade, bondline thickness, cure schedule, de-rim etchant,
> and per-area / per-litre figures are identical** to the 150 mm procedure — only
> the **wafer, bond area, fixture, bath charge, and mass** scale with the larger
> wafer. All dimensions come from `300mm-datum-reference.md`; this SOP does not
> restate them independently.

---

# Working Procedure & Specification

## Phase-1 Bonding: Nanovoid Foil to Silicon-Wafer Backer, and Rim Trim (300 mm)
### Vacuum-compatible foil-to-wafer die-attach on the bench — polished wafer face preserved as the neighbour's void cap

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-050-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 4.2) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-040-300 (strip / clean / dry) | Next step | ZnO-SOP-060-300 (Phase-2 vacuum stack close) |

---

## 1. Purpose and scope

This procedure performs **Phase 1** of the two-phase assembly: it bonds the freed Ni-P nanovoid foil (high-P face) to the **unpolished back side of a 300 mm silicon wafer**, cures the bond flat and near-isothermally on the bench, then **chemically de-rims** the sacrificial zinc handling rim and gives the voids their **single final deep-clean and capillary-safe dry** (deferred here from ZnO-SOP-040-300). The output is a **wafer-backed nanovoid cell** whose *working* (mid-P void) face is open and clean and whose *polished* wafer face is pristine — that polished face becomes, in ZnO-SOP-060-300, the vacuum-facing cap over the **next** cell's working voids.

**Architecture (inherited from the 150 mm Rev 4.0).** The backer is a **silicon wafer**, not a conversion-coated aluminium plate; the finished stack runs under a **single common vacuum** (ZnO-SOP-060-300), not an N₂-filled, spacer-gapped, butyl-sealed cell array. Consequently **this SOP creates no butyl seal land**; there is no PTFE film mask, no land-cleanliness gate, and no masking carrier. Phase 1 is a single clean die-attach.

**What is new at 300 mm.** The bond geometry scales from a **⌀150 wafer / ⌀130 active** to a **⌀300 wafer / ⌀280 active** (`300mm-datum-reference.md` §1), so the **bonded area grows ~4×** and every mass grows ~4×. The wafer is now **0.775 mm thick** (SEMI 300 mm nominal, `300mm-datum-reference.md` §1) and, being larger, is **much heavier (≈128 g bare, `300mm-datum-reference.md` §2) and more fragile in bending** than the 150 mm part. This makes **full-area flat support, bondline uniformity over the larger ⌀280 area, and edge-only handling** the governing practical concerns — see the added notes in §2, §3, §6, and §8. **The chemistry and process are unchanged from the 150 mm line;** only geometry, tooling, bath charge, and mass scale.

**Governing principles.**
- **Bond direction is the safety principle.** Silicone is metered onto the rigid wafer; the fragile 25 µm foil arrives last and is **laid on, never pressed.** (Even more important over ⌀280: a larger membrane is easier to tear.)
- **Two clean faces out, bond in the middle.** The bond is Ni **high-P face ↔ wafer rough (back) side.** The two faces that must stay pristine are the Ni **mid-P void face** (stays open) and the wafer **polished (front) face** (stays clean — it is a functional surface, not just a backer).
- **Low-outgassing governs the material choice.** Everything this bond is made of ends up *inside* the vacuum in Phase 2, where it outgasses into the common volume the getter must maintain. Low-outgassing is therefore the controlling silicone requirement. (The outgassing area is ~4× larger at 300 mm; the getter is sized for it in ZnO-SOP-060-300.)
- **CTE discipline.** Ni/Si thermal-expansion mismatch is ≈ 10.8 ppm/°C (α_Ni ≈ 13.4, α_Si ≈ 2.6). Cure **at or near room temperature** and keep the bondline **thin and compliant** so the bonded pair does not bow the brittle wafer bimetallically. **Bow is more consequential at ⌀300** — the same curvature gives a larger edge deflection over the wider wafer — so near-isothermal cure and a thin, even bondline matter more here. Wafer bow is a measured release parameter.
- **Support transfer via the zinc rim.** The unetched 13 mm zinc rim (from ZnO-SOP-040-300) tensions the etched centre like a drumhead through transfer; it is removed (by chemical de-rim, §6.5) only after the wafer bond has cured and taken over support.

**Substrate at entry:** clean, dry, rim-framed Ni-P nanovoid foil (⌀306 blank: ⌀280 active + 13 mm rim; mid-P void working face, high-P bond face), held under N₂.

**Output:** a silicon-wafer-backed nanovoid cell — **de-rimmed to the ⌀280 active area, voids finally cleaned and capillary-safe dried**, working face open and clean, **polished wafer face pristine**, wafer bow within budget, held under N₂ — ready for the Phase-2 vacuum close, where it stacks **polished (shiny) Si face down** (the hypothesised thrust direction; ZnO-SOP-060-300 §6.2).

---

## 2. Definitions and interpretation

- **Wafer backer.** A **300 mm silicon wafer, 0.775 mm thick** (`300mm-datum-reference.md` §1), **polished on one face only**. The **unpolished (back) face** receives the bond; the **polished (front) face** is preserved. Prime/test/reclaim grade is acceptable as long as the polished face meets the cleanliness/flatness gate — this is a mechanical/vacuum part, not a device wafer.
- **Bonding platen / wafer chuck.** A **300 mm vacuum chuck (ZnO-DR-006-300)** holds the wafer flat, **polished face down on a clean, compliant, particle-free chuck pad** (the pad protects the polished face), rough face up and accessible for bonding. **Full-area support is mandatory:** the ⌀300 / 0.775 mm wafer sags and cracks far more readily than the 150 mm part under any point load or unsupported span. The chuck holds the wafer flat through cure. *(The 300 mm wafer-chuck cut-set is ZnO-DR-006-300; note `300mm-datum-reference.md` §3 flags the ⌀300+ aluminium chuck as a heavier cut — no waterjet — to be finalised when the chuck is designed.)*
- **One silicone → one vacuum-grade silicone.** A single **low-outgassing**, RT/addition-cure, dielectric silicone serves the Phase-1 bond. "Low-outgassing" means qualified to **ASTM E595: TML < 1.0 %, CVCM < 0.1 %.** A thermally-conductive low-outgassing grade is *preferred* (it shortens the thermal-drift path for the force test), but outgassing is the pass/fail requirement; thermal conductivity is a tiebreaker. **The grade and cure are unchanged from the 150 mm line;** only the dispensed quantity scales with the ⌀280 area.
- **Which faces bond.** Ni **high-P (outer)** face → wafer **rough (back)** side. The Ni **mid-P void face** and the wafer **polished face** both stay open/clean.
- **No butyl lands.** There is no butyl anywhere in this architecture, so there is no seal land to mask or gate here.
- **Polished-face preservation is a release gate.** The wafer's polished front is the Casimir/vacuum cap for the adjacent cell (ZnO-SOP-060-300). Handle wafers by the edge; protect the polished face on the chuck; a contaminated or scratched polished face fails release. **At ⌀300 the polished face is a much larger area to keep particle-free** — cleanroom discipline and a full-face protective film matter more.
- **Uniform bondline over ⌀280 (new emphasis at 300 mm).** The bondline must stay **bubble-free and even in thickness across the full ⌀280 area**, roughly four times the 150 mm bond area. A larger span is more prone to trapped air, edge-to-centre thickness variation, and starved corners — all of which drive wafer bow and outgassing volume. Uniformity of the bondline is a first-class release concern here.
- **Silver retained** in the void walls by design (ZnO-SOP-040-300).

---

## 3. Health, safety and environment

- **Silicone adhesive** — SDS; skin/eye irritant; ventilate during cure (addition-cure grades are low-byproduct).
- **Silicon wafer handling** — brittle; fractures to sharp shards. **The 300 mm / 0.775 mm wafer is heavier (≈128 g) and much more fragile in bending than the 150 mm part** — support the **whole** face at all times, handle by the edge with a **large-format wafer wand / edge-grip tweezers**, never point-load or flex it, and never lift or carry it on an unsupported span. Eye protection; two-hand or wand transfer for the larger disc.
- **De-rim etch** — **dilute acetic acid** (HCl works but is avoided for vapour/toxicity, per ZnO-SOP-010-300): irritant. **Evolves H₂ (~9 L per cell as the ~4× larger zinc rim dissolves)** — ventilate, no ignition sources, do not seal the vessel. Spares Ni-P / Ag / Si / cured silicone (non-HF acid only). **Solvent dry** (IPA): flammable — no ignition sources.
- **Vacuum chuck** — pinch hazard at the port; keep hands clear. Larger chuck / heavier wafer — mind fingers on load and release.
- **PPE:** gloves, safety glasses, lab coat.
- **Waste:** trimmed rim is **zinc-bearing nickel** — segregate as heavy-metal metal scrap (~4× the mass of the 150 mm rim). Broken-wafer scrap → sharps/silicon scrap.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents / consumables

- **Low-outgassing, RT / addition-cure, dielectric silicone** adhesive (ASTM E595: TML < 1.0 %, CVCM < 0.1 %) — thermally-conductive grade preferred. The one Phase-1 silicone. **Provision ~4× the per-cell quantity of the 150 mm line** (≈5 g/cell over the ⌀280 bond, `300mm-datum-reference.md` §2) — the grade is unchanged.
- **300 mm silicon wafers**, single-side polished, **0.775 mm nominal** (SEMI 300 mm standard; `300mm-datum-reference.md` §1), polished front / unpolished back; grade per §2.
- Isopropanol; dry nitrogen; **large-format** particle-free chuck pad / protective film sized for the ⌀300 polished face.
- **De-rim etchant:** **dilute acetic acid, ~5–10 % v/v** (diluted from glacial acetic acid, ≥99 %; §5.1), zinc-selective; DI water for make-up and the final rinse. (Dilute HCl also dissolves zinc but acetic is preferred — lower toxicity, no vapour, per ZnO-SOP-010-300.) **Concentration is unchanged; the per-cell charge scales ~4× with the larger rim (§5.1).**

### 4.2 Equipment

- **300 mm vacuum wafer chuck / bonding platen (ZnO-DR-006-300)** with full-face polished-face protection pad; venturi/pump, valve, gauge. Must support the whole ⌀300 wafer flat.
- Silicone metering/dispense (thin, uniform film) able to lay an **even, bubble-free bondline over the full ⌀280 area** — a larger sweep than the 150 mm line.
- De-rim bath + cascade DI rinse station + solvent-exchange (IPA) dry; optional critical-point (CO₂) / freeze dryer for the final capillary-safe dry. **Bath / rinse / soak vessels sized for the ⌀306 cell** (larger tanks, ~4× charge volume; §5.1, §6.5). (Laser trimmer with a ⌀280-concentric fixture is an acceptable dry alternative to the etch.)
- **Wafer-bow / flatness gauge** with **⌀300 travel/aperture** (dial indicator on a flat, optical flat, or profilometer) — bow is a QC output now, and edge deflection is read over the wider wafer.
- N₂ hold; large-format PTFE-tipped / edge-grip wafer tweezers or wand; SEM/EDS; adhesion coupons.

---

## 5. Specifications

| Parameter | Specification | Notes |
|---|---|---|
| Wafer / active | ⌀300 wafer (0.775 mm) → ⌀280 active | per `300mm-datum-reference.md` §1 |
| Bonded face | high-P (outer) Ni face → wafer **rough/back** side | mid-P void face and wafer polished face stay open/clean |
| Method | silicone on wafer; foil laid on, not pressed | protects the 25 µm membrane over the larger span |
| Silicone | low-outgassing (ASTM E595 TML<1.0 % / CVCM<0.1 %), dielectric, RT/addition-cure | thermally-conductive grade preferred; outgassing governs; grade unchanged from 150 mm |
| Bondline | ~50–100 µm, uniform, void-free, thin | thin + compliant to limit CTE bow and outgassing volume; **evenness over ⌀280 is a release concern** |
| Cure | RT per silicone spec; **near-isothermal**; vacuum chuck held through cure | limits bimetallic bow of the wafer; matters more over the wider ⌀300 |
| Wafer bow (post-cure) | within the full-face-contact budget of ZnO-SOP-060-300 | measured every cell; excessive bow = reject/rework |
| Polished-face cleanliness | pristine, un-scratched, particle-free | **release gate** — it caps the neighbour's voids in Phase 2 |
| Rim removal | **chemical de-rim** — dilute zinc-selective acid, self-stopping at ⌀280 (laser alt.) | after cure; spares Ni-P/Si/silicone; no mechanical cutting on the brittle wafer |
| Final void clean | cascade rinse → ~10 h deep-void DI soak → capillary-safe dry | the deferred SOP-040-300 clean, done once here post-de-rim; soak time is void-geometry-limited (unchanged) |
| Residual Zn (post-de-rim) | none detectable in the active part | EDS |
| Voids (final) | clean, dry, no capillary collapse | SEM; escalate dry to critical-point if needed |

### 5.1 De-rim etchant (dilute acetic acid)

Reaction: **Zn + 2 CH₃COOH → Zn(CH₃COO)₂ + H₂↑.** The dilute acid dissolves the zinc handling rim and spares the high-P Ni-P, the Ag seeds on the void walls, the silicon wafer, and the cured silicone bond. **Acid concentration is identical to the 150 mm line; only the per-cell charge and the H₂ volume scale ~4× with the larger ⌀306→⌀280 rim.**

| Parameter | Specification | Notes |
|---|---|---|
| Acid | dilute acetic acid, **~5–10 % v/v** (≈0.9–1.7 M) | from glacial acetic acid (≥99 %) + DI; start ~10 %, drop toward 5 % if a witness shows Ni-P attack; **unchanged from 150 mm** |
| Temperature | RT (optionally 30–40 °C to speed) | warm shortens the dissolve; not required |
| Agitation | mild | feeds fresh acid, sweeps H₂ off the rim |
| Charge | ~2–4 L per cell, single | rim ≈ 26 g Zn (≈0.40 mol) needs ≈0.80 mol acid; ~4 L at 10 % holds ≈7 mol → ample excess |
| H₂ | **~9 L per cell** | ~4× the 150 mm rim; ventilate; no ignition; do not seal |
| Endpoint | rim fully gone; no Zn by EDS | self-stops at the ⌀280 Ni-P boundary; time qualifies on first run (~tens of min; warm/►10 % if slow) |
| Selectivity | spares Ni-P, Ag, Si, cured silicone | confirm Ni-P survival on a witness coupon |

**Make-up (representative):**

| Target v/v | Per 2.0 L | Per 4.0 L |
|---|---|---|
| 5 % acetic | 100 mL glacial + DI to 2.0 L | 200 mL glacial + DI to 4.0 L |
| 10 % acetic | 200 mL glacial + DI to 2.0 L | 400 mL glacial + DI to 4.0 L |

**Always add acid to water.** Scale linearly (the per-litre make-up is unchanged from the 150 mm line; only the charge volume grows).

---

## 6. Procedure

### 6.1 Chuck set-up

1. Verify the **300 mm chuck (ZnO-DR-006-300)** face and its full-area protection pad are clean and particle-free. Load the wafer **polished face down** onto the pad, rough face up; pull vacuum; confirm seated and flat across the full ⌀300 (gauge). **Support the whole wafer during load** — never let the ⌀300 / 0.775 mm disc bridge an unsupported gap.
2. Confirm the wafer's polished face was protected and uncontaminated at load (it will not be accessible again until release).

### 6.2 Silicone application

1. Meter a thin, uniform layer of the low-outgassing Phase-1 silicone onto the wafer's **rough** bond footprint (the ⌀280 area), inboard of a small edge exclusion (keep the extreme wafer edge and the polished face clean). **Over the larger ⌀280 area, aim for an even film with no starved centre or edge** — a non-uniform spread here is the main driver of bondline thickness variation and wafer bow at 300 mm.

### 6.3 Lay the foil (never press)

1. Bring the rim-framed foil to the wafer, **high-P face down**, tensioned by its own rim.
2. Lay from one edge across, letting bondline air escape at the advancing front. Do not press. **The larger ⌀280 span traps air more easily** — advance the wetting front slowly and steadily so trapped bubbles are swept out ahead of it.
3. Settle lightly; verify no trapped bubbles anywhere in the active area (inspect centre-to-edge over the full ⌀280 field).

### 6.4 Cure and release

1. Cure at room temperature per spec, **near-isothermal**, vacuum chuck held. Keep the whole ⌀300 wafer supported and thermally uniform through cure (edge-to-centre thermal gradients bow the wider wafer more).
2. Release vacuum; lift the bonded cell by the wafer edge, **supporting the full disc** (it is now a heavier, larger pair).
3. Inspect the **polished wafer face** — clean, un-scratched, particle-free (**release gate**). Measure **wafer bow** across the full ⌀300; confirm within the ZnO-SOP-060-300 contact budget.

### 6.5 Chemical de-rim + final void clean

1. **Dissolve the zinc rim.** With the foil now bonded and fully supported by the wafer, remove the ⌀306→⌀280 zinc handling rim in the **dilute acetic-acid etchant of §5.1** (~5–10 % v/v, RT, mild agitation), which dissolves the zinc and spares the high-P Ni-P, the Ag seeds, the cured silicone, and the silicon wafer. The etch **self-stops at the ⌀280 Ni-P boundary**; no mechanical cutting (the wafer is brittle — even more so at 0.775 mm / ⌀300). Manage H₂ (~9 L/cell) — ventilate, no ignition, do not seal. *(Laser trim with a ⌀280-concentric fixture is an acceptable dry alternative.)*
2. **Flush the voids.** The de-rim etchant also acidifies and dissolves any zincate/NaOH left deep in the blind voids from ZnO-SOP-040-300 — this is why that deep-void clean was deferred to here.
3. **Final rinse — the single deep-void soak.** Cascade-rinse to neutral, then hold a **~10 h static DI soak** to diffuse all residual zincate/salt out of the blind void apexes; refresh the DI at least once; verify effluent neutral and Zn-free. **The soak time is set by void geometry (unchanged from 150 mm); only the tank / DI charge scales ~4× by volume/area** to cover the ⌀280 field.
4. **Final capillary-safe dry.** Solvent-exchange DI → IPA and evaporate under N₂; finish with a gentle warm N₂ dry. If SEM shows residue, trapped liquid, or deformed features, escalate this (single) final dry to critical-point (CO₂) or freeze-drying. **Any bath in this deep-void clean scales by volume/area** for the larger cell; the exchange chemistry and dry method are unchanged.
5. Keep etchant and debris off the polished wafer face throughout. Bare silicon at the wafer edge is unharmed by the dilute (non-HF) acid.

### 6.6 Inspect and hold

1. Verify: void-free, **uniform bondline over the full ⌀280 area**; **no detectable Zn in the active part (EDS)** after de-rim; **voids clean and dry — no salt residue, no trapped liquid, no capillary-collapsed features (SEM)**; working face undamaged; polished wafer face pristine; wafer bow within budget over ⌀300.
2. Hold under N₂, both faces protected, **flat and fully supported** (the larger, heavier pair sags if edge-stored). Label with run ID. The cell is now Phase-2-ready.

---

## 7. Acceptance criteria and QC

- **Bond:** continuous, void-free, **uniform in thickness across the ⌀280 field**; passes adhesion check; no edge delamination.
- **Silicone grade:** cert confirms ASTM E595 low-outgassing class (TML<1.0 % / CVCM<0.1 %). If the grade changes, re-run one adhesion + one outgassing-relevant coupon before release.
- **Polished wafer face:** pristine, un-scratched, particle-free — **release gate** for Phase 2 (larger area to keep clean).
- **Wafer bow:** within the full-face-contact budget of ZnO-SOP-060-300 (measured over the full ⌀300 — edge deflection is read over the wider wafer).
- **De-rim complete:** zinc rim fully removed to the ⌀280 boundary; **no detectable Zn in the active part (EDS)**.
- **Working face / voids (final):** open mid-P voids clean, dry, undamaged; no salt residue, trapped liquid, or capillary collapse (SEM); sample multiple sites across the ⌀280 field.
- **Dimensional:** de-rimmed to the ⌀280 active area; bondline ~50–100 µm uniform.
- **Handling:** wafer-supported over the full face, both faces protected, under N₂.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Bondline voids / bubbles | Laid too fast or silicone uneven → lay slower from one edge; meter evenly. **More likely over the ⌀280 span — advance the wetting front slowly and sweep air ahead of it.** |
| Membrane torn during lay-down | Rim tension lost or foil pressed → confirm rim intact; lay, never press; front-side support fallback. The larger ⌀280 membrane is easier to tear — extra care. |
| Wafer bowed beyond budget | Cure too warm or bondline too thick/stiff/uneven (CTE mismatch) → cure nearer RT; thinner, more compliant, **more uniform** bondline; verify near-isothermal cure. Bow shows a larger edge deflection over ⌀300 — tighten cure uniformity. |
| Wafer cracked | Point load, flex, unsupported span, or debris under the chuck → handle by edge, **fully support the ⌀300 / 0.775 mm disc**; flat clean chuck/pad; no flexing. The larger, thin wafer is markedly more fragile. |
| Polished face scratched/contaminated | Poor handling or unprotected chuck → protect the (larger) polished face on load; re-clean if recoverable, else scrap the wafer (gate). |
| Uneven / thick-then-thin bondline across the wafer (new emphasis at 300 mm) | Starved spread or non-flat support over ⌀280 → meter an even film to the full active area; confirm full-face chuck flatness; re-spread before laying the foil. |
| Residual Zn in active part | De-rim etch incomplete → extend the etch to the ⌀280 boundary; re-verify EDS. |
| Voids damaged / capillary-collapsed after final dry | Evaporative stress on delicate voids → escalate the single final dry to critical-point (CO₂) / freeze-dry; verify by SEM. |
| Etchant wicked into / marked the working face | Uncontrolled de-rim exposure → mask the ⌀280 active area or run a rim-only edge etch; rinse promptly (the acid is rinse-able, unlike glue). |
| Wafer edge attacked | Wrong etchant (HF) → use only dilute non-HF acid (acetic/HCl); silicon and cured silicone are spared. |

---

## 9. Waste and storage

- Spent de-rim etchant is **zinc-acetate solution** (~4× the 150 mm volume per cell) → collect as aqueous heavy-metal (Zn) waste; do not drain-dispose; neutralise/dispose per local rules. Broken silicon → silicon/sharps scrap. Cured silicone per local rules.
- Store finished cells flat, **both faces protected and fully supported**, under N₂, labelled. The larger, heavier pair must not be edge-stored or allowed to sag.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | ____ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-050` Rev 4.2.** Scaled geometry only: wafer ⌀150→**⌀300** (thickness 0.675→**0.775 mm**), active ⌀130→**⌀280**, coupon/rim ⌀156→**⌀306**, per `300mm-datum-reference.md`; **bond area ~4×** and all masses ~4× (≈128 g wafer, ≈5 g silicone, `300mm-datum-reference.md` §2); vacuum chuck / bonding platen to **ZnO-DR-006-300**; de-rim per-cell charge **~2–4 L** and H₂ **~9 L/cell** (rim ≈26 g Zn), make-up table re-tabulated for 2–4 L; final deep-void soak / clean tanks scaled by volume/area. Cross-references updated to the **-300** line (ZnO-SOP-040-300 predecessor, ZnO-SOP-060-300 next step, ZnO-DR-006-300 chuck, ZnO-SOP-010-300 acid rationale). Added 300 mm-specific handling notes (heavier, more fragile 0.775 mm wafer → full-area support, flatness, edge-only handling), bondline-uniformity-over-⌀280 emphasis, and matching troubleshooting rows. **The bond chemistry, silicone grade (ASTM E595 low-outgassing), ~50–100 µm bondline, near-isothermal RT cure, de-rim acid concentration (5–10 % v/v acetic), per-litre / per-area figures, and target results are unchanged** — they are material/chemistry effects independent of wafer size; only geometry, tooling, bath charge, and mass scale. |
