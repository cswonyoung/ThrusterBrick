<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Two-Step Electroless Nickel-Phosphorus Plating of Seeded ZnO Nanotips
### Mid-P near-neutral strike + High-P acid bulk — 25 µm total

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-030 | Revision | 2.0 |
| Effective date | ____________ | Supersedes | Rev 1.0 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-020 (APTES + Ag seeding) | Next step | ZnO-SOP-040 (caustic strip / release) |

---

## 1. Purpose and scope

This procedure deposits a two-layer electroless nickel-phosphorus (Ni-P) coating onto the seeded ZnO nanotip surface, building a coherent, low-stress metal replica that will later be released as a free-standing foil. Plating proceeds in two baths:

- **Step 1 — mid-P, near-neutral, low-temperature strike.** Gentle initiation on the Ag seeds that fully covers the amphoteric ZnO/Zn substrate before it can be attacked.
- **Step 2 — high-P, low-pH, high-temperature bulk.** Builds the majority of the thickness as a corrosion-resistant, low-stress, amorphous layer that survives the downstream NaOH strip and stays flat when freed.

**Target:** 25 µm total nickel thickness (~2–3 µm Step 1 + balance Step 2), one face only.

**Substrate:** Ag-seeded ZnO nanotips on Zn foil, 70 µm × ~100 × 125 mm, mounted in a carrier that masks the reverse face; from ZnO-SOP-020.

**Output:** a 25 µm Ni-P-coated coupon ready for temporary-carrier mounting and the NaOH strip.

---

## 2. Definitions and interpretation

- **Phosphorus is set by pH.** In hypophosphite-reduced Ni-P, lower bath pH gives higher co-deposited phosphorus. Hence Step 1 (near-neutral) yields mid-P (~5–8 %) and Step 2 (acidic) yields high-P (~10–12 %). This is the mechanism behind the two-bath split, not an incidental difference.
- **Strike-then-bulk.** Step 1 exists to protect the substrate: it must be **continuous and pinhole-free** before Step 2, because the low-pH, high-temperature Step 2 bath would attack any exposed ZnO or Zn. Do not enter Step 2 until Step 1 coverage is confirmed.
- **Autocatalytic transfer.** Once Step 1 lays down a nickel surface, Step 2 plates directly onto that nickel (electroless Ni is autocatalytic). Only a rinse and, if needed, a brief re-activation are required between baths — no re-seeding.
- **Why high-P for the bulk.** High-P Ni-P is amorphous, low internal stress (so the freed foil does not curl), and broadly corrosion-resistant. Its resistance to the specific NaOH strip conditions must still be **qualified experimentally** (see ZnO-SOP-040); keep the strip minimal.
- **Stabiliser — bismuth (Rev 2.0).** The Step 2 stabiliser is trace bismuth(III), the established lead-free route used in ELV/RoHS-compliant commercial EN baths, replacing lead acetate (and the thiourea fallback, itself a suspected carcinogen). Bi performs the same catalytic-poison stabilising role at ~0.5–1 ppm but runs a **narrower operating window** than Pb: both under-dose (decomposition risk) and over-dose (poisoned, slow, stressed deposit) are nearer. First-run re-qualification is mandatory (§7).
- **Galvanic caution.** Bare Zn in an electroless bath cements nickel and dissolves zinc. Coverage of the tips by the seeded layer plus prompt Step 1 initiation is the mitigation; keep exposed Zn masked.

---

## 3. Health, safety and environment

Consult the SDS for each reagent before starting. Key hazards:

- **Nickel salts (nickel sulfate)** — carcinogenic by inhalation, skin sensitiser, toxic, aquatic hazard. Avoid dust and aerosols; gloves and eye protection; work over containment.
- **Sodium hypophosphite** — can liberate **phosphine (PH₃, highly toxic)** if a bath overheats, decomposes, or is contaminated; run baths in a fume hood, do not overheat, and never let a bath go stagnant/decompose. Dry hypophosphite is an oxidiser-incompatible fire risk. Note the bismuth stabiliser's narrower window makes decomposition-margin qualification (§7) part of the phosphine-risk control.
- **Bismuth stabiliser (trace)** — bismuth salts are markedly lower-toxicity than the lead they replace and are not classified carcinogens; still handle the stock with normal chemical hygiene and dose by micro-addition. The nitric- or lactic-acid stock solution is corrosive/irritant.
- **Hot acidic bath (Step 2, 85–90 °C, pH ~4.5)** — burn and fume hazard; fume hood; vented, loosely covered vessel.
- **Hydrogen** — evolved at the plating surface; keep ventilated, no ignition sources.
- **PPE:** nitrile gloves, safety goggles, lab coat; all baths in a fume hood.
- **Waste:** nickel- and phosphite-bearing solutions are regulated heavy-metal waste (Step 2 additionally carries trace Bi — still segregated, but lead-free). Collect spent baths and rinses separately by bath; do not drain-dispose; treat/dispose per local regulations.

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

