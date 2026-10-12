# Study verification record

**2026-10-12. Documentation and analytical checks only.** No printer or engineering gate passed.

| Check | Result and limits |
| --- | --- |
| Git baseline | Clean `main` matched freshly fetched `origin/main` at 716834a501c3217f192417bac85600d6302c2316 before dedicated branch creation |
| Supporting authority | Project-knowledge local HEAD matched GitHub main at 46ff107e35053b970915a3ca147f5513571f7be6; no Tesseract project record found locally or in remote tree. Home Infrastructure instructions read from current main (963185a4d528884473a28a87ef81ffb0d1e59dd4 observed during this task). Both repositories left unchanged |
| Requirement/classification review | [Coverage audit](risks-and-decisions.md) checked against unchanged requirements; all six modes and both mixed orientations addressed, conditional/failing concepts explicit |
| Scalar calculation reproduction | `python docs/phase1/screening_calculations.py` executed successfully using bundled Python; outputs compared against all tabulated values; two last-digit transcription differences corrected |
| Documentation structure | Local Markdown link targets exist; code fences balanced; tables/headings and cross-document terminology reviewed |
| Scope preservation | `git diff --exit-code -- docs/requirements.md docs/roadmap.md README.md` passed; existing architecture changed only to link/contextualize study |
| Reporting regression tests | `python -m unittest discover -s tests -v`: all 15 passed. First run had one sandbox temporary-directory permission error; rerun used the repository as process-local TMP/TEMP/TMPDIR. Reporting code unchanged; tests mock external delivery |
| Independent desk review | Separate read-only agent inspected actual files, requirements and architecture diff under shared review rubric; zero Critical/Important/Minor findings. Independently recalculated scalar values. Recommended approval as an exploratory study subject to human review; overall confidence Medium |

The default WindowsApps Python alias was inaccessible, so the bundled runtime reported by Codex workspace dependencies was used. This environment detail does not impose a CAD or Python distribution choice on builders; the calculation aid uses the Python standard library.

The independent reviewer did not reopen external technical references or verify catalog stock, solid sweeps, singularity maps, hardware, or electrical safety. Primary sources were inspected by the author; the imperial shaft product's direct page timed out, with details available only through the manufacturer's search-indexed record. Order-drawing confirmation remains outstanding.

Not performed: CAD generation, finite-element/multibody simulation, dimensioned component fit, head/object swept-volume verification, instrument calibration, physical measurements, purchases, wiring/firmware changes, thermal/motion tests or qualified safety sign-off. They require future reviewed artifacts and authorization; they are not substitutes for documentation checks. AgentMemory was unavailable. No source-repository knowledge updates were made.

Final staged whitespace/full-diff checks, commit, PR and CI evidence are recorded in the Draft PR handoff so this document does not predict unperformed checks or need a self-referential commit update. The PR remains Draft and requires human review; no final architecture decision is adopted.
