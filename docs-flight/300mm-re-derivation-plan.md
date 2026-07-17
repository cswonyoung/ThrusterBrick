# 300 mm re-derivation plan — flying-machine line

Working plan for deriving the 300 mm flight line (`docs-flight/`) from the
established 150 mm rotor line (`../docs-rotor/`) in this same repository. The
**chemistry is unchanged**; what changes is geometry,
tooling, bath scale, and mass. Numbers below are **scaled estimates to confirm**,
not final — decisions the maker must lock are flagged **[DECIDE]**.

## 1. Datum change (150 mm → 300 mm)

| Parameter | 150 mm (current) | 300 mm (proposed) | Note |
|---|---|---|---|
| Wafer diameter | ⌀150.0 | **⌀300.0** | — |
| Wafer thickness | 0.675 mm | **0.775 mm** | SEMI standard for 300 mm — **[DECIDE/confirm]** |
| Active (etched) region | ⌀130 (10 mm margin) | **⌀280** (keep 10 mm margin) | or scale margin → ⌀260 **[DECIDE]** |
| Zinc foil thickness | 0.15 mm | **0.15 mm (unchanged)** | template thickness is wafer-independent — **[confirm]** |
| Zinc handling rim | 13 mm | **13 mm (unchanged)** | or scale **[DECIDE]** |
| Zinc blank | ⌀156 | **⌀306** | = active ⌀280 + 2×13 rim |
| Ni-P thickness | 25 µm | **25 µm (unchanged)** | thickness is diameter-independent |
| Per-cell pitch | ≈0.78 mm | **≈0.875 mm** | wafer 0.775 + Ni-P 0.025 + bond ~0.075 |
| Per-cell mass | ≈32 g | **≈140 g** | ~4.4× (Si ⌀300×0.775 ≈128 g + Ni-P ≈12 g + bond) |
| Active area / cell | (⌀130) | **~4.6×** | (280/130)² — drives thrust *and* handling |

## 2. Per-document work

**Fabrication chain (re-derive each at the new datum):**
- **SOP-010** (ZnO growth) — ⌀306 zinc blank; bath volume ~4× (vessel ⌀360–400+);
  growth chemistry unchanged, immersion geometry scaled.
- **SOP-020** (APTES + Ag seed) — seeding carrier scaled to ⌀306; glovebox/vapour
  chamber must clear the larger coupon; reagent volumes ~4×.
- **SOP-030** (electroless Ni-P) — bath ~4× (~6–10 L; vessel ⌀360–400+); plating
  chemistry and 25 µm target unchanged; longer fill/agitation for the larger area.
- **SOP-040** (caustic strip / clean / dry) — strip time set by **area not
  thickness**, so ~4× the H₂/zincate load and bath charge; the ~10–12 h
  void-clearing is void-geometry-limited (unchanged); larger dry fixtures.
- **SOP-050** (Phase-1 wafer bond + de-rim) — ⌀300 wafer chuck; bigger bond fixture;
  chemical de-rim self-stops at ⌀280; handle 300 mm wafer fragility.
- **SOP-060** (Phase-2 vacuum stack close) — ⌀300 stack; envelope + chamber sealer
  must clear ⌀300+; getter sized to ~4× area/outgassing; platens ⌀≥300 (step to
  ¼″ likely needed for flatness under load); **N and mass budget re-computed** (see §3).

**Design references (rewrite to the ⌀306 datum, bump revs):**
- **DR-001…005** — carrier/bath/immersion/strip references at the new diameter;
  larger vessels; re-do nesting (a ⌀340+ carrier likely = 1 plate per larger sheet).
- **DR-006** — wafer bonding chuck for 300 mm.

**DXF cut set (regenerate all at the new datum):**
- Carrier plate: outer ~⌀340–360 **[DECIDE]**, window ⌀280, coupon pocket ⌀306.3,
  O-ring groove ~⌀293, bolt circle ~⌀324 ×16 M4 **[DECIDE]** (more bolts for the
  larger plate); PP/PVDF backer + clamp frame scaled; aluminium wafer chuck → ⌀300.
- New/larger stock sizes — confirm bed/sheet size against your cutter.

**Application integration:**
- **SOP-080** (flying-vehicle) — re-derive against the 300 mm ruggedized puck
  handoff (§4) and the new masses; complete the `[TBD]` fields (per-puck thrust,
  vehicle mass, T/W). Currently in `docs/` as a 150 mm-based **seed**.

**Consolidated shop packet:**
- **SP-001** — full rewrite to the 300 mm datum (index, purchasing, station list,
  bath volumes, fixtures).