- Two dedicated heated baths (hotplate or immersion heater) with stable control; **do not share vessels between Step 1 and Step 2** (dragout cross-contaminates).
- Calibrated thermometer/thermocouple per bath; pH meter.
- Fume hood; loosely covered inert (glass/PP/PTFE) vessels sized to submerge the 125 mm coupon.
- Continuous or periodic filtration (1–5 µm), mild agitation (air sparge or gentle mechanical).
- Micropipette / micro-burette for stabiliser stock dosing.
- Substrate carrier masking the reverse face; PTFE-tipped tweezers; analytical balance; timer; DI rinse stations.
- Thickness metrology (XRF or cross-section SEM) and P-content metrology (EDS/XRF).

---

## 5. Bath specifications

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

Bi(NO₃)₃·5H₂O hydrolyses to insoluble basic salts in plain water — **make the stock acidic**. Representative stock: dissolve 100 mg Bi(NO₃)₃·5H₂O in 100 mL of ~5 % lactic acid (or ~1 M nitric acid) → ~0.43 g Bi/L. Dosing to 1 ppm Bi in a 1 L bath then takes ~2.3 mL of stock; to 0.5 ppm, ~1.2 mL. Add drop-wise with stirring to the fully made-up, still-cool bath; never add solid salt directly. Label and date the stock; remake if any precipitate/cloudiness appears.

### 5.3 Bath operating envelope (both steps)

- **Loading:** ~0.5–1 dm² plated area per litre of bath.
- **Volume:** size to submerge the coupon with clearance; ~1.0–1.5 L per coupon is typical. A single charge easily supplies 25 µm on one 125 cm² face (~0.28 g Ni) without replenishment.
- **Agitation:** mild and uniform; avoid vigorous turbulence over the nanostructure.
- **Filtration:** continuous or frequent to prevent nodular roughness.

---

## 6. Procedure

### 6.1 Pre-plating preparation

1. Confirm the coupon is seeded and held under N₂ per ZnO-SOP-020; inspect for a uniform activated (grey) surface.
2. Verify the reverse face is masked by the carrier and that cut edges expose minimal bare Zn.
3. Handle only by an edge with PTFE-tipped tweezers; do not touch the working face.

### 6.2 Bath make-up (each bath, in order)

1. Dissolve the nickel sulfate in ~80 % of the target DI volume with stirring.
2. Add and dissolve the complexant(s)/buffer (citrate + glycine for Step 1; lactic acid + acetate for Step 2).
3. Add the sodium hypophosphite **last**; stir until clear.
4. Step 2 only: micro-dose the bismuth stabiliser stock to ~0.5–1 ppm Bi (§5.2a), drop-wise with stirring.
5. Adjust pH to the specified range (dilute H₂SO₄ down / dilute NaOH up).
6. Make up to volume; bring to operating temperature; confirm pH and temperature before immersion.

### 6.3 Step 1 — mid-P strike

1. Immerse the carried coupon, working face out, in the 65–70 °C Step 1 bath. Start the timer; ensure no bubbles are trapped on the face.
2. Hold with mild agitation for ~20–30 min to deposit 2–3 µm.
3. Withdraw and rinse in flowing DI. **Confirm continuous, pinhole-free coverage** (visual + witness coupon SEM) before proceeding — this is a hold point.

### 6.4 Inter-stage transfer

1. Rinse thoroughly in DI to prevent Step 1 dragout into the Step 2 bath.
2. If the nickel surface has been exposed to air or has sat, briefly activate in dilute (~2–5 %) H₂SO₄ (a few seconds) and rinse, to keep the fresh Ni catalytic. Transfer promptly.

### 6.5 Step 2 — high-P bulk

1. Immerse in the 85–90 °C, pH 4.5–5.0 Step 2 bath. Start the timer.
2. Hold with mild agitation and filtration for ~70–85 min to reach ~22 µm (25 µm cumulative).
3. Monitor temperature (±2 °C) and pH; replenish/adjust as the bath drifts (see §7).

### 6.6 Post-plate finish

