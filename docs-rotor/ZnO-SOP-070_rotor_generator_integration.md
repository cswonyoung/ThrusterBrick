<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Rotor Integration & Commissioning — self-driven rotor demonstrator / high-gain thrust-hypothesis test
### Ruggedized pucks on a balanced rotor · vectored thrust · fail-safe braking · N pucks in opposed pairs (min 2)

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-070 | Revision | 0.1 (DRAFT) |
| Effective date | ____________ | Supersedes | — (new) |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-060 Appendix A (ruggedized puck: carrier datum + CoG budget) | Next step | Operation / data logging |
| Variant | 2…N pucks, opposed pairs · r = 457 mm · 500 rpm · ≈128 G at puck | — | — |

---

## 1. Purpose and scope

This procedure integrates **ruggedized pucks** (ZnO-SOP-060 Appendix A — potted into a carrier, with a documented **thrust-axis datum** and **CoG within budget**) onto a **self-driven rotor**. The rotor has two purposes at once:

1. **A power demonstrator.** *If* the hypothesised per-puck thrust exists, each puck's thrust can be vectored tangentially to drive the rotor, and the shaft can drive a generator / power take-off (PTO).
2. **A high-gain test of the thrust hypothesis.** The rotor is a large, low-loss mechanical integrator: a small steady tangential force accumulates into measurable angular acceleration and self-sustained speed. Built with the confound controls of §6.9 and Appendix A, it is a sensitive, **self-controlling** test that is informative **whether the thrust is real or null.**

> **Hypothesis discipline.** No net thrust has been measured. Nothing in this document asserts that the rotor will self-drive or generate power. The rig is engineered to be **safe and informative in the absence of an effect** — a rotor that will not spin under its own pucks (once drag is accounted for) is a valid, publishable result, not a failure. State the goal plainly as *what is being tested*, never as *what has been shown*.

**Governing numbers** (recompute for your build):

| Quantity | Value | Basis |
|---|---|---|
| Rotor radius *r* | 457.2 mm (18 in) | to puck CoG |
| Speed | 500 rpm = 52.36 rad/s | design point |
| Centripetal accel. at puck | ω²r ≈ 1253 m/s² ≈ **128 G** | sets SOP-060 App. A spec |
| Rim speed | ωr ≈ **23.9 m/s** (~54 mph) | windage + projectile energy |
| Thrust goal (whole rotor) | **50 lbf ≈ 222 N** | design goal |
| Drive torque at goal | 222 N × 0.4572 m ≈ **102 N·m** | all pucks tangential |
| Shaft power at 500 rpm | τω ≈ **5.3 kW** | the ~5 kW design target |
| Pucks | even number, opposed pairs, **min 2** | rotor balance |

> **Thrust units (avoid the classic slip).** The goal is **50 lbf ≈ 222 N** — note **1 lbf ≈ 4.45 N, *not* ≈1 N**. At 18″/500 rpm that gives τ ≈ 102 N·m and **P ≈ 5.3 kW**, the intended ~5 kW target. (An earlier "50 N" figure was the lbf→N slip; 50 N at this geometry would deliver only ≈1.2 kW.)

**Out of scope:** puck fabrication and ruggedization (ZnO-SOP-010…060); detailed electrical design of the generator/PTO and load (referenced, not specified); the flying-vehicle application (the 300 mm line in `../docs-flight/`).

---

## 2. Definitions and interpretation

- **Puck.** A ruggedized, potted stack from SOP-060 Appendix A, carrying a **thrust-axis datum** (indexed to the shiny-Si / hypothesised-thrust direction) and a **CoG within the App. A budget**.
- **Spin axis.** Each puck rotates on its **own axis, vertical and parallel to the main rotor axis.** Parallel axes are deliberate: they null gyroscopic precession torque from the rotor's rotation.
- **Thrust vectoring.** Rotating the puck about its spin axis points the (hypothesised) body-fixed thrust: **tangential = drive**, **radial = null (no rotor torque)**, **anti-tangential = brake**. A stepper sets the angle.
- **Opposed pair.** Two pucks at equal radius, 180° apart, oriented in **mirror image** so both drive the *same* rotational sense (tangential points opposite ways on opposite sides). Even numbers only, so the rotor stays statically balanced.
- **On-board controller.** Rides the rotor; monitors rotor speed and trims puck angle to hold the set speed; executes graceful shutdown by nulling the pucks.
- **Off-board controller.** Stationary; independent speed monitor; commands the master brake on overspeed or loss of the on-board health signal.
- **Signal logic — "low-to-slow" (fail-safe).** Both slip-ring signal lines are energised-to-run: a **fault** line (on-board health) and a **graceful-shutdown** line (manual). **Loss of either (wire cut, power loss) stops the machine** — the brake is spring-applied and released only by power/signal.
- **Master brake.** A **fail-safe-applied** friction brake (spring-clamped, held *off* by power). Sized to **hold against stall thrust** (N·T·r) *and* absorb rotor kinetic energy plus the work the pucks add during a stop. A car-derived rotor/caliper has ample capacity but **must be re-plumbed spring-apply / power-release** — a normal service brake fails *off* and would violate the fail-safe logic.
- **Thrust-vector braking (2nd channel).** With control healthy, the on-board controller can vector pucks anti-tangential to decelerate — an independent stop that fails in a different mode than the friction brake. Costs no extra hardware.
- **Containment cage.** A **closed-geometry** steel enclosure (not a fence) rated to catch a liberated puck at rim speed (see Appendix B for energy). Bearing/axle failure can throw a puck **out of plane** — cover top and bottom.
- **Windage.** Aerodynamic drag/torque on pucks moving at ~24 m/s (open-air build). Parasitic; shape pucks **edge-on** to the airflow to spare the steppers and reduce the thrust needed to self-sustain.
- **Self-sustain condition.** Steady speed holds when **puck tangential thrust = total drag torque** (windage + bearing + PTO load) at that speed.

