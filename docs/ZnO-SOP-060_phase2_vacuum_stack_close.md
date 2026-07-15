<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Phase-2 Stack Close: Wafer-Backed Cells in a Getter-Maintained Common Vacuum
### Zero-gap Ni-void / Si-wafer stack · conformal barrier envelope · atmospheric preload · N cells (recommended N ≤ 117)

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-060 | Revision | 3.3 |
| Effective date | ____________ | Supersedes | Rev 3.2 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-050 (Phase-1 wafer-backed cells) | Next step | Final QC / packaging |
| Variant | Common vacuum · conformal envelope · N cells (≤ 117) | — | — |

---

## 1. Purpose and scope

This procedure performs **Phase 2** of the assembly: **N** wafer-backed cells from ZnO-SOP-050 are stacked **coaxially with no gap**, **each cell polished (shiny) Si face down** so its polished face caps the working voids of the cell below — a getter is added, and the whole stack is enclosed in a **metallized barrier envelope**, evacuated, and heat-sealed so that **atmospheric pressure preloads the stack**. There is no N₂ fill, no spacer, no cavity gap, and no per-interface seal. The entire stack shares **one common vacuum**, maintained for service life by a **getter**.

**Plain-language picture — a vacuum-packed brick.** The finished package is essentially a **vacuum-sealed brick of coffee**: the cells and getter sit inside a flexible metallized (foil-laminate) bag, the air is pumped out, and the bag is **heat-sealed shut** (one-shot — not a reclosable zip). The instant it is vented back to air, ~1 atm shrink-wraps the bag down onto the contents and the whole thing goes **rock-hard**, exactly like an unopened coffee brick — and *that* squeeze is the preload holding every wafer pressed flat against its neighbour. The getter is the little oxygen-absorber sachet, and two rigid end plates spread the ~1 atm as flat, even pressure over the brittle wafers.

**Cell count is a design variable.** Per cell the pitch is ≈ 0.78 mm (wafer 0.675 + Ni-P 0.025 + silicone bond ~0.075). **Recommended maximum N = 117** → a stack ≈ 91 mm tall (still wider than tall) and ≈ 3.7 kg of active cells. Choose N for the force signal you need to resolve and for what you can handle/assemble and fit in the sealer chamber (see §2, §5).

**The governing rules.**
1. **Vacuum, not fill.** All voids share one common vacuum; the seal carries a permanent ~1 atm (~101 kPa) differential, so the hermetic function lives in the outer envelope, never in an inner interface.
2. **Zero gap, mechanical contact.** The working face is **not bonded** to the neighbouring wafer — it is held in intimate contact by atmospheric pressure through the conformal envelope. No adhesive touches the working face.
3. **The getter maintains the vacuum**, sized to N (permeation + outgassing both scale with stack size).
4. **A single common vacuum is a single-point failure** — one envelope breach vents the whole stack; accepted for simplicity/gas-exclusion, mitigated (§2), not eliminated.
5. **Preload exists only after venting.** During assembly, pump-down, and sealing there is **no atmospheric clamping** (see §2, §6.4). A light **silicone-band cartridge** holds the loose stack together until the vent takes over.
6. **Orientation — shiny down.** Every cell is stacked **polished (shiny) Si face down** — the hypothesised thrust direction — so that any always-on thrust presses each cell *into* the stack (self-seating) rather than lifting it off ("popping up"). Harmless if no thrust is present; see §2, §6.2.

**Substrate at entry:** Phase-1 wafer-backed cells (de-rimmed, voids finally cleaned, polished wafer face pristine, bow within budget), aluminium end platens, silicone retaining bands, getter, barrier-envelope stock.

**Output:** a sealed, getter-maintained, common-vacuum N-cell wafer stack, atmospherically preloaded (§5 mass estimate).

> **Ruggedization option (application-agnostic).** This procedure closes the brick **independent of its end use.** A unit that will see **in-service inertial loading at arbitrary orientation** — any dynamic application, e.g. a flying vehicle or the spinning generator rotor — takes two optional features: an inside-envelope silicone **edge-cushion** and an outboard **carrier pot**, sized to that application's design acceleration and specified in **Appendix A**. A **static / bench-measurement** brick omits both. Where a numeric g-load appears (e.g. "128 G"), "G" means multiples of standard gravity (acceleration), never grams.

