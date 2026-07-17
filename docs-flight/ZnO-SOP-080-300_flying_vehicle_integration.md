<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

> 🚧 **SEED — 150 mm-based, needs 300 mm re-derivation.** This procedure was moved
> from the 150 mm line and still references the 150 mm ruggedized-puck handoff and
> masses. In this **300 mm flying-machine** set it must be re-derived against the
> 300 mm puck (per-cell ≈140 g, larger active area) and its `[TBD]` fields
> (per-puck thrust, vehicle mass, thrust-to-weight) completed. See
> `300mm-re-derivation-plan.md` (this directory). Do not treat as final.

---

# Working Procedure & Specification

## Flying-Vehicle Integration — staged lift demonstrator (thrust-to-weight hypothesis)
### Ruggedized pucks in an airframe · constrained thrust/lift measurement first · free flight gated behind proof

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-080 | Revision | 0.1 (DRAFT) |
| Effective date | ____________ | Supersedes | — (new) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-060 Appendix A (ruggedized puck: carrier datum + CoG budget) | Next step | Flight-test programme (out of scope) |
| Variant | N vectored pucks · Stage A constrained rig → Stage B gated free flight | — | — |

---

## 1. Purpose and scope

This procedure integrates **ruggedized pucks** (ZnO-SOP-060 Appendix A) into an **airframe** to test whether their (hypothesised) net thrust can lift and control a vehicle — i.e. whether **thrust-to-weight (T/W) > 1** and whether the thrust can be **vectored for stable attitude control.** It is deliberately **staged and safety-gated:**

- **Stage A — constrained demonstrator.** The vehicle is held on a rig (load cell / gimbal stand / guide rails / tether) that **cannot let it escape.** Measure net vertical thrust, the vectoring map, control authority, and the fail-safe. *This stage produces the data; free flight does not.*
- **Stage B — free flight.** Attempted **only if** Stage A shows T/W > 1 with margin, demonstrated vectored control, and a verified fail-safe. Tethered-in-arena first; never over persons.

> **Hypothesis discipline — read this.** No net thrust has been measured, and **there is no evidence the vehicle will lift.** With the pucks' mass and structure, the most likely Stage A outcome is **T/W < 1** (it does not fly). That is a valid, honest measurement, not a failure. This document does not claim flight; it specifies how to **measure** the lift hypothesis safely. Never present Stage A hardware as "a working flying machine."

> **Baseline assumptions (redirect as needed).** The airframe, puck count, per-puck thrust, and mass are **undefined** at this revision; fields marked **[TBD]** await your inputs (especially per-puck thrust, ideally from the ZnO-SOP-070 rotor or a dedicated thrust stand). The staging and fail-safe philosophy below are the fixed part; the vehicle specifics are placeholders.

**Two hard design facts that shape everything:**
1. **The thrust cannot be switched off (hypothesis).** A lifter you cannot turn off is dangerous. The vehicle **must** be able to drive its net thrust to zero **mechanically** (vector opposed / to a null) on command and on loss of control — see §2, §6A.5.
2. **CoG must sit below the thrust centroid** (pendulum-stable) unless active control provides the stability margin — see Appendix B.

**Out of scope:** puck fabrication/ruggedization (SOP-010…060); the rotor generator (SOP-070); the free-flight *test programme* itself (a separate flight-ops document, gated by Stage A).

---

## 2. Definitions and interpretation

- **Puck.** Ruggedized potted stack (SOP-060 App. A) with a **thrust-axis datum** (shiny-Si / hypothesised-thrust direction) and CoG within budget.
- **Lift line / thrust centroid.** The resultant line of action of all pucks' thrust. Vehicle CoG is placed **on and below** it for passive stability.
- **Thrust-to-weight (T/W).** Net measured vertical thrust ÷ vehicle weight. **The quantity Stage A exists to measure.** T/W > 1 is the precondition for any lift.
- **Vectoring.** Rotating/gimballing pucks (or differential vectoring across several fixed pucks) to tilt the resultant for attitude control and to **null** net thrust.
- **Kill-to-null (fail-safe).** On command or loss of control/power, the pucks are driven to a **net-zero-thrust** state (opposed / neutral) so lift collapses in a controlled way. Because thrust cannot be switched off, this mechanical null **is** the kill.
- **Stage A constrained rig.** Any fixture that measures force while **physically preventing escape** — a load-cell thrust stand, a 2–3-axis gimbal stand, vertical guide rails, or a short hard tether inside a net.
- **Stage B free flight.** Untethered operation, attempted only behind the §6A gate; tethered-in-arena before open flight.
- **Arena / net.** Enclosed, netted volume with no personnel underneath or within fall/again radius.