---

## 3. Health, safety and environment

- **Stored rotational energy + projectile hazard.** Pucks at ~24 m/s carry tens of joules each (Appendix B); a liberated puck is an airgun-class projectile. **Closed containment cage, rated; hard exclusion zone; no personnel in the plane of the rotor during spin.**
- **The thrust cannot be switched off (hypothesis).** All stop authority rests on the **fail-safe brake** (+ thrust-vector braking). Prove the brake holds against stall **before** first puck-driven run.
- **Remote/interlocked operation.** Start, run, and stop from outside the cage; door interlock inhibits run; emergency stop drops power (→ brake clamps).
- **Rotating machinery / entanglement / pinch** — standard guarding; no loose clothing; lockout for access.
- **Electrical** — slip-ring power, controller supplies, PTO/generator output; isolate and lock out for service.
- **PPE:** eye/face protection outside the cage; hearing protection (windage/bearing noise).

---

## 4. Materials and equipment

- **Rotor arm** (balanced), **vertical spindle**, **2 × pillow-block bearings** (one each end) rated for the load (Appendix B), non-slump lubrication (grease can separate/fling under sustained 128 G — oil-with-seals or solid lube preferred).
- **N × puck holders** with **stub axles**, puck-spin bearings (rated for the sustained radial load ≈ 1253·m_puck N), and **CoG trim masses** (opposed, lockable, two in-plane axes).
- **N × stepper motors** (or a synchronised drive) with **angle encoders**; steppers themselves rated for 128 G radial while on the arm.
- **Slip-ring assembly** — power, ground, and **two signal lines** (fault, graceful-shutdown).
- **On-board controller** and **off-board controller** with **independent** rotor-speed sensors (two channels).
- **Master brake** — fail-safe-applied (spring-clamp / power-release), holding torque > stall (Appendix B).
- **Closed steel containment cage**, rated; door interlock.
- **Vibration sensor(s), temperature sensors** (bearings, steppers), current monitoring.
- **External commissioning drive** (motor to spin the rotor *without* relying on puck thrust) with a torque/coast-down means to measure drag.
- Optional **generator / PTO + load bank** to extract and dissipate shaft power.
- Balancing capability (in-situ two-plane, or a balancing machine).

---

## 5. Specifications

| Element | Specification | Notes |
|---|---|---|
| Rotor radius / speed | 457 mm / 500 rpm | ≈128 G at puck; rim ≈23.9 m/s |
| Pucks | even, opposed pairs, **min 2**; thrust-axis datum indexed | mirror-orient opposite pairs |
| Puck CoG | **on the puck spin axis** (both in-plane coords) | nulls stepper holding torque *and* rotating imbalance; consumes App. A CoG budget |
| Rotor balance | static **and** dynamic (couple); grade per ISO 1940 (target ~G2.5, confirm) | balance with pucks at a defined reference angle |
| Bearings | pillow blocks + puck axles rated to sustained radial load (Appendix B); non-slump lube | grease slump under steady 128 G is a real failure mode |
| Signal logic | two lines, **low-to-slow**; loss of either → brake | verify by wire-cut test |
| Master brake | **fail-safe-applied**; holding torque **> N·T·r** + decel margin | car-derived OK **only if re-plumbed spring-apply** |
| Overspeed | off-board watchdog trips brake above set rpm | independent of on-board channel |
| Containment | closed geometry, rated to puck rim energy | top + bottom covered |
| Windage | pucks shaped edge-on | parasitic drag sets self-sustain thrust |
| PTO/load | optional generator + dissipative load ≤ available shaft power | ~5.3 kW at 50 lbf |