---

## 2. Definitions and interpretation

- **Contact stack / repeat unit.** All cells face the same way — **polished (shiny) Si down.** Reading a cell top-to-bottom: `working/void face (up) │ Ni foil │ silicone bond │ Si wafer │ polished Si face (down) ══ contact ══ (working/void face of the next cell down) …`. The polished face of each cell caps the working voids of the cell **below** it; every interface is a **mechanical contact**, not a bond.
- **Orientation / thrust axis.** Every cell is oriented **polished (shiny) Si face down.** The hypothesised thrust is toward the polished-Si (capped) side, so the finished stack's thrust axis points toward the shiny faces — *down as assembled* (orient the sealed brick per the test). Building shiny-down means any always-on thrust presses each cell into the stack (self-seating) rather than lifting it off; it is the prudent orientation whether or not a thrust turns out to be present. See §6.2.
- **Conformal barrier envelope.** A heat-sealable **metallized multilayer barrier laminate** (vacuum-insulation-panel grade — e.g. aluminised PET / metal-foil laminate). Under external atmosphere it conforms and presses the evacuated stack together. Sole hermetic boundary.
- **Atmospheric preload — appears at the vent.** Once the sealed bag is vented back to air, ~101 kPa applies a **uniform axial compression**, wringing each polished Si face against the neighbouring void mouths. **Critically, this force does not exist until the vent:** in a chamber sealer the bag is *open* during chamber pump-down, so inside and outside evacuate together and the bag stays limp with **no clamping** the whole way down and through sealing. The preload is a *post-seal, post-vent* event.
- **Assembly cartridge.** To survive handling and pump-down before the preload exists, the stack is built as a self-retaining cartridge: **bottom platen → cells → top platen**, held coaxial by a **lateral registration feature** (posts / ring / locating lip on the bottom platen so the ⌀150 wafers cannot slide) and bundled by **retaining bands** (below). Rigid enough to pick up and set in the bag; superseded by atmospheric preload after the vent.
- **Retaining bands.** **2–3 low-outgassing silicone bands** wrapping the full cartridge height (over the top platen, under the bottom platen), seated in shallow platen-edge notches so they stay off the wafer load path. They give a few newtons — enough to keep the platen-stack-platen a single bundle for handling and pump-down, far below the eventual ~1 atm. They remain **inside** the envelope (low-outgassing silicone; the getter is sized to include their outgassing).
- **End platens.** **1/8″ (3.175 mm) aluminium**, flat (MIC-6 tooling plate or surfaced flat), ⌀ ≥ the wafer (a small overhang shields the brittle wafer edges and anchors the bands). They spread the ~1 atm as uniform axial compression. **Clean/degreased** (they live in the vacuum). If flatness under load proves inadequate for a tall/heavy stack, step up to 1/4″. In the shiny-down build the **bottom platen bears on a polished Si face** and the **top platen on a working (void) face** — keep both platen faces clean and flat.
- **Achievable vacuum (stated honestly).** Bench chamber-sealer + getter gives **rough-to-medium vacuum (~1–100 Pa), durable for years via the getter — not UHV.** At ≤~100 Pa the mean free path exceeds the void size (free-molecular): convection gone, gas effectively excluded.
- **Getter.** General O₂ + H₂O + molecular-sieve (± NEG), **sized to N** (permeation through the envelope and internal outgassing — including the silicone bands and bonds — both scale with stack size), oversized for life, low-dust, restrained.
- **Optional outboard structure.** For ruggedness / a defined external form, an optional **light rigid frame, end-caps, or thin shell** may be added **outboard of the envelope** (never contacting the stack) to help retain preload and protect the package. Keep it light — parasitic mass hurts the force-to-weight ratio the propulsion hypothesis cares about. A full **epoxy pot is possible but discouraged for a static / measurement package**: it must stay strictly outboard of the sealed envelope (epoxy in contact with the stack would wick into the contacts and voids and destroy the mechanism), and it adds substantial dead mass — a light frame beats a solid pot. **Exception — ruggedized (in-service) units:** a brick that must survive service inertial loads at arbitrary orientation (a flying vehicle, or — the bounding case — the 128 G generator rotor) *requires* a carrier pot, not merely an optional frame; the dead mass is unavoidable and is traded for survival. Ruggedization — the inside-envelope **edge-cushion** and the outboard **carrier pot**, both sized to the application's design acceleration — is specified in **Appendix A**.
- **Edge-cushion frame (ruggedized variant, inside envelope).** For units that will see in-service inertial loading, a **pre-cured, die-cut platinum-silicone** cushion wraps the **wafer-stack rim** to protect the brittle wafer edges from dynamic, omnidirectional loads. **Pre-cured sheet only — never painted or dispensed:** liquid silicone would wick by capillary action into the contacts and voids and destroy the mechanism. It touches **only the wafer rim, outboard of the ⌀130 active region**, and is the **same low-outgassing class as the retaining bands** (ASTM E595), so it joins the getter's outgassing budget. Material, geometry, and placement in **Appendix A.1**.
- **Fault tolerance (reduced, by design).** Common vacuum → one breach vents all. Mitigations: robust/defect-free envelope (optionally double-enveloped), generous getter margin, end platens that guard against the likeliest initiator (wafer fracture). Verify the failure mode is a **graceful** slow decay the getter buys time against, not a sudden collapse.
- **No reheat over the stack.** Envelope heat-sealing is confined to the seam, away from the wafers, bands, and cured bonds.

