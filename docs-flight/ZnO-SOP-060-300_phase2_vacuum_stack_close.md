<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set (300 mm flying line). Verify file integrity against `CHECKSUMS.sha256`.

---

> **300 mm line · derived from the 150 mm `ZnO-SOP-060` Rev 3.3.** The **process
> logic is identical** to the 150 mm procedure — shiny-Si-face-down cells, zero-gap
> mechanical contact (no inner bonds), one common vacuum held by a getter in a
> metallized barrier envelope, atmospheric preload that appears only at the chamber
> vent, and the assembly-cartridge + silicone-retaining-band build. **Only the
> geometry, tooling, and mass that the larger ⌀300 wafer forces have changed** —
> per-cell pitch, per-cell mass, platen thickness/flatness, getter size, chamber
> clearance, cartridge/band size, and the Appendix A cushion dimensions. All
> dimensions come from `300mm-datum-reference.md`; this SOP does not restate them
> independently.

---

# Working Procedure & Specification

## Phase-2 Stack Close: Wafer-Backed Cells in a Getter-Maintained Common Vacuum (300 mm)
### Zero-gap Ni-void / Si-wafer stack · conformal barrier envelope · atmospheric preload · N cells (recommended N ≤ 117)

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-060-300 | Revision | 1.0 |
| Effective date | ____________ | Supersedes | — (new; derived from 150 mm Rev 3.3) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-050-300 (Phase-1 wafer-backed cells) | Next step | Final QC / packaging (ruggedized handoff → ZnO-SOP-080-300 flying integration) |
| Variant | Common vacuum · conformal envelope · N cells (≤ 117) | — | — |

---

## 1. Purpose and scope

This procedure performs **Phase 2** of the assembly: **N** wafer-backed cells from ZnO-SOP-050-300 are stacked **coaxially with no gap**, **each cell polished (shiny) Si face down** so its polished face caps the working voids of the cell below — a getter is added, and the whole stack is enclosed in a **metallized barrier envelope**, evacuated, and heat-sealed so that **atmospheric pressure preloads the stack**. There is no N₂ fill, no spacer, no cavity gap, and no per-interface seal. The entire stack shares **one common vacuum**, maintained for service life by a **getter**.

**Plain-language picture — a vacuum-packed brick.** The finished package is essentially a **vacuum-sealed brick of coffee**: the cells and getter sit inside a flexible metallized (foil-laminate) bag, the air is pumped out, and the bag is **heat-sealed shut** (one-shot — not a reclosable zip). The instant it is vented back to air, ~1 atm shrink-wraps the bag down onto the contents and the whole thing goes **rock-hard**, exactly like an unopened coffee brick — and *that* squeeze is the preload holding every wafer pressed flat against its neighbour. The getter is the little oxygen-absorber sachet, and two rigid end plates spread the ~1 atm as flat, even pressure over the brittle wafers.

**Cell count is a design variable.** Per cell the pitch is **≈ 0.875 mm** (wafer 0.775 + Ni-P 0.025 + silicone bond ~0.075; per `300mm-datum-reference.md`). **Recommended maximum N = 117** → a stack **≈ 102 mm tall** (still far wider than tall at ⌀300) and **≈ 17 kg** of active cells. Choose N for the force signal you need to resolve, for the flyer's mass/thrust budget, and for what you can handle/assemble and fit in the sealer chamber (see §2, §5). **At 300 mm each cell is ≈ 145 g** (vs ≈ 32 g at 150 mm), so the stack is materially heavier for a given N — plan handling and lifting accordingly (§3, §6.2).