---

## 6. Procedure

### 6.1 Pre-integration checks
1. Confirm each puck passed **SOP-060 §6.5 and Appendix A** (verified brick, potted void-free, thrust-axis datum marked, CoG measured and within budget). Reject otherwise.

### 6.2 Mount pucks
1. Seat each puck in its holder, **indexing the thrust-axis datum** to the holder's tangential reference.
2. For each **opposed pair**, set the two pucks in **mirror orientation** so both drive the same rotational sense. Set both to equal radius.

### 6.3 CoG trim (per puck)
1. Using the trim masses, null each puck's CoG **onto its spin axis** in both in-plane coordinates (balance the holder on the axles / two-plane check). Lock the trims. This nulls the sustained stepper holding torque *and* the per-puck rotating imbalance.

### 6.4 Rotor balance
1. With pucks at a **defined reference angle** (e.g. all radial), balance the rotor **statically and dynamically** (couple), even pairs, to the target grade. Record residual imbalance.

### 6.5 Slip rings and signal logic
1. Fit the slip-ring assembly; wire power, ground, and the two signal lines.
2. **Verify low-to-slow:** with the machine safe and stationary, cut/de-energise each signal line in turn and confirm the **brake engages** (spring-applied). Both lines must fail safe.

### 6.6 Master brake
1. Fit the fail-safe-applied brake. **Confirm it is spring-applied / power-released** (power off → clamped).
2. Measure **holding torque**; confirm it exceeds **stall** (N·T·r at the thrust goal) with margin (Appendix B).

### 6.7 Containment
1. Fit the closed steel cage; verify top/bottom coverage and door interlock (open → run inhibited).

### 6.8 Commissioning **without** relying on puck thrust
> Establish that the *machine* is sound before asking the *pucks* to do anything.
1. With pucks at **null (radial)**, spin the rotor with the **external drive** in steps (e.g. 50 → 500 rpm). Log vibration, bearing/stepper temperature, slip-ring integrity. Abort on out-of-band vibration; rebalance.
2. From speed, verify the **brake stops** the rotor and that the **overspeed watchdog** trips independently.
3. **Measure drag torque vs speed** (drive-torque reading or coast-down from each speed). This defines the **thrust required to self-sustain** at 500 rpm — the number the thrust goal must beat. Record the drag curve.

### 6.9 Puck commissioning — the thrust-hypothesis tests (with confound controls)
> Run these with the external drive **disengaged** unless noted. See Appendix A for the full confound protocol.
1. **Null test.** All pucks **radial**; release the brake from rest. The rotor must **not self-accelerate** (no net tangential force). Any spin-up here indicates an artifact (air current, magnetic, wiring, vibration rectification) — hunt it down before proceeding.
2. **Drive test (core).** Set pucks **tangential**; from rest, brake released, no external drive. Log angular acceleration and any self-sustained speed. Compare the measured torque to the ≈102 N·m the 50 lbf goal predicts, and to the §6.8 drag curve.
3. **Reversal test (control).** Reverse all pucks to **anti-tangential**. The torque should **reverse sign** — same hardware, orientation only. This is the primary control against systematic artifacts: a real body-fixed thrust flips with the pucks; most confounds do not.
4. **Balanced-pair null.** Orient one pair opposed (equal and opposite tangential): net torque should cancel → coast. Confirms the effect scales with alignment, not with mere spinning.
5. Record all four outcomes, **including nulls**, with the drag curve as the baseline.

### 6.10 Operation
1. Hold the set speed by closed-loop trim of puck angle (on-board controller). Keep trims small; large slews are for start/stop.
2. Engage the PTO/generator and dissipative load as required; log speed, puck angles, currents, temperatures, vibration.

### 6.11 Shutdown
1. **Graceful:** on the shutdown signal, the on-board controller **nulls the pucks** (radial) or vectors them anti-tangential to decelerate; the rotor coasts/brakes down; park the master brake.
2. **Emergency / fail-safe:** loss of either signal, overspeed, or E-stop → **master brake clamps** (spring-applied) and holds against stall.

---

## 7. Acceptance criteria and QC

