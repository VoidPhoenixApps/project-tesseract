# Fusion component libraries — Stage C research

**2026-10-15; research only.** Companion to [Stage C findings](stage-c-verification.md). These are discovery/placement services, not an approved reusable asset collection. No component was downloaded, inserted, exported or uploaded; no extension was installed and no existing design changed.

## What was verified on Forbidden Fruit

Fusion **2705.1.30**, title **Autodesk Fusion Personal (Not for Commercial Use)**, empty unsaved **Untitled / Part Design**, millimetres. Read-only API inspection in the existing Python text console returned:

| Source | Command ID | Registered | Insert-panel visibility / enablement in this context | Practical access conclusion |
| --- | --- | --- | --- | --- |
| Insert Fastener | `FusionFastenersCommand` | Yes | Visible, **disabled** | Present; usability in another design/license context not established |
| McMaster-Carr | `InsertMcMasterCarrComponentCommand` | Yes | Visible, **disabled** | Present; current context does not enable insertion |
| Parts4CAD / manufacturer parts | `cadenasparts4cad` | Yes | Visible, **enabled** | Entry point available; account, terms and component retrieval untested |
| TraceParts | `traceparts_insert` | Yes | Visible, **enabled** | Entry point available; account, terms and component retrieval untested |

This is not a claim that two services are unavailable globally or that two successful imports occurred. No design/context/license changes were made to enable disabled controls. Remote service health, entitlement and download completion remain untested. The Autodesk website documents the [Insert tools](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-INSERT-TOOLS.htm), but documentation alone does not establish this installation's access.