**The governing rules.**
1. **Vacuum, not fill.** All voids share one common vacuum; the seal carries a permanent ~1 atm (~101 kPa) differential, so the hermetic function lives in the outer envelope, never in an inner interface.
2. **Zero gap, mechanical contact.** The working face is **not bonded** to the neighbouring wafer — it is held in intimate contact by atmospheric pressure through the conformal envelope. No adhesive touches the working face.
3. **The getter maintains the vacuum**, sized to N (permeation + outgassing both scale with stack size), and for the 300 mm line to the **~4× larger permeation/outgassing area** of the ⌀300 stack (datum §4).
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
- **Conformal barrier envelope.** A heat-sealable **metallized multilayer barrier laminate** (vacuum-insulation-panel grade — e.g. aluminised PET / metal-foil laminate). Under external atmosphere it conforms and presses the evacuated stack together. Sole hermetic boundary. Envelope stock (and the sealer chamber) is sized for the ⌀300 footprint (§4).
- **Atmospheric preload — appears at the vent.** Once the sealed bag is vented back to air, ~101 kPa applies a **uniform axial compression**, wringing each polished Si face against the neighbouring void mouths. **Critically, this force does not exist until the vent:** in a chamber sealer the bag is *open* during chamber pump-down, so inside and outside evacuate together and the bag stays limp with **no clamping** the whole way down and through sealing. The preload is a *post-seal, post-vent* event. (The preload is a *pressure*, ~101 kPa, so it is the same per unit area at 300 mm as at 150 mm — the larger wafer simply sees the same clamp stress over ~4× the area.)
- **Assembly cartridge.** To survive handling and pump-down before the preload exists, the stack is built as a self-retaining cartridge: **bottom platen → cells → top platen**, held coaxial by a **lateral registration feature** (posts / ring / locating lip on the bottom platen so the ⌀300 wafers cannot slide) and bundled by **retaining bands** (below). Rigid enough to pick up and set in the bag; superseded by atmospheric preload after the vent. The 300 mm cartridge is larger and heavier (≈ 17 kg of cells at N = 117), so the registration feature and bands are sized to the larger disc and the whole cartridge is handled as a two-person / lifting-aid item.
- **Retaining bands.** **2–3 low-outgassing silicone bands** wrapping the full cartridge height (over the top platen, under the bottom platen), seated in shallow platen-edge notches so they stay off the wafer load path, and **sized to the larger ⌀300 cartridge**. They give a few newtons — enough to keep the platen-stack-platen a single bundle for handling and pump-down, far below the eventual ~1 atm. They remain **inside** the envelope (low-outgassing silicone; the getter is sized to include their outgassing).
- **End platens.** **1/8″ (3.175 mm) aluminium minimum**, flat (MIC-6 tooling plate or surfaced flat), ⌀ ≥ the wafer (**⌀ ≥ 300**, with a small overhang to shield the brittle wafer edges and anchor the bands), cut per ZnO-DR-006-300. They spread the ~1 atm as uniform axial compression. **Clean/degreased** (they live in the vacuum). **For the 300 mm line, likely step up to 1/4″ (6.35 mm):** flatness must be held across the larger ⌀300 span and under the heavier stack, and a 1/8″ plate is more prone to bow over the wider unsupported footprint — spec 1/4″ unless a flatness check on the thinner plate passes under load. In the shiny-down build the **bottom platen bears on a polished Si face** and the **top platen on a working (void) face** — keep both platen faces clean and flat.
- **Achievable vacuum (stated honestly).** Bench chamber-sealer + getter gives **rough-to-medium vacuum (~1–100 Pa), durable for years via the getter — not UHV.** At ≤~100 Pa the mean free path exceeds the void size (free-molecular): convection gone, gas effectively excluded. *(Physics is diameter-independent — unchanged from the 150 mm line.)*
- **Getter.** General O₂ + H₂O + molecular-sieve (± NEG), **sized to N** and to the **~4× larger permeation/outgassing area** of the ⌀300 stack (permeation through the envelope and internal outgassing — including the silicone bands and bonds — both scale with the stack's surface/footprint), oversized for life, low-dust, restrained.
- **Optional outboard structure.** For ruggedness / a defined external form, an optional **light rigid frame, end-caps, or thin shell** may be added **outboard of the envelope** (never contacting the stack) to help retain preload and protect the package. Keep it light — parasitic mass hurts the force-to-weight ratio the propulsion hypothesis cares about (and at 300 mm the stack is already heavy). A full **epoxy pot is possible but discouraged for a static / measurement package**: it must stay strictly outboard of the sealed envelope (epoxy in contact with the stack would wick into the contacts and voids and destroy the mechanism), and it adds substantial dead mass — a light frame beats a solid pot. **Exception — ruggedized (in-service) units:** a brick that must survive service inertial loads at arbitrary orientation (a flying vehicle, or — the bounding case — the 128 G generator rotor) *requires* a carrier pot, not merely an optional frame; the dead mass is unavoidable and is traded for survival. Ruggedization — the inside-envelope **edge-cushion** and the outboard **carrier pot**, both sized to the application's design acceleration — is specified in **Appendix A**.
- **Edge-cushion frame (ruggedized variant, inside envelope).** For units that will see in-service inertial loading, a **pre-cured, die-cut platinum-silicone** cushion wraps the **wafer-stack rim** to protect the brittle wafer edges from dynamic, omnidirectional loads. **Pre-cured sheet only — never painted or dispensed:** liquid silicone would wick by capillary action into the contacts and voids and destroy the mechanism. It touches **only the wafer rim, outboard of the ⌀280 active region**, and is the **same low-outgassing class as the retaining bands** (ASTM E595), so it joins the getter's outgassing budget. Material, geometry, and placement in **Appendix A.1**.
- **Fault tolerance (reduced, by design).** Common vacuum → one breach vents all. Mitigations: robust/defect-free envelope (optionally double-enveloped), generous getter margin, end platens that guard against the likeliest initiator (wafer fracture). Verify the failure mode is a **graceful** slow decay the getter buys time against, not a sudden collapse.
- **No reheat over the stack.** Envelope heat-sealing is confined to the seam, away from the wafers, bands, and cured bonds.

---

## 3. Health, safety and environment

- **Vacuum sealing** — chamber-sealer / seal-bar pinch and implosion hazards are low at this scale; keep hands clear.
- **Silicon wafer handling** — brittle; sharp fracture shards. The ⌀300 wafers are large and heavier — edge handling; eye protection; uniform full support only; never grip a large disc at a point.
- **Heavy-stack handling (new at 300 mm)** — a full cartridge is ≈ 17 kg of cells at N = 117 (plus platens); use two people or a lifting aid, keep the axis vertical, and stage it so a slip cannot shatter the wafers or trap a hand.
- **Getter handling** — molecular sieve / desiccant / O₂ scavengers are generally safe; **if a non-evaporable getter (NEG) is used, some grades are reactive/pyrophoric when activated** — handle per SDS, keep sealed until placement.
- **Barrier-film heat-seal** — hot seal bar; burn hazard.
- **PPE:** gloves, safety glasses.
- **Waste:** film, getter, and silicon scrap per local rules.

---

## 4. Materials, reagents and equipment

### 4.1 Components (per N-cell stack, recommended N ≤ 117)

- **N × Phase-1 wafer-backed cells** (ZnO-SOP-050-300) — de-rimmed, voids finally cleaned, polished wafer face pristine, bow within budget.
- **2 × aluminium end platens**, flat (MIC-6 or surfaced), **⌀ ≥ 300** (small overhang for edge protection + band anchor), clean/degreased for vacuum; cut per ZnO-DR-006-300; bottom platen carries the **lateral registration feature** (posts / ring / locating lip). **Nominally 1/8″ (3.175 mm), but step to 1/4″ (6.35 mm)** for flatness across the ⌀300 span under the heavier stack unless a load flatness check on the thinner plate passes (§2).
- **2–3 × low-outgassing silicone retaining bands** (ASTM E595 class), **sized to wrap the larger ⌀300 cartridge** over both platens.
- **1 × general getter assembly** — O₂ + H₂O + molecular sieve (± NEG), **sized to N and to the ~4× larger permeation/outgassing area** of the ⌀300 stack, oversized, low-dust, restrained.
- **Metallized barrier laminate envelope stock**, heat-sealable (VIP grade), **sized for the ⌀300 footprint**; double-envelope stock if redundancy is specified.
- Optional: **light outboard frame / end-caps / shell** (kept outboard of the envelope; see §2).
- **(Ruggedized variant) 1 × pre-cured platinum-silicone edge-cushion set** — die-cut rim strip (+ optional recessed platen end-ring), ASTM E595 low-outgassing, **vacuum-baked before use**; sized to the ⌀300 stack per Appendix A.1. Add its outgassing to the getter sizing.
- **(Ruggedized variant) Carrier / mould + filled low-exotherm potting epoxy** for the larger, heavier outboard pot; see Appendix A.2.

### 4.2 Equipment

- **Chamber vacuum sealer** (or vacuum chamber + heat sealer) capable of the target pressure (~1–100 Pa) **with an internal footprint that clears the ⌀300 stack + bag (⌀300+, so a chamber footprint of order ⌀330–350) and an internal height that clears the stack + bag** (≈ 120 mm+ for N near 117); vacuum gauge. **A chamber sizer/sealer that clears ⌀300+ is a likely long-lead procurement item** — size and source it early; it may gate the buildable N (see §5).
- Registration / alignment fixture for coaxial stacking of the ⌀300 discs; flatness fixture.
- **Vacuum-decay / pressure-rise test** capability; optional He leak check on the seam.
- SEM; edge-grip wafer tweezers rated for the ⌀300 disc; **lifting aid for the heavy cartridge**; particle-controlled staging area.

---

## 5. Specifications

| Element | Specification | Notes |
|---|---|---|
| Stack | **N cells (recommended ≤ 117)**, zero gap, coaxial, contact-preloaded | **every cell shiny-Si-down**; its polished face caps the cell below's voids; thrust toward the shiny (down-as-built) side |
| Per-cell pitch / mass | **≈ 0.875 mm / ≈ 145 g active** (datum) | wafer 0.775 mm + Ni-P 0.025 mm + bond ~0.075 mm |
| Inner interfaces | **mechanical contact only** — no bond, no gap, no seal | atmospheric-preloaded; nothing wicks into voids |
| Preload | ~101 kPa uniform axial, **applied at the chamber vent (post-seal)** | via conformal envelope + aluminium end platens; same *pressure* as 150 mm over ~4× the area |
| Assembly retention | 2–3 low-outgassing silicone bands + lateral registration | holds the loose cartridge through handling + pump-down only; bands sized to the ⌀300 cartridge |
| Edge-cushion (ruggedized variant) | pre-cured platinum silicone, **50 A, 1.0 mm**, E595, vacuum-baked; **rim wrap** | protects wafer edges under in-service loads; inside envelope, off the ⌀280 active area (App. A.1) |
| End platens | aluminium, flat, clean; **⌀ ≥ 300**; **1/8″ min, step to 1/4″** | spread the load; step to 1/4″ for flatness across the ⌀300 span under the heavier stack |
| Vacuum | target **~1–100 Pa**, getter-maintained, durable years | rough–medium, **not UHV** (§2) |
| Getter | general O₂/H₂O + molecular sieve (± NEG), **sized to N and ~4× area** | pumps permeation + outgassing (incl. bands/bonds) over the larger footprint |
| Envelope | metallized barrier laminate (VIP grade), continuous heat seal, **⌀300 footprint** | sole hermetic boundary; optional double-envelope |
| Chamber sealer | clears **⌀300+ footprint** and ≈ 120 mm+ height | **likely long-lead item;** may gate buildable N |
| Outboard structure | optional light frame/shell, **outboard of envelope**; **carrier pot for the ruggedized variant** | epoxy pot discouraged for static/bench packages (dead mass); **required for in-service (dynamic) units, sized to the app's g-load (App. A.2)** — always outboard of the stack |
| Fault mode | single common vacuum → one breach vents all | accepted trade; mitigations per §2 |
| Target mass | ≈ N × 145 g active + platens + envelope/getter (**assumption-based**) | see note |

> **Mass estimate (assumptions stated; masses per `300mm-datum-reference.md`).** Active cell ≈ 145 g (⌀300 wafer 0.775 mm ≈ 128 g + ⌀280 Ni-P 25 µm ≈ 12 g + ⌀280 bond ≈ 5 g). **At N = 117: ≈ 17 kg active + ≈ 2.4 kg platens (two 1/4″ ⌀300 Al; ≈ 1.2 kg if 1/8″) + ~0.5 kg envelope/getter/bands ≈ 20 kg total.** Recompute for your actual N and wafer thickness. The stack is ~5× the 150 mm brick's mass at equal N — this is a handling and flyer-mass driver, not a lift-ratio change (T/W is scale-invariant per the datum).
>
> **Stack-height / count guidance.** The 300 mm wafer diameter keeps the column *wider than tall* out to ~343 cells, and the preload is a pressure (~101 kPa) so it does not weaken with height. There is no sharp structural limit near the recommended N ≤ 117 (~102 mm). The real ceilings are getter sizing, **the chamber-sealer footprint/height (the likely long-lead item)**, assembly/handling of the heavy cartridge, the flyer's mass budget, and the measurement: **if the hypothesised force and the mass both scale ~linearly with N, force-to-weight is roughly constant with N** — so more cells give a *bigger absolute force* (easier to resolve, and it aids the balanced-pair null test), not a better levitation ratio. The reason to run 300 mm at all is **handling / throughput** (fewer, larger parts per unit active area), not a better lift ratio — state this plainly wherever lift is discussed (datum §2).

---

## 6. Procedure

### 6.1 Staging

1. Stage in a particle-controlled area: the N cells, both aluminium platens, silicone bands, getter (kept sealed), envelope stock, alignment fixture, and the lifting aid for the heavy cartridge.
2. Inspect each cell: working face open/clean, **polished wafer face pristine**, bow within budget, no wafer cracks. Reject failures.

### 6.2 Build the cartridge (zero gap)

1. Place the bottom platen in the alignment fixture, registration feature up. **Keep the assembly axis vertical from here on** — gravity (and, in this orientation, any always-on thrust) seats the slick wafers.
2. Lay cells one at a time in registration, **each cell polished (shiny) Si face DOWN**, its polished face landing on the **working (void) face of the cell below**, coaxial. **No adhesive.** Seat lightly — do not press or slide (sliding scratches the polished cap; the wafers are slippery and shingle easily). The ⌀300 discs are large and heavier — support each fully on landing and never grip at a point.

   > **Orientation is not optional.** Shiny-Si-down is the hypothesised thrust direction, so built this way any always-on thrust presses each cell *down into* the stack and self-seats it. Built shiny-**up**, that same thrust would push cells *off* the stack ("popping up") — making assembly impossible. When in doubt: **shiny down.**
3. After each cell, confirm coaxial seating (no rock, no debris). Never slide a landed wafer.
4. Land the top platen on the final cell.
5. **Wrap 2–3 silicone retaining bands** over the top platen, down the sides, under the bottom platen (seated in the platen-edge notches), tensioned to hold the platen-stack-platen as one firm bundle — enough to handle, far below atmospheric preload. The stack is now a **cartridge** (a ≈ 17 kg one at N = 117 — move it with two people or the lifting aid, axis vertical).
6. **(Ruggedized variant only)** Fit the pre-cured silicone **edge-cushion rim strip** around the wafer-stack cylinder — over the wafer edges, between the platens, off the ⌀280 active faces — with the splice and vent-notches placed per Appendix A.1. Keep it clear of the retaining-band paths. It rides **under the envelope, inside the vacuum**. Static / bench units skip this step.

### 6.3 Getter placement

1. Place the getter (sized to N and the ~4× larger area) in its vented pocket alongside the cartridge (within the future envelope, clear of contact faces), mechanically restrained so it cannot shift onto a wafer.

### 6.4 Enclose, evacuate, seal (chamber sequence)

1. Enclose the cartridge + getter in the barrier envelope, seam accessible. If double-enveloping, stage the inner envelope now.
2. Place in the chamber sealer, **keeping the cartridge vertical if the chamber allows** (confirm the chamber clears the ⌀300 footprint and the stack height — §4.2). Note that from here until the vent (step 5) there is **no atmospheric clamping** — the silicone-band cartridge is what holds the stack.
3. **Evacuate — start gently.** As the chamber pumps down, air trapped between the near-touching wafers vents out the edges; a violent initial pump can lift or shuffle a loose disc (and the larger ⌀300 disc traps more edge air). Ramp the pump so the stack is not disturbed. Pump to the target (~1–100 Pa); hold to confirm stable.
4. **Heat-seal the envelope seam** — continuous, no wrinkles or channels — while under vacuum. Seal the second envelope if used. (The seal bar acts on the mouth/seam, away from the stack.)
5. **Vent the chamber to atmosphere.** ~1 atm now returns *outside* the sealed bag: the envelope draws taut and the preload appears, clamping the stack. The silicone bands are now redundant (they remain inside, low-outgassing).

### 6.5 Verify

1. Confirm **atmospheric preload present**: envelope taut, stack compressed to a firm "brick," platens seated square.
2. Inspect the seam: continuous, no leak channel or wrinkle path.
3. Run the **initial vacuum-decay / pressure-rise check**; record the baseline for life monitoring.
4. Inspect for wafer cracks initiated by preload (through the envelope) — pay attention across the larger ⌀300 span where platen bow would first tell.
5. If an outboard frame/shell is specified, fit it now (outboard of the envelope, not contacting the stack).

### 6.6 Recovery

1. Label with stack ID, **cell count N**, seal date, getter lot, initial vacuum/decay baseline. Proceed to final QC (ruggedized units → ZnO-SOP-080-300 flying integration).

---

## 7. Acceptance criteria and QC

- **Envelope integrity:** continuous seam, no leak channel or pinhole; vacuum-decay / pressure-rise within spec; optional He leak check passes.
- **Vacuum level:** meets the ~1–100 Pa target at seal (gauge, or validated by decay behaviour).
- **Atmospheric preload:** confirmed (taut envelope, compressed stack, platens seated).
- **Cartridge integrity:** stack stayed coaxial through pump-down (no shingling); bands seated, off the load path.
- **Getter margin:** type and capacity documented against the estimated permeation + outgassing load for N, the ~4× larger ⌀300 area, and target life.
- **Platens / wafers:** platens flat and clean **across the full ⌀300 span under load** (verify the 1/8″-vs-1/4″ decision held — no bow print, no centre lift); no wafer cracks post-preload (inspection).
- **Stack:** coaxial, flat, self-supporting; every working face fully seated on its neighbour's polished cap.
- **Chamber fit:** the ⌀300 stack + bag cleared the sealer footprint and height with margin (confirms the long-lead chamber was sized correctly for the built N).
- **Fault mode:** confirm (analysis or test) that an envelope breach produces a **graceful** vacuum decay, not a sudden collapse; document the single-point-failure acceptance.
- **(Ruggedized variant) Edge-cushion:** seated over the full wafer-stack rim, off the ⌀280 active area, vent-notches clear; vacuum-baked lot recorded and added to the getter's outgassing budget (App. A.1).
- **(Ruggedized variant) Carrier pot:** cured **void-free** (tap / CT if available), **strictly outboard of the envelope** (no epoxy ingress, seam intact), CoG within the application's balance/CoG budget; **only a §6.5-verified brick was potted** (the pot is permanent and hides the envelope) (App. A.2).

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Cells lift / pop off during assembly | Built shiny-side-**up** → the always-on thrust points up and unseats them → build **shiny-Si-down** so thrust seats them; verify orientation. |
| Stack shingled / misaligned during pump-down | Loose cartridge or violent pump | tighten/register bands (sized to ⌀300); add/verify the lateral registration; keep axis vertical; ramp the pump gently (the larger disc traps more edge air). |
| Envelope will not hold vacuum | Seam channel / film pinhole / fold leak → re-seal continuous; inspect film; adopt double-envelope; verify seal-bar temperature/dwell. |
| Vacuum decays quickly in service | Getter undersized for N **or for the ~4× larger ⌀300 area**, or outgassing high → larger getter; lower-outgassing silicone (bands/bonds); pre-condition/bake components before sealing. |
| Bag not taut after vent | No preload — leak or vacuum not reached → re-check seam and gauge; the bag must go firm at the vent. |
| Wafer cracked under preload | Non-flat platen (more likely across the ⌀300 span), edge pinch, or trapped debris → flat full-footprint platens (**use 1/4″ at 300 mm** if the thinner plate bows), platen overhang shields edges, clean staging. |
| Platen prints / centre lift on the wafer | 1/8″ plate bowing over the wider ⌀300 span → step to 1/4″ (6.35 mm) aluminium; re-verify flatness under load. |
| Stack won't fit / clears the chamber poorly | Chamber sealer not sized for the ⌀300 footprint → source the long-lead ⌀300+ chamber; reduce N to fit until it arrives. |
| Contact not intimate (poor cap seating) | Debris or wafer bow → clean faces; tighten the ZnO-SOP-050-300 bow and polished-face gates; never slide landed wafers. |
| Polished cap scratched during build | Wafer slid rather than landed → land vertically into registration; no lateral motion once seated. |

---

## 9. Waste and storage

- Barrier film, getter, silicone bands, and silicon scrap per local regulations.
- Store finished stacks flat, protected, labelled; retain seal-date, cell count, getter-lot, and vacuum-decay baseline records per stack for life monitoring. The ⌀300 stacks are heavy — store on rigid flat supports rated for the mass.

---

## Appendix A — Ruggedization for in-service (dynamic) applications (edge-cushion + carrier pot)

**Scope — application-agnostic.** SOP-060-300 closes the brick **independent of end use**; this appendix adds the mechanical ruggedization a unit needs **only if it will experience in-service inertial loading at arbitrary orientation.** The trigger is the *service environment*, not a particular product. Current applications span the load range:

| Application | Design accel. *a_d* | Orientation | Ruggedization |
|---|---|---|---|
| Static / bench / measurement package | ≈ 1 G, fixed | fixed | **None** (baseline brick; optional light frame per §2) |
| Flying vehicle | modest (maneuver + vibration + landing shock) | omnidirectional | **Recommended,** sized to the vehicle's g-envelope |
| Spinning generator rotor | **128 G steady**, sweeping every in-plane direction as the puck rotates on its own axis | omnidirectional | Required — **the bounding case** for current uses |

Two additions do the work: **A.1** a pre-cured silicone **edge-cushion** *inside* the envelope; **A.2** an epoxy **carrier pot** *outboard* of the envelope. Both stay strictly clear of the working faces and voids — the cushion touches only the wafer rim (outboard of the ⌀280 active region); the pot never touches the stack (it encapsulates the *sealed envelope* only).

**Size to your *a_d*.** The material spec below (50 A / 1.0 mm cushion; filled epoxy pot) is written to the **128 G bounding case**, so it is **conservative for any lighter application** — a flying unit may relax durometer, thickness, or pot mass if a load analysis supports it, but the baseline recipe is safe as-is.

**Out of scope here** (separate, application-specific integration procedures): mounting / axles or airframe attachment, CoG-trim, bearings, containment, and any control or safety system particular to the end use. This appendix delivers a **ruggedized puck** plus its **carrier datum and CoG budget**, which the integration step (ZnO-SOP-080-300 for the flying line) consumes.

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

**Geometry — rim strip (primary) + optional recessed end-ring.** Dimensions parametric in wafer diameter **D = 300 mm**, silicone thickness **s = 1.0 mm**, and measured bonded-stack height **H** (cells only, platen-to-platen interior; H ≈ N × 0.875 mm → ≈ 102 mm at N = 117; all per `300mm-datum-reference.md`).

- **Rim strip (primary).** One continuous 1.0 mm layer wrapping the wafer-stack cylinder — protecting every wafer edge at once.
  - Width = **H** (matches the stack height ≈ 102 mm at N = 117).
  - Length = **π (D + s) + 8 mm** splice overlap ≈ **π (301) + 8 ≈ 954 mm** at ⌀300 (the π(D + s) core ≈ π(301) ≈ **946 mm**).
  - **Vent notches** (~1 × 2 mm, ×2–3) on an arc that will **not** be the primary load-bearing direction in service (for the rotor, the arc crossing the spin axis; for an omnidirectional or undefined load, keep the notches minimal and evenly spread) — so the main load-bearing arc stays fully covered while trapped gas still escapes during pump-down.
- **End-face corners.** Handled first by the **aluminium platen overhang** already in the baseline design (§2). For extra margin, an **optional recessed silicone ring** — OD 300, **ID ≥ 284 mm** (stays outboard of the ⌀280 active region), 1.0 mm — may be seated in a **shallow relief groove machined into the platen face.**
  - **Do NOT stack a proud ring in the axial load path.** At only ~101 kPa preload a 1 mm 50 A ring will not compress and would hold the platen off the wafer centre, breaking the zero-gap contact the SOP depends on. Recess it flush, or omit it and rely on the platen overhang.

```
   Cross-section (vertical slice through the spin axis):

      |<--------------------- D = 300 --------------------->|
       _____________________________________________________
      |   platen overhang (+ optional recessed ring in groove)  |
      |_____________________________________________________|
     ||                                                     ||
  R  ||                 wafer stack  (H ≈ 102 @ N=117)      ||  R   ] rim strip
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

**Purpose.** Rigidize the flexible brick into a **puck** that survives its service g-load at any angle and carries the application's mounting datum. This **overrides the baseline "epoxy pot discouraged" stance** (§2), which is for static/measurement packages where dead mass hurts force-to-weight; an in-service unit needs the pot and the mass is unavoidable. At 300 mm the puck, mould, and epoxy charge are **larger and heavier** — size the carrier, degassing capacity, and heat-sink accordingly.

**Rules.**
1. **Strictly outboard of the sealed, vented envelope.** The pot encapsulates the *finished brick* (post-§6.5); epoxy never contacts the stack, contacts, or voids.
2. **Pot into a defined carrier / thin-wall mould** so external geometry, mass, and CoG are predictable and the shell carries the mounting features (the datum the application-integration step consumes). Size the carrier to the ⌀300 puck.
3. **Epoxy = silica/alumina-filled, low-exotherm, slow cure.** The **envelope heat-seal is the thermal weak point** — keep peak exotherm well below its rating; the **larger 300 mm epoxy charge stores more heat**, so pour in **thin lifts**, heat-sink the mould, and **cure cool** with extra margin.
4. **Vacuum-degas the resin.** Voids are stress concentrators under service loads and shift the CoG unpredictably (more so on the larger puck).

**Procedure.**
1. Confirm the brick passed **§6.5** (preload present, seam sound, decay baseline recorded). **Only pot a verified brick** — the pot is permanent and hides the envelope.
2. Prepare the carrier/mould; place the brick with its **thrust axis (shiny-down) indexed to the carrier datum.**
3. Pour degassed, filled, low-exotherm epoxy in **thin lifts**; degas between lifts; heat-sink and cure cool (the larger charge needs it).
4. Post-cure per the resin data sheet; verify **void-free** (tap test / CT if available) and **CoG within the application's balance/CoG budget.** Hand off to the application-integration procedure (ZnO-SOP-080-300 for the flying line).

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | __________ | Croft Swonyoung | **Initial release of the 300 mm flying-line variant, derived from the 150 mm `ZnO-SOP-060` Rev 3.3.** Pure **scale-up, not a redesign** — the process logic is **unchanged**: shiny-Si-face-down cell orientation and its self-seating rationale, zero-gap mechanical contact (no inner bonds), one common vacuum held by a getter in a metallized barrier envelope, atmospheric preload appearing only at the chamber vent, the assembly-cartridge + silicone-retaining-band build, and the single-point-failure framing all carry over verbatim. **Scaled per `300mm-datum-reference.md`:** per-cell pitch ≈ 0.78 → **≈ 0.875 mm** and per-cell mass ≈ 32 → **≈ 145 g** (stack ≈ 0.145·N kg; ≈ 17 kg active / ≈ 20 kg total at N = 117, ≈ 102 mm tall); active region ⌀130 → **⌀280**; end platens ⌀ ≥ 300 and **likely stepped 1/8″ → 1/4″ aluminium** for flatness across the larger span under the heavier stack; getter sized to **~4× the permeation/outgassing area**; envelope and **chamber-sealer clearance sized for ⌀300+ (flagged a likely long-lead item)**; retaining bands and cartridge sized to the larger disc; added heavy-stack-handling notes. **Appendix A ruggedization scaled to 300 mm** keeping it application-agnostic and the **platinum-silicone spec verbatim** (50 A / 1.0 mm / ASTM E595 / vacuum-baked; cured sheet only — no wicking) and the filled low-exotherm epoxy discipline: edge-cushion **rim-strip length π(D + s) ≈ π(301) ≈ 946 mm** (core; ≈ 954 mm with 8 mm splice), width = stack height H (≈ 102 mm at N = 117); optional recessed platen end-ring **OD 300, ID ≥ 284 mm**, recessed (never proud in the preload path); larger/heavier carrier pot with extra exotherm/degassing margin. Cross-references updated to the -300 names (**ZnO-SOP-050-300** predecessor, **ZnO-DR-006-300** platens, **ZnO-SOP-080-300** flying-integration consumer). Section numbering/structure (including Appendix A) preserved. |