---

## 3. Health, safety and environment

- **Vacuum sealing** — chamber-sealer / seal-bar pinch and implosion hazards are low at this scale; keep hands clear.
- **Silicon wafer handling** — brittle; sharp fracture shards. Edge handling; eye protection; uniform support only.
- **Getter handling** — molecular sieve / desiccant / O₂ scavengers are generally safe; **if a non-evaporable getter (NEG) is used, some grades are reactive/pyrophoric when activated** — handle per SDS, keep sealed until placement.
- **Barrier-film heat-seal** — hot seal bar; burn hazard.
- **PPE:** gloves, safety glasses.
- **Waste:** film, getter, and silicon scrap per local rules.

---

## 4. Materials, reagents and equipment

### 4.1 Components (per N-cell stack, recommended N ≤ 117)

- **N × Phase-1 wafer-backed cells** (ZnO-SOP-050) — de-rimmed, voids finally cleaned, polished wafer face pristine, bow within budget.
- **2 × 1/8″ (3.175 mm) aluminium end platens**, flat (MIC-6 or surfaced), ⌀ ≥ wafer (small overhang for edge protection + band anchor), clean/degreased for vacuum; bottom platen carries the **lateral registration feature** (posts / ring / locating lip).
- **2–3 × low-outgassing silicone retaining bands** (ASTM E595 class), sized to wrap the cartridge over both platens.
- **1 × general getter assembly** — O₂ + H₂O + molecular sieve (± NEG), **sized to N**, oversized, low-dust, restrained.
- **Metallized barrier laminate envelope stock**, heat-sealable (VIP grade); double-envelope stock if redundancy is specified.
- Optional: **light outboard frame / end-caps / shell** (kept outboard of the envelope; see §2).
- **(Ruggedized variant) 1 × pre-cured platinum-silicone edge-cushion set** — die-cut rim strip (+ optional recessed platen end-ring), ASTM E595 low-outgassing, **vacuum-baked before use**; see Appendix A.1. Add its outgassing to the getter sizing.
- **(Ruggedized variant) Carrier / mould + filled low-exotherm potting epoxy** for the outboard pot; see Appendix A.2.

### 4.2 Equipment

- **Chamber vacuum sealer** (or vacuum chamber + heat sealer) capable of the target pressure (~1–100 Pa) **with an internal height that clears the stack + bag** (≈100 mm+ for N near 117); vacuum gauge.
- Registration / alignment fixture for coaxial stacking; flatness fixture.
- **Vacuum-decay / pressure-rise test** capability; optional He leak check on the seam.
- SEM; edge-grip wafer tweezers; particle-controlled staging area.

---

## 5. Specifications

