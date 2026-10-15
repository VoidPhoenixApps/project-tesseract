# D6 — can four print jobs really run independently?

**Research result, 2026-10-15: plausible to investigate, not demonstrated.**
Project Tesseract would need more than four sets of motor drivers. Each job needs its
own progress, temperatures and pause/cancel state, while the machine prevents conflicts
between heads, printed objects, moving beds and shared supports.

We compared three approaches: one central multi-job controller; separate controllers
for regions; and independent motion controllers with one central configuration and
resource planner. None is selected. RepRapFirmware provides a useful asynchronous-motion
precedent, but that does not prove four independently managed print jobs. Klipper's
multiple-MCU and carriage features also do not establish that complete capability.
See the [firmware evidence](d6-firmware.md) and [source ledger](d6-references.md).

A simpler fixed-region system is worth keeping as a comparison. It makes independent
jobs easier but cannot meet automatic row pairs, column pairs and joined printing by
itself. A single ordinary printer queue cannot satisfy four unrelated simultaneous jobs.
More complicated software cannot fix missing mechanical reach or a shared Z mechanism
that forces unrelated jobs to the same height.

The proposed planner reserves the beds, head, motion paths, lift ownership and power
needed for each job. It refuses conflicts. Finishing or cancelling a job does not make
its physical object disappear. Reconfiguration must leave occupied affected beds alone;
a parked nozzle is insufficient if its beam, cables or columns still obstruct motion.
The [eight-mode matrix](d6-states.md) covers singles, both pair directions, all four mixed
arrangements and one joined job using one full-region head. Four-head cooperation on one
object remains a separate stretch goal.

The [small Python model and tests](d6-scheduling.md) exercise synthetic admissions,
independent progress and conservative fault behavior. They do not simulate an actual
printer or operate hardware. Separate [power calculations](d6-electrical.md) illustrate
how heater startup can greatly exceed typical consumption; all loads are hypothetical.
A stopped motor can still allow a heavy Z mechanism to fall, and software cannot turn
off a physically shorted heater switch. Protective functions need qualified design.

Ordinary open-air printing remains available in all required modes. Environmental-panel
removal alone is not a protective fault or an interlock requirement. Controls must
distinguish printing, docking, panel handling, actual protective-guard access and
maintenance isolation. Hazard-specific assessment still justifies necessary protection
against closing gaps, falling loads, electrical/heater faults and unexpected restart;
ordinary open-frame precedent does not prove those mechanisms safe.

Next, establish firmware lifecycle limits, obtain the missing mechanical/geometry
contracts, and compare grouped-Z failure behavior and real component load data.
Qualified mechanical, electrical and controls/safety reviews are required before
implementation. The first physical proof remains two-bed docking and cross-seam printing.
No controller, firmware, protective circuit, component, CAD toolchain or license is chosen.

The [complete package](d6-engineering-study.md) preserves negative findings and lists
assumptions and next experiments. Contributions that challenge the queue semantics,
resource model or failure cases are welcome through [GitHub Discussions](https://github.com/VoidPhoenixApps/project-tesseract/discussions).
