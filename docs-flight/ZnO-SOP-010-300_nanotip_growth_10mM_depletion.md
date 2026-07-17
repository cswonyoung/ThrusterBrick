<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-010` Rev 2.2.** The growth
> **chemistry, temperatures, and target tip geometry are identical** to the 150 mm
> procedure — only the **substrate blank, vessel, and bath volume** scale with the
> larger wafer. All dimensions come from `300mm-datum-reference.md`; this SOP does
> not restate them independently.

---

# Working Bath Procedure & Specification

## Self-Seeded Hydrothermal Growth of ZnO Nanotips on Zinc Foil (300 mm)
### 10 mM Equimolar Zn(NO₃)₂·6H₂O / HMTA — Depletion Run (no post-growth acid etch)

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-010-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 2.2) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Process | ACG / hydrothermal | Deposit face | One side (back masked) |

---

## 1. Purpose and scope

This procedure grows a dense, vertically oriented array of ZnO nanotips on one face of zinc foil by self-seeded aqueous chemical (hydrothermal) growth. A single charge of dilute (10 mM) equimolar zinc nitrate / hexamethylenetetramine solution is held at 90 °C and run to depletion; the declining supersaturation of the depleting bath produces the tapered tips without any post-growth acid treatment.

**Target geometry (per crystal):** base 70–120 nm (measured across the hexagonal flats), height < 300 nm, tapered to a point, densely packed, c-axis vertical. *(Unchanged from the 150 mm line — tip geometry is set by the bath chemistry, not the coupon size.)*

**Substrate:** zinc foil, **0.15 mm thick**, cut as a **⌀306 round blank** (the downstream etch/plate/strip flow defines a **⌀280 active area** inside a **13 mm handling rim**, to back a **300 mm silicon wafer** — see `300mm-datum-reference.md`). Mounted in a carrier that masks the reverse face so growth occurs on one side only.

---

## 2. Definitions and interpretation

- **"Acid etch" (post-growth)** — the tip-sharpening step applied *after* growth — is deliberately omitted here; taper is obtained from bath depletion alone.
- **Light etch (pre-growth)** — a brief, separate dilute-**acetic-acid** dip *before* growth (§6.2) that strips the native oxide and raises nucleation density. It is retained, and is **not** the same step as the omitted post-growth etch.
- **Depletion run:** running the fresh bath until the zinc precursor is spent and no fresh precipitate forms. A single, un-replenished charge self-limits rod height, which is how sub-300 nm height is held.
- **Base diameter:** dimensions are stated face-to-face (across flats). Across corners is ~1.155× larger; fix the across-flats convention for all SEM measurements.

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **Hexamethylenetetramine (HMTA)** — flammable solid; on heating in water it releases formaldehyde and ammonia. Weigh and run in a fume hood.
- **Zinc nitrate hexahydrate** — oxidiser; skin/eye/respiratory irritant. Keep away from combustibles.
- **Dilute acetic acid** (light-etch dip, ~2–5 % v/v) — irritant to eyes and skin at working strength; pungent vapour. Gloves and goggles. The **glacial acetic acid concentrate** used to make dilutions is corrosive and combustible — dilute in a fume hood, and always add acid to water, never water to acid.
- **Hot solution** — the 90 °C aqueous bath is a burn/scald hazard, and at 300 mm the **bath is ~4× larger (4–6 L) and heavier** — use a stable, well-supported vessel and safe lifting practice. Use a loosely covered (vented) vessel; never seal a hot bath and keep ≤ 95 °C to avoid pressure build-up.
- **PPE:** nitrile gloves, safety goggles, lab coat; all HMTA weighing and bath heating in a fume hood.
- **Waste:** the spent bath carries dissolved and particulate zinc (now ~4× the volume). Collect as aqueous heavy-metal waste; do not pour to drain. Neutralise/dispose per local regulations. Spent etch dip carries dissolved zinc acetate — same heavy-metal stream.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents

- Zinc nitrate hexahydrate, Zn(NO₃)₂·6H₂O, ACS grade (M = 297.48 g/mol).
- Hexamethylenetetramine (HMTA), C₆H₁₂N₄, ≥ 99 % (M = 140.19 g/mol).
- Deionised water, Type I/II (≥ 18 MΩ·cm preferred), for bath make-up and rinsing.
- Acetone and isopropanol (IPA), reagent grade, for degreasing.
- Dilute acetic acid, ~2–5 % v/v (≈ 0.35–0.9 M), for the pre-growth light etch; dilute from glacial acetic acid (≥ 99 %) with DI water.
- Dry nitrogen (or clean, oil-free compressed air) for drying.

### 4.2 Equipment

- Hotplate or water/oil bath, stable to 90 ± 2 °C, **sized for the larger 4–6 L charge** (heat-up is slower — allow for it), with a calibrated thermometer/thermocouple in the bath.
- **Wide inert growth vessel** (borosilicate or PP) able to submerge the **⌀306 foil with ~10–20 mm clearance — inner ⌀ ~340–360 mm**, ~4–6 L, with a loose lid/watch-glass cover.
- Substrate carrier that masks the reverse face and holds the **⌀306** foil face-down or tilted 15–45° (a larger, floppier coupon than the 150 mm line — support it fully to keep it flat; see §6.5).
- Analytical balance (0.1 mg), volumetric glassware, PTFE-tipped tweezers, timer, sonicator large enough for the ⌀306 coupon, drying stand.

---

## 5. Bath specification

| Parameter | Specification | Notes / tolerance |
|---|---|---|
| Chemistry | Zn(NO₃)₂·6H₂O + HMTA, equimolar | 1 : 1 molar ratio |
| Concentration | 10 mM each | Dilute — thin bases, low per-rod budget |
| Solvent | Type I/II DI water | ≥ 18 MΩ·cm preferred |
| Zn(NO₃)₂·6H₂O loading | 2.975 g per litre | = 0.010 mol/L × 297.48 g/mol |
| HMTA loading | 1.402 g per litre | = 0.010 mol/L × 140.19 g/mol |
| As-mixed pH | ~5.5–6.5 | Do not adjust; not externally buffered |
| Temperature | 90 °C | Acceptable 88–92 °C; never seal, ≤ 95 °C |
| Agitation | Static (no stirring) | Convection re-feeds supersaturation and blunts tips |
| Charge | Single, un-replenished | Defines zinc budget → self-limited height |
| Run mode | Run to depletion | End when solution clears / no fresh precipitate |
| Typical run time | ~45–90 min | **Calibrate on first run;** record actual time |
| Substrate orientation | Face-down or tilted | Lets homogeneous particles fall clear of the face |

> **Concentration and temperature are unchanged from the 150 mm line** — the per-rod
> zinc budget that sets tip geometry is a *concentration* effect, independent of
> coupon size. The larger coupon simply needs more litres of the same 10 mM bath.

### 5.1 Reagent quantities by bath volume

| Bath volume | Zn(NO₃)₂·6H₂O | HMTA |
|---|---|---|
| 4.0 L | 11.900 g | 5.608 g |
| 5.0 L | 14.875 g | 7.010 g |
| 6.0 L | 17.850 g | 8.412 g |

**Sizing:** use the smallest volume that fully submerges the ⌀306 foil with ~10–20 mm clearance — typically **~4–6 L** in a ~⌀340–360 mm vessel. Scale masses linearly: mass = (2.975 g/L Zn(NO₃)₂ or 1.402 g/L HMTA) × volume in L.

---

## 6. Procedure

### 6.1 Blank the round substrate

Cut the **⌀306 round zinc blank** from 0.15 mm zinc foil stock **before** any cleaning. The cut sits 13 mm outside the ⌀280 active zone, so it never touches the nanostructured area, and the rim it forms is sacrificial (dissolved at the ZnO-SOP-050-300 de-rim) — so edge finish is uncritical. The one spec that matters is that the blank drops cleanly into the carriers' **⌀306.3 locating pocket** (ZnO-DR-003-300 / ZnO-DR-005-300).

1. **Method (in order of preference for a ⌀306 disc):**
   - **Adjustable rotary circle cutter** — set to **153 mm radius** on a backing mat; no tooling, and practical at this larger diameter (a ⌀306 steel-rule die or punch is large and costly). Hand-guided, so verify roundness/diameter.
   - **Custom ⌀306 steel-rule die / hollow punch** — ideal repeatability for batches if the tooling cost is justified; press-driven.
   - *(Laser is acceptable but zinc fume needs extraction.)* **Do not use the CNC router** — it deflects and grabs 0.15 mm foil and throws swarf; the larger, floppier ⌀306 blank is even more prone to this.
2. **Backing:** cut over end-grain wood, a poly cutting board, or a self-healing mat so the blade fully severs the foil without tearing.
3. **Burr:** orient the tool so any burr lands on the **rim** (the sacrificial, de-rimmed side); knock down a burr that would keep the blank from seating.
4. **Fit check:** confirm the blank is round and drops flush into the ⌀306.3 carrier pocket; deburr or retrim if proud. **Flatness:** the larger blank is floppier — keep it flat during handling and store between flat supports.
5. Handle by the rim only; keep the future growth face clean.

### 6.2 Substrate preparation — before-growth cleaning

1. Handle the foil only with PTFE-tipped tweezers by an edge; never touch the growth face. The ⌀306 coupon is large — support the whole disc during transfers so it does not fold.
2. Sonicate 5 min in acetone.
3. Sonicate 5 min in fresh isopropanol.
4. Sonicate 5 min in DI water to remove solvent residue.
5. **Light etch:** dip 15–30 s in dilute acetic acid (~2–5 % v/v) to strip the native oxide and open nucleation sites. **Calibrate the time on the first run** and keep it a controlled parameter; over-etching still thins and roughens the foil.
6. **Immediately** rinse under copious flowing DI water to stop the etch; do not let the freshly etched surface sit in air.
7. Blow dry at once with N₂ (or clean air), sheeting water off the face to avoid spots.
8. Mount in the carrier (reverse face masked) and proceed to growth promptly to minimise native-oxide regrowth.

> **Note — light etch.** Removing the passivating native oxide and slightly roughening the surface raises self-seeded nucleation density and improves uniformity, directly serving the "densely packed" goal. This is the pre-growth activation step only; the post-growth tip-sharpening etch remains omitted. Start at the short end of the dip window and **re-verify nucleation density (base diameter and packing) against §7 on the first qualified run**; if bases come out too sparse, lengthen the dip toward 30 s rather than concentrating the acid.

### 6.3 Bath preparation

1. Charge the vessel with ~90 % of the target DI water volume (4–6 L).
2. Weigh Zn(NO₃)₂·6H₂O and HMTA to the quantities in §5.1; record actual masses.
3. Dissolve the zinc nitrate fully with gentle stirring, then dissolve the HMTA; stir until completely clear.
4. Make up to final volume with DI water. Optionally filter (0.2 µm) to remove stray particulates.
5. Cover and pre-heat the solution to 90 °C — **allow extra time for the larger charge to reach temperature.** Confirm with the in-bath probe before loading the substrate.

### 6.4 Growth run (to depletion)

1. Immerse the carried substrate, growth face down or tilted, into the 90 °C bath. Start the timer (t₀). Ensure no air bubbles are trapped on the face — a larger face traps bubbles more easily, so tilt on entry to sweep them off.
2. Hold at 90 °C, static and loosely covered. Do not stir, agitate, or replenish the bath.
3. Let the run proceed to depletion: the solution turns milky at peak nucleation, then clears as zinc is consumed. Endpoint = a clear (or markedly clarified) bath with no fresh precipitate forming.
4. Record the actual depletion time (expect ~45–90 min on the first calibration run) and the bath temperature profile. **Re-calibrate for this line:** the larger bath and coupon may shift the observed depletion time — treat the first 300 mm run as a fresh calibration.

### 6.5 Recovery — after-growth cleaning

1. At the endpoint, withdraw the substrate promptly, supporting the full ⌀306 disc.
2. Immediately rinse under copious flowing DI water to quench the reaction and float off loosely bound homogeneous particles. Do not wipe or brush the surface.
3. Optional, if loose powder persists: a few seconds of very gentle low-power DI sonication. **Caution** — aggressive sonication dislodges rods; use sparingly and inspect afterward.
4. Blow dry with N₂, holding the foil so water sheets off cleanly; avoid drying spots.
5. Optional consolidation dry: up to ~150–250 °C in air to drive off residual water (gentle ramp; the 0.15 mm foil thickness is unchanged from the 150 mm line, but the **larger ⌀306 disc has more unsupported area and is more warp-prone** — support it flat and ramp gently; stay far below the 419.5 °C zinc melting point). Not required for geometry.
6. Store the finished foil flat between clean flat supports, in a covered container.

---

## 7. Acceptance criteria and QC

- **Visual:** uniform matte white/grey coating over the growth face; no bare patches, no thick powdery cake. Over the larger ⌀280 active area, check uniformity **centre-to-edge** (a bigger face is more prone to edge-to-centre gradients from bath convection).
- **SEM (plan + cross-section) — base** (across flats) 70–120 nm; height < 300 nm; tips tapered to a point; densely packed without coalescing into a film; rods c-axis vertical. Sample **multiple sites across the ⌀280 field**, not just the centre.
- **Process:** spent bath clear at pull; depletion time logged.
- **First-run gate:** nucleation density and base diameter re-verified (acetic-acid etch) and **cross-field uniformity** confirmed before releasing the recipe to routine use.

**Expected first-pass output (10 mM depletion):** base ~60–100 nm, height ~250–380 nm, strong taper, moderate-to-dense. Height may edge over 300 nm; if it does, reduce concentration toward ~8 mM (which depletes sooner and shorter) and re-qualify.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Height > 300 nm | Per-rod zinc budget too high → dilute toward 8 mM; confirm single charge; optionally drop to 88 °C. |
| Bases > 120 nm / merging | Too much lateral growth → lower concentration; verify not double-charged. |
| Bases < 70 nm / sparse | Weak nucleation → lengthen the light etch and/or improve degrease; transfer to the bath promptly after etching. |
| **Centre-to-edge non-uniformity** (new at 300 mm) | Convection gradients over the larger face → keep strictly static and level; ensure even immersion depth; consider a deeper bath so the whole face sees similar hydrostatic/thermal conditions. |
| Blunt / flat tips | Bath not truly depleted, or convection re-fed it → confirm run to clear; keep strictly static. |
| Loose powdery deposit | Excess homogeneous nucleation settling on the face → keep face-down; filter make-up; gentler heat-up. |
| Foil thinned / warped / pitted | Light etch too long or acid too concentrated → shorten the dip; dilute the acid; rinse promptly. Support the large disc flat throughout. |
| Rods detached after rinse | Recovery too aggressive → gentler DI rinse; reduce or eliminate sonication. |

---

## 9. Waste and storage

- Collect spent baths and zinc-bearing rinse water (including the spent acetic etch, now zinc acetate solution) as aqueous heavy-metal waste; neutralise and dispose per local regulations. Do not drain-dispose. Volumes are ~4× the 150 mm line — size your waste collection accordingly.
- Store unused reagents dry and sealed; HMTA away from heat and ignition; zinc nitrate away from combustibles; glacial acetic acid away from oxidisers and bases.
- Store finished substrates flat (between flat supports), dry, covered, and labelled with run ID and depletion time.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-010` Rev 2.2.** Substrate scaled to a **⌀306 round zinc blank** (⌀280 active + 13 mm rim, backing a 300 mm wafer per `300mm-datum-reference.md`); growth vessel to ~⌀340–360 mm / **4–6 L**; reagent-by-volume table re-tabulated for 4–6 L; blanking method favours the rotary circle cutter (153 mm radius) at this diameter; added centre-to-edge uniformity checks and large-floppy-coupon handling/flatness notes. **Growth chemistry, 10 mM concentration, 90 °C temperature, and target tip geometry are unchanged** — they are concentration/temperature effects independent of coupon size. |