| Element | Specification | Notes |
|---|---|---|
| Stack | **N cells (recommended ≤ 117)**, zero gap, coaxial, contact-preloaded | **every cell shiny-Si-down**; its polished face caps the cell below's voids; thrust toward the shiny (down-as-built) side |
| Per-cell pitch / mass | ≈ 0.78 mm / ≈ 32 g active | wafer 0.675 mm + Ni-P 0.025 mm + bond ~0.075 mm |
| Inner interfaces | **mechanical contact only** — no bond, no gap, no seal | atmospheric-preloaded; nothing wicks into voids |
| Preload | ~101 kPa uniform axial, **applied at the chamber vent (post-seal)** | via conformal envelope + aluminium end platens |
| Assembly retention | 2–3 low-outgassing silicone bands + lateral registration | holds the loose cartridge through handling + pump-down only |
| Edge-cushion (ruggedized variant) | pre-cured platinum silicone, **50 A, 1.0 mm**, E595, vacuum-baked; **rim wrap** | protects wafer edges under in-service loads; inside envelope, off the ⌀130 active area (App. A.1) |
| End platens | 1/8″ (3.175 mm) aluminium, flat, clean; ⌀ ≥ wafer | spread the load; step to 1/4″ if flatness under load fails |
| Vacuum | target **~1–100 Pa**, getter-maintained, durable years | rough–medium, **not UHV** (§2) |
| Getter | general O₂/H₂O + molecular sieve (± NEG), **sized to N** | pumps permeation + outgassing (incl. bands/bonds) |
| Envelope | metallized barrier laminate (VIP grade), continuous heat seal | sole hermetic boundary; optional double-envelope |
| Outboard structure | optional light frame/shell, **outboard of envelope**; **carrier pot for the ruggedized variant** | epoxy pot discouraged for static/bench packages (dead mass); **required for in-service (dynamic) units, sized to the app's g-load (App. A.2)** — always outboard of the stack |
| Fault mode | single common vacuum → one breach vents all | accepted trade; mitigations per §2 |
| Target mass | ≈ N × 32 g active + platens + envelope/getter (**assumption-based**) | see note |

> **Mass estimate (assumptions stated).** Active cell ≈ 32 g (⌀150 wafer 0.675 mm ≈ 27.8 g + ⌀130 Ni-P 25 µm ≈ 3.0 g + ⌀130 bond ≈ 1.3 g). **At N = 117: ≈ 3.7 kg active + ≈ 0.30 kg platens (two 1/8″ Al) + ~0.15 kg envelope/getter/bands ≈ 4.1 kg total.** Recompute for your actual N and wafer thickness.
>
> **Stack-height / count guidance.** The 150 mm wafer diameter keeps the column *wider than tall* out to ~190 cells, and the preload is a pressure (~101 kPa) so it does not weaken with height. There is no sharp structural limit near the recommended N ≤ 117 (~91 mm). The real ceilings are getter sizing, assembly/handling, chamber height, and the measurement: **if the hypothesised force and the mass both scale ~linearly with N, force-to-weight is roughly constant with N** — so more cells give a *bigger absolute force* (easier to resolve, and it aids the balanced-pair null test), not a better levitation ratio.

---

## 6. Procedure

### 6.1 Staging

1. Stage in a particle-controlled area: the N cells, both aluminium platens, silicone bands, getter (kept sealed), envelope stock, alignment fixture.
2. Inspect each cell: working face open/clean, **polished wafer face pristine**, bow within budget, no wafer cracks. Reject failures.

### 6.2 Build the cartridge (zero gap)

1. Place the bottom platen in the alignment fixture, registration feature up. **Keep the assembly axis vertical from here on** — gravity (and, in this orientation, any always-on thrust) seats the slick wafers.
2. Lay cells one at a time in registration, **each cell polished (shiny) Si face DOWN**, its polished face landing on the **working (void) face of the cell below**, coaxial. **No adhesive.** Seat lightly — do not press or slide (sliding scratches the polished cap; the wafers are slippery and shingle easily).

   > **Orientation is not optional.** Shiny-Si-down is the hypothesised thrust direction, so built this way any always-on thrust presses each cell *down into* the stack and self-seats it. Built shiny-**up**, that same thrust would push cells *off* the stack ("popping up") — making assembly impossible. When in doubt: **shiny down.**
