<!-- Public Domain Dedication: CC0 1.0 Universal -->
> **Public Domain · CC0 1.0 Universal.** Author: **Croft Swonyoung**. To the extent possible under law, the author has waived all copyright and related or neighbouring rights to this document and dedicates it to the public domain worldwide (CC0 1.0). No warranty. See `LICENSE` or <https://creativecommons.org/publicdomain/zero/1.0/>.
>
> Part of the *ZnO nanovoid process* document set. Verify file integrity against `CHECKSUMS.sha256`.

---

# Working Procedure & Specification

## Phase-1 Bonding: Silicone Bond, Butyl-Land Masking, and Rim Trim
### Foil-to-plate bond in the bonding/masking carrier — all silicone finished before any butyl exists

| Field | Value | Field | Value |
|---|---|---|---|
| Document no. | ZnO-SOP-050 | Revision | 3.2 |
| Effective date | ____________ | Supersedes | Rev 3.1 |
| Author | Croft Swonyoung | Approved by | ____________ |
| Predecessor step | ZnO-SOP-040 (strip / clean / dry) | Next step | ZnO-SOP-060 (Phase-2 stack close) |

---

## 1. Purpose and scope

This procedure performs **Phase 1** of the two-phase assembly: every silicone bond is made and fully cured here, in a bonding/masking carrier that physically shields the future butyl seal lands, before any butyl exists anywhere in the build. It bonds the freed Ni-P nanovoid foil (high-P face) to its aluminium plate, cures, and trims the sacrificial zinc rim. The output is a finished cell plate whose butyl lands have never seen silicone.

**Governing principle (two-phase assembly).** Silicone and butyl are separated **in time and by fixture**:
- **Phase 1 (this SOP):** all silicone bonds, made and cured with the butyl lands masked by the carrier.
- **Phase 2 (ZnO-SOP-060):** all butyl bonds, made by compression during the plate-by-plate stack close. No silicone is applied in Phase 2; no butyl is applied in Phase 1.

**Bonding direction is the safety principle.** Silicone is applied to the rigid aluminium plate; the fragile 25 µm foil arrives last and is **laid on, never pressed**.

**Support transfer via the zinc rim.** The unetched 13 mm zinc rim (from ZnO-SOP-040) tensions the etched centre like a drumhead through transfer; it is trimmed only after the plate bond has cured and taken over support.

**Substrate at entry:** clean, dry, rim-framed Ni-P nanovoid foil (mid-P void working face, high-P bond face), held under N₂.

**Output:** an aluminium-backed nanovoid cell plate, rim trimmed, working face open and clean, **butyl lands pristine (masked throughout)**, held under N₂ — ready for the Phase-2 glovebox close.

---

## 2. Definitions and interpretation

- **Bonding/masking carrier.** The Phase-1 fixture is the vacuum bonding platen with **PTFE film mask and clamp frame**, dimensioned in ZnO-DR-006. The mask is a 0.13 mm (0.005″) skived-PTFE picture-frame film lying on the plate's 13 mm top-face butyl land, its overhang clamped to the platen from outside the plate footprint; the plate's bottom-face land is masked by contact with the platen itself. Nothing tall sits over the border, so the rim-framed foil can descend and land — and the film doubles as the bondline stop (rim lands on the film; foil centre sits at a ~0.13 mm bondline, ~100 µm target). The platen holds the plate dead flat by vacuum, supports the lay-down bond, and guarantees the butyl lands never contact silicone — the contamination rule is enforced by the fixture, not by care.
- **One silicone.** A single RT-cure, addition-cure, **thermally-conductive**, dielectric, low-outgassing silicone serves all Phase-1 bonds. The foil-to-plate joint is the thermal path and needs the conductive grade; consolidating on that grade satisfies every joint. Plain (non-conductive) structural silicone is used only for the outboard skin in Phase 2, applied from outside after closure.
- **Which face bonds.** Aluminium bonds to the **high-P (outer) face**; the **mid-P void face** stays open and later faces the N₂ cavity.
- **Conversion coating — Cr(VI)-free (Rev 3.2).** All aluminium conversion coating in this build is **hexavalent-chromium-free**: a trivalent-chromium process (MIL-DTL-5541 Type II class — e.g. SurTec 650, Bonderite T 5900) or a chromium-free Zr/Ti-based coating. These are functionally equivalent for adhesion and land corrosion protection on 5052/6061 and remove a Cr(VI) carcinogen from the flow. Legacy hex-chrome chromate (Alodine 1200-type) is **not permitted**; the requirement must be stated on purchase orders and outside-plating travellers so the plater's default cannot reintroduce it.
- **The spacer is NOT silicone-bedded.** In the two-phase architecture the aluminium spacer is bare, bonded top and bottom by butyl beads in Phase 2. No spacer bedding happens in this SOP.
- **Border does triple duty across time.** The ~13 mm border is the strip clamp, then the handling frame, then — after trim — the butyl seal land. Because the rim is trimmed before Phase 2, the butyl lands on clean conversion-coated aluminium, never on zinc (zinc creeps under sustained seal load).
- **Silver retained** in the void walls by design (ZnO-SOP-040).

