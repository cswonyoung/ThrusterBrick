#!/usr/bin/env python3
# CC0 1.0 Universal (Public Domain Dedication) — Author: Croft Swonyoung.
# To the extent possible under law, the author has waived all copyright and
# related or neighbouring rights to this file. No warranty.
# https://creativecommons.org/publicdomain/zero/1.0/
# Part of the ZnO nanovoid process document set (300 mm flying line).
"""
gen_round_dxf_300.py — parametric cut-file generator for the ZnO nanovoid
process, 300 mm flying line (docs-flight/).

Single geometry model → two emitters:
  * R12 DXF  (mm, datum bottom-left, part centred on its bed) — matches the
    150 mm house format: 999 CC0 block, empty HEADER, fixed 8-layer table.
  * to-scale SVG plan view (same geometry, layer colours, key-⌀ caption) — the
    authoritative drawing embedded in the DR cut-set docs.

All dimensions come from 300mm-datum-reference.md. Stdlib only to generate;
validate the DXFs with ezdxf if available.

Usage:  python gen_round_dxf_300.py       # writes *.dxf and *.svg into docs-flight/
"""
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- locked 300 mm datum (diameters, mm; per 300mm-datum-reference.md) -----
CARRIER_OD, WINDOW_D, ORING_D, POCKET_D = 350.0, 280.0, 296.0, 306.3
BOLT_BC_D, BOLT_N, BOLT_START = 330.0, 16, 11.25          # ×16 M4, half-step off axis
HOLE_M4_CLR, HOLE_SMALL = 4.3, 3.3
# chuck (own stock, cut on a mill — no waterjet)
CHUCK_OD, WAFER_RECESS = 340.0, 300.5
VAC_RING_O, VAC_RING_I, CROSS_HALF = 240.0, 120.0, 120.0
PORT_D, FOOT_BC_D, TAP_M4 = 5.0, 310.0, 4.2
# beds
BED_W, BED_H, BED_GAP = 500.0, 600.0, 30.0               # DR-004-300: bed-B at +530

LAYERS = [("SHEET",8),("CUT",5),("WINDOW",4),("GROOVE",1),
          ("POCKET",3),("DRILL",2),("TAP",6),("DOWEL",7)]
SVG_COLOR = {"SHEET":"#b0b0b0","CUT":"#0050c8","WINDOW":"#00a0a0","GROOVE":"#c00000",
             "POCKET":"#008000","DRILL":"#d07000","TAP":"#a000a0","DOWEL":"#808080"}
CC0 = ["CC0 1.0 Universal (Public Domain Dedication)","Author: Croft Swonyoung",
 "To the extent possible under law, the author has waived all copyright and",
 "related or neighbouring rights to this file. No warranty.",
 "https://creativecommons.org/publicdomain/zero/1.0/",
 "Part of the ZnO nanovoid process document set (300 mm flying line)."]

# ---- geometry model (primitives) ------------------------------------------
def sheet(x0,y0,w,h):            return ("sheet",x0,y0,w,h)
def circ(lay,cx,cy,r):           return ("circle",lay,cx,cy,r)
def ln(lay,x1,y1,x2,y2):         return ("line",lay,x1,y1,x2,y2)
def bolts(lay,cx,cy,hole_d,n=BOLT_N,bc=BOLT_BC_D,start=BOLT_START):
    r=bc/2.0
    return [circ(lay,cx+r*math.cos(math.radians(start+k*360/n)),
                     cy+r*math.sin(math.radians(start+k*360/n)),hole_d/2) for k in range(n)]

def part_pp_half():
    cx,cy=BED_W/2,BED_H/2
    P=[sheet(0,0,BED_W,BED_H),circ("CUT",cx,cy,CARRIER_OD/2)]+bolts("DRILL",cx,cy,HOLE_M4_CLR)
    return ("ZnO_cut_PP_half_300","ZnO strip backer (300 mm) — 1/2 in PP",
      ["ZnO strip backer (300 mm), 1/2 in PP. Solid carrier disc + M4 bolt ring.",
       "Dimensions per 300mm-datum-reference.md. Bed 500x600 mm; 1 plate/sheet."],P)