Computer Use initially failed screen capture, then succeeded; coordinate menu clicks failed window targeting. Accessibility controls allowed console inspection. An initial query incorrectly read `CommandControl.isEnabled` and raised `AttributeError`; the successful query reads `commandDefinition.controlDefinition.isEnabled`. No write or command execution was involved. Context7 had no matching detail; [Autodesk's commandDefinitions API](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/core_UserInterface_commandDefinitions.htm) was used.

Reproduce in Fusion's **Py** text console; these statements only read application/UI state:

```python
import adsk.core
app = adsk.core.Application.get()
ui = app.userInterface
print(app.version)
print([(c.id, c.name) for c in ui.commandDefinitions if any(s in (c.name + ' ' + c.id).lower() for s in ['fastener', 'mcmaster', 'parts4cad', 'traceparts', 'manufacturer'])])
print([(p.id, c.id, c.isVisible, c.commandDefinition.controlDefinition.isEnabled) for p in ui.allToolbarPanels for c in p.controls if any(s in c.id.lower() for s in ['fastener', 'mcmaster', 'parts4cad', 'traceparts'])])
```

The relevant `InsertPanel` results were `(FusionFastenersCommand, True, False)`, `(InsertMcMasterCarrComponentCommand, True, False)`, `(cadenasparts4cad, True, True)`, `(traceparts_insert, True, True)`. Recheck in a future session rather than treating enablement as permanent. Command registration is not a download test.

Installed application resources also contain built-in Parts4CAD and TraceParts manifests, both version 1.0.0, startup-enabled and supporting macOS/Windows. Parts4CAD is authored by CADENAS; TraceParts' integration manifest names Autodesk. The former points to the [Fusion PARTcommunity portal](https://autodesk-fusion.partcommunity.com/3d-cad-models/), which the web service could read; the latter points to [TraceParts' Fusion catalog](https://www.traceparts.com/els/fusion-360/en/catalogs), which that service could not retrieve. No additional installation is needed merely to register these observed commands; this does not promise backend access. Application resource inspection was limited to these installed add-in scripts/manifests, not account data or model caches.

## Coverage, formats and library value

| Source | Coverage and formats documented by provider | Opportunity versus the existing 45-record catalog |
| --- | --- | --- |
| Insert Fastener | [Autodesk fastener workflow](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-INSERT-FASTENER.htm): bolts, nuts and washers; standard/size filtering and placement into Fusion. No standalone downloadable neutral-library format was verified | Could fill standard-fastener coverage beyond MISUMI SCBS4-10 and HNTT5-5 after rights review. A standard fastener is not automatically an exact manufacturer SKU, material/finish or purchased revision |
| McMaster-Carr | Broad industrial hardware, fasteners, bearings, shafts, belts/pulleys, raw stock and fittings. [Fusion integration supports SAT and STEP](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-90FD5419-A8AF-4A7C-AB1E-75D027077709.htm); not every product necessarily has a model | Substantial overlap with bearings, structural stock, fasteners and motion candidates. Supplier identity may differ from OEM; do not relabel as SKF, NTN, Gates or HIWIN. Rights make it unsuitable as the default public library source |
| Parts4CAD / manufacturer parts | Manufacturer-configured mechanical, motion, structural and electrical components. [CADENAS supported formats](https://www.cadenas.de/de/produkte/partsolutions/unterstuetzte-systeme/cad-systeme) include Fusion, STEP and SAT; exact export choice depends on portal/part | Potential alternate discovery route for existing manufacturer records, not new candidate identities by default. Seek exact manufacturer code/configuration; no exact cataloged SKU availability was verified here |
| TraceParts | Multi-supplier mechanical/electrical catalogs; [provider format overview](https://info.traceparts.com/designers/use-and-manage-3d-cad-models/cad-library/) lists Fusion compatibility and STEP, IGES, SAT and other neutral formats | Could help find exact bearing, connector, switch or motion records; no exact cataloged SKU/model was verified. Keep supplier/manufacturer, revision, option string and model origin distinct |

Priority is resolving existing records, not collecting lookalikes: HIWIN configuration, LDO revision, BTT rights and Feather revision gaps cannot be solved by a visually similar portal part. Potential searches for SKF/NTN bearings, WAGO connectors, OMRON switches, MISUMI/80-20 structure and Gates transmission components are **opportunities, not verified portal stock or model availability**. Raspberry Pi, Adafruit, BTT, Duet, E3D and Bondtech already have direct manufacturer paths in the catalog; do not repeat broad discovery unless those paths fail for the exact variant.

## Rights and AI-access assessment

The following is a conservative action-gate assessment of the cited terms, not a license grant or legal opinion. Tool availability, “free download,” local storage and account entitlement are distinct from reuse permissions. Local automated measurement, sending geometry to a hosted assistant, and model training are different actions. No provider's training prohibition is treated as an automatic ban on every local script, or as permission for cloud processing.

| Source | Download / local inspection | Derived interfaces and commercial use | Redistribution / reusable library decision |
| --- | --- | --- | --- |
| Autodesk Fastener | In-product use subject to Fusion entitlement and terms. Local automated/Codex processing of library content **unknown**; no asset-specific permission found | Rights to user-authored work do not by themselves establish rights in third-party/generated library assets. Commercial entitlement must be reviewed separately from this Personal installation | No explicit standalone fastener-library redistribution grant established; keep **unknown**, do not extract/cache an asset collection |
| McMaster-Carr | CAD offered for purchase evaluation; project authorization absent. Local AI inspection **unknown**; training/fine-tuning expressly prohibited | Do not assume permission for public derivative assemblies or commercial CAD reuse; ask for written scope | Public sharing of models and drawings/prototypes incorporating them restricted. **Do not populate the public or shared Tesseract model library from this source** under current evidence |
| CADENAS / Parts4CAD | CAD/BIM-design purpose, fair-use and user-eligibility conditions; additional supplier terms may apply. Local AI inspection **unknown**; ML/training use prohibited absent written consent | Internal design use is not a blanket downstream commercial/derivative grant. Confirm exact portal and supplier terms | Replacing/copying database content prohibited. Public model redistribution **unknown**, not presumed licensed; no bulk collection |
| TraceParts | CAD/viewing use under terms; exact vendor conditions and account requirements must be checked. Local AI inspection **unknown** | Model-based interface/assembly publication and commercial reuse need scope confirmation | Written consent required for posting/distributing data; keep models out of public/shared library without it |

Sources and limits:

- [McMaster-Carr Terms](https://www.mcmaster.com/termsandconditions), version **September 17, 2026**, “Use of CAD Models” and “Prohibited Uses.” The sharing restriction includes designs containing models; model dimensions may omit manufacturing tolerances. Do not use the service as a mirrored database. No contact or agreement acceptance occurred.
- [CADENAS PARTcommunity CAD-download terms](https://www.cadenas.de/en/legal/partcommunity-b2b/terms-of-use), sections 2 and 5. Their CAD/BIM-design purpose, database-copying restriction, ML/training exclusion and business-user eligibility need review for the actual account/use. The site's 50-ticket fair-use limit is **not** project authorization. Supplier data and contact-sharing terms also matter. Do not substitute unrelated PARTS4CAD Professional subscription terms for the bundled Fusion integration.
- [TraceParts published terms](https://info.traceparts.com/ru/legal/general-terms-and-conditions-of-use/), English text at this locale, section 5: CAD/viewing purpose and written-consent requirements for external distribution. The current generic GTU endpoint was unavailable to this session, so verify applicable current terms before any future asset action. [TraceParts Developer Hub](https://developers.traceparts.com/reference/developer-hub) offers specific AI/ML data endpoints; their existence does not authorize using ordinary CAD downloads for those purposes.
- [Autodesk general terms](https://www.autodesk.com/company/terms-of-use/en/general-terms) do not establish a reviewed, asset-specific open redistribution grant for the fastener collection. Final content provenance, applicable subscription terms and rights remain a question for Autodesk before a reusable library export. No extension or entitlement was purchased.

No catalog permission flag was broadened by this assessment. No third-party CAD was sent to a hosted model or cloud CAD service. Reading public documentation or command metadata is not equivalent to reading protected local geometry.

## Recommended workflow for future Codex sessions

1. Read the [reference-library workflow](README.md); search the existing catalog by exact manufacturer, part, physical revision and configuration. Reuse an existing record, adding a reviewed alternative source link rather than duplicating it.
2. Use Fusion libraries as **discovery entry points**. Record provider, manufacturer/OEM, complete option string, drawing revision, formats and terms URL/date. Registration or an enabled menu is not evidence of geometry accuracy or permission.
3. Resolve the five catalog actions separately: download, local AI processing, derivative use, public redistribution and commercial reuse. Also resolve hosted-model/cloud-upload exposure separately. Preserve attribution and supplier restrictions. Prefer directly licensed manufacturer assets when they provide a clearer reproducibility path.
4. If rights or identity remain unclear, consolidate the request: exact item, intended local numerical inspection, desired STEP/native source, derived mounting use, public assembly/model distribution and commercial intent. Ask for correct files or acceptable source approval; do not contact the provider without authorization.
5. Obtain explicit approval for each additional retrieval. Prefer a pinned local neutral file in the existing read-only-reference workflow over inserting directly into a working design or letting a service create a cloud-saved component. Verify where transfer/save occurs before use. No auto-download cache harvesting, scraping or broad synchronization.
6. After authorization, retain original bytes and license, hash and catalog the asset, inspect it in a temporary document, compare revision-matched dimensions, then pursue independent free/open reproduction. Keep physical fit and operating safety unverified until measured.
7. For disabled controls, first document the exact workspace, document type, save state and license. A future authorized UI check may use an appropriate temporary design context; do not modify existing designs, upgrade a subscription, install an add-in or accept new terms merely to make a command work.

Remaining actions: confirm service access/terms for exact candidates, resolve local-AI and public-sharing permissions, and test one separately authorized sample only when it adds evidence beyond the current Feather. This Stage C research selects no source as a final library provider or CAD toolchain.