---

## 3. Health, safety and environment

- **Silicone adhesive** — SDS; skin/eye irritant; ventilate during cure (addition-cure grades are low-byproduct).
- **Trimming** — mechanical or laser: standard cut/eye/fume precautions.
- **Vacuum platen** — pinch/implosion hazards are negligible at this scale; keep hands clear of the port.
- **Conversion coating** — performed by the supplier/plating shop; the Cr(VI)-free requirement (§2) removes hexavalent-chromium exposure from both the shop and any in-house touch-up.
- **PPE:** gloves, safety glasses, lab coat.
- **Waste:** trimmed rim is **zinc-bearing nickel** — segregate as heavy-metal metal scrap.

---

## 4. Materials, reagents and equipment

### 4.1 Reagents / consumables

- Thermally-conductive, dielectric, **RT / addition-cure**, low-outgassing silicone adhesive (the one Phase-1 silicone).
- Aluminium plate, pre-cut, conversion-coated — **trivalent-chromium (MIL-DTL-5541 Type II class, e.g. SurTec 650 / Bonderite T 5900) or Cr-free Zr/Ti-based; hexavalent-chromium coatings not permitted** — (5052 interior 0.025″; 6061 end plate 0.125″), **silicone-free**.
- Isopropanol; dry nitrogen.

### 4.2 Equipment

- **Bonding/masking carrier** (per ZnO-DR-006): vacuum platen (½″ MIC-6 aluminium, surfaced flat in place on the router) + **butyl-land film mask** (0.005″ skived PTFE, 130 × 155 outer / 74 × 99 window — consumable) + PVDF clamp frame with thumbscrews + venturi/pump, valve, gauge.
- Trim tool (shear/die/laser/router) cutting the rim flush without touching the void face.
- N₂ hold; PTFE-tipped tweezers; SEM/EDS; adhesion coupons.

---

## 5. Specifications

| Parameter | Specification | Notes |
|---|---|---|
| Bonded face | high-P (outer) Ni face → Al plate | mid-P void face stays open |
| Method | silicone on plate; foil laid on, not pressed | protects the 25 µm membrane |
| Silicone | thermally-conductive, dielectric, RT/addition-cure, low-outgassing | ONE grade for all Phase-1 bonds |
| Bondline | ~100 µm (0.004″), uniform, void-free | thermal path |
| Butyl-land protection | intact PTFE film mask clamped for every silicone operation (ZnO-DR-006) | lands verified clean before release; log film changes |
| Al prep | **Cr(VI)-free** conversion coat (trivalent-Cr Type II or Zr/Ti-based) or anodise; silicone-free | hex-chrome not permitted; seal-land cleanliness is a release gate |
| Cure | RT per silicone spec; vacuum hold through cure | plate flat throughout |
| Rim trim | flush to etched extent (13 mm border) | after cure; removes trapped edge zinc |
| Residual Zn (post-trim) | none detectable in the active part | edge EDS |

---

## 6. Procedure

### 6.1 Carrier set-up

