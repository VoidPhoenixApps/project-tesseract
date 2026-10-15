# D5 — tool-free attachment and retention

[Study](d5-engineering-study.md) · [service](d5-service.md) · [safety](d5-safety.md).
Tool-free means installation **and** removal by hand in the actual assembled access
corridor. A coin, hex key, screwdriver, hidden screw or structural-member removal fails
that requirement. Factory/initial assembly fasteners may exist, but conversion must not
loosen frame nodes, rail clamps, electronics mounts or heated-bed mechanisms.

## Comparative mechanisms

| Method | Engagement and load path | Heat, wear, vibration and adverse handling | Adjustment, access and disposition |
| --- | --- | --- | --- |
| Mechanically retained magnetic panel | Magnets locate/preload; lower ledge carries gravity; separate positive hand retainer blocks outward motion/lift. Visible retainer state required | Gap, paint, dirt, peel and shear reduce useful attraction; temperature and corrosion affect magnet/adhesive. Mechanically capture magnets; a loose magnet can enter motion/wiring | Easy alignment but magnetic attraction is not engagement proof. A1/A2 explain shear and temperature limits; retain only as hybrid, not sole guarding/support |
| Captive hand quarter-turn | Matched stud/receptacle carries closure; bail/wing/knob exposes state; support panel before release | Grip range, gasket set and warped panels can give apparent closure without correct engagement. Verify vibration unlock, temperature, wear and one-fastener loss | A3 establishes hand and tool variants exist; select neither yet. Require hand style, matching stack thickness, usable finger clearance and inspectable engagement; shortlist |
| Hand cam / over-center latch | Defined cam/bail mechanically captures panel; hard stop separates closure from excessive gasket compression | Over-center geometry may be lost by wear, creep or misalignment; hot distorted sheet can require excessive force. Accidental snag release and finger pinch need assessment | Adjustable catch must remain stable without frequent tool adjustment. Secondary anti-release feature may be needed; shortlist with retained support |
| Captive snap | Hook flexure retains edge; engagement witness and redundant capture can be added | Temperature, layer direction, notch stress and fatigue change insertion/release force; dirt hides engagement; repeated flexing may crack | Replaceable clips accessible by hand; distinguish sheet clip from structural load joint. Not accepted as sole long-life restraint without actual cyclic data |
| Captured-edge / slide-in | Tracks bear edge loads; captive hand end stop prevents escape; one reference plus followers allows growth | Track dirt, swollen seals, bow and unequal expansion can jam; vibration frets edges; clearance can rattle | Full extraction corridor needed; cannot remove primary brace to free panel. Retain where both directions and debris access are proven |
| Lift-off / removable hinges | Hinges support gravity; opposite latch retains closure; separate anti-lift capture where unintended lift is possible | Sag, pin wear and unequal expansion misalign latch; partial lift can leave one hinge engaged; door moment loads frame even open | A4 shows removable families exist. Verify swing, pin withdrawal and hand release; ordinary fixed hinge is not removable. Shortlist framed moderate-size panels |
| Captive hand knob / thumbscrew | Threaded retention with visible seated shoulder; weight remains on ledge | Cross-threading, galling, excessive torque, gasket compression set and cold/hot seizure impair hand use | Simple comparison baseline; slower repeated turns and access around knobs. A tool-required “last turn” fails conversion |
| Hybrid cassette | Protected insert in nonstructural perimeter; positive hand retention with supported edge and optional magnetic location | Adds gasket/fastener interfaces and differential expansion; perimeter can conduct heat into grip | Separates sacrificial sheet from frame hardware; does not transfer frame-bracing duty to panel. Candidate across editions |

These are mechanism families, not purchased hardware specifications. Manufacturer
vibration or cycle claims are application-dependent and not credited as tested Tesseract
performance. No pull force, fastener count, retention capacity or hand-force limit selected.

## Loads and fault sensitivity

Separate downward weight/inertia, outward force and eccentric overturning moment.
[Calculation](d5-calculations.md) uses a hypothetical 3.6 kg glass panel, 2 m/s² vertical
acceleration, 30 N outward force at mid-height, 30 mm support offset and 500 mm retainer
spacing. It yields 42.516 N downward and 17.551 N total upper retention demand. This is
an equilibrium example, **not** a proof load, impact model, safety factor or hardware rating.
With two ideal supports each carries 21.258 N; one remaining support must carry 42.516 N
and may also need a moment path omitted from that scalar split. Losing one upper retainer
can twist the panel; do not divide loads equally without stiffness/contact evidence.

A separate hypothetical friction joint with 200 N preload and coefficient .2 carries
40 N initially, 20 N at half preload and 10 N at quarter preload. Against 20 N shear,
its margin disappears at half preload. No relaxation time is predicted. Prefer positive
capture with a defined thermal release direction; simply tightening a polymer clamp
harder can increase creep or panel cracking.

## Interface principles to compare

Panel load → nonstructural cassette support → dedicated accessory attachment → permanent
braced frame. “Nonstructural” means no role in printer alignment or bed/head gravity
restraint; the accessory still needs strength for its own panel and user loads.

One fixed in-plane datum plus sliding/floating followers can avoid incompatible thermal
constraints. The panel remains restrained out of plane at all permitted follower positions.
Slot clearance must include differential expansion, assembly error, edge engagement and
wear; use a retained shoulder/guide if needed, not uncontrolled fastener friction. Gasket
compression must neither lock followers nor become a primary shear path. Compare heat-safe
replaceable grips, visible capture, captive hardware, two-hand support during final release,
and a safe storage cradle. No loose keepers should fall into beds or electronics.

Environmental panels are not automatically protective guards, and their absence alone
requires no interlock. Convenience latches and presence sensors do not establish protection.
If hazard-specific assessment assigns a panel protection against access or ejection,
its whole assembly, stopping/access time and interlock strategy need qualified review. Open-air operation cannot be achieved by defeating
that protection; see the distinct protection alternatives in the [safety register](d5-safety.md).
