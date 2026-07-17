# Manifest — ZnO Nanovoid Process document set

All files are dedicated to the public domain under CC0 1.0 (see `LICENSE`). This
one set covers **two end-use lines** built from the same fabrication chemistry,
in two directories:

- **`docs-rotor/` — 150 mm rotor / generator line** (19 files, complete).
- **`docs-flight/` — 300 mm flying-machine line** (under construction).

## `docs-rotor/` — 150 mm rotor / generator line

| # | File | Description |
|---|------|-------------|
| 1 | `ZnO-DR-001_carrier_bath_design_reference.html` | Carrier & bath design reference (round) |
| 2 | `ZnO-DR-002_carrier_build_detail.html` | Carrier build detail (round plates, circular O-ring) |
| 3 | `ZnO-DR-003_immersion_carrier_cut_set.html` | Immersion & seeding carrier cut set (round) |
| 4 | `ZnO-DR-004_carrier_cutfile_nesting.html` | Carrier cut-file nesting (round) |
| 5 | `ZnO-DR-005_strip_carrier_cut_set.html` | Strip carrier cut set (round) |
| 6 | `ZnO-DR-006_wafer_chuck_cut_set.html` | Wafer bonding chuck cut set |
| 7 | `ZnO-SOP-010_nanotip_growth_10mM_depletion.md` | SOP-010 ZnO nanotip growth (10 mM depletion; ⌀156 / 0.15 mm Zn) |
| 8 | `ZnO-SOP-020_APTES_Ag_seeding.md` | SOP-020 APTES functionalisation & Ag seeding |
| 9 | `ZnO-SOP-030_electroless_NiP_plating.md` | SOP-030 electroless Ni-P plating |
| 10 | `ZnO-SOP-040_caustic_strip_clean_dry.md` | SOP-040 caustic strip / bulk clean / dry |
| 11 | `ZnO-SOP-050_phase1_wafer_bond_rim_trim.md` | SOP-050 Phase-1 wafer die-attach, chemical de-rim & final clean |
| 12 | `ZnO-SOP-060_phase2_vacuum_stack_close.md` | SOP-060 Phase-2 common-vacuum stack close (+ App. A application-agnostic ruggedization variant) |
| 13 | `ZnO-SOP-070_rotor_generator_integration.md` | SOP-070 Rotor integration & commissioning (self-driven rotor / thrust-hypothesis test) |
| 14 | `ZnO-SP-001_consolidated_shop_packet.html` | Consolidated shop packet |
| 15 | `ZnO_cut_PP_half.dxf` | Cut file — 1/2 in PP (strip backer, round) |
| 16 | `ZnO_cut_PP_threeEighth.dxf` | Cut file — 3/8 in PP (strip clamp frame, round) |
| 17 | `ZnO_cut_PVDF_quarter.dxf` | Cut file — 1/4 in PVDF (immersion/seeding carrier, round) |
| 18 | `ZnO_cut_frame_PVDF.dxf` | Cut file — PVDF clamp frame (RETIRED — no butyl mask) |
| 19 | `ZnO_cut_platen_alum.dxf` | Cut file — aluminium wafer bonding chuck |

## `docs-flight/` — 300 mm flying-machine line (🚧 under construction)

Naming: the 150 mm step numbers with a `-300` suffix (e.g. `ZnO-SOP-010-300`).

