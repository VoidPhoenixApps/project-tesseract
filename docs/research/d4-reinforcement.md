# D4 — independently reproducible stock variants

[Study](d4-engineering-study.md) · [source ledger](d4-references.md).
**Sourcing candidates only, accessed 2026-10-14.** Catalog orderability is evidence of a
supply route, not confirmed stock, a quote, installed hardware or an approved purchase.
No final reinforcement size or grade is selected.

## Exact candidates and unresolved tolerances

| Candidate / regional route | Nominal and physical definition | Tolerances / material / ordering gaps | Interface implications |
| --- | --- | --- | --- |
| US-S: Thomson `1/2 L RL`, North American direct/distributor route [S1](d4-references.md) | Nominal 0.5 in = 12.7 mm solid; actual Class L range 0.4990–0.4995 in = 12.6746–12.6873 mm; random length 166 in, cut-to-length offered | Product table identifies 1566 carbon steel, HRC 60 minimum; length ±1/32 in for custom cut. Page also rounds diameter to 13 mm: **do not use that rounded field**. Lot and final drawing needed | Separate split socket/retainer, not 12 mm fit. Hardened shaft drilling/cross-pinning requires a specified machining route; precision finish does not establish frame stiffness |
| M-S: Thomson `12 TCM` standard unplated T-Case, European/global route [S2](d4-references.md) | 12 mm solid, 11.989–12.000 mm h6; basic code with CTL/length option to be confirmed | 2019 brochure: 0.15 mm/m straightness, 2 µm roundness/taper, nominal 0.9 kg/m. Chrome option is h7 and cannot inherit h6 fit. Current lead time and alloy certificate unresolved | Distinct socket, end-retention and cut list. Same centerline datum is possible, but nominal radial offset from US-S is 0.35 mm, much larger than shaft tolerance |
| US-T: Speedy Metals `dom1x.065`, product 3494, US cut stock [S3](d4-references.md) | OD 1.000 in = 25.4 mm; wall .065 in = 1.651 mm; nominal ID .870 in = 22.098 mm | Material page says generally ASTM A513 Type 5 and describes C1020, while linked items include 1026: obtain exact grade/condition and OD/wall/straightness tolerances. Custom cut +1/8 in, -0; not a precision datum cut | Tube-specific socket and crush-resistant load spreader. Do not use ID as a precision bearing seat or assume a seamless bore. Supplied length needs a documented final cutting/alignment method |
| M-T1: Fluidics `HR 25X1,5`, item FL-312264, EU route [S4](d4-references.md) | 25 mm OD × 1.5 mm wall; nominal ID 22 mm; 6 m manufacturing length/part lengths | E235+N, EN 10305-4, black phosphated; supplier cites DIN 2391 grade C but does not give numeric OD/wall limits in inspected text. Confirm applicable revision, coating and numeric limits before fit design | Shares centerline concept with US-T, not the same socket. Different wall/ID changes clamp crushing and mass; numerical stiffness uses nominal dimensions only |
| M-T2: Parker `R25X2` phosphated / `R25X2CF` finish alternative, EU/global catalog [S5](d4-references.md) | 25 mm OD × 2 mm wall, nominal ID 21 mm, E235+N tube family | CAT-4041-2/UK p.19: OD ±0.08 mm and 1.134 kg/m. Confirm wall/straightness/cut tolerances, final delivery standard/revision and regional quote; do not transfer M-T1 limits | Thicker alternative to M-T1, not a substitution. Reinforcement interface must explicitly record wall and finish |
| US-R: Bolt Depot 23747 [S6](d4-references.md) | 5/16-18 right-hand coarse thread, 3 ft (914.4 mm); major nominal 7.9375 mm, pitch 25.4/18 = 1.41111 mm | ASTM A193 B7 alloy, plain; dimensional standard ASME B18.31.3. Exact thread limits/straightness and nut engagement require drawing/standard confirmation | Matching 5/16-18 nuts/load spreaders, no M8 nut substitution. Tension tie preferred role; root section and thread stress concentration must be used for capacity |
| M-R: norelem `07640-08`, European/global catalog lead [S7](d4-references.md) | M8 RH, grade 8.8 bright, 1000 mm, DIN 976-1; coarse M8×1.25 candidate must be confirmed on order drawing | Manufacturer search-index table identifies code; direct PDF returned 404. Exact pitch/fit/straightness therefore unresolved rather than procurement-ready | Separate M8 nut pockets, washers and length adjustment. Grade 8.8 is not an equivalence claim to B7 |
| 2020 reference: 80/20 `20-2020` [S8](d4-references.md) | 20 × 20 mm, four slots; Ix=Iy=.6826 cm⁴ = 6826 mm⁴ | Live page says 6063-T6; older catalog/model results differ in alloy/mass. Modulus field has malformed punctuation. Use separately labeled 69 GPa reference, not an exact vendor guarantee | Exact slot/nut/end-joint drawings required; not interchangeable with every product called 2020 |

Precision shaft, mechanical tube and nominal pipe are different supply forms. A pipe
nominal size is not its actual OD. Listing a tolerance standard does not establish that
all suppliers, finishes and manufacturing conditions share the same limit. For comparison,
SSAB's **different** Form Tube 420 family [S9](d4-references.md) publishes ±0.15 mm OD
for 20–<32 mm and ±0.15 mm wall at ≤1.5 mm, with a cut-end caveat. These are not applied
to the seamless Fluidics/Parker candidates or US DOM tube.

## One family, distinct reproducible outputs

Proposed datum scheme: common bed-plane origin, lift attachment planes, rail reference
planes and head-root bolt patterns; reinforcement centerlines referenced to those planes.
A variant changes socket diameter, wall support, node exterior clearance, retention and
possibly member count/depth **without scaling the machine**. A larger tube must not move
a rail plane simply because the socket grew outward. Verify wall ligaments and tool
access for each node; common external datums are a hypothesis until both variants fit.

Future identifiers could be `frame-node-[revision]-US-T` and `...-M-T2`, with matching
BOM, material/finish specification, cut list, print orientation and assembly sequence.
Identifiers here are planning examples, not released parts. No mixed-size assembly,
mesh scaling, builder CAD edits, reaming or improvised shims is a reproduction strategy.
A designed split clamp or calibrated built-in adjustment may accommodate a specified
stock/process tolerance range; it still needs measured fit and repeatability evidence.

Keep expensive precision rails, beds and motors independent of structural stock where
possible by using the same datum plate/attachment pattern. Using reinforcement shafts
also as motion races couples variant choice to bearings and undermines this goal. If
an interface cannot remain common, record the affected component explicitly; do not
promise a drop-in upgrade to the later 2020 edition.

For every shortlisted SKU, next sourcing packet needs supplier drawing/revision, OD,
wall/ID, straightness, finish/coating, cut squareness, grade/condition, certificates,
region-specific availability, matching fasteners and a validated interface tolerance
stack. Neither the candidate list nor [nominal beam results](d4-calculations.md) is a BOM.