- **Balance:** static + dynamic within the target grade; vibration within band across 50–500 rpm.
- **Brake:** verified **fail-safe-applied**; holding torque > stall; stops the rotor from overspeed.
- **Signal logic:** both lines verified **low-to-slow** (wire-cut test engages brake).
- **Overspeed watchdog:** trips independently of the on-board channel.
- **Containment:** closed geometry, rated to puck rim energy; interlock functions.
- **Bearings/steppers:** temperatures stable at 500 rpm; lubrication non-slump.
- **Drag baseline:** §6.8 drag curve recorded.
- **Hypothesis tests:** §6.9 null, drive, reversal, balanced-pair outcomes logged **with nulls reported honestly**; reversal sign-flip (or its absence) documented.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Excess vibration | Residual imbalance / CoG off spin axis → re-trim pucks (§6.3), rebalance rotor (§6.4). |
| Won't hold set speed | Drag > available thrust, or control loop → check §6.8 drag vs thrust goal; reduce windage (edge-on pucks), lighten PTO load; tune loop. |
| Overspeed / runaway | Puck stuck at drive angle → confirm brake **> stall** and that the watchdog trips; add mechanical means to force pucks radial if margin is thin. |
| Brake won't hold / won't stop | Wrong brake type (fails off) or actuator fault → confirm **spring-applied / power-released**; service actuator. |
| Bearing overheating | Lube slump under 128 G → oil-with-seals or solid lube; verify axle rating. |
| Slip-ring noise on signals | Contact/EMI → filter, shield, debounce; fail-safe logic must still trip on true loss. |
| No self-drive at drive angle | Possible **null result** (no net thrust) — a valid outcome. Confirm against §6.8 drag and the reversal test before concluding; report honestly. |

---

## 9. Waste and storage

- Store pucks per SOP-060 §9. Lock out the rotor when not in use (brake parked, power isolated).
- Retain per-run logs (speed, angles, currents, temperatures, vibration, drag baseline, hypothesis-test outcomes) for provenance.

---

## Appendix A — Confound controls and the honest-null protocol

The rotor is a sensitive integrator, which means it is also sensitive to **artifacts**. Design the test to **convince yourself in the absence of an effect** (the project's guiding rule); controls are for catching self-deception, not for placating critics.

- **Reversal is the master control.** A body-fixed thrust reverses sign when the pucks are flipped (§6.9.3); airflow, stray magnetic/electrostatic forces, wiring reaction, and vibration rectification largely do not. Always pair a drive run with a reversal run.
- **Null orientation must coast.** Pucks radial → no net tangential force. Self-spin here is an artifact to be eliminated (shroud against room air currents; shield stray fields; route wiring symmetrically; isolate vibration).
- **Balanced-pair null** confirms the effect scales with alignment, not with the mere fact of spinning.
- **Blind the operator where practical** (randomise drive/reversal/null order; log by code) so expectation cannot bias trimming.
- **Report nulls.** An honestly documented null is a feature. Do not tune the rig until it "works."

## Appendix B — Governing equations (worked)

- Centripetal accel.: a = ω²r; ω = 2π·rpm/60. At 500 rpm, r = 0.4572 m → a ≈ 1253 m/s² ≈ 128 G.
- Rim speed: v = ωr ≈ 23.9 m/s.
- Drive torque: τ = N·T·r (all tangential). At T_total = 50 lbf ≈ 222 N, r = 0.4572 → τ ≈ 102 N·m.
- Shaft power: P = τω ≈ 102 × 52.36 ≈ 5.3 kW. (Unit check: 50 lbf = 222 N, 1 lbf ≈ 4.45 N; the ~5 kW target is met. A "50 N" goal would give only ≈1.2 kW.)
- Puck projectile energy: E = ½·m·v² ≈ 285·m J (m in kg) → e.g. 0.2 kg ≈ 57 J. **Size the cage to this.**
- Puck sustained radial (bearing) load: F = m·a ≈ 1253·m N → e.g. 0.2 kg ≈ 251 N.
- Windage (open-air): q = ½ρv² ≈ 0.5·1.225·23.9² ≈ 350 Pa; broadside drag ≈ q·A_face; drag *power* ≈ drag·v (parasitic — feeds the self-sustain thrust requirement).
- Brake sizing: holding torque > **stall** (N·T·r ≈ **102 N·m** at the 50 lbf goal) with margin; a single emergency stop also absorbs rotor KE + puck work during the stop (both modest vs a car brake's per-stop capacity).

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 0.1 | ____ | Croft Swonyoung | **Initial draft.** Integration + commissioning of ruggedized pucks (SOP-060 App. A) onto a self-driven, thrust-vectored rotor: opposed-pair mounting, CoG trim onto the spin axis, static+dynamic balance, slip-ring **low-to-slow** signal logic, **fail-safe-applied** master brake sized > stall, closed containment, windage handling, and a commissioning sequence that proves the machine on an external drive and measures the drag baseline **before** the puck-thrust hypothesis tests (null / drive / reversal / balanced-pair) with confound controls and honest-null reporting. Thrust goal is **50 lbf ≈ 222 N** → τ ≈ 102 N·m → **≈5.3 kW** at 500 rpm (the ~5 kW target); an earlier "50 N" was an lbf→N slip. |