---

## 3. Health, safety and environment

- **Overhead lift + fall hazard.** A vehicle that lifts can fall; a vehicle that lifts unexpectedly during Stage A must be **restrained.** Constrained rig at all times until the Stage B gate is passed. **No personnel under or beside** the vehicle.
- **Cannot be switched off (hypothesis).** Verify **kill-to-null** works — including on power loss — **before** any lift attempt. This is the single most important safety item.
- **Tether / arena.** Stage B begins **tethered inside a net**; height- and excursion-limited; remote kill in hand.
- **Sharp edges, brittle silicon, stored energy** in any springs/gimbals; **electrical** (battery/controller) — isolate for service.
- **PPE and standoff:** eye protection; maintain standoff; treat every powered run as live-lift.

---

## 4. Materials and equipment

- **Airframe / structure** **[TBD]** — mounts N pucks with their **thrust axes aligned** to the vehicle's lift axis; stiff, light.
- **Puck mounts** — fixed with **differential vectoring** across pucks, or individually **gimballed** (servo/stepper) for attitude control and kill-to-null.
- **Flight controller + IMU** (attitude sensing), vectoring actuators + encoders, **power source** [TBD], remote link with **hardware kill**.
- **Stage A constrained rig** — **load cell(s)** (vertical force; ideally a 6-axis or multi-cell for the vectoring map), plus a **gimbal stand** and/or **guide rails / hard tether** and **net/arena**.
- **Mass properties tooling** — scale; CoG rig (knife-edge / multi-point) to place CoG relative to the thrust centroid.
- **Data logging** — force, puck/gimbal angles, IMU, currents, temperatures.

---

## 5. Specifications

| Element | Specification | Notes |
|---|---|---|
| Pucks | N **[TBD]**, thrust axes aligned to lift axis, datums indexed | more pucks → more thrust *and* more mass (T/W ~ constant if both scale) |
| Per-puck thrust | **[TBD]** — measure first (SOP-070 / thrust stand) | do not assume; it sets everything |
| Vehicle dry mass | **[TBD]**, minimised | mass is the enemy of T/W |
| T/W target | **> 1 with margin** (e.g. ≥1.3) for controllable lift | Stage A measures the actual value |
| CoG | **on and below** the thrust centroid by margin *h* | passive pendulum stability (App. B) |
| Vectoring authority | tilt range + rate sufficient for attitude control | quantify on the gimbal stand |
| Kill-to-null | net thrust → 0 on command **and** on power loss, within [TBD] time | the fail-safe; verify before lift |
| Stage A rig | measures force while **preventing escape** | load cell + gimbal/rails/tether + net |
| Stage B gate | T/W>1 margin **AND** control shown **AND** kill verified | all three, no exceptions |

---

## 6. Procedure

### Stage A — constrained demonstrator (produces the data)

#### 6A.1 Mount and align
1. Confirm each puck passed **SOP-060 §6.5 / App. A**. Mount N pucks with **thrust-axis datums indexed** so all thrusts point along the vehicle lift axis.

#### 6A.2 Mass properties
1. Weigh the assembled vehicle. Set **CoG on and below the thrust centroid** by the stability margin *h* (Appendix B) using placement/ballast. Record mass and CoG.

#### 6A.3 Install on the constrained rig
1. Mount the vehicle to the **load-cell / gimbal / rail** rig so it **cannot escape** in any axis. Verify the restraint before powering the pucks.

#### 6A.4 Measure thrust and the vectoring map
1. Power up; log **net vertical force** vs commanded puck/gimbal angles. Derive **net thrust** and the **vectoring authority map** (tilt vs command).
2. Compute **T/W** = net thrust ÷ measured weight. **Record honestly**, including T/W < 1.

#### 6A.5 Verify kill-to-null (fail-safe) — before any lift
1. Command **kill-to-null**; confirm net thrust falls to ~0 within spec.
2. **Cut power** to the vectoring actuators/controller; confirm the mechanism defaults to (or can be driven to) net-zero — the vehicle must not be left in a full-lift state on failure. Redesign until this holds.

#### 6A.6 Attitude-control test (gimbal stand)
1. On the gimbal stand, command attitude corrections; verify the vectoring produces **stabilising** response; measure control **authority and bandwidth**.

#### 6A.7 Stage A acceptance / GATE
1. Proceed to Stage B **only if all three**: **T/W > 1 with margin**, **attitude control demonstrated**, **kill-to-null verified (incl. power-loss)**. Otherwise stop — iterate mass, puck count, or control, or **report the null** and hold.