## 3. Mass / stack recompute (flyer-critical)

- Per-cell ≈140 g at 0.875 mm pitch. A stack of N cells ≈ **0.14N kg** active +
  platens + envelope/getter.
- **Honest scaling caveat:** active area (~4.6×) and cell mass (~4.4×) scale
  *together*, so going to 300 mm raises **absolute** thrust and mass in step —
  **thrust-to-weight is roughly scale-invariant.** The 300 mm choice buys larger
  absolute thrust per layer and fewer cells/interfaces for a given area, **not**
  a better lift ratio. Confirm the intended rationale before committing, and keep
  T/W > 1 as the open, to-be-measured question (SOP-080).

## 4. Ruggedization at 300 mm (SOP-060 Appendix A equivalent)

- Edge-cushion **rim strip**: width = stack height H; length = π(D + s) ≈
  **π(301) ≈ 946 mm**; same 50 A / 1.0 mm platinum-silicone, E595, vacuum-baked.
- Optional recessed **end-ring**: OD 300, ID ≥ (active ⌀280 + margin), recessed
  into the platen (never proud in the preload path).
- **Carrier pot**: larger, heavier; same filled low-exotherm epoxy discipline;
  CoG/mass budget set by the flyer's needs, not a rotor's 128 G.

## 5. Equipment / cost implications

- ~4× reagent volumes; vessels, glovebox, and **chamber sealer** all sized for
  ⌀300+ — the sealer clearance is a likely long-lead/cost item.
- 300 mm wafers: higher unit cost, more fragile handling, larger clean staging.

### 5.1 Cutter (router) bed sizing
The bed size is driven by the largest single part — the **shared carrier plate**.
On the 150 mm line that plate is ⌀190 (⌀156 coupon) and cuts ~1/sheet on a
~300 × 287 mm bed. At 300 mm the coupon (zinc blank) is ⌀306, so the carrier
scales to roughly **⌀350–380** (straight 2× → ⌀380; coupon ⌀306 + the same
absolute land/bolt-circle margins → ⌀340–356). Add ~30–50 mm workholding all
round → stock blank ~⌀450–480.

| Usable cutting envelope | Fit |
|---|---|
| ~**500 × 500 mm** (minimum) | one ⌀380 carrier with clamps; tight |
| ~**600 × 600 mm** (24″×24″, recommended) | carrier + companion parts (clamp frame, backer) without re-fixturing |
| ~**600 × 900** or **1220 × 1220** (4′×4′) | nesting / full-sheet stock |

Heuristic: **≈ double each dimension of the current ~300 × 287 bed → ~600 × 600**.

**DECIDED (2026-07-15):** target a standard **500 × 600 mm** bed. The carrier is
held to ⌀≤~380 to fit with clamp margin; **lock the carrier at ⌀350** (see
`300mm-datum-reference.md`) so clamping stays comfortable on the 500 mm axis (use
the 600 mm axis for clamp length; ⌀350 + ~2×50 mm ≈ ⌀450 blank fits 500 × 600).

**Caveat — the aluminium chuck needs another machine.** The carriers are plastic
(PVDF/PP/PEEK) and suit the 500 × 600 router. The **aluminium wafer chuck at
⌀300+** is a heavier cut; **waterjet is ruled out on cost**, so the options are a
**rigid mill**, a **slow router pass** (right bit/feeds, stepped depths),
**outsourcing** just that part, or reconsidering the chuck material (a thick, flat
polymer or cast tooling-plate alternative) — decide when the chuck is designed.

## 6. Open decisions (flag before building)

1. Wafer thickness (0.775 mm standard vs thinned) — **default 0.775 mm** in the
   datum reference; confirm.
2. Active-region margin (fixed 10 mm → ⌀280, or scaled) — **default 10 mm** (⌀280);
   confirm.
3. Zinc rim width and blank ⌀306 vs scaled — **default 13 mm → ⌀306**; confirm.
4. Carrier outer ⌀ and bolt pattern — **RESOLVED: ⌀350 outer, bolt circle ⌀330 ×16
   M4** (bounded by the 500 × 600 bed; see the datum reference); confirm bolt
   count/size against your cutter.
5. **Numbering — RESOLVED:** `-300` suffix on the 150 mm step numbers
   (`ZnO-SOP-010-300`, `ZnO-DR-001-300`, `ZnO_cut_<part>_300.dxf`).
6. **300 mm rationale — RESOLVED:** handling / throughput (fewer, larger parts per
   unit active area); T/W ~scale-invariant, so the win is process efficiency, not
   lift ratio.