1. Verify the platen face is clean and flat. Load the conversion-coated aluminium plate into the locating pocket (the platen face masks the plate's bottom-face land); pull vacuum; confirm seated and flat (gauge). Confirm the plate's traveller/cert shows a Cr(VI)-free coating per §5.
2. Lay a **clean, unused PTFE film mask** over the plate's 13 mm seal border, window centred; drape the overhang onto the platen and clamp it with the frame's thumbscrews. Never reuse a contaminated film or flip a used film; log the film change with the run ID.

### 6.2 Silicone application (lands masked)

1. Meter a thin, uniform layer of the Phase-1 silicone onto the plate's bond footprint, inboard of the film-mask window. The film physically covers the seal land, and PTFE releases any stray silicone.

### 6.3 Lay the foil (never press)

1. Bring the rim-framed foil to the plate, high-P face down, tensioned by its own rim. The zinc rim lands on the film mask, which sets the ~100 µm bondline.
2. Lay from one edge across, letting bondline air escape at the advancing front. Do not press.
3. Settle lightly; verify no trapped bubbles in the active area.

### 6.4 Cure and release

1. Cure at room temperature per spec, vacuum held, film mask clamped in place.
2. Release vacuum; unclamp the frame and remove the film mask (inspect it — any silicone on the film means replace it before the next run); lift the bonded assembly.
3. **Gate:** inspect the butyl lands — clean, dry, silicone-free (water-break or wipe test). Any silicone on a land = re-clean or scrap; the land cannot be reliably recovered by casual wiping.

### 6.5 Trim the rim

1. Trim the zinc rim flush to the etched extent (13 mm border), removing all trapped edge zinc. Keep tooling and debris off the void face.

### 6.6 Inspect and hold

1. Verify: void-free bond, no residual Zn at trimmed edges (EDS), working face clean/undamaged, lands silicone-free, assembly flat.
2. Hold under N₂. Label with run ID. The plate is now Phase-2-ready.

---

## 7. Acceptance criteria and QC

- **Bond:** continuous, void-free; passes adhesion check; no edge delamination.
- **Butyl lands:** verifiably silicone-free (this is the release gate for Phase 2).
- **Al coating:** supplier cert / traveller confirms Cr(VI)-free conversion coating per §5. If the coating chemistry changes (e.g. trivalent-Cr → Zr/Ti), re-run one silicone-adhesion coupon set before release.
- **Residual zinc:** none detectable in the active part (EDS).
- **Working face:** open mid-P voids clean, dry, undamaged, silicone-free.
- **Dimensional:** trimmed to etched extent; flat; bondline ~100 µm uniform.
- **Handling:** aluminium-supported, under N₂.

---

## 8. Troubleshooting

| Observation | Likely cause → corrective action |
|---|---|
| Bondline voids / bubbles | Laid too fast or silicone uneven → lay slower from one edge; meter evenly. |
| Membrane torn during lay-down | Rim tension lost or foil pressed → confirm rim intact; lay, never press; front-side support fallback. |
| Silicone found on a butyl land | Film mask torn, mis-placed, reused, or over-metered silicone → replace with a fresh film, verify window centring and clamping; reduce volume; solvent-clean + re-verify or scrap the land. |
| Edge delamination | Poor Al prep → re-prep with the qualified Cr(VI)-free conversion coating (§5); if a coating-chemistry change coincided, re-run adhesion coupons. |
| Residual Zn in active part | Trim short of the trapped-zinc line → trim to full etched extent; re-verify EDS. |

---

## 9. Waste and storage

- Zinc-bearing rim trim → heavy-metal metal scrap. Cured silicone per local rules.
- Store finished cell plates flat, working-face-protected, under N₂, labelled.

---

## 10. Revision history

| Rev | Date | Author | Change summary |
|---|---|---|---|
| 1.0 | ____ | ____ | Initial release (bond-in-carrier concept). |
| 2.0 | ____ | ____ | Out-of-carrier lay-down bond; zinc-rim handling frame. |
| 3.0 | ____ | ____ | Recast as Phase 1 of two-phase assembly: single Phase-1 silicone; butyl-land mask ring in the bonding carrier; land-cleanliness release gate; spacer bedding removed (spacer is butyl-bonded in Phase 2). |
| 3.1 | ____ | ____ | Mask ring replaced by 0.005″ PTFE film mask + clamp frame per ZnO-DR-006 (closes O7): film covers the top-face land and sets the bondline; platen face masks the bottom-face land; film treated as a logged consumable. |
| 3.2 | ____ | ____ | Lower-toxicity substitution: aluminium conversion coating specified as Cr(VI)-free (trivalent-Cr MIL-DTL-5541 Type II class, or Zr/Ti-based); hex-chrome explicitly prohibited; requirement flowed to purchasing/travellers; adhesion-coupon check on coating-chemistry change. |
