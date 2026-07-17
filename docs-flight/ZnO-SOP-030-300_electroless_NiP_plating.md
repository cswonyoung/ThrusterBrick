<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-030` Rev 2.1.** The plating
> **chemistry, two-bath split, per-litre loadings, temperatures, per-area plating
> rates, and the 25 µm total thickness target are identical** to the 150 mm
> procedure — only the **substrate blank, vessel, bath volume, reagent masses, and
> fixtures** scale with the larger wafer. All dimensions come from
> `300mm-datum-reference.md`; this SOP does not restate them independently.

---

# Working Procedure & Specification

## Two-Step Electroless Nickel-Phosphorus Plating of Seeded ZnO Nanotips (300 mm)
### Mid-P near-neutral strike + High-P acid bulk — 25 µm total

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-030-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 2.1) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-020-300 (APTES + Ag seeding) | Next step | ZnO-SOP-040-300 (caustic strip / release) |

---

## 1. Purpose and scope

This procedure deposits a two-layer electroless nickel-phosphorus (Ni-P) coating onto the seeded ZnO nanotip surface, building a coherent, low-stress metal replica that will later be released as a free-standing foil. Plating proceeds in two baths:

- **Step 1 — mid-P, near-neutral, low-temperature strike.** Gentle initiation on the Ag seeds that fully covers the amphoteric ZnO/Zn substrate before it can be attacked.
- **Step 2 — high-P, low-pH, high-temperature bulk.** Builds the majority of the thickness as a corrosion-resistant, low-stress, amorphous layer that survives the downstream NaOH strip and stays flat when freed.

**Target:** 25 µm total nickel thickness (~2–3 µm Step 1 + balance Step 2), one face only. *(Thickness is diameter-independent — unchanged from the 150 mm line.)*

**Substrate:** Ag-seeded ZnO nanotips on zinc foil, **0.15 mm × ⌀306 round blank** (⌀280 active area, backing a 300 mm silicon wafer — see `300mm-datum-reference.md`), mounted in a carrier that masks the reverse face; from ZnO-SOP-020-300.

**Output:** a 25 µm Ni-P-coated coupon ready for temporary-carrier mounting and the NaOH strip.

---

## 2. Definitions and interpretation

- **Phosphorus is set by pH.** In hypophosphite-reduced Ni-P, lower bath pH gives higher co-deposited phosphorus. Hence Step 1 (near-neutral) yields mid-P (~5–8 %) and Step 2 (acidic) yields high-P (~10–12 %). This is the mechanism behind the two-bath split, not an incidental difference.
- **Strike-then-bulk.** Step 1 exists to protect the substrate: it must be **continuous and pinhole-free** before Step 2, because the low-pH, high-temperature Step 2 bath would attack any exposed ZnO or Zn. Do not enter Step 2 until Step 1 coverage is confirmed. *(Over the larger ⌀280 field, verify coverage across the whole face, not just the centre — see §6.3 and §8.)*
- **Autocatalytic transfer.** Once Step 1 lays down a nickel surface, Step 2 plates directly onto that nickel (electroless Ni is autocatalytic). Only a rinse and, if needed, a brief re-activation are required between baths — no re-seeding.
- **Why high-P for the bulk.** High-P Ni-P is amorphous, low internal stress (so the freed foil does not curl), and broadly corrosion-resistant. Its resistance to the specific NaOH strip conditions must still be **qualified experimentally** (see ZnO-SOP-040-300); keep the strip minimal.
- **Stabiliser — bismuth.** The Step 2 stabiliser is trace bismuth(III), the established lead-free route used in ELV/RoHS-compliant commercial EN baths, replacing lead acetate (and the thiourea fallback, itself a suspected carcinogen). Bi performs the same catalytic-poison stabilising role at ~0.5–1 ppm but runs a **narrower operating window** than Pb: both under-dose (decomposition risk) and over-dose (poisoned, slow, stressed deposit) are nearer. First-run re-qualification is mandatory (§7).
- **Galvanic caution.** Bare Zn in an electroless bath cements nickel and dissolves zinc. Coverage of the tips by the seeded layer plus prompt Step 1 initiation is the mitigation; keep exposed Zn masked.
- **Loading, not diameter, sizes the bath.** The Ni-P thickness target is diameter-independent, but the *plated area* is ~4.6× the 150 mm coupon. Bath volume must scale with area to hold the same per-litre metal reserve (loading, §5.3) — this is the governing new-at-300 mm constraint on uniform, complete plating.

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **Nickel salts (nickel sulfate)** — carcinogenic by inhalation, skin sensitiser, toxic, aquatic hazard. Avoid dust and aerosols; gloves and eye protection; work over containment. At 300 mm the per-bath nickel-salt mass is ~4× (§5.1a) — weigh and handle the larger charges with proportionate care.
- **Sodium hypophosphite** — can liberate **phosphine (PH₃, highly toxic)** if a bath overheats, decomposes, or is contaminated; run baths in a fume hood, do not overheat, and never let a bath go stagnant/decompose. Dry hypophosphite is an oxidiser-incompatible fire risk. Note the bismuth stabiliser's narrower window makes decomposition-margin qualification (§7) part of the phosphine-risk control. **The larger ~8–12 L bath heats more slowly and less evenly (§4.2/§7); a local hot spot decomposes a bath — control and map temperature before trusting a big charge.**
- **Bismuth stabiliser (trace)** — bismuth salts are markedly lower-toxicity than the lead they replace and are not classified carcinogens; still handle the stock with normal chemical hygiene and dose by micro-addition. The nitric- or lactic-acid stock solution is corrosive/irritant.
- **Hot acidic bath (Step 2, 85–90 °C, pH ~4.5)** — burn and fume hazard; fume hood; vented, loosely covered vessel. The 300 mm bath is ~4× larger and heavier (~8–12 kg of hot solution) — use a stable, well-supported vessel and safe lifting practice.
- **Hydrogen** — evolved at the plating surface; keep ventilated, no ignition sources.
- **PPE:** nitrile gloves, safety goggles, lab coat; all baths in a fume hood.
- **Waste:** nickel- and phosphite-bearing solutions are regulated heavy-metal waste (Step 2 additionally carries trace Bi — still segregated, but lead-free). Collect spent baths and rinses separately by bath; **volumes are ~4× the 150 mm line — size collection accordingly.** Do not drain-dispose; treat/dispose per local regulations.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents

**Common:** deionised water (Type I/II), dilute H₂SO₄ and dilute NaOH for pH adjustment, dilute H₂SO₄ (~2–5 %) for optional inter-stage activation.

**Step 1 (mid-P, near-neutral):**
- Nickel sulfate hexahydrate, NiSO₄·6H₂O
- Sodium hypophosphite monohydrate, NaH₂PO₂·H₂O
- Sodium citrate dihydrate (complexant/buffer)
- Glycine (secondary complexant)

**Step 2 (high-P, acidic):**
- Nickel sulfate hexahydrate, NiSO₄·6H₂O
- Sodium hypophosphite monohydrate, NaH₂PO₂·H₂O
- Lactic acid (complexant)
- Sodium acetate (buffer)
- Stabiliser: bismuth(III) nitrate pentahydrate, Bi(NO₃)₃·5H₂O (M = 485.07 g/mol), dosed from an acidic stock solution (§5.2a) — or a commercial Bi-based EN stabiliser concentrate per its TDS. **Lead acetate and thiourea are not permitted.**

### 4.2 Equipment

- Two dedicated heated baths (hotplate or immersion heater) with stable control, **sized for the larger ~8–12 L charge**; **do not share vessels between Step 1 and Step 2** (dragout cross-contaminates). At this volume prefer a distributed or immersion heater over a single hotplate footprint — **the bigger bath is slower to reach temperature and harder to hold uniform** (see §7); allow extra heat-up time and confirm even temperature across the vessel before loading.
- Calibrated thermometer/thermocouple per bath (place the probe near the coupon, not just at the vessel wall — check for centre-to-edge and top-to-bottom gradients in the larger bath); pH meter.
- Fume hood; loosely covered inert (glass/PP/PTFE) vessels sized to submerge the ⌀306 coupon in its round carrier (carrier outer ⌀350 per `300mm-datum-reference.md`) — **inner ⌀ ~380–410 mm**, ~8–12 L working volume, with clearance.
- Continuous or periodic filtration (1–5 µm), mild **and uniform** agitation (air sparge or gentle mechanical) — even agitation over the whole ⌀280 face matters more at this size (§7).
- Micropipette / micro-burette for stabiliser stock dosing.
- Substrate carrier (ZnO-DR-006-300 bonding/masking set or equivalent) masking the reverse face; PTFE-tipped tweezers; analytical balance able to weigh the larger reagent charges; timer; DI rinse stations sized for the ⌀306 coupon.
- Thickness metrology (XRF or cross-section SEM) and P-content metrology (EDS/XRF), **sampling multiple sites across the ⌀280 field**.

---

## 5. Bath specifications

*(All per-litre loadings, pH, temperatures, deposit P content, per-area rates, and target thicknesses below are **unchanged from the 150 mm line**. Only bath volume and total reagent mass scale — see §5.1a and §5.3.)*

### 5.1 Step 1 — mid-P, near-neutral, low-temperature strike

| Parameter | Specification | Notes / tolerance |
|---|---|---|
| NiSO₄·6H₂O | 28 g/L | nickel source |
| NaH₂PO₂·H₂O | 27 g/L | reducing agent |
| Sodium citrate dihydrate | 18 g/L | complexant + buffer |
| Glycine | 10 g/L | secondary complexant |
| pH | 6.5–7.0 | near-neutral; adjust minimally |
| Temperature | 65–70 °C | "low" temperature step |
| Deposit P content | ~5–8 wt% | mid-P |
| Deposition rate | ~5–8 µm/hr | qualify on first run |
| Target thickness | 2–3 µm | **continuous, pinhole-free cover** |
| Time | ~20–30 min | to target coverage |

> pH adjustment: keep near-neutral with the citrate buffer. **Avoid ammonia and strong caustic** while any ZnO/Zn is still exposed — they attack the substrate. Make only small dilute additions.

### 5.1a Reagent masses by bath volume (representative)

Per-litre loadings are unchanged; total mass scales with the larger volume. Representative charges (scale linearly, mass = g/L × litres):

| Bath volume | NiSO₄·6H₂O (28 g/L) | NaH₂PO₂·H₂O (27 g/L) | Na citrate·2H₂O (18 g/L) | Glycine (10 g/L) |
|---|---|---|---|---|
| 8 L | 224 g | 216 g | 144 g | 80 g |
| 10 L | 280 g | 270 g | 180 g | 100 g |
| 12 L | 336 g | 324 g | 216 g | 120 g |

*(Step 2 masses: NiSO₄·6H₂O 28 g/L, NaH₂PO₂·H₂O 32 g/L, lactic acid 28 g/L, sodium acetate 10 g/L — e.g. for 10 L: 280 g / 320 g / 280 g / 100 g; Bi per §5.2a.)*

### 5.2 Step 2 — high-P, low-pH, high-temperature bulk

| Parameter | Specification | Notes / tolerance |
|---|---|---|
| NiSO₄·6H₂O | 28 g/L | nickel source |
| NaH₂PO₂·H₂O | 32 g/L | higher hypophosphite:Ni → higher P |
| Lactic acid | 28 g/L | complexant |
| Sodium acetate | 10 g/L | buffer |
| Stabiliser (Bi from bismuth nitrate) | ~0.5–1 ppm Bi | trace; micro-dose from acidic stock (§5.2a); narrower window than the former Pb — qualify per §7 |
| pH | 4.5–5.0 | acidic → high P |
| Temperature | 85–90 °C | high temperature |
| Deposit P content | ~10–12 wt% | high-P, amorphous, low stress |
| Deposition rate | ~15–20 µm/hr | qualify on first run |
| Target thickness | ~22 µm | balance to 25 µm total |
| Time | ~70–85 min | to target thickness |

#### 5.2a Bismuth stabiliser stock

Bi(NO₃)₃·5H₂O hydrolyses to insoluble basic salts in plain water — **make the stock acidic**. Representative stock: dissolve 100 mg Bi(NO₃)₃·5H₂O in 100 mL of ~5 % lactic acid (or ~1 M nitric acid) → ~0.43 g Bi/L. **Dose is proportional to bath volume** (the target is ppm, i.e. per-litre): per litre of bath, ~2.3 mL of stock gives 1 ppm Bi and ~1.2 mL gives 0.5 ppm — so a **10 L** Step 2 bath takes ~**23 mL** (1 ppm) or ~**12 mL** (0.5 ppm). Add drop-wise with stirring to the fully made-up, still-cool bath, distributing the addition as you stir so the larger volume mixes evenly; never add solid salt directly. Label and date the stock; remake if any precipitate/cloudiness appears.

### 5.3 Bath operating envelope (both steps)

- **Loading:** ~0.5–1 dm² plated area per litre of bath *(unchanged)*. The ⌀280 active face is **~616 cm² (≈6.16 dm²)** — about **4.6× the 150 mm ⌀130 face (≈1.33 dm²)**.
- **Volume:** size to submerge the round coupon (in its ⌀350 carrier) with clearance **and** to satisfy loading: 6.16 dm² ÷ (0.5–1 dm²/L) ⇒ **~6–12 L; use ~8–12 L per coupon** so a single charge supplies 25 µm without replenishment and stays comfortably inside the loading window. This is the ~4× area scale-up of the 150 mm 1.5–2.5 L charge. Confirm on the first run.
- **Bath-loading caution (new at 300 mm):** the plated area quadrupled but a bath is only as good as its metal reserve. An under-volumed bath depletes nickel/hypophosphite before the ⌀280 field finishes — showing as **thinner deposit toward the last-plated regions and centre-to-edge thickness gradients**. Keep to the loading spec; if reuse or a smaller vessel is unavoidable, plan mid-run replenishment and re-qualify (§7).
- **Agitation:** mild, **uniform, and symmetric** across the whole face; avoid vigorous turbulence over the nanostructure. Over ⌀280 an off-centre sparge or single-sided flow prints as a thickness gradient — distribute agitation (e.g. multiple sparge points or gentle rotation) so every part of the face sees comparable transport.
- **Filtration:** continuous or frequent to prevent nodular roughness; size the filter loop for the larger volume.
- **Temperature uniformity (new at 300 mm):** the larger bath develops thermal gradients more readily; because rate and P content are temperature-sensitive, an uneven bath prints an uneven deposit. Hold the whole working volume within ±2 °C, not just the set point at the probe (§7).

---

## 6. Procedure

### 6.1 Pre-plating preparation

1. Confirm the coupon is seeded and held under N₂ per ZnO-SOP-020-300; inspect for a uniform activated (grey) surface **across the whole ⌀280 field**.
2. Verify the reverse face is masked by the carrier and that cut edges expose minimal bare Zn.
3. Handle only by an edge/rim with PTFE-tipped tweezers; **support the full ⌀306 disc** — the larger coupon is floppier and folds or creases more easily than the 150 mm blank. Do not touch the working face.

### 6.2 Bath make-up (each bath, in order)

1. Dissolve the nickel sulfate in ~80 % of the target DI volume with stirring. *(Larger charges take longer to dissolve fully — stir to complete clarity.)*
2. Add and dissolve the complexant(s)/buffer (citrate + glycine for Step 1; lactic acid + acetate for Step 2).
3. Add the sodium hypophosphite **last**; stir until clear.
4. Step 2 only: micro-dose the bismuth stabiliser stock to ~0.5–1 ppm Bi (§5.2a), drop-wise with stirring, distributing across the larger volume.
5. Adjust pH to the specified range (dilute H₂SO₄ down / dilute NaOH up).
6. Make up to volume; bring to operating temperature — **allow extra heat-up time for the ~8–12 L charge and confirm the whole bath is at temperature and uniform** — then confirm pH and temperature before immersion.

### 6.3 Step 1 — mid-P strike

1. Immerse the carried coupon, working face out, in the 65–70 °C Step 1 bath. Start the timer; **tilt on entry and ensure no bubbles are trapped on the face** — a larger face traps bubbles more easily.
2. Hold with mild, uniform agitation for ~20–30 min to deposit 2–3 µm.
3. Withdraw and rinse in flowing DI. **Confirm continuous, pinhole-free coverage across the whole ⌀280 field** (visual + witness coupon SEM, sampling centre and edge) before proceeding — this is a hold point.

### 6.4 Inter-stage transfer

1. Rinse thoroughly in DI to prevent Step 1 dragout into the Step 2 bath.
2. If the nickel surface has been exposed to air or has sat, briefly activate in dilute (~2–5 %) H₂SO₄ (a few seconds) and rinse, to keep the fresh Ni catalytic. Transfer promptly, supporting the full disc.

### 6.5 Step 2 — high-P bulk

1. Immerse in the 85–90 °C, pH 4.5–5.0 Step 2 bath. Start the timer.
2. Hold with mild, uniform agitation and filtration for ~70–85 min to reach ~22 µm (25 µm cumulative).
3. Monitor temperature (±2 °C, checked across the bath, not just at the wall) and pH; replenish/adjust as the bath drifts (see §7).

### 6.6 Post-plate finish

1. Withdraw and rinse in copious flowing DI, supporting the full ⌀306 disc.
2. Blow dry with N₂.
3. Inspect (see §8). Store the coupon clean, dry, and **flat between clean flat supports**, ready for temporary-carrier mounting and the NaOH strip.

---

## 7. Process control

- **Temperature:** hold each bath within ±2 °C; rate and P content are strongly temperature-sensitive. **At 300 mm this is a whole-volume requirement** — map the larger bath for centre-to-edge and top-to-bottom gradients, use a distributed/immersion heater, and let heat-up complete before loading; a hot spot risks decomposition (phosphine) and a cold zone prints a thin/low-rate patch.
- **pH:** both baths acidify as H⁺ is released during deposition. Monitor and correct into range; in Step 2 (substrate now nickel-covered) dilute NaOH may be used for pH-up, but keep additions small and watch any still-exposed Zn.
- **Uniformity across the ⌀280 field (new at 300 mm):** thickness uniformity is the governing acceptance concern at this size. Drive it with (a) **adequate bath loading** (§5.3 — enough litres/metal reserve for the ~4.6× area), (b) **even, symmetric agitation** over the whole face, and (c) **uniform bath temperature**. Map thickness centre-to-edge on the first runs (§8) and adjust agitation/loading until the field is within tolerance.
- **Stabiliser window (hold point):** the Bi stabiliser runs a narrower stability window than the Pb it replaces. **Before committing a real coupon**, qualify on witness coupons at the chosen Bi level: deposition rate, P content (must hold ~10–12 wt%), deposit stress/flatness (freed witness strip must not curl), and bath decomposition margin (no spontaneous plating over a full run at temperature). Record the qualified Bi dose and hold it.
- **Replenishment / bath life:** track nickel and hypophosphite consumption in metal turnovers (MTO); a single correctly-loaded charge covers one coupon to 25 µm, but the ~4.6× plated area draws ~4.6× the metal per coupon — **confirm the charge is not near depletion at pull**, and qualify bath life before reusing across coupons. Bi is consumed by co-deposition — re-qualify stabiliser level if a bath is reused.
- **Filtration & housekeeping:** filter continuously; never let a bath overheat or stagnate (phosphine and spontaneous decomposition risk — margins are tighter with Bi, so treat any cloudiness as an immediate stop).

---

## 8. Acceptance criteria and QC

- **Total thickness:** 25 µm ± tolerance (XRF or cross-section SEM); Step 1 ~2–3 µm, Step 2 ~22 µm. **Measure at multiple sites across the ⌀280 field (centre, mid-radius, edge)** and report the centre-to-edge spread, not a single point.
- **Phosphorus:** Step 1 ~5–8 wt%, Step 2 ~10–12 wt% (EDS/XRF on witness coupons) — re-verified at the qualified Bi dose.
- **Coverage:** continuous, pinhole-free over the whole seeded ⌀280 face — verified after Step 1 (hold point) and after Step 2, sampling edge as well as centre.
- **Surface:** smooth, no nodules, roughness, or skip-plating.
- **Stress/flatness:** low-stress deposit; confirm the coating does not curl (witness strip or post-strip check) — mandatory on the first Bi-stabilised runs. The larger freed foil shows any residual stress as more visible warp — keep it flat and confirm low stress.
- **Adhesion:** coating well-anchored to the seeded ZnO.
- **First-run gate (300 mm):** cross-field thickness uniformity and complete edge coverage confirmed before releasing the recipe to routine use.

---

## 9. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Skip-plating / bare patches after Step 1 | Weak/uneven seeding or trapped bubbles → re-check ZnO-SOP-020-300; tilt on immersion to ensure full wetting of the larger face. |
| Substrate attacked / pitting in Step 2 | Step 1 cover incomplete (pinholes) → do not enter Step 2 until coverage is confirmed across the whole field; thicken Step 1. |
| **Centre-to-edge thickness gradient** (new at 300 mm) | Uneven agitation, thermal gradient, or under-loaded/depleting bath → distribute agitation symmetrically; map and even out bath temperature; increase bath volume/loading (§5.3) or replenish mid-run. |
| **Thin deposit toward last-plated regions** (new at 300 mm) | Bath under-volumed for the ~4.6× area → increase litres to hold the loading spec; confirm the charge is not near depletion at pull. |
| Slow or stalled deposition | Low temperature, low pH drift, depleted hypophosphite, **or Bi over-dose (poisoning)** → correct temperature/pH; check bath age/loading; verify stabiliser dose against the qualified level. |
| Nodular / rough deposit | Particulates or lost stabiliser → filter; verify Bi dose (the Bi window is narrow — both under- and over-dose show up as deposit defects). |
| Bath cloudiness / spontaneous plating | Bath decomposition (overheated/local hot spot/contaminated/**Bi under-dosed**) → discard safely (phosphine risk); remake, map temperature uniformity, and re-verify stabiliser dosing. |
| Coating curls when freed | Stress too high → confirm high-P (>10 %) in Step 2; check pH/temperature; check Bi not over-dosed (excess stabiliser raises stress). Larger foil shows warp more readily — support flat. |
| Coupon creased / folded in handling | Large floppy ⌀306 coupon unsupported → support the full disc on every transfer; store flat between supports. |
| Dark silver/Ni on foil edges | Galvanic cementation on exposed Zn → improve masking/edge trim. |

---

## 10. Waste and storage

- Collect Step 1 and Step 2 spent baths and their rinses **separately**; both are regulated nickel/phosphite heavy-metal waste (Step 2 carries trace bismuth; the stream is now lead-free). **Volumes are ~4× the 150 mm line — size collection accordingly.** Treat/dispose per local regulations; do not drain-dispose.
- Store nickel sulfate as a toxic/sensitiser, away from incompatibles; keep hypophosphite dry and away from oxidisers; store the Bi stock (acidic) sealed and labelled, away from bases.
- Store finished coupons clean, dry, **flat between flat supports**, and labelled with run ID, measured thickness (with centre-to-edge spread), and P content.

---

## 11. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-030` Rev 2.1.** Substrate scaled to a **0.15 mm × ⌀306 round blank** (⌀280 active ≈6.16 dm², backing a 300 mm wafer per `300mm-datum-reference.md`); bath volume raised to **~8–12 L per bath per coupon** (~4× the 150 mm 1.5–2.5 L charge, to hold the unchanged 0.5–1 dm²/L loading over the ~4.6× active area); vessels to inner ⌀ ~380–410 mm for the ⌀350 carrier; reagent masses re-tabulated per bath volume (§5.1a) and Bi stock dosing restated per-volume (§5.2a); heavier/slower-heating baths, whole-volume temperature mapping, even symmetric agitation, adequate bath loading, cross-field thickness-uniformity QC, and large-floppy-coupon handling/flatness notes added throughout (§2–§9). Cross-references updated to the -300 document set. **Plating chemistry, the two-step mid-P/high-P split, all per-litre loadings, pH, temperatures, per-area deposition rates, and the 25 µm total thickness target are unchanged** — they are chemistry/concentration/area effects independent of coupon diameter. |