3. After each cell, confirm coaxial seating (no rock, no debris). Never slide a landed wafer.
4. Land the top platen on the final cell.
5. **Wrap 2–3 silicone retaining bands** over the top platen, down the sides, under the bottom platen (seated in the platen-edge notches), tensioned to hold the platen-stack-platen as one firm bundle — enough to handle, far below atmospheric preload. The stack is now a **cartridge**.
6. **(Ruggedized variant only)** Fit the pre-cured silicone **edge-cushion rim strip** around the wafer-stack cylinder — over the wafer edges, between the platens, off the ⌀130 active faces — with the splice and vent-notches placed per Appendix A.1. Keep it clear of the retaining-band paths. It rides **under the envelope, inside the vacuum**. Static / bench units skip this step.

### 6.3 Getter placement

1. Place the getter in its vented pocket alongside the cartridge (within the future envelope, clear of contact faces), mechanically restrained so it cannot shift onto a wafer.

### 6.4 Enclose, evacuate, seal (chamber sequence)

1. Enclose the cartridge + getter in the barrier envelope, seam accessible. If double-enveloping, stage the inner envelope now.
2. Place in the chamber sealer, **keeping the cartridge vertical if the chamber allows**. Note that from here until the vent (step 5) there is **no atmospheric clamping** — the silicone-band cartridge is what holds the stack.
3. **Evacuate — start gently.** As the chamber pumps down, air trapped between the near-touching wafers vents out the edges; a violent initial pump can lift or shuffle a loose disc. Ramp the pump so the stack is not disturbed. Pump to the target (~1–100 Pa); hold to confirm stable.
4. **Heat-seal the envelope seam** — continuous, no wrinkles or channels — while under vacuum. Seal the second envelope if used. (The seal bar acts on the mouth/seam, away from the stack.)
5. **Vent the chamber to atmosphere.** ~1 atm now returns *outside* the sealed bag: the envelope draws taut and the preload appears, clamping the stack. The silicone bands are now redundant (they remain inside, low-outgassing).

### 6.5 Verify

1. Confirm **atmospheric preload present**: envelope taut, stack compressed to a firm "brick," platens seated square.
2. Inspect the seam: continuous, no leak channel or wrinkle path.
3. Run the **initial vacuum-decay / pressure-rise check**; record the baseline for life monitoring.
4. Inspect for wafer cracks initiated by preload (through the envelope).
5. If an outboard frame/shell is specified, fit it now (outboard of the envelope, not contacting the stack).

### 6.6 Recovery

1. Label with stack ID, **cell count N**, seal date, getter lot, initial vacuum/decay baseline. Proceed to final QC.

---

## 7. Acceptance criteria and QC

- **Envelope integrity:** continuous seam, no leak channel or pinhole; vacuum-decay / pressure-rise within spec; optional He leak check passes.
- **Vacuum level:** meets the ~1–100 Pa target at seal (gauge, or validated by decay behaviour).
- **Atmospheric preload:** confirmed (taut envelope, compressed stack, platens seated).
- **Cartridge integrity:** stack stayed coaxial through pump-down (no shingling); bands seated, off the load path.
- **Getter margin:** type and capacity documented against the estimated permeation + outgassing load for N and target life.
- **Platens / wafers:** platens flat and clean; no wafer cracks post-preload (inspection).
- **Stack:** coaxial, flat, self-supporting; every working face fully seated on its neighbour's polished cap.
- **Fault mode:** confirm (analysis or test) that an envelope breach produces a **graceful** vacuum decay, not a sudden collapse; document the single-point-failure acceptance.
- **(Ruggedized variant) Edge-cushion:** seated over the full wafer-stack rim, off the ⌀130 active area, vent-notches clear; vacuum-baked lot recorded and added to the getter's outgassing budget (App. A.1).
- **(Ruggedized variant) Carrier pot:** cured **void-free** (tap / CT if available), **strictly outboard of the envelope** (no epoxy ingress, seam intact), CoG within the application's balance/CoG budget; **only a §6.5-verified brick was potted** (the pot is permanent and hides the envelope) (App. A.2).

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Cells lift / pop off during assembly | Built shiny-side-**up** → the always-on thrust points up and unseats them → build **shiny-Si-down** so thrust seats them; verify orientation. |
| Stack shingled / misaligned during pump-down | Loose cartridge or violent pump | tighten/register bands; add/verify the lateral registration; keep axis vertical; ramp the pump gently. |
| Envelope will not hold vacuum | Seam channel / film pinhole / fold leak → re-seal continuous; inspect film; adopt double-envelope; verify seal-bar temperature/dwell. |
| Vacuum decays quickly in service | Getter undersized for N or outgassing high → larger getter; lower-outgassing silicone (bands/bonds); pre-condition/bake components before sealing. |
| Bag not taut after vent | No preload — leak or vacuum not reached → re-check seam and gauge; the bag must go firm at the vent. |
| Wafer cracked under preload | Non-flat platen, edge pinch, or trapped debris → flat full-footprint platens (step to 1/4″ if bowing), platen overhang shields edges, clean staging. |
| Contact not intimate (poor cap seating) | Debris or wafer bow → clean faces; tighten the ZnO-SOP-050 bow and polished-face gates; never slide landed wafers. |
| Polished cap scratched during build | Wafer slid rather than landed → land vertically into registration; no lateral motion once seated. |