1. Withdraw and rinse in copious flowing DI.
2. Blow dry with N₂.
3. Inspect (see §8). Store the coupon clean and dry, ready for temporary-carrier mounting and the NaOH strip.

---

## 7. Process control

- **Temperature:** hold each bath within ±2 °C; rate and P content are strongly temperature-sensitive.
- **pH:** both baths acidify as H⁺ is released during deposition. Monitor and correct into range; in Step 2 (substrate now nickel-covered) dilute NaOH may be used for pH-up, but keep additions small and watch any still-exposed Zn.
- **Stabiliser window (Rev 2.0 hold point):** the Bi stabiliser runs a narrower stability window than the Pb it replaces. **Before committing a real coupon**, qualify on witness coupons at the chosen Bi level: deposition rate, P content (must hold ~10–12 wt%), deposit stress/flatness (freed witness strip must not curl), and bath decomposition margin (no spontaneous plating over a full run at temperature). Record the qualified Bi dose and hold it.
- **Replenishment / bath life:** track nickel and hypophosphite consumption in metal turnovers (MTO); a single charge covers one coupon to 25 µm, but qualify bath life before reusing across coupons. Bi is consumed by co-deposition — re-qualify stabiliser level if a bath is reused.
- **Filtration & housekeeping:** filter continuously; never let a bath overheat or stagnate (phosphine and spontaneous decomposition risk — margins are tighter with Bi, so treat any cloudiness as an immediate stop).

---

## 8. Acceptance criteria and QC

- **Total thickness:** 25 µm ± tolerance (XRF or cross-section SEM); Step 1 ~2–3 µm, Step 2 ~22 µm.
- **Phosphorus:** Step 1 ~5–8 wt%, Step 2 ~10–12 wt% (EDS/XRF on witness coupons) — re-verified at the qualified Bi dose.
- **Coverage:** continuous, pinhole-free over the whole seeded face — verified after Step 1 (hold point) and after Step 2.
- **Surface:** smooth, no nodules, roughness, or skip-plating.
- **Stress/flatness:** low-stress deposit; confirm the coating does not curl (witness strip or post-strip check) — mandatory on the first Bi-stabilised runs.
- **Adhesion:** coating well-anchored to the seeded ZnO.

---

## 9. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Skip-plating / bare patches after Step 1 | Weak/uneven seeding or trapped bubbles → re-check ZnO-SOP-020; ensure full wetting on immersion. |
| Substrate attacked / pitting in Step 2 | Step 1 cover incomplete (pinholes) → do not enter Step 2 until coverage is confirmed; thicken Step 1. |
| Slow or stalled deposition | Low temperature, low pH drift, depleted hypophosphite, **or Bi over-dose (poisoning)** → correct temperature/pH; check bath age; verify stabiliser dose against the qualified level. |
| Nodular / rough deposit | Particulates or lost stabiliser → filter; verify Bi dose (the Bi window is narrow — both under- and over-dose show up as deposit defects). |
| Bath cloudiness / spontaneous plating | Bath decomposition (overheated/contaminated/**Bi under-dosed**) → discard safely (phosphine risk); remake and re-verify stabiliser dosing. |
| Coating curls when freed | Stress too high → confirm high-P (>10 %) in Step 2; check pH/temperature; check Bi not over-dosed (excess stabiliser raises stress). |
| Dark silver/Ni on foil edges | Galvanic cementation on exposed Zn → improve masking/edge trim. |

---

## 10. Waste and storage

- Collect Step 1 and Step 2 spent baths and their rinses **separately**; both are regulated nickel/phosphite heavy-metal waste (Step 2 carries trace bismuth; the stream is now lead-free). Treat/dispose per local regulations; do not drain-dispose.
- Store nickel sulfate as a toxic/sensitiser, away from incompatibles; keep hypophosphite dry and away from oxidisers; store the Bi stock (acidic) sealed and labelled, away from bases.
- Store finished coupons clean, dry, and labelled with run ID, measured thickness, and P content.

---

## 11. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | ____________ | Initial release — two-step mid-P/high-P electroless Ni-P to 25 µm total; Pb (or thiourea) stabiliser. |
| 2.0 | __________ | ____________ | Lower-toxicity substitution: lead acetate / thiourea stabiliser replaced by bismuth (~0.5–1 ppm Bi from acidic Bi(NO₃)₃ stock, §5.2a). Narrower-window caution and mandatory first-run re-qualification (rate, P content, stress/flatness, decomposition margin) added to §7. |
