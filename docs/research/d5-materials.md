# D5 — enclosure material trade study

[Study](d5-engineering-study.md) · [sources](d5-references.md) · [calculations](d5-calculations.md).
Properties below identify reference products, not interchangeable generic grades or
printer operating limits. No sheet thickness is selected. Cost drivers are qualitative;
there are no quotations, procurement approvals or claims of local inventory.

## Source evidence and application limits

| Candidate | Primary evidence | Thermal/mechanical consequence and unresolved limit |
| --- | --- | --- |
| Solid polycarbonate | M1 PALSUN leaflet: density 1200 kg/m³, expansion 65 µm/m/K, tensile E 2.3 GPa, k .21 W/m/K. Lists long/short service upper temperatures 100/120 °C and HDT 130 °C at 1.82 MPa | Different tests and durations must not be conflated. Mount stress, creep, radiation, coating and actual grade need limits below any damage condition; no chamber rating inferred |
| Cast acrylic / PMMA | M2 PERSPEXre: 1190 kg/m³, 70 µm/m/K, tensile E 3.3 GPa, k .19 W/m/K; continuous/short use 80/90 °C, HDT 105 °C. M3 separately describes PLEXIGLAS GS about 80 °C and XT about 70 °C | Brand/process differences matter. Stiffer reference sheet than PC at equal thickness, but impact/crack behavior needs separate evidence; no cross-test impact ranking from unlike methods |
| Tempered soda-lime glass | M4 Pilkington discusses safety-glass mechanical design. M5 AGC glass property proxy: 2500 kg/m³, E 70 GPa, alpha 9 µm/m/K, k 1 W/m/K | M5 is patterned-glass data, **not selected tempered stock**. Its properties support a labeled mass/expansion sensitivity only; tempering quality, edges, holes, thermal differential limits and breakage retention remain unsourced for any final panel |
| Aluminum sheet; steel alternative | M6 EN AW-5754 guidance: 2660 kg/m³, E 70.5 GPa, alpha 23.9 µm/m/K, k 140–160 W/m/K. Sheet/temper-specific strength tables exist | Formed edge/rib stiffness can exceed flat-sheet performance but is not calculated here. Metal transmits heat to handles and interfaces; electrical bonding assessment needed. Steel sheet may offer dent resistance at higher mass; no steel grade/gauge selected or numeric panel rating inferred |
| Hybrid metal perimeter/opaque faces plus window | Combination of the above; an original integration concept | Smaller clear spans can reduce deflection and replacement cost. Window/frame differential expansion and extra gasket/retainer interfaces can negate the benefit; electrically conductive perimeter remains even with an insulating window |
| Aluminum composite sheet | M7 DIBOND FR identifies mineral-core construction and B-s1,d0 classification | Exact region, product, core and thickness matter; cannot transfer FR evidence to polyethylene-core or unknown signage panels. Core/adhesive heat, smoke and edge delamination need evidence; retained as secondary comparison |
| Other sheet families | Multiwall PC, PETG sheet, wood and mineral board are possible sourcing categories, not adopted products | Multiwall edges complicate cleaning/sealing; PETG sheet needs sheet-grade heat/creep data; wood adds moisture/combustibility uncertainties; mineral boards can be heavy, brittle and dusty. Defer numerical ranking until exact primary data exist |

## Practical comparison (engineering inferences to verify)

| Material | Impact, transparency and surface | Cleaning / attachment / replacement | Availability and cost drivers |
| --- | --- | --- | --- |
| PC | Transparent and impact-tolerant candidate; scratching and long-term distortion remain concerns. Hard-coated variants are separate products | Spread fastener load; allow sliding growth; chemically induced cracking at stressed holes must be assessed. M8 room-temperature chemical tables do not approve a hot, stressed cleaning recipe | M1 lists flat sheet including 2.5–6 mm and large standard formats; regional stock, cut waste, coating and FR grade affect price. Local cut-sheet replacement is a hypothesis pending quotes |
| Acrylic | Transparent, optically attractive; brittle crack propagation at holes/edges is a concern under rough repeated handling | Avoid overclamping/notches; protect cut edges; review cleaner compatibility. Replacement can use flat stock, but cast/extruded thickness and thermal behavior differ | M2 lists clear 3/4/5/6/8/10 mm sheet in 3050 × 2030 mm; nesting, finish and local availability matter more than an unsupported cheapest-material claim |
| Tempered glass | Transparent, scratch-resistant comparison; heavy and vulnerable to edge damage. Breakage removes the barrier and may release fragments | Design finished holes/edges before tempering; use isolated supported edges, no improvised drilling/reaming. Replacement must match finish and temper specification | Custom processing, shipping/breakage, minimum orders and repeatability can dominate cost. No exact tempered-glass service temperature or local source verified |
| Metal | Opaque; may dent or oil-can rather than fracture. Scratches affect coatings and exposed edges | Deburred/hemmed edges, isolated handles, compatible cleaners; corrosion and bonding paths reviewed. Supports must accommodate metal expansion without loading printed frame nodes | Alloy/temper, sheet gauge, cuts, bends, coatings and shop access; a formed panel may need processes unavailable to a self-builder |
| Hybrid/composite | Selective visibility; smaller windows trade fewer large fragile surfaces for more interfaces | Separate replaceable inserts and seals; avoid bonding the whole panel permanently if that frustrates repair; inspect core/edge damage | Multiple materials/hardware and stocked spares; savings from smaller windows are unproven until a BOM exists |

## Fire evidence is not fire containment

M1 lists thickness-dependent PALSUN classifications and a distinct FR product; a
classification is not transferable across thickness/color/coating or the assembled printer.
M7's FR construction likewise requires the exact tested product. No specific PMMA fire
classification has been established here. M5 reports reaction-to-fire A1 for its listed
glass but no declared fire-resistance performance; it does not certify a glazed enclosure.
Bare metal sheet does not make coatings, gaskets, polymer mounts or electrical failures
safe. No candidate is credited as fireproof, unbreakable or a fire-rated assembly.

Adjacent printed joints may govern before the sheet does. Keep D4's material/process
uncertainty: warm preload, layer direction, local radiation and reinforcement mismatch
need actual creep/relaxation evidence. A high panel service-temperature number cannot
approve PLA/PETG/ASA/PC structural nodes or magnet adhesives. Ordinary Ender 3 print
fit and process capability still apply to every printed adapter in both stock variants.