---

## 9. Waste and storage

- Barrier film, getter, silicone bands, and silicon scrap per local regulations.
- Store finished stacks flat, protected, labelled; retain seal-date, cell count, getter-lot, and vacuum-decay baseline records per stack for life monitoring.

---

## Appendix A — Ruggedization for in-service (dynamic) applications (edge-cushion + carrier pot)

**Scope — application-agnostic.** SOP-060 closes the brick **independent of end use**; this appendix adds the mechanical ruggedization a unit needs **only if it will experience in-service inertial loading at arbitrary orientation.** The trigger is the *service environment*, not a particular product. Current applications span the load range:

| Application | Design accel. *a_d* | Orientation | Ruggedization |
|---|---|---|---|
| Static / bench / measurement package | ≈ 1 G, fixed | fixed | **None** (baseline brick; optional light frame per §2) |
| Flying vehicle | modest (maneuver + vibration + landing shock) | omnidirectional | **Recommended,** sized to the vehicle's g-envelope |
| Spinning generator rotor | **128 G steady**, sweeping every in-plane direction as the puck rotates on its own axis | omnidirectional | Required — **the bounding case** for current uses |

Two additions do the work: **A.1** a pre-cured silicone **edge-cushion** *inside* the envelope; **A.2** an epoxy **carrier pot** *outboard* of the envelope. Both stay strictly clear of the working faces and voids — the cushion touches only the wafer rim (outboard of the ⌀130 active region); the pot never touches the stack (it encapsulates the *sealed envelope* only).

**Size to your *a_d*.** The material spec below (50 A / 1.0 mm cushion; filled epoxy pot) is written to the **128 G bounding case**, so it is **conservative for any lighter application** — a flying unit may relax durometer, thickness, or pot mass if a load analysis supports it, but the baseline recipe is safe as-is.

**Out of scope here** (separate, application-specific integration procedures): mounting / axles or airframe attachment, CoG-trim, bearings, containment, and any control or safety system particular to the end use. This appendix delivers a **ruggedized puck** plus its **carrier datum and CoG budget**, which the integration step consumes.

### A.1 Edge-cushion silicone

**Why pre-cured sheet, not painted/dispensed.** Uncured silicone has low enough viscosity to wick into micron-scale contacts and into the voids — destroying the mechanism this whole process exists to build. A **cured, die-cut sheet cannot wick.** This is not negotiable.

**Material callout** (hand to a distributor as-is; same low-outgassing class as the retaining bands):

| Property | Spec | Why |
|---|---|---|
| Chemistry | **Platinum (addition) cure**, solid (non-foam) | No tin catalyst, no volatile cure byproducts into the vacuum |
| Durometer | **50 ± 5 Shore A** | Resists extrusion/creep under sustained in-service load, still spreads a silicon edge. 40 A if edges left sharp; 60 A if well-chamfered |
| Thickness | **1.0 mm nominal (±0.1)** | Standoff without bulking the envelope; tight tolerance keeps the puck balanced. 1.5 mm if edges stay sharp |
| Outgassing | **ASTM E595: TML ≤ 1.0 %, CVCM ≤ 0.10 %** | Sealed-vacuum requirement — demand the E595 data sheet |
| Compression set | **ASTM D395-B, ≤ ~15 %** | So it does not take a permanent set under continuous load |
| Temp range | **−50 to +200 °C min** | Covers the potting exotherm (A.2) and service |