def part_pp_threeeighth():
    cx,cy=BED_W/2,BED_H/2
    P=[sheet(0,0,BED_W,BED_H),circ("CUT",cx,cy,CARRIER_OD/2),circ("WINDOW",cx,cy,WINDOW_D/2)]+bolts("DRILL",cx,cy,HOLE_M4_CLR)
    return ("ZnO_cut_PP_threeEighth_300","ZnO strip clamp frame (300 mm) — 3/8 in PP",
      ["ZnO strip clamp frame (300 mm), 3/8 in PP. Window ring + M4 bolt ring.",
       "Dimensions per 300mm-datum-reference.md. Bed 500x600 mm; 1 plate/sheet."],P)

def part_pvdf_quarter():
    ax,ay=BED_W/2,BED_H/2
    P=[sheet(0,0,BED_W,BED_H),circ("CUT",ax,ay,CARRIER_OD/2),circ("WINDOW",ax,ay,WINDOW_D/2),
       circ("GROOVE",ax,ay,ORING_D/2)]+bolts("DRILL",ax,ay,HOLE_M4_CLR)
    hw,hh=380.0,25.0; top=ay+CARRIER_OD/2+5.0
    P+=[ln("CUT",ax-hw/2,top,ax+hw/2,top),ln("CUT",ax+hw/2,top,ax+hw/2,top+hh),
        ln("CUT",ax+hw/2,top+hh,ax-hw/2,top+hh),ln("CUT",ax-hw/2,top+hh,ax-hw/2,top)]
    bx0=BED_W+BED_GAP; bx,by=bx0+BED_W/2,BED_H/2
    P+=[sheet(bx0,0,BED_W,BED_H),circ("CUT",bx,by,CARRIER_OD/2),circ("POCKET",bx,by,POCKET_D/2)]+bolts("DRILL",bx,by,HOLE_SMALL)
    return ("ZnO_cut_PVDF_quarter_300","ZnO immersion & seeding carrier (300 mm) — 1/4 in PVDF",
      ["ZnO immersion & seeding carrier (300 mm), 1/4 in PVDF.",
       "Bed A: window plate + handle (O-ring groove).  Bed B: back/mask plate (coupon pocket).",
       "Dimensions per 300mm-datum-reference.md. Bed 500x600 mm; 1 plate/sheet."],P)

def part_platen_alum():
    S=360.0; cx,cy=S/2,S/2
    P=[sheet(0,0,S,S),circ("CUT",cx,cy,CHUCK_OD/2),circ("POCKET",cx,cy,WAFER_RECESS/2),
       circ("GROOVE",cx,cy,VAC_RING_O/2),circ("GROOVE",cx,cy,VAC_RING_I/2),
       ln("GROOVE",cx-CROSS_HALF,cy,cx+CROSS_HALF,cy),ln("GROOVE",cx,cy-CROSS_HALF,cx,cy+CROSS_HALF),
       circ("DRILL",cx,cy,PORT_D/2)]
    r=FOOT_BC_D/2
    for a in (45,135,225,315):
        P.append(circ("TAP",cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)),TAP_M4/2))
    return ("ZnO_cut_platen_alum_300","ZnO wafer bonding chuck (300 mm) — aluminium",
      ["ZnO wafer bonding chuck (300 mm), aluminium.",
       "Holds a 300 mm wafer polished-face-DOWN on a clean pad; vacuum from below.",
       "Heavier cut: NO waterjet (cost) -> rigid mill / slow router / outsource.",
       "Dimensions per 300mm-datum-reference.md. Own 360x360 mm stock."],P)

# ---- emitters -------------------------------------------------------------
def _f(x): return f"{x:.4f}"

def dxf_emit(P, desc):
    L=[]
    for c in CC0+desc: L+=["999",c]
    L+=["0","SECTION","2","HEADER","0","ENDSEC",
        "0","SECTION","2","TABLES","0","TABLE","2","LAYER","70",str(len(LAYERS))]
    for n,col in LAYERS: L+=["0","LAYER","2",n,"70","0","62",str(col),"6","CONTINUOUS"]
    L+=["0","ENDTAB","0","ENDSEC","0","SECTION","2","ENTITIES"]
    def dline(lay,x1,y1,x2,y2): return ["0","LINE","8",lay,"10",_f(x1),"20",_f(y1),"30","0.0","11",_f(x2),"21",_f(y2),"31","0.0"]
    for p in P:
        if p[0]=="sheet":
            _,x0,y0,w,h=p
            for seg in [(x0,y0,x0+w,y0),(x0+w,y0,x0+w,y0+h),(x0+w,y0+h,x0,y0+h),(x0,y0+h,x0,y0)]:
                L+=dline("SHEET",*seg)
        elif p[0]=="circle":
            _,lay,cx,cy,r=p; L+=["0","CIRCLE","8",lay,"10",_f(cx),"20",_f(cy),"30","0.0","40",_f(r)]
        elif p[0]=="line":
            _,lay,x1,y1,x2,y2=p; L+=dline(lay,x1,y1,x2,y2)
    L+=["0","ENDSEC","0","EOF"]
    return "\n".join(L)+"\n"