| File | Description | Status |
|------|-------------|--------|
| `300mm-datum-reference.md` | Master datum — the locked dimensions every 300 mm doc cites | **locked** (a few `[confirm]`s) |
| `300mm-re-derivation-plan.md` | What changes from the 150 mm datum, per document | working plan |
| `ZnO-SOP-010-300_nanotip_growth_10mM_depletion.md` | SOP-010 ZnO nanotip growth (⌀306 blank, 4–6 L bath) | **re-derived** (Rev 1.0) |
| `ZnO-SOP-020-300_APTES_Ag_seeding.md` | SOP-020 APTES functionalisation & Ag seeding | **re-derived** (Rev 1.0) |
| `ZnO-SOP-030-300_electroless_NiP_plating.md` | SOP-030 electroless Ni-P plating (⌀280 active; ~8–12 L bath) | **re-derived** (Rev 1.0) |
| `ZnO-SOP-040-300_caustic_strip_clean_dry.md` | SOP-040 caustic strip / bulk clean / dry (void-clear time unchanged) | **re-derived** (Rev 1.0) |
| `ZnO-SOP-050-300_phase1_wafer_bond_rim_trim.md` | SOP-050 Phase-1 wafer die-attach (300 mm wafer), de-rim & clean | **re-derived** (Rev 1.0) |
| `ZnO-SOP-060-300_phase2_vacuum_stack_close.md` | SOP-060 Phase-2 common-vacuum stack close (+ App. A ruggedization, 300 mm) | **re-derived** (Rev 1.0) |
| `ZnO-SOP-080-300_flying_vehicle_integration.md` | Flying-vehicle integration (staged lift demonstrator) | **seed** — still 150 mm-based; re-derive |
| `ZnO-DR-001-300_carrier_bath_design_reference.html` | Carrier & bath design reference | **re-derived** (Rev 1.0) ¹ |
| `ZnO-DR-002-300_carrier_build_detail.html` | Carrier build detail | **re-derived** (Rev 1.0) ¹ |
| `ZnO-DR-003-300_immersion_carrier_cut_set.html` | Immersion & seeding carrier cut set | **re-derived** (Rev 1.0) ¹ |
| `ZnO-DR-004-300_carrier_cutfile_nesting.html` | Carrier cut-file nesting (500 × 600 bed, 1 plate/sheet) | **re-derived** (Rev 1.0) ¹ |
| `ZnO-DR-005-300_strip_carrier_cut_set.html` | Strip carrier cut set | **re-derived** (Rev 1.0) ¹ |
| `ZnO-DR-006-300_wafer_chuck_cut_set.html` | Wafer bonding chuck cut set (⌀300; no waterjet) | **re-derived** (Rev 1.0) ¹ |
| `ZnO-SP-001-300_consolidated_shop_packet.html` | Consolidated shop packet (300 mm) | **re-derived** (Rev 1.0) |
| `ZnO_cut_PP_half_300.dxf` | Cut file — 1/2 in PP strip backer (⌀350 carrier; ×16 M4 on ⌀330) | **generated** ✓ |
| `ZnO_cut_PP_threeEighth_300.dxf` | Cut file — 3/8 in PP strip clamp frame (window ⌀280) | **generated** ✓ |
| `ZnO_cut_PVDF_quarter_300.dxf` | Cut file — 1/4 in PVDF immersion/seeding carrier (2 beds: window+handle, back/mask) | **generated** ✓ |
| `ZnO_cut_platen_alum_300.dxf` | Cut file — aluminium wafer chuck (⌀340 / recess ⌀300.5; no waterjet) | **generated** ✓ |
| `ZnO_cut_PP_half_300.svg` | To-scale plan (generated) — strip backer | drawing |
| `ZnO_cut_PP_threeEighth_300.svg` | To-scale plan (generated) — strip clamp frame | drawing |
| `ZnO_cut_PVDF_quarter_300.svg` | To-scale plan (generated) — immersion/seeding carrier (2 beds) | drawing |
| `ZnO_cut_platen_alum_300.svg` | To-scale plan (generated) — wafer chuck | drawing |
| `gen_round_dxf_300.py` | Parametric generator — emits the DXF cut set + to-scale SVG plans from the datum (stdlib; validate DXFs with ezdxf) | tool |

¹ Text/table dimensions are on the 300 mm datum. Each cut-set/nesting doc now embeds a **to-scale plan generated from the DXF geometry** (`ZnO_cut_*_300.svg`); the remaining hand drawings are schematic context.

**The 300 mm fabrication line and tooling are complete:** SOP-010–060-300,
DR-001–006-300, SP-001-300, the DXF cut set, and the reproducible **generator +
to-scale plan drawings**, all at the locked datum. DXFs validated with ezdxf.
(`ZnO_cut_frame_PVDF` stays retired — no 300 mm version.) Remaining: the
flying-integration procedure `ZnO-SOP-080-300` is still a 150 mm-based **seed**,
to be re-derived when the flyer / airframe is defined.