**Sources** (all carry platinum-cured sheet; confirm the E595 sheet): **Stockwell Elastomerics** (sheet + in-house die-cutting — single-vendor path), **Specialty Silicone Products (SSP)**, or **NuSil / Avantor** controlled-volatility (CV) grades for the cleanest outgassing.

**Mandatory pre-conditioning.** **Vacuum-bake the cut parts before insertion** (≈200 °C, several hours, under vacuum) to drive out residual volatiles and absorbed moisture. Record the lot; add its outgassing area to the getter sizing (§2, §5).

**Geometry — rim strip (primary) + optional recessed end-ring.** Dimensions parametric in wafer diameter **D = 150 mm**, silicone thickness **s = 1.0 mm**, and measured bonded-stack height **H** (cells only, platen-to-platen interior; H ≈ N × 0.78 mm → ≈ 91 mm at N = 117).

- **Rim strip (primary).** One continuous 1.0 mm layer wrapping the wafer-stack cylinder — protecting every wafer edge at once.
  - Width = **H** (matches the stack height).
  - Length = **π (D + s) + 8 mm** splice overlap ≈ **π (151) + 8 ≈ 482 mm** at ⌀150.
  - **Vent notches** (~1 × 2 mm, ×2–3) on an arc that will **not** be the primary load-bearing direction in service (for the rotor, the arc crossing the spin axis; for an omnidirectional or undefined load, keep the notches minimal and evenly spread) — so the main load-bearing arc stays fully covered while trapped gas still escapes during pump-down.
- **End-face corners.** Handled first by the **aluminium platen overhang** already in the baseline design (§2). For extra margin, an **optional recessed silicone ring** — OD 150, **ID ≥ 134 mm** (stays outboard of the ⌀130 active region), 1.0 mm — may be seated in a **shallow relief groove machined into the platen face.**
  - **Do NOT stack a proud ring in the axial load path.** At only ~101 kPa preload a 1 mm 50 A ring will not compress and would hold the platen off the wafer centre, breaking the zero-gap contact the SOP depends on. Recess it flush, or omit it and rely on the platen overhang.

```
   Cross-section (vertical slice through the spin axis):

      |<--------------------- D = 150 --------------------->|
       _____________________________________________________
      |   platen overhang (+ optional recessed ring in groove)  |
      |_____________________________________________________|
     ||                                                     ||
  R  ||                 wafer stack  (H ≈ 91 @ N=117)       ||  R   ] rim strip
  I  ||          contact interfaces — no gap, no cushion    ||  I     1.0 mm, wraps
  M  ||                    between cells                    ||  M     the cylinder
     ||_____________________________________________________||
      |   platen overhang (+ optional recessed ring in groove)  |
      |_____________________________________________________|
       ^                                                   ^
     rim strip on the load-bearing rim (fore/aft arcs full;
     vent notches only on the top/bottom arcs)
```

**Edge dressing.** The strip is the belt; a **chamfer / dressed edge on the wafers** is the suspenders — under sustained load a sharp silicon corner can cold-flow into the silicone and concentrate stress on a line. With N up to 117 stacked edges the load concentrates, so chamfer where practical or step the strip to 1.5 mm.

**Placement in flow:** fit the rim strip in **§6.2 step 6**, after banding and before enclosing (§6.4). It rides under the envelope, inside the vacuum, and also serves as the compliant **CTE-decoupling layer** between the silicon and the rigid pot (A.2).

### A.2 Carrier pot (outboard)

**Purpose.** Rigidize the flexible brick into a **puck** that survives its service g-load at any angle and carries the application's mounting datum. This **overrides the baseline "epoxy pot discouraged" stance** (§2), which is for static/measurement packages where dead mass hurts force-to-weight; an in-service unit needs the pot and the mass is unavoidable.