def _esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def svg_emit(P, title):
    title=_esc(title)
    xs,ys=[],[]
    for p in P:
        if p[0]=="sheet": _,x0,y0,w,h=p; xs+=[x0,x0+w]; ys+=[y0,y0+h]
        elif p[0]=="circle": _,l,cx,cy,r=p; xs+=[cx-r,cx+r]; ys+=[cy-r,cy+r]
        elif p[0]=="line": _,l,x1,y1,x2,y2=p; xs+=[x1,x2]; ys+=[y1,y2]
    m=15; minx,maxx,miny,maxy=min(xs)-m,max(xs)+m,min(ys)-m,max(ys)+m
    W,H=maxx-minx,maxy-miny
    # key diameters by layer for the caption
    dias={}
    for p in P:
        if p[0]=="circle" and p[1] in ("CUT","WINDOW","GROOVE","POCKET"):
            dias.setdefault(p[1],round(p[4]*2,1))
    cap=" · ".join(f"{k} ⌀{v}" for k,v in dias.items())
    def yflip(y): return (miny+maxy)-y            # flip so DXF y-up renders correctly
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx:.1f} {miny:.1f} {W:.1f} {H:.1f}" '
         f'style="width:100%;height:auto;max-width:760px;font-family:sans-serif" role="img" '
         f'aria-label="{title} — to-scale plan (generated from 300mm-datum-reference.md)">']
    out.append(f'<title>{title}</title>')
    sw=max(W,H)/700.0                              # ~1px stroke at display size
    for p in P:
        if p[0]=="sheet":
            _,x0,y0,w,h=p
            out.append(f'<rect x="{x0:.2f}" y="{yflip(y0+h):.2f}" width="{w:.2f}" height="{h:.2f}" '
                       f'fill="none" stroke="{SVG_COLOR["SHEET"]}" stroke-width="{sw:.2f}" stroke-dasharray="{6*sw:.1f},{4*sw:.1f}"/>')
        elif p[0]=="circle":
            _,lay,cx,cy,r=p
            out.append(f'<circle cx="{cx:.3f}" cy="{yflip(cy):.3f}" r="{r:.3f}" fill="none" stroke="{SVG_COLOR[lay]}" stroke-width="{sw:.2f}"/>')
        elif p[0]=="line":
            _,lay,x1,y1,x2,y2=p
            out.append(f'<line x1="{x1:.3f}" y1="{yflip(y1):.3f}" x2="{x2:.3f}" y2="{yflip(y2):.3f}" stroke="{SVG_COLOR[lay]}" stroke-width="{sw:.2f}"/>')
    fs=max(W,H)/45.0
    out.append(f'<text x="{minx+m:.1f}" y="{miny+fs*1.2:.1f}" font-size="{fs:.1f}" fill="#222">{title}</text>')
    out.append(f'<text x="{minx+m:.1f}" y="{miny+fs*2.4:.1f}" font-size="{fs*0.72:.1f}" fill="#555">to-scale (mm) · {cap}</text>')
    out.append('</svg>')
    return "\n".join(out)+"\n"

if __name__=="__main__":
    for fn in (part_pp_half,part_pp_threeeighth,part_pvdf_quarter,part_platen_alum):
        base,title,desc,P=fn()
        open(os.path.join(OUT,base+".dxf"),"w",newline="\n",encoding="utf-8").write(dxf_emit(P,desc))
        open(os.path.join(OUT,base+".svg"),"w",newline="\n",encoding="utf-8").write(svg_emit(P,title))
        print("wrote",base+".dxf",base+".svg")