### Stage B — free flight (gated)

> Enter only past the §6A.7 gate. Tethered-in-arena before open flight; never over persons.

#### 6B.1 Tethered hover
1. In the **netted arena**, on a **short hard tether**, attempt a low, height-limited hover. Remote **kill** in hand. Verify stability and control against Stage A predictions.

#### 6B.2 Incremental untether (within arena)
1. Only after stable tethered hover, extend excursion **inside the arena/net**. Keep the kill immediate. **No personnel underneath.** Expand envelope in small, logged increments.

---

## 7. Acceptance criteria and QC

- **Mass properties:** vehicle mass and **CoG below thrust centroid** by margin, recorded.
- **Stage A thrust:** net thrust and **T/W measured on the constrained rig**, logged with nulls.
- **Vectoring:** authority map and attitude-control bandwidth quantified.
- **Fail-safe:** **kill-to-null verified on command and on power loss** — mandatory before any lift.
- **Gate:** Stage B entered only with T/W-margin **and** control **and** kill all satisfied.
- **Stage B:** tethered-in-arena first; kill immediate; no overhead personnel; incremental logged envelope.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| No lift (T/W < 1) | Mass exceeds thrust — the likely honest outcome → minimise structure/mass, add pucks (note T/W is ~constant if thrust and mass both scale — you need thrust *density*), or **report the null** and stop. |
| Unstable / diverging attitude | CoG at/above thrust line, or weak control → lower CoG below the thrust centroid (App. B); increase vectoring authority/bandwidth. |
| Cannot null thrust | Fail-safe inadequate → redesign kill-to-null; **do not attempt lift** until verified, including on power loss. |
| Vibration / resonance | Airframe modes near control/vectoring rates → stiffen/detune; damp puck mounts. |
| Vehicle strains the rig unexpectedly | Real lift present — good, but stay constrained → keep restraint until the §6A.7 gate is fully met. |

---

## 9. Waste and storage

- Store pucks per SOP-060 §9. Safe the vehicle (kill-to-null engaged, power isolated) between runs.
- Retain mass-property records, Stage A force/vectoring/fail-safe logs, and Stage B envelope logs for provenance.

---

## Appendix A — Why staged, and the fail-safe-null rationale

- **You do not free-fly an unproven, un-switchable lifter.** The information (thrust, vectoring, control, fail-safe) comes from the **constrained** rig; free flight only adds risk until those are known. Stage A is where the science is.
- **Kill-to-null is the kill.** Because the thrust cannot be switched off (hypothesis), safety rests on being able to drive **net** thrust to zero — mechanically, and by default on failure. Treat any state that leaves full lift on a fault as a design defect.
- **Report the null.** T/W < 1 is the expected and honest result until measurement shows otherwise. Publishing it is a credibility asset, consistent with the project's test-first philosophy.

## Appendix B — T/W and pendulum-stability (worked relations)

- **Lift condition:** net thrust T_net > weight m·g, i.e. **T/W > 1**. Controllable lift wants margin (e.g. ≥1.3).
- **Scaling caution:** if per-puck thrust and per-puck mass both scale ~linearly with puck count, **T/W is roughly constant with N** — adding pucks raises absolute thrust (and mass) but not the *ratio*. Lifting therefore needs thrust **per unit mass** > g, not merely "more pucks." State this plainly in any write-up.
- **Passive (pendulum) stability:** with CoG a distance *h* **below** the thrust centroid, a tilt θ creates a restoring moment ≈ m·g·h·sinθ. Larger *h* → stiffer passive stability; CoG **above** the thrust line is statically unstable and requires active control to fly.
- **Active margin:** if CoG cannot be placed below the thrust line, the vectoring loop must supply the stabilising moment — quantify authority and bandwidth (§6A.6) against the divergence rate before trusting it.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 0.1 | ____ | Croft Swonyoung | **Initial draft.** Staged integration of ruggedized pucks (SOP-060 App. A) into a flying-vehicle test article: **Stage A** constrained thrust/lift measurement (net thrust, vectoring map, attitude authority, **kill-to-null** fail-safe verified incl. power-loss) producing the **T/W** data; **Stage B** free flight **gated** on T/W>1-with-margin + demonstrated control + verified kill, tethered-in-arena first. Emphasises CoG-below-thrust-centroid stability, the un-switchable-thrust fail-safe philosophy, honest-null reporting, and the T/W-constant-with-N scaling caution. Airframe/puck-count/per-puck-thrust/mass left **[TBD]** pending inputs and a measured per-puck thrust (SOP-070 or thrust stand). |