**Rules.**
1. **Strictly outboard of the sealed, vented envelope.** The pot encapsulates the *finished brick* (post-§6.5); epoxy never contacts the stack, contacts, or voids.
2. **Pot into a defined carrier / thin-wall mould** so external geometry, mass, and CoG are predictable and the shell carries the mounting features (the datum the application-integration step consumes).
3. **Epoxy = silica/alumina-filled, low-exotherm, slow cure.** The **envelope heat-seal is the thermal weak point** — keep peak exotherm well below its rating; pour in **thin lifts**, heat-sink the mould, **cure cool**.
4. **Vacuum-degas the resin.** Voids are stress concentrators under service loads and shift the CoG unpredictably.

**Procedure.**
1. Confirm the brick passed **§6.5** (preload present, seam sound, decay baseline recorded). **Only pot a verified brick** — the pot is permanent and hides the envelope.
2. Prepare the carrier/mould; place the brick with its **thrust axis (shiny-down) indexed to the carrier datum.**
3. Pour degassed, filled, low-exotherm epoxy in **thin lifts**; degas between lifts; cure cool.
4. Post-cure per the resin data sheet; verify **void-free** (tap test / CT if available) and **CoG within the application's balance/CoG budget.** Hand off to the application-integration procedure.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | ____ | ____ | Initial release. |
| 1.1 | ____ | ____ | Working face = mid-P; seal border on clean Al. |
| 2.0 | ____ | ____ | Recast as Phase 2 of two-phase assembly: plate-by-plate glovebox close; butyl-by-compression; bare-Al spacer; outboard structural skin. |
| 2.1 | ____ | ____ | Bottom end plate clarified as 0.125″ 6061. |
| 2.2 | ____ | ____ | Cr(VI)-free conversion coating flowed to spacer lands. |
| 3.0 | ____ | ____ | **Architecture change: zero-gap common-vacuum stack.** N₂ fill, spacers/gap, butyl seals retired; working face contacts the neighbour's polished Si; hermetic duty in a single metallized barrier envelope; atmospheric preload via end platens; general getter; single-point-failure stated. |
| 3.2 | ____ | Croft Swonyoung | **Corrected cell orientation: polished (shiny) Si face DOWN for every cell** (was working-face-down). The hypothesised thrust is toward the polished-Si side, so shiny-down makes any always-on thrust *self-seat* each cell during assembly instead of lifting it off ("popping up"); the finished stack's thrust axis is toward the shiny faces (down as built). Updated the repeat-unit, governing rules, build procedure (§6.2), specs, platen note, and troubleshooting. |
| 3.1 | ____ | Croft Swonyoung | **Parameterised cell count N** (recommended ≤ 117; per-cell pitch/mass basis; height/force-to-weight guidance). Added the **plain-language "vacuum-packed brick"** description. Specified the **assembly cartridge** (lateral registration + **2–3 low-outgassing silicone retaining bands**) and corrected the procedure to the **chamber pump → seal → vent** sequence, making explicit that **atmospheric preload appears only at the vent** (gentle initial pump; keep vertical). End platens defined as **1/8″ aluminium** (flat, clean; 1/4″ fallback). Getter sized to N; optional light **outboard structure** noted (epoxy pot discouraged — dead mass, must not touch the stack). |
| 3.3 | ____ | Croft Swonyoung | **Added application-agnostic ruggedization variant (Appendix A).** An optional inside-envelope **pre-cured platinum-silicone edge-cushion** (rim strip; 50 A / 1.0 mm / ASTM E595; vacuum-baked; sized into the getter budget; **cured sheet only — no wicking**) protecting the wafer rim outboard of the ⌀130 active area, plus an outboard **filled low-exotherm epoxy carrier pot** (strictly outboard of the sealed envelope; low-exotherm to protect the seal; degassed, void-free, CoG-controlled). Added **only for units that see in-service inertial loading at arbitrary orientation** (e.g. a flying vehicle, or the 128 G generator rotor as the *bounding* case) and **sized to the application's design acceleration**; static/bench bricks omit both. Cushion spec written to the 128 G bounding case (conservative for lighter apps). Corrected the earlier three-piece cushion concept to a **rim strip + optional recessed platen end-ring** (a proud end-ring would break the atmospheric preload path). Reconciled the "epoxy pot discouraged" stance: still discouraged for static/measurement packages, **required** for in-service units. Added hooks in §1, §2, §4, §5, §6.2 (step 6), §7; "G" defined as acceleration to avoid clash with grams. |
